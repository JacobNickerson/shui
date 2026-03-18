{
  description = "Django inventory dev environment";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };

        python = pkgs.python312;

        pythonEnv = python.withPackages (ps: with ps; [
          django
          psycopg
          psycopg2-binary
          python-dotenv
          black
          isort
          pillow
          gunicorn
        ]);
      in
      {
        devShells.default = pkgs.mkShell {
          packages = [
            pythonEnv
            pkgs.postgresql
            pkgs.sqlite
          ];

          shellHook = ''
            export DJANGO_SETTINGS_MODULE=shui.settings
            export PYTHONPATH=$PWD
            echo "Django inventory dev shell"
          '';
        };
      });
}

