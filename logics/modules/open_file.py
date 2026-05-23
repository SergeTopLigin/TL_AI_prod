'''
открытие файла из каталога
форматы: .txt, .json
file_dir = каталог размещения файла.
file_name = имя файла с расширением (пр: example.txt).
'''
def open_file(file_dir, file_name):
    
    try:

        # определение каталога файла
        if file_dir == "cache":
            path = "cache/"
        elif file_dir == "sub_results":
            path = "cache/sub_results/"
        elif file_dir == "club_sets":
            path = "cache/sub_results/club_sets/"
        elif file_dir == "data_conversion":
            path = "data_conversion/"
        elif file_dir == "support":
            path = "support/"
        elif file_dir == "input_data":
            path = "cache/input_data/"
        elif file_dir == "bug_files":
            path = "bug_files/"
        elif file_dir == "standings_history":
            path = "cache/standings_history/"
        elif file_dir == "round_standings":
            path = "cache/sub_results/round_standings/"
        elif file_dir == "tourn_standings":
            path = "cache/sub_results/tourn_standings/"
        elif file_dir == "nat_cup_round_ratings":
            path = "cache/sub_results/nat_cup_round_ratings/"
            
        # открытие файла
        import os
        with open((os.path.abspath(__file__))[:-27]+path+file_name, 'r', encoding='utf-8') as f:
            if file_name[-3:] == 'txt':
                file_content = f.read()
            elif file_name[-4:] == 'json':
                import json
                file_content = json.load(f)

        return(file_content)
            
    except:

        # запись ошибки/исключения в переменную
        import traceback
        bug_info = traceback.format_exc()

        import os
        mod_name = os.path.basename(__file__)[:-3]
        try:    # доступ к модулям при main в logics/
            from modules.bug_file import bug_file
            from modules.bug_alert import bug_alert
        except:    # доступ к модулям из модуля
            from bug_file import bug_file
            from bug_alert import bug_alert
        # создание bug_file
        bug_file(mod_name, bug_info)
        # отправка уведомления bug_info
        bug_alert(mod_name, bug_info)