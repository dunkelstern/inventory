from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import get_template
from django.db.models import Q
from django.core.paginator import Paginator
from django.conf import settings

from re import finditer

from inventory.models import Item

@method_decorator(login_required, name='dispatch')
class SearchView(View):
    
    def get(self, request):
        page = int(request.GET.get('page', "1"))
        query = request.GET.get('q', None)
        if not query:
            return render(request, "inventory/search.html")
                
        results: list[dict[str, str]] = []

        tokens = query.split(" ")
        tokens = map(str.lower, map(str.strip, tokens))
        
        q: Q = None
        item_template = get_template("inventory/search_result_item.html")
        t: list[str] = []
        for token in tokens:
            combiner = 'or'
            if token.startswith("+"):
                token = token[1:]
                combiner = 'and'
            elif token.startswith("-"):
                token = token[1:]
                combiner = 'and not'

            t.append(token)

            q1 = Q(name__icontains=f'{token}')
            q2 = Q(description__icontains=f'{token}')
            q3 = Q(tags__name__icontains=f'{token}')
            q4 = Q(tags__description__icontains=f'{token}')
            q5 = Q(form_factor__tags__name__icontains=f'{token}')
            q6 = Q(form_factor__tags__description__icontains=f'{token}')

            qx = q1 | q2 | q3 | q4 | q5 | q6

            if q == None:
                q = qx
            elif combiner == 'or':
                q = q | qx
            elif combiner == 'and':
                q = q & qx
            elif combiner == 'and not':
                q = q & ~qx
        items = Item.objects.filter(q).select_related("container", "form_factor").prefetch_related("tags", "documentation").distinct()

        # FIXME: Rank search results

        paginator = Paginator(items, getattr(settings, "PAGE_SIZE", 10))

        for item in paginator.get_page(page):
            text = item_template.render({
                "item": item,
                "tokens": t
            })
            result = {
                "title": item.name,
                "text": text,
                "url": reverse('item-detail', kwargs={"pk": item.pk})
            }
            results.append(result)

        return render(request, "inventory/search_result.html", {
            "q": query,
            "results": results,
            "tokens": t,
            "page": page,
            "pages": paginator.num_pages
        })