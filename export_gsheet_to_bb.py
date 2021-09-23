import os
from os import walk
import pathlib
import zipfile
import re
import html

test_name = "TEST_202102_XX"
test_instructions = "TEST_INSTRUCCIONES"
test_description = "TEST_DESCRIPCIÓN"

file_input = "data/evaluations 202102 - tsv XX.tsv"

def replace(search, replace, subject):
    p = re.compile(search)
    return p.sub(replace, subject)

def replace_arr(search, replace, subject):
    result = subject
    for i, _search in enumerate(search):
        p = re.compile(_search)
        result = p.sub(replace[i], result)
    return result
def escape_html(text):
    text = html.escape(text)
    text = text.replace("\r", "<br>")
    return html.escape("<span style=\"white-space: pre;\">" + text + "</span>")

mode = "2"
tpl = "tpl" + mode
tpl_res = tpl + "/res00001.tpl"
tpl_item = tpl + "/item.tpl" 
tpl_answer_flow_label = tpl + "/answer_flow_label.tpl" 
tpl_answer_respcondition_error = tpl + "/answer_respcondition_error.tpl"
tpl_answer_itemfeedback_error = tpl + "/answer_itemfeedback_error.tpl"

_zip = "zip" + mode
file_output = _zip + "/res00001.dat"

f_input = open(file_input, "r", encoding="utf8", newline="\r\n")
f_questions = f_input.readlines()

t_res = open(tpl_res, "r")
t_res_content = replace("\s{2,}|\n", "", t_res.read())
t_item = open(tpl_item, "r")
t_item_content = t_item.read()
t_item_content = re.sub(r"\n\s*", "", t_item_content, flags=re.UNICODE)
t_answer_flow_label = open(tpl_answer_flow_label, "r")
t_answer_flow_label_content = t_answer_flow_label.read()
t_answer_respcondition_error = open(tpl_answer_respcondition_error, "r")
t_answer_respcondition_error_content = t_answer_respcondition_error.read()
t_answer_itemfeedback_error = open(tpl_answer_itemfeedback_error, "r")
t_answer_itemfeedback_error_content = t_answer_itemfeedback_error.read()

IDS = ["87f3e776dcd849279accc371a0284d5f", 
"7821820a6f024fbda4c3ed32c0833b1c",
"066c184798b94bb8a94d2d2755727b53", 
"ddf7196a8e934bf1b2c95e8fbd9ac205", 
"bf7ed082a4be41a39bb4cf71df8d82f8"]

items = []

# set ITEM
for line, f_question in enumerate(f_questions):
    if line == 0:
        continue
    SEPARATOR = "\t"
    question = f_question.strip().split(SEPARATOR)

    flows = []
    respconditions = []
    itemfeedbacks = []
    COLUMN_QUESTION_ID = 0
    COLUMN_QUESTION = 2
    COLUMN_ANSWER = 3
    
    for index in range(5):
        if COLUMN_ANSWER + index >= len(question):
            continue
        answer = question[COLUMN_ANSWER + index]
        
        if len(answer.strip()):
            answer_flow_label = replace_arr(
                ['___IDENT___', '___ANSWER___'], 
                [IDS[index], escape_html(answer)], 
                t_answer_flow_label_content
            )
            answer_respcondition_error = replace(
                '___IDENT___', IDS[index],
                t_answer_respcondition_error_content
            )
            answer_itemfeedback_error = replace(
                '___IDENT___', IDS[index],
                t_answer_itemfeedback_error_content
            )
            flows.append(answer_flow_label)
            respconditions.append(answer_respcondition_error)
            itemfeedbacks.append(answer_itemfeedback_error)

    if COLUMN_QUESTION >= len(question):
        continue
    UNIFIER = ""
    question_text = question[COLUMN_QUESTION]
    question_id = question[COLUMN_QUESTION_ID]
    
    question_title = question_text
    item = replace_arr(
        ['___QUESTION_TITLE___', '___QUESTION_TEXT___', '___IDENT_OK___',
        '___FLOW_LABELS___', 
        '___respcondition_errors___', '___itemfeedback_errors___'], 
        [question_id,escape_html(question_text), 
        IDS[0],
        UNIFIER.join(flows), 
        UNIFIER.join(respconditions), 
        UNIFIER.join(itemfeedbacks)
        ],
        t_item_content
    )
    items.append(item)
    #print(question_id)

res = replace_arr(
    ['___NAME___', '___INSTRUCTIONS___', '___DESCRIPTION___', 
    '___ITEMS___'],
    [test_name, test_instructions, test_description,
    UNIFIER.join(items)],
    t_res_content
)

f_input.close()
t_res.close()
t_answer_flow_label.close()
t_answer_itemfeedback_error.close()
t_answer_respcondition_error.close()

f_output = open (file_output, 'w', encoding="utf8")
f_output.write(res)
f_output.close()

zip_file = os.path.join(_zip, _zip + ".zip")
if os.path.exists(zip_file):
    os.remove(zip_file)

zipf = zipfile.ZipFile(zip_file, 'w', zipfile.ZIP_DEFLATED)
for root, dirs, files in os.walk(_zip):
    for file in files:
        if not (pathlib.Path(file).suffix == ".zip"):
            zipf.write(
                os.path.join(root, file),
                os.path.relpath(os.path.join(root, file), os.path.join(_zip))
            )
    for diri in dirs:
        zipf.write(
            os.path.join(root, diri),
            os.path.relpath(os.path.join(root, diri), os.path.join(_zip))
        )

zipf.close()