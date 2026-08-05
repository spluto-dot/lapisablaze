from pathlib import Path
import shutil

PASTA = Path(".")  # Pasta atual

for extensao in ("*.html", "*.htm"):
    for arquivo in PASTA.rglob(extensao):

        # Backup
        backup = arquivo.with_suffix(arquivo.suffix + ".bak")
        if not backup.exists():
            shutil.copy2(arquivo, backup)

        # Lê como Windows-1252
        texto = arquivo.read_text(encoding="windows-1252")

        # Troca o charset
        texto = texto.replace(
            '<meta charset="windows-1252">',
            '<meta charset="UTF-8">'
        )

        # Salva em UTF-8
        arquivo.write_text(texto, encoding="utf-8")

        print("Convertido:", arquivo)

print("\nConcluído!")