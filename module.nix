{ config, lib, pkgs, ... }:

let
  cfg = config.services.shui;
in
{
  options.services.shui = {

    enable = lib.mkEnableOption "Shui";

    package = lib.mkOption {
      type = lib.types.package;
    };

    settingsFile = lib.mkOption {
      type = lib.types.path;
    };

    host = lib.mkOption {
      type = lib.types.str;
      default = "127.0.0.1";
    };

    port = lib.mkOption {
      type = lib.types.port;
      default = 8000;
    };

    dataDir = lib.mkOption {
      type = lib.types.path;
      default = "/var/lib/shui";
    };

    user = lib.mkOption {
      type = lib.types.str;
      default = "shui";
    };
  };

  config = lib.mkIf cfg.enable {

    users.users.${cfg.user} = {
      isSystemUser = true;
      group = cfg.user;
      home = cfg.dataDir;
    };

    users.groups.${cfg.user} = {};

    systemd.tmpfiles.rules = [
      "d ${cfg.dataDir} 0755 ${cfg.user} ${cfg.user} -"
      "d ${cfg.dataDir}/media 0755 ${cfg.user} ${cfg.user} -"
      "d ${cfg.dataDir}/static 0755 ${cfg.user} ${cfg.user} -"
    ];

    systemd.services.shui = {

      wantedBy = [ "multi-user.target" ];

      after = [ "network.target" ];

      environment = {
        DJANGO_SETTINGS_MODULE = "shui.settings";

        STATIC_ROOT = "${cfg.dataDir}/static";
        MEDIA_ROOT = "${cfg.dataDir}/media";
      };

      serviceConfig = {

        User = cfg.user;
        Group = cfg.user;

        EnvironmentFile = cfg.settingsFile;

        ExecStart = ''
          ${cfg.package}/bin/gunicorn \
            shui.wsgi:application \
            --bind ${cfg.host}:${toString cfg.port}
        '';

        Restart = "always";
      };
    };
  };
}