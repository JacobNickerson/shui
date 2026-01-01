{
  description = "Shui-App Flake, includes .NET and SQLite";

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
        devShells.default = pkgs.mkShell {
          packages = with pkgs; [
            dotnetCorePackages.dotnet_10.sdk
            sqlite
            sqlitebrowser
            omnisharp-roslyn
          ];

          DOTNET_ROOT = "${pkgs.dotnetCorePackages.dotnet_10.sdk}";
          DOTNET_CLI_TELEMETRY_OPTOUT = "1";
          DOTNET_NOLOGO = "1";

          shellHook = ''
            echo Activated Shui-App shell
          '';
        };
      });
}

