# INSTALL
- Crear carpeta data
- Exportar hoja tsv desde google sheets
- Ubicar y renombrar en data/tsv.tsv
- Crear una carpeta zip y colocar el archivo zip.zip enviado por correo

# EXECUTE
````
python export_gsheet_to_bb.py
````

- El archivo se genera en .zip
- Incluir res00001.dat en zip.zip
- Importar en BlackBoard

# Notas
- la hoja tsv tiene un caracter especial para importar adecuadamente los saltos de línea
- BlackBoard no soporta caracteres especiales html como texto.
