Generación de .zip para importar en banco de preguntas de blackboard

# INSTALL
- Crear carpeta data
- Exportar hoja tsv desde google sheets
  - Verificar que no haya saltos de línea repetidos.
- Ubicar en data/

# CONFIG
- actualizar en 
````
test_name = "TEST_202102_XX"
test_instructions = "TEST_INSTRUCCIONES"
test_description = "TEST_DESCRIPCIÓN"

file_input = "data/evaluations 202102 - tsv XX.tsv"
````

# EXECUTE
````
python export_gsheet_to_bb.py
````

- El archivo zip2.zip se genera en zip2
- Importar en BlackBoard

# USE
- Ir a Herramientas del curso/Banco de preguntas
  - Clic en Importar banco de preguntas
  - Cargar archivo zip2.zip
- Ir a Evaluaciones y envíos de trabajos, y crear un examen
  - Definir examen
  - En lienzo del examen, clic en Reutilizar pregunta/Buscar preguntas
    - Seleccionar el banco importado en el panel lateral
    - Clic en Mostrar todos
    - Seleccionar todos y clic en Enviar

# Notas
- la hoja tsv tiene un caracter especial para importar adecuadamente los saltos de línea
- BlackBoard no soporta caracteres especiales html como texto.


# TO DO
- Fix Error KeyError: '\\L', KeyError: '\\A' cuando se usa  \