<item title="___QUESTION_TITLE___" maxattempts="0"><itemmetadata><bbmd_asi_object_id>_2085721_1</bbmd_asi_object_id><bbmd_asitype>Item</bbmd_asitype><bbmd_assessmenttype>Pool</bbmd_assessmenttype><bbmd_sectiontype>Subsection</bbmd_sectiontype><bbmd_questiontype>Multiple Choice</bbmd_questiontype><bbmd_is_from_cartridge>false</bbmd_is_from_cartridge><bbmd_is_disabled>false</bbmd_is_disabled><bbmd_negative_points_ind>N</bbmd_negative_points_ind><bbmd_canvas_fullcrdt_ind>false</bbmd_canvas_fullcrdt_ind><bbmd_all_fullcredit_ind>false</bbmd_all_fullcredit_ind><bbmd_numbertype>letter_lower</bbmd_numbertype><bbmd_partialcredit>false</bbmd_partialcredit><bbmd_orientationtype>vertical</bbmd_orientationtype><bbmd_is_extracredit>false</bbmd_is_extracredit><qmd_absolutescore_max>1.000000000000000</qmd_absolutescore_max><qmd_weighting>0</qmd_weighting><qmd_instructornotes></qmd_instructornotes></itemmetadata><presentation><flow class="Block"><flow class="QUESTION_BLOCK"><flow class="FORMATTED_TEXT_BLOCK"><material><mat_extension><mat_formattedtext type="HTML">&lt;p&gt;___QUESTION_TEXT___&lt;/p&gt;</mat_formattedtext></mat_extension></material></flow></flow><flow class="RESPONSE_BLOCK"><response_lid ident="response" rcardinality="Single" rtiming="No"><render_choice shuffle="Yes" minnumber="0" maxnumber="0">___FLOW_LABELS___</render_choice></response_lid></flow></flow></presentation><resprocessing scoremodel="SumOfScores"><outcomes><decvar varname="SCORE" vartype="Decimal" defaultval="0" minvalue="0" maxvalue="1.00000"/></outcomes>
    <respcondition title="correct"><conditionvar><varequal respident="response" case="No">___IDENT_OK___</varequal></conditionvar><setvar variablename="SCORE" action="Set">SCORE.max</setvar><displayfeedback linkrefid="correct" feedbacktype="Response"/></respcondition><respcondition title="incorrect"><conditionvar><other/></conditionvar><setvar variablename="SCORE" action="Set">0</setvar><displayfeedback linkrefid="incorrect" feedbacktype="Response"/></respcondition>
    <respcondition><conditionvar><varequal respident="___IDENT_OK___" case="No"/></conditionvar><setvar variablename="SCORE" action="Set">100</setvar><displayfeedback linkrefid="___IDENT_OK___" feedbacktype="Response"/></respcondition>
    ___respcondition_errors___
</resprocessing>
    <itemfeedback ident="correct" view="All"><flow_mat class="Block"><flow_mat class="FORMATTED_TEXT_BLOCK"><material><mat_extension><mat_formattedtext type="HTML"/></mat_extension></material></flow_mat></flow_mat></itemfeedback>
    <itemfeedback ident="incorrect" view="All"><flow_mat class="Block"><flow_mat class="FORMATTED_TEXT_BLOCK"><material><mat_extension><mat_formattedtext type="HTML"/></mat_extension></material></flow_mat></flow_mat></itemfeedback>
    ___itemfeedback_errors___
</item>