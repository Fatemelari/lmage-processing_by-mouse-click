import cv2                                                               #opencvکردن کتابخانه import
import numpy as np                                                       #numpy کردن کتابخانه import


def draw_rectangle(event,x,y,flags,param):                               #تابع رسم مستطیل حول نقطه کلیلک شده                                         
 
   if event==cv2.EVENT_LBUTTONDBLCLK:                                    #|      در صورتی ک کاربر روی تصویر دوبار چپ کلیک کند
        cv2.rectangle(img,(x-20,y-20),(x+20,y+20),(0,0,0),1)             #|      مربعی با ابعاد 40 حول ان نقطه رسم می شود      
        p=img[y-20:y+20,x-20:x+20]                                       #|
        m=cv2.resize(p,(p.shape[0]+20,p.shape[1]+20))                    #|=>    ابعاد مستطیل انتخاب شده را بزگتر میکینم resize با استفاده از  تابع
        img[y-30:y+30,x-30:x+30]=m                                       #|      شودzoomتا مستطیل انتخاب شده
                                                                         #|      سپس با توجه به ابعاد جدید مستطیل،ان را در مختصات نقطه کلیک شده کپی میکینم
                                                                         
   
   if event==cv2.EVENT_RBUTTONDBLCLK:                                    #|      در صورتی که کاربر دوبار روی تصویر راست کلیک کند 
          cv2.rectangle(img,(x-20,y-20),(x+20,y+20),(0,0,0),1)           #|      مربعی با ابعاد 40 حول ان نقطه رسم می شود
          s=img[y-20:y+20,x-20:x+20]                                     #|=>    سپس با استخراج مستطیل و
          n=cv2.blur(s,(7,7))                                            #|     مسطیل انتخابی را مات می کنیمblurاستفاده از تابع 
          img[y-20:y+20,x-20:x+20]=n                                     #|     و در همان نقطه ی اول کپی می کنیم

   
      

img=cv2.imread('girl.jpeg')                                              #گرفتن تصویر ورودی                       
cv2.namedWindow('image')                                                 #ایجاد پنجره جدید برای نگهداری تصویر اصلی
cv2.setMouseCallback('image',draw_rectangle)                             #کنترل کننده موس را برای پنجره ایجاد شده تنظیم می کینمsetmousecallbackبا استفده از تابع


while(1):                                                                #را فشار دهد و برنامه بسته شود.qایجاد حلقه بی نهایت برای نمایش تصویر و ایجاد دایره روی آن تا زمانی ک کاربر کلید 
    cv2.imshow('image',img)
    if cv2.waitKey(1) & 0xff==ord('q'):
        break
cv2.destroyAllWindows()                                                   #از بین بردن پنجره های ایجاد شده ک فضای حافظه را اشغال کردند
