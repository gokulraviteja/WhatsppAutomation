import time
import keyboard
from selenium import webdriver
from time import strftime
a=[]
b=[]
driver = webdriver.Chrome('C:\\Users\\username\\Desktop\\auto\\chromedriver.exe')
driver.get('https://web.whatsapp.com/')
input('Enter anything after scanning QR code')

def fun1():

    print("WHOM SHOULD I SEND : \n")
    s1=input()
    while(s1[0] in '$@'):
        s1=s1[1:]
        
    print("WHAT SHOULD I SEND : \n")
    s2=input()
    while(s2[0] in '$@'):
        s2=s2[1:]
        
    print("ON WHICH DATE SHOULD I SEND :  day-month-year \n")
    s3=input().split('-')
    while(s3[0][0] in '$@'):
        s3[0]=s3[0][1:]
    
    print("ON WHAT TIME SHOULD I SEND :  HH-MM-SS \n")
    s4=input().split('-')
    while(s4[0][0] in '$@'):
        s4[0]=s4[0][1:]
        
    
    print("request recorded")
    return [s1,s2,s3,s4]
    kk=s3[1]+s3[0]+s3[2]+' '+s4[0]+s4[1]+s4[2]
    


b=[['Amma Airtel',"GOOD EVENING",[],['17','00','11']],
   ['Amma New',"GOOD EVENING",[],['17','00','13']],
   ['Amma Airtel',"GOOD NIGHT",[],['22','00','11']],
   ['Amma New',"GOOD NIGHT",[],['22','00','13']],
   ['Amma Airtel',"GOOD MORNING",[],['07','00','11']],
   ['Amma New',"GOOD MORNING",[],['07','00','13']],
   ['Amma Airtel',"GOOD AFTERNOON",[],['12','00','11']],
   ['Amma New',"GOOD AFTERNOON",[],['12','00','13']],
   ['XXX',"GOOD EVENING -- XXX",[],['17','00','15']],
   ['XXX',"XXX",[],['22','00','15']],
   ['XXX',"GOOD NIGHT -- XXX",[],['12','00','13']],
   ['XXX',"GOOD MORNING --XXX",[],['07','00','15']],
   ['XXX',"GOOD AFTERNOON --XXX",[],['12','00','15']]
   ]



while(True):
    k=strftime("%S")
    if(int(k)%35==0 and int(k)!=0):
        print("press @ to show all remainders -BE FAST\n")
        s=''
        t_end=time.time()+5
        while(time.time()<t_end):
            if(keyboard.is_pressed('@')):
                if(a==[]):
                    print(a)
                    break
                for i in a:
                    print(i)
                break
            else:
                pass
        
    if(int(k)%60==0):
        
        print("press $ to keep remainder -BE FAST\n")
        s=''
        t_end=time.time()+10
        while(time.time()<t_end):
            if(keyboard.is_pressed('$')):
                s=fun1()
                break
            else:
                pass
        if(s!=''):
            s[3][2]=str(int(s[3][2])+10)
            a.append(s)
    else:
        for i in a:
            s3=i[2]
            s4=i[3]
            kk=s3[1]+s3[0]+s3[2]+' '+s4[0]+s4[1]+s4[2]
            
            if(kk==strftime("%m%d%Y %H%M%S")):
                user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(i[0]))
                user.click()
                msg_box = driver.find_element_by_class_name('_2S1VP')
                msg_box.send_keys(i[1])
                button = driver.find_element_by_class_name('_35EW6')
                button.click()
                print()
                print("---------------------------------")
                print("YOUR MSG SENT TO : "+str(i[0]))
                print("---------------------------------")
                print()
                a.remove(i)
                time.sleep(1)
        for i in b:
            s3=i[2]
            s4=i[3]
            kk=s4[0]+s4[1]+s4[2]
            
            if(kk==strftime("%H%M%S")):
                user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(i[0]))
                user.click()
                msg_box = driver.find_element_by_class_name('_2S1VP')
                msg_box.send_keys(i[1])
                button = driver.find_element_by_class_name('_35EW6')
                button.click()
                print()
                print("---------------------------------")
                print("YOUR MSG SENT TO : "+str(i[0]))
                print("---------------------------------")
                print()
                
                time.sleep(1)
        
            

        
        
    
            
    

