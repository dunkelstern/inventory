{ pkgs ? import <nixpkgs> {} }:
let
  pypkgs-build-requirements = {
    sqlparse = [ "flit-core" ];
    python-monkey-business = [ "setuptools" ];
    # typed-ast = [ "setuptools" ];
    # typing_extensions = [ "setuptools" ];
  };
  p2n-overrides = pkgs.poetry2nix.defaultPoetryOverrides.extend (self: super:
    builtins.mapAttrs (package: build-requirements:
      (builtins.getAttr package super).overridePythonAttrs (old: {
        buildInputs = (old.buildInputs or [ ]) ++ (builtins.map (pkg: if builtins.isString pkg then builtins.getAttr pkg super else pkg) build-requirements);
      })
    ) pypkgs-build-requirements
  );

  inventoryAppEnv = pkgs.poetry2nix.mkPoetryEnv {
    projectDir = ./.;
    python = pkgs.python311;
    preferWheels = true;
    overrides = p2n-overrides;
    editablePackageSources = {
      inventory = ./inventory;
    };
  };
in inventoryAppEnv.env.overrideAttrs (oldAttrs: {
  buildInputs = with pkgs ; [ 
    postgresql.lib
  ];
  # shellHook = ''
  #   export LD_LIBRARY_PATH="$LD_LIBRARY_PATH:${pkgs.postgresql.lib}/lib"
  # '';
})