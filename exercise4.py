# برنامه ای بنویسید که از کاربر درخواستکند که یک عدد را در ورودی ارسال کند و با استفاده از حلقه while تا زمانی که عدد ارسال نکرده (یعنی متن یا علامت یا خالی یا … ارسال کند) دوباره از او درخواست کند.

def adadgir(prompt):
    while True:
        user=input('adad bede golam')
        try:
            return float(user)
        except ValuError:
            print('adad befres aziz dell')
    
    age=adadgir('chand sall dari?  :')
            
