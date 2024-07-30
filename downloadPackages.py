# downloadPackages.py
import argostranslate.package

# Lista de traducciones necesarias
translation_pairs = [
    ("en", "es"),
    ("en", "pt"),
    ("en", "fr")
]

# Descargar e instalar los paquetes
for from_code, to_code in translation_pairs:
    available_packages = argostranslate.package.get_available_packages()
    available_package = next(
        filter(
            lambda x: x.from_code == from_code and x.to_code == to_code,
            available_packages
        ),
        None
    )
    if available_package:
        download_path = available_package.download()
        argostranslate.package.install_from_path(download_path)
