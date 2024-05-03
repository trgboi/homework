import os
import logging
from collections import namedtuple

logging.basicConfig(filename='directory_info.log', level=logging.INFO, format='%(asctime)s - %(message)s',encoding='utf8')


FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def get_directory_info(directory_path):
    
    try:
        files = os.listdir(directory_path)
    except FileNotFoundError:
        logging.error(f"Директория {directory_path} не найдена")
        return None
    except Exception as e:
        logging.error(f"Ошибка при получении списка файлов: {e}")
        return None

   
    file_info_list = []
    for file in files:
        
        file_path = os.path.join(directory_path, file)
        
        name, extension = os.path.splitext(file)
       
        is_directory = os.path.isdir(file_path)
       
        parent_directory = os.path.basename(directory_path)
        
        file_info = FileInfo(name, extension, is_directory, parent_directory)
       
        file_info_list.append(file_info)
    return file_info_list

if __name__ == "__main__":
    directory_path = input("Введите путь до директории: ")
    directory_info = get_directory_info(directory_path)
    if directory_info:
        for i in directory_info:
            logging.info(i)