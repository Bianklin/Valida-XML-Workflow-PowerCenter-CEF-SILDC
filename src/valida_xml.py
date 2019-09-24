import os
import xml.etree.ElementTree as ET
import re

list_workflows_wrongs = []
def func_name_workflow(check_name_workflow):
    print('\n[WORKFLOW]\n')
    if re.search('FULL', check_name_workflow, re.IGNORECASE):
        valida_name_workflow = 'NO'
        global list_workflows_wrongs
        global name_workflow
        if name_workflow not in list_workflows_wrongs:
            list_workflows_wrongs.append(name_workflow)
    else:
        valida_name_workflow = 'YES'
    print(f'NOME DO WORKFLOW: {name_workflow:.<91}{valida_name_workflow}')


def func_var_workflow(check_var_workflow):
    name_workflowvariable = []
    var_workflow_all = '$$NU_WORKFLOW', '$$TipoCarga', '$$DT_PROC_WKF', '$$MascaraData_WKF', '$$NU_EXECUCAO_WKF', '$$URL_CONTROLE'
    for workflowvariable_field in check_var_workflow:
        if workflowvariable_field.get('NAME') in var_workflow_all:
            name_workflowvariable.append(workflowvariable_field.get('NAME'))
    for var_workflow in var_workflow_all:
        if var_workflow in name_workflowvariable:
            continue
        else:
            print(f'{var_workflow:.<109}NO')
            global list_workflows_wrongs
            global name_workflow
            if name_workflow not in list_workflows_wrongs:
                list_workflows_wrongs.append(name_workflow)


def func_name_worklet(check_name_worklet):
    name_worklet = check_name_worklet[:17]
    if re.findall(r'WKL_LDC_[1-9][0-9][0-9][0-9]_[0-9][0-9][0-9][0-9]', name_worklet):
        if re.search('FULL', check_name_worklet, re.IGNORECASE):
            valida_name_worklet = 'NO'
            global list_workflows_wrongs
            global name_workflow
            if name_workflow not in list_workflows_wrongs:
                list_workflows_wrongs.append(name_workflow)
        else:
            valida_name_worklet = 'YES'
        print(f'\nNOME: {check_name_worklet:.<103}{valida_name_worklet}')


def func_var_worklet(check_var_worklet):
    var_worklet_all = '$$URL_CONTROLE', '$$QT_PROCESSADOS', '$$QT_REJEITADOS', '$$DE_ARQUIVO_LOG', '$$DE_MENSAGEM_ERRO', '$$CO_ERRO', '$$NU_EXECUCAO_PROCESSO_WKL', '$$NU_MODULO', '$$NU_PROCESSO', '$$NU_EXECUCAO_WKL', '$$HadoopFileDir', '$$TipoCarga', '$$ScriptFileDir', '$$DE_FILTRO', '$$MascaraData_WKL', '$$DT_PROCESSAMENTO_WKL', '$$DT_PROC_FILE'
    for i in var_worklet_all:
        if i in check_var_worklet:
            continue
        else:
            print(f'- {i:.<107}NO')
            global list_workflows_wrongs
            global name_workflow
            if name_workflow not in list_workflows_wrongs:
                list_workflows_wrongs.append(name_workflow)


def func_name_var_wkf_wkl(check_name_var_wkf_wkl, check_value_var_wkf_wkl):
    var_attrib_worklet = ['$$NU_EXECUCAO_WKL', '$$URL_CONTROLE', '$$DT_PROCESSAMENTO_WKL', '$$MascaraData_WKL']
    var_attrib_workflow = ['$$NU_EXECUCAO_WKF', '$$URL_CONTROLE', '$$DT_PROC_WKF', '$$MascaraData_WKF']
    for i in range(len(var_attrib_worklet)):
        if check_name_var_wkf_wkl == var_attrib_worklet[i] and check_value_var_wkf_wkl == var_attrib_workflow[i]:
            var_attrib_workflow_worklet.append(var_attrib_worklet[i])
            var_attrib_workflow_worklet.append(var_attrib_workflow[i])


def func_var_attrib_workflow_worklet(check_var_attrib_workflow_worklet):
    var_attrib_worklet = ['$$NU_EXECUCAO_WKL', '$$URL_CONTROLE', '$$DT_PROCESSAMENTO_WKL', '$$MascaraData_WKL']
    var_attrib_workflow = ['$$NU_EXECUCAO_WKF', '$$URL_CONTROLE', '$$DT_PROC_WKF', '$$MascaraData_WKF']
    for i in var_attrib_worklet:
        if i in check_var_attrib_workflow_worklet:
            continue
        else:
            global list_workflows_wrongs
            global name_workflow
            if name_workflow not in list_workflows_wrongs:
                list_workflows_wrongs.append(name_workflow)
            print(f'--- {i:.<106}NO')
    for j in var_attrib_workflow:
        if j in check_var_attrib_workflow_worklet:
            continue
        else:
            valida_var_attrib = 'NO'
            if name_workflow not in list_workflows_wrongs:
                list_workflows_wrongs.append(name_workflow)
            print(f'--- {j:.<106}NO')

#Valida se nome da Assignment de atribuição de variáveis é "SSN_SETA_INICIO_PROCESSO"
def func_name_seta_inicio_processo(check_name_task_worklet):
    type = check_name_task_worklet.get('TYPE')
    name = check_name_task_worklet.get('NAME')
    if type == "Assignment":
        if name.startswith('SSN_SETA_RESULTS'):
            return
        if name == 'SSN_SETA_INICIO_PROCESSO':
            print(f'- {name:.<106}YES')
        else:
            global list_workflows_wrongs
            global name_workflow
            if name_workflow not in list_workflows_wrongs:
                list_workflows_wrongs.append(name_workflow)
            print(f'- {name:.<106}NO')
    return

#Valida nomes e valores das variáveis da Assignment "SSN_SETA_INICIO_PROCESSO"
def func_values_seta_inicio_processo(check_name_task_worklet):
    list_of_valid_names_valuepair = ['$$NU_MODULO', '$$NU_PROCESSO', '$$NU_EXECUCAO_PROCESSO_WKL', '$$DE_FILTRO', '$$DT_PROC_FILE']
    name_task = check_name_task_worklet.get('NAME')
    if name_task == 'SSN_SETA_INICIO_PROCESSO':
        for i_name_valuepair in check_name_task_worklet.iter('VALUEPAIR'):
            name_valuepair = i_name_valuepair.get('NAME')
            value_valuepair = i_name_valuepair.get('VALUE')
            if name_valuepair in list_of_valid_names_valuepair:
                if name_valuepair == list_of_valid_names_valuepair[0] and re.search(r'\d{4}', value_valuepair):
                    continue
                if name_valuepair == list_of_valid_names_valuepair[1] and re.search(r'\d{1,2}', value_valuepair):
                    continue
                if name_valuepair == list_of_valid_names_valuepair[2] and value_valuepair == '0':
                    continue
                if name_valuepair == list_of_valid_names_valuepair[3] and (value_valuepair.startswith("IIF($$TipoCarga = 'incr',") or value_valuepair == "'1=1'"):
                    continue
                if name_valuepair == list_of_valid_names_valuepair[4] and value_valuepair == "TO_CHAR(TO_DATE($$DT_PROCESSAMENTO_WKL,$$MascaraData_WKL),'YYYYMMDDHH24MISS')":
                    continue
                global list_workflows_wrongs
                global name_workflow
                if name_workflow not in list_workflows_wrongs:
                    list_workflows_wrongs.append(name_workflow)
                print(f'-- {name_valuepair:.<106}NO')
            else:
                if name_workflow not in list_workflows_wrongs:
                    list_workflows_wrongs.append(name_workflow)
                print(f'-- {name_valuepair:.<106}NO')
    return

# Valida nomes e valores das variáveis da Assignment "SSN_SETA_RESULTS"
def func_name_and_values_seta_results(check_name_task_worklet,name_table_of_seta_results):
    list_of_valid_names_valuepair = ['$$QT_PROCESSADOS', '$$QT_REJEITADOS', '$$DE_MENSAGEM_ERRO', '$$DE_ARQUIVO_LOG']
    name_task_of_worklet = check_name_task_worklet.get('NAME')
    if name_task_of_worklet.startswith('SSN_SETA_RESULTS'):
        print(f'- {name_task_of_worklet:.<106}YES')
        for i_name_valuepair in check_name_task_worklet.iter('VALUEPAIR'):
            name_valuepair = i_name_valuepair.get('NAME')
            value_valuepair = i_name_valuepair.get('VALUE')
            if name_valuepair in list_of_valid_names_valuepair:
                if name_valuepair == list_of_valid_names_valuepair[0] and re.search(r'\$SSN_LDC_\d{4}_\d{4}_'+name_table_of_seta_results+'\.TgtSuccessRows', value_valuepair):
                    continue
                if name_valuepair == list_of_valid_names_valuepair[1] and re.search(r'\$SSN_LDC_\d{4}_\d{4}_'+name_table_of_seta_results+'\.TgtFailedRows', value_valuepair):
                    continue
                if name_valuepair == list_of_valid_names_valuepair[2] and re.search(r'\$SSN_LDC_\d{4}_\d{4}_'+name_table_of_seta_results+'\.FirstErrorMsg', value_valuepair):
                    continue
                if name_valuepair == list_of_valid_names_valuepair[3] and re.search(r'\$SSN_LDC_\d{4}_\d{4}_'+name_table_of_seta_results+'\.ErrorMsg', value_valuepair):
                    continue
                global list_workflows_wrongs
                global name_workflow
                if name_workflow not in list_workflows_wrongs:
                    list_workflows_wrongs.append(name_workflow)
                print(f'-- {name_valuepair:.<106}NO')
            else:
                if name_workflow not in list_workflows_wrongs:
                    list_workflows_wrongs.append(name_workflow)
                print(f'-- {name_valuepair:.<106}NO')
    return

#Valida links entre sessions
def func_link_between_sessions(workflowlink,name_table_session,ic_partitioned1):
    fromtask = workflowlink.get('FROMTASK')
    totask = workflowlink.get('TOTASK')
    condition = workflowlink.get('CONDITION')
    condition_standard_is_ok = re.search('\$SSN_LDC_0000_0000_INICIO_PROCESSO\.TgtSuccessRows\s{0,1}>\s{0,1}0\s{0,1}\r\nAND\r\n\$SSN_LDC_0000_0000_INICIO_PROCESSO\.Status\s{0,1}=\s{0,1}Succeeded',condition)
    partitioned_full_is_ok = re.search('\$SSN_LDC_0000_0000_INICIO_PROCESSO\.TgtSuccessRows\s{0,1}>\s{0,1}0\s{0,1}\r\nAND\r\n\$SSN_LDC_0000_0000_INICIO_PROCESSO\.Status\s{0,1}=\s{0,1}Succeeded\r\nAND\r\n\$\$TipoCarga\s{0,1}=\s{0,1}\'full\'',condition)
    partitioned_diff_is_ok = re.search('\$SSN_LDC_0000_0000_INICIO_PROCESSO\.TgtSuccessRows\s{0,1}>\s{0,1}0\s{0,1}\r\nAND\r\n\$SSN_LDC_0000_0000_INICIO_PROCESSO\.Status\s{0,1}=\s{0,1}Succeeded\r\nAND\r\n\$\$TipoCarga\s{0,1}=\s{0,1}\'diff\'',condition)
    partitioned_incr_is_ok = re.search('\$SSN_LDC_0000_0000_INICIO_PROCESSO\.TgtSuccessRows\s{0,1}>\s{0,1}0\s{0,1}\r\nAND\r\n\$SSN_LDC_0000_0000_INICIO_PROCESSO\.Status\s{0,1}=\s{0,1}Succeeded\r\nAND\r\n\$\$TipoCarga\s{0,1}=\s{0,1}\'incr\'',condition)
    if fromtask == 'SSN_LDC_0000_0000_INICIO_PROCESSO' and name_table_session in totask:
        if ic_partitioned1 and ('_FULL' in totask or '_INC' in totask):
            if partitioned_full_is_ok or partitioned_diff_is_ok or partitioned_incr_is_ok:
                return
            else:
                global list_workflows_wrongs
                global name_workflow
                if name_workflow not in list_workflows_wrongs:
                    list_workflows_wrongs.append(name_workflow)
                print(f'-- Link da {fromtask:.<99}NO')
    
        elif condition_standard_is_ok:
            return
        else:
            if name_workflow not in list_workflows_wrongs:
                list_workflows_wrongs.append(name_workflow)
            print(f'-- Link da {fromtask:.<99}NO')
    return

#Valida nomenclaturas e opções das sessions principais, bem como valores de links entre sessions
def func_name_and_values_session(session, name_session, name_table_of_session,ic_partitioned2,modulo_and_processo_worklet):
    if name_table_of_session in name_session:
        if '_FULL' in name_session or '_INC' in name_session:
            if ic_partitioned2:
                print(f'- {name_session:.<106}YES')
            else:
                global list_workflows_wrongs
                global name_workflow
                if name_workflow not in list_workflows_wrongs:
                    list_workflows_wrongs.append(name_workflow)
                print(f'- {name_session:.<106}NO')
        elif re.search(r'SSN_LDC_' + modulo_and_processo_worklet + name_table_of_session, name_session):
            print(f'- {name_session:.<106}YES')

        #Valida se "Fail task and continue workflow" está macado em "General"- Localização 'WORKFLOW/WORKLET/SESSION/ATTRIBUTE'
        for session_atribute in session.iter('ATTRIBUTE'):
            name_atribute = session_atribute.get('NAME')
            value_atribute = session_atribute.get('VALUE')
            if name_atribute == 'Recovery Strategy':
                if value_atribute == 'Fail task and continue workflow':
                    continue
                else:
                    if name_workflow not in list_workflows_wrongs:
                        list_workflows_wrongs.append(name_workflow)
                    print(f'-- {value_atribute:.<106}NO')

        # Valida se "Session timestamp" está em "Config Object"- Localização 'WORKFLOW/WORKLET/SESSION/CONFIGREFERENCE'
        for session_config in session.iter('CONFIGREFERENCE'):
            # Localização 'WORKFLOW/WORKLET/SESSION/CONFIGREFERENCE/ATTRIBUTE'
            for config_atribute in session_config.iter('ATTRIBUTE'):
               name_config_atribute = config_atribute.get('NAME')
               value_config_atribute = config_atribute.get('VALUE')
               if name_config_atribute == 'Save session log by':
                   if value_config_atribute == 'Session timestamp':
                       continue
                   else:
                       if name_workflow not in list_workflows_wrongs:
                           list_workflows_wrongs.append(name_workflow)
                       print(f'-- {value_config_atribute:.<106}NO')

        # Valida sintaxe da post-session e se "Fail task if any command fails" = "YES" - Localização 'WORKFLOW/WORKLET/SESSION/SESSIONCOMPONENT'
        for session_component in session.iter('SESSIONCOMPONENT'):
            name_component = session_component.get('REFOBJECTNAME')
            if name_component == 'post_session_success_command':
                # Localização 'WORKFLOW/WORKLET/SESSION/SESSIONCOMPONENT/TASK'
                for component_task in session_component.iter('TASK'):
                    # Localização 'WORKFLOW/WORKLET/SESSION/SESSIONCOMPONENT/TASK/ATTRIBUTE'
                    for task_atribute in component_task.iter('ATTRIBUTE'):
                        name_task_atribute = task_atribute.get('NAME')
                        value_task_atribute = task_atribute.get('VALUE')
                        if name_task_atribute == 'Fail task if any command fails':
                            if value_task_atribute == 'YES':
                                continue
                            else:
                                if name_workflow not in list_workflows_wrongs:
                                    list_workflows_wrongs.append(name_workflow)
                                print(f'-- Post-session {name_task_atribute:.<93}NO')
                    # Localização 'WORKFLOW/WORKLET/SESSION/SESSIONCOMPONENT/TASK/VALUEPAIR'
                    for task_valuepair in component_task.iter('VALUEPAIR'):
                        name_task_valuepair = task_valuepair.get('NAME')
                        value_task_valuepair = task_valuepair.get('VALUE')
                        #if name_task_valuepair == 'COMMAND':  desativado, pois o nome da COMMAND pode ser outro
                        part = re.search(r'\$\$ScriptFileDir/rename-hadoop.sh \$\$HadoopFileDir \$\$TipoCarga '+name_table_of_session.lower()+' tgt_ldc_'+name_table_of_session.lower()+'\.out part \$\$DT_PROC_FILE', value_task_valuepair)
                        incr = re.search(r'\$\$ScriptFileDir/rename-hadoop.sh \$\$HadoopFileDir \$\$TipoCarga '+name_table_of_session.lower()+' tgt_ldc_'+name_table_of_session.lower()+'\.out incr \$\$DT_PROC_FILE', value_task_valuepair)
                        diff = re.search(r'\$\$ScriptFileDir/rename-hadoop.sh \$\$HadoopFileDir \$\$TipoCarga '+name_table_of_session.lower()+' tgt_ldc_'+name_table_of_session.lower()+'\.out diff \$\$DT_PROC_FILE', value_task_valuepair)
                        off = re.search(r'\$\$ScriptFileDir/rename-hadoop.sh \$\$HadoopFileDir \$\$TipoCarga '+name_table_of_session.lower()+' tgt_ldc_'+name_table_of_session.lower()+'\.out off \$\$DT_PROC_FILE', value_task_valuepair)
                        if part or incr or diff or off or value_task_valuepair.startswith('cat') or value_task_valuepair.startswith('rm'):
                            continue
                        else:
                            if name_workflow not in list_workflows_wrongs:
                                list_workflows_wrongs.append(name_workflow)
                            print(f'-- Post-session {name_task_valuepair:.<92}NO')
    for session_atribute in session.iter('ATTRIBUTE'):
        name_atribute = session_atribute.get('NAME')
        value_atribute = session_atribute.get('VALUE')
        if name_atribute == 'Session Log File Name':
            name_log = name_session[18:]
            if re.search(r'SSN_LDC_' + modulo_and_processo_worklet + '_' + name_log + '\.log', value_atribute):
                continue
            else:
                if name_workflow not in list_workflows_wrongs:
                    list_workflows_wrongs.append(name_workflow)
                print(f'-- {value_atribute:.<106}NO')
    return


all_original_files = os.listdir('../XML/')
for each_original_file in all_original_files:
    tree = ET.parse('../XML/'+each_original_file)
    root = tree.getroot()

    # Localização 'WORKFLOW'
    for workflow_field in root.iter('WORKFLOW'):
        name_workflow = workflow_field.get('NAME')
        func_name_workflow(name_workflow)

        # Localização 'WORKFLOW/WORKFLOWVARIABLE'
        func_var_workflow(workflow_field.findall('./WORKFLOWVARIABLE'))

        # Localização 'WORKFLOW/TASKINSTANCE'
        for taskinstance_field in workflow_field.iter('TASKINSTANCE'):

            # Localização 'WORKFLOW/TASKINSTANCE/VALUEPAIR'
            var_attrib_workflow_worklet = []
            for valuepair_field in taskinstance_field.iter('VALUEPAIR'):
                name_var_wkf_wkl = valuepair_field.get('NAME')
                value_var_wkf_wkl = valuepair_field.get('VALUE')
                func_name_var_wkf_wkl(name_var_wkf_wkl, value_var_wkf_wkl)
            if len(var_attrib_workflow_worklet) > 0:
                func_var_attrib_workflow_worklet(var_attrib_workflow_worklet)
        print('\n[WORKLET(S)]')

        # Localização 'WORKFLOW/WORKLET'
        for worklet_field in workflow_field.iter('WORKLET'):
            name_worklet = worklet_field.get('NAME')
            nu_modulo_and_nu_processo_worklet = name_worklet[8:17]
            name_table = name_worklet[18:]
            ic_worklet_is_partitioned = False
            cont_seta_results = 0
            func_name_worklet(name_worklet)
            name_worklet_workflowvariable_field = []

            # Localização 'WORKFLOW/WORKLET/TASK'
            for task_worklet_field in worklet_field.iter('TASK'):
                name_task = task_worklet_field.get('NAME')
                func_name_seta_inicio_processo(task_worklet_field)
                func_values_seta_inicio_processo(task_worklet_field)
                func_name_and_values_seta_results(task_worklet_field, name_table)
                if name_task.startswith('SSN_SETA_RESULTS'):
                    cont_seta_results += 1
                if cont_seta_results == 2:  # Se a worklet possui duas seta_results, é particionada
                    ic_worklet_is_partitioned = True

            # Localização 'WORKFLOW/WORKLET/WORKFLOWVARIABLE'
            for worklet_workflowvariable_field in worklet_field.iter('WORKFLOWVARIABLE'):
                name_worklet_workflowvariable_field.append(worklet_workflowvariable_field.get('NAME'))
            func_var_worklet(name_worklet_workflowvariable_field)

            # Localização 'WORKFLOW/WORKLET/WORKFLOWLINK'
            for worklet_workflowlink_field in worklet_field.iter('WORKFLOWLINK'):
                func_link_between_sessions(worklet_workflowlink_field,name_table,ic_worklet_is_partitioned)

            # Localização 'WORKFLOW/WORKLET/SESSION'
            for worklet_session_field in worklet_field.iter('SESSION'):
                name_session_field = worklet_session_field.get('NAME')
                func_name_and_values_session(worklet_session_field, name_session_field, name_table,ic_worklet_is_partitioned,nu_modulo_and_nu_processo_worklet)

    print('\n#############################################################################################################')
total=len(list_workflows_wrongs)
print('TOTAL DE WORKFLOWS FORA DO PADRÃO: ' + str(total))
print('\n')
print('NOMES DOS WORKFLOWS: '+ str(list_workflows_wrongs))
