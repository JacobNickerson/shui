{ lib,
  python312,
  python312Packages
}:

python312Packages.buildPythonApplication rec {
  pname = "shui";
  version = "0.1.0";

  src = lib.cleanSource ./.;

  pyproject = true;

  build-system = with python312Packages; [
    setuptools
  ];

  dependencies = with python312Packages; [
    django
    psycopg
    psycopg2-binary
    python-dotenv
    pillow
    gunicorn
    boto3
    django-storages
    django-cleanup
  ];

  doCheck = false;

  meta = with lib; {
    description = "Django inventory application";
    license = licenses.mit;
    platforms = platforms.linux;
  };
}