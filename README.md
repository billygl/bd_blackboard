Generación de .zip para importar en banco de preguntas de blackboard

# INSTALL
- Crear carpeta data
- Exportar hoja tsv desde google sheets
- Ubicar y renombrar en data/tsv.tsv
- Crear una carpeta zip2 y colocar el archivo zip2.zip enviado por correo

# EXECUTE
````
python export_gsheet_to_bb.py
````

- El archivo se genera en zip2
- Incluir res00001.dat en zip2.zip
- Importar en BlackBoard

# Notas
- la hoja tsv tiene un caracter especial para importar adecuadamente los saltos de línea
- BlackBoard no soporta caracteres especiales html como texto.
