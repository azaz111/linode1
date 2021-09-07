import os
import time



i = 0
while i < 1:
        time.sleep(30)
        
        fnon = open("/root/aknomber.txt", "r") 
        ns = fnon.readlines()
        print(f"Imya Servera  :'{ns}'")
        
        sozd = '/root/aknomber.txt' # Это файл даты создания
        t2 = os.path.getctime(sozd ) 
        print (f"Sozdan : ' {time.ctime(t2)} '")
        
        sub = ": Deleted"   # Слово для поиска
        
        sfa = open("/root/rclone1.log", "r") 
        str1 = sfa.read()
        rcl1= str1.count(sub)
        #print(f"Переданно плотов 1:'{rcl1}'")
        
        sfa = open("/root/rclone2.log", "r") 
        str2 = sfa.read()
        rcl2= str2.count(sub)
        #print(f"Переданно плотов 2:'{rcl2}'")
        
        print(f"Plotov peredanno VSEGO  :'{rcl2+rcl2}'")
        
        files = os.listdir(path="/disk3/video")
        plot1 = len(files)
        files2 = os.listdir(path="/disk3/video1")
        plot2 = len(files2)
        print(f"Plotov na SERVERE : '{plot1+plot2}'")
        
        path = '/disk2/vid2' # Это путь к файлу который часто обновляется 
        t = os.path.getmtime(path) # дата последнего изменения файла она же дата конекта
        print (f"Poslednii raz v seti : ' {time.ctime(t)} '")
        #t1 = os.path.getmtime(file) # дата последнего изменения файла 
        
        #t2 = os.path.getctime(file) # дата создания файла - мой мониторинг даты старта
        
        files32 = os.listdir(path="/aws32")
        plot_vs = len(files32)
        print (f"Na diske PLOTOV  : ' {plot_vs} '")
        #t2=1629754844.820516
        
        #if (time.time() - t) < 600 :
        #    print("Текущий статус : 'Online'")
        #else:
        #    print('Текущий статус : "Off-line"')
        
        #sub = input('Please enter a sub-string:\n') 
        
        
        
        lines = [f"Imya Servera  :'{ns}'", f"Sozdan : ' {time.ctime(t2)} '", f"Переданно VSEGO  :'{rcl2+rcl2}'", f"Сейчас непереданно плотов: '{plot1+plot2}'" , f"Последнй раз в сети : ' {time.ctime(t)} '" , f"Na diske PLOTOV  : ' {plot_vs} '" ]
        with open(f"/aws32/Otchet-{ns}.txt", "w") as filef:
            for  line in lines:
                filef.write(line + '\n')
                #file.close()