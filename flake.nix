{
  description = "Django inventory";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
    let
      pkgs = import nixpkgs {
        inherit system;
      };
    in
    {
      packages.default =
        pkgs.callPackage ./package.nix { };

      devShells.default = pkgs.mkShell {
        packages = [
          pkgs.uv
          pkgs.python312
          pkgs.sqlite
        ];

        shellHook = ''
          export DJANGO_SETTINGS_MODULE=shui.settings
          export PYTHONPATH=$PWD
        '';
      };
    });
}