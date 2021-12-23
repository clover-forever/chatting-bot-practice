# from transitions.extensions import GraphMachine
# from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, PostbackTemplateAction
# from utils import send_button_message,send_text_message,send_fsm

# class TocMachine(GraphMachine):
#     breakfast = {'calorie':0,'starch':0,'protein':0,'money':0,'meal':'none'} #starch:澱粉
#     lunch     = {'calorie':0,'starch':0,'protein':0,'money':0,'meal':'none'}   
#     dinner    = {'calorie':0,'starch':0,'protein':0,'money':0,'meal':'none'}
#     height = 160
#     weight = 60
#     Totalmoney = 0
#     Totalcalorie = 0
#     Totalstarch = 0
#     Totalprotein = 0
#     def __init__(self, **machine_configs):
#         self.machine = GraphMachine(model=self, **machine_configs)
#     #start
#     def is_going_to_start(self, event):
#         text = event.message.text
#         return text.lower() == "start"
#     def on_enter_start(self, event):
#         TocMachine.breakfast['calorie'] = 0
#         TocMachine.breakfast['starch'] = 0
#         TocMachine.breakfast['protein'] = 0
#         TocMachine.breakfast['money'] = 0
#         TocMachine.breakfast['meal'] = 'none'
        
#         TocMachine.lunch['calorie'] = 0
#         TocMachine.lunch['starch'] = 0
#         TocMachine.lunch['protein'] = 0
#         TocMachine.lunch['money'] = 0
#         TocMachine.lunch['meal'] = 'none'
        
#         TocMachine.dinner['calorie'] = 0
#         TocMachine.dinner['starch'] = 0
#         TocMachine.dinner['protein'] = 0
#         TocMachine.dinner['money'] = 0
#         TocMachine.dinner['meal'] = 'none'
        
#         btn_action=[
#             MessageTemplateAction(
#                 label='更新個人資訊',
#                 text='information'
#             ),
#             MessageTemplateAction(
#                 label='檢驗  早/午/晚餐熱量',
#                 text='regfood'
#             ),
#             MessageTemplateAction(
#                 label='顯示   建議營養比例',
#                 text='showsuggest'
#             ),
#             MessageTemplateAction(
#                 label='顯示 fsm圖',
#                 text='showfsm'
#             ),
#         ]
#         reply_token = event.reply_token
#         send_button_message(reply_token,btn_action,"功能表單","提供以下功能")

#     #input the food
#     def is_going_to_regfood(self, event):
#         text = event.message.text
#         return text.lower() == "regfood"
#     def on_enter_regfood(self, event):
#         btn_action=[
#             MessageTemplateAction(
#                 label='早餐',
#                 text='breakfast'
#             ),
#             MessageTemplateAction(
#                 label='午餐',
#                 text='lunch'
#             ),
#             MessageTemplateAction(
#                 label='晚餐',
#                 text='dinner'
#             ),
#             MessageTemplateAction(
#                 label='顯示     營養比例/熱量',
#                 text='showeat'
#             ),
#         ]
#         reply_token = event.reply_token
#         send_button_message(reply_token,btn_action,"選擇餐點","返回功能選單請按1")
    
#     #input the information
#     def is_going_to_information(self, event):
#         text = event.message.text
#         if(text.lower() == "start" or text.lower() == "information"):
#             return True
#         else:
#             return False
#         # return text.lower() == "information"
#     def on_enter_information(self, event):
#         reply_token = event.reply_token
#         send_text_message(reply_token, "歡迎使用維持體脂小幫手\n******請先輸入基本資訊******\n\n輸入身高(cm)")
#     #input the height
#     def is_going_to_height(self, event):
#         text = event.message.text
#         return True
#     def on_enter_height(self, event):
#         print("in height")
#         text = event.message.text
#         TocMachine.height = int(text)
#         reply_token = event.reply_token
#         send_text_message(reply_token, "輸入體重(kg)")
#     #input the weight
#     def is_going_to_weight(self, event):
#         text = event.message.text
#         return True
#     def on_enter_weight(self, event):
#         text = event.message.text
#         TocMachine.weight = int(text)
#         print("in weight")
#         reply_token = event.reply_token
#         send_text_message(reply_token, "輸入每日預算(dollar)")

#     #input the money
#     def is_going_to_money(self, event):
#         text = event.message.text
#         return True
#     def on_enter_money(self, event):
#         text = event.message.text
#         TocMachine.Totalmoney = int(text)
#         print("in money")
#         reply_token = event.reply_token
#         send_text_message(reply_token, "輸入年齡")
#     #input the age
#     def is_going_to_age(self, event):
#         text = event.message.text
#         return True
#     def on_enter_age(self, event):
#         text = event.message.text
#         TocMachine.age = int(text)
#         # bmr = (13.7 x 體重) + (5.0 x 身高) – (6.8 x 年齡) + 66
#         bmr = (13.7*TocMachine.weight) + (5*TocMachine.height) - (6.8*TocMachine.age) + 66
#         tdee = bmr * 1.375 - 300
#         TocMachine.Totalstarch = tdee * 0.3/4 #starch=tdee*0.3/4
#         TocMachine.Totalcalorie = tdee
#         print(TocMachine.Totalmoney,"totalmoney")
#         print(tdee,'tdee')
#         print(TocMachine.Totalcalorie,"Totalcalorie")
#         print(TocMachine.Totalstarch,"Totalstarch")
#         self.go_regtostart(event)

#     #check
#     def on_enter_examine(self, event, strback):
#         print("in examine")
#         print(strback)
#         self.go_money(event,strback)
    
#     def on_enter_money_check(self, event, strback):
#         print("in money check")
#         sum = TocMachine.dinner['money'] +TocMachine.breakfast['money'] + TocMachine.lunch['money'] 
#         print(TocMachine.breakfast['money'],"breakfast")
#         print(TocMachine.lunch['money'],"lunch")
#         print(TocMachine.dinner['money'],"dinner")
#         print(sum,"sum = ")
#         if sum <= TocMachine.Totalmoney:
#             self.go_calorie(event,strback)
#         else:
#             self.go_money_deny(event,strback,sum)

#     def on_enter_calorie_check(self, event,strback):
#         print("in calorie check")
#         sum = TocMachine.dinner['calorie'] + TocMachine.breakfast['calorie'] + TocMachine.lunch['calorie'] 
#         print(TocMachine.breakfast['calorie'],"breakfast")
#         print(TocMachine.lunch['calorie'],"lunch")
#         print(TocMachine.dinner['calorie'],"dinner")
#         print(sum,"sum = ")

#         if sum < TocMachine.Totalcalorie:
#             self.go_starch(event,strback)
#         else:
#             self.go_calorie_deny(event,strback,sum)
        
#     def on_enter_starch_check(self, event,strback):
#         print("in starch check")
#         sum = TocMachine.dinner['starch'] +TocMachine.breakfast['starch'] + TocMachine.lunch['starch'] 
#         print(TocMachine.breakfast['starch'],"breakfast")
#         print(TocMachine.lunch['starch'],"lunch")
#         print(TocMachine.dinner['starch'],"dinner")
#         print(sum,"sum = ")
#         if sum < TocMachine.Totalstarch:
#             self.go_regfood(event)
#         else:
#             self.go_starch_deny(event,strback,sum)
    
#     #deny
#     def on_enter_money_deny(self, event, strback,sum):
#         reply_token = event.reply_token
#         msg0="餘額不足\n輸入1返回功能表單"
#         send_text_message(reply_token,msg0)
#         print("in money deny")
        
#         if strback == "breakfast":
#             sum -= TocMachine.breakfast['money']
#             self.go_regfood(event)
#         elif strback == "lunch":
#             sum -= TocMachine.lunch['money']
#             self.go_regfood(event)
#         else:
#             sum -= TocMachine.dinner['money']
#             self.go_regfood(event)
        
#     def on_enter_calorie_deny(self, event,strback,sum):
#         reply_token = event.reply_token
#         msg0="熱量太高\n輸入1返回功能表單"
#         send_text_message(reply_token,msg0)
#         print("in calorie deny")
#         if strback == "breakfast":
#             sum -= TocMachine.breakfast['calorie']
#             self.go_regfood(event)
#         elif strback == "lunch":
#             sum -= TocMachine.lunch['calorie']
#             self.go_regfood(event)
#         else:
#             sum -= TocMachine.dinner['calorie']
#             self.go_regfood(event)
        
#     def on_enter_starch_deny(self, event,strback,sum):
#         reply_token = event.reply_token
#         msg0="澱粉太多\n輸入1返回功能表單"
#         send_text_message(reply_token,msg0)
#         print("in starch deny")
#         if strback == "breakfast":
#             sum -= TocMachine.breakfast['starch']
#             self.go_regfood(event)
#         elif strback == "lunch":
#             sum -= TocMachine.lunch['starch']
#             self.go_regfood(event)
#         else:
#             sum -= TocMachine.dinner['starch']
#             self.go_regfood(event)
 
#     #showeat
#     def is_going_to_showeat(self, event,indic=""):
#         text = event.message.text
#         return text.lower() == "showeat"
#     def on_enter_showeat(self, event ,indic=""):  
#         msg0 = '餐點:\n       早餐%10s\n       午餐%10s\n       晚餐%10s\n' % (TocMachine.breakfast['meal'],TocMachine.lunch['meal'],TocMachine.dinner['meal'])
#         msg1 = '卡路里:\n       早餐%20d卡\n       午餐%20d卡\n       晚餐%20d卡\n' % (TocMachine.breakfast['calorie'],TocMachine.lunch['calorie'],TocMachine.dinner['calorie'])
#         msg2 = '澱粉:\n       早餐%20d克\n       午餐%20d克\n       晚餐%20d克\n' % (TocMachine.breakfast['starch'],TocMachine.lunch['starch'],TocMachine.dinner['starch'])
#         msg3 = '蛋白質:\n       早餐%20d克\n       午餐%20d克\n       晚餐%20d克\n' % (TocMachine.breakfast['protein'],TocMachine.lunch['protein'],TocMachine.dinner['protein'])
#         msg4 = '金額:\n       早餐%20d元\n       午餐%20d元\n       晚餐%20d元\n' % (TocMachine.breakfast['money'],TocMachine.lunch['money'],TocMachine.dinner['money'])
#         msg5 = '返回請輸入1'
#         reply_token = event.reply_token
#         send_text_message(reply_token,msg0+msg1+msg2+msg3+msg4+msg5)
#     #show back
#     def is_going_to_showback(self, event,indic=""):
#         text = event.message.text
#         return text.lower() == "1"
#     def on_enter_showback(self, event ,indic=""):  
#         self.go_regfood(event)

#     #showsuggest
#     def is_going_to_showsuggest(self, event,indic=""):
#         text = event.message.text
#         return text.lower() == "showsuggest"
#     def on_enter_showsuggest(self, event ,indic=""):
#         print("in show suggest")  
#         print(TocMachine.Totalmoney,"totalmoney")
#         print(TocMachine.Totalcalorie,"Totalcalorie")
#         print(TocMachine.Totalstarch,"Totalstarch")
        
#         msg0 = '設定完身高體重即可換算\n\n'
#         msg1 = '建議攝取熱量:%20d大卡\n' % (TocMachine.Totalcalorie)
#         msg2 = '建議攝取澱粉:%20d公克\n' % (TocMachine.Totalstarch)
#         msg3 = '每日金額:         %20d元\n\n' % (TocMachine.Totalmoney)
#         msg4 = '返回請輸入1'
#         reply_token = event.reply_token
#         send_text_message(reply_token,msg0+msg1+msg2+msg3+msg4)
    
#     #showfsm
#     def is_going_to_showfsm(self, event,indic=""):
#         text = event.message.text
#         return text.lower() == "showfsm"

#     def on_enter_showfsm(self, event ,indic=""):
#         reply_token = event.reply_token
#         send_fsm(reply_token)

#     #regfood back to start
#     def is_going_to_regtostart(self, event,indic=""):
#         text = event.message.text
#         reply_token = event.reply_token
#         if text.lower() != "1":
#             send_text_message(reply_token,"輸入1回到上一個階段")
#         return text.lower() == "1"
#     def on_enter_regtostart(self, event ,indic=""):  
#         print(" go to start")
#         self.go_regtostart(event)
    
#     #breakfast
#     def is_going_to_breakfast(self, event,indic=""):
#         text = event.message.text
#         return text.lower() == "breakfast"
#     def on_enter_breakfast(self, event ,indic=""):
#         btn_action=[
#             MessageTemplateAction(
#                 label='三明治 輸入(1空格$)',
#                 text='hamegg'
#             ),
#             MessageTemplateAction(
#                 label='蛋餅 輸入(2空格$)',
#                 text='chiomelet'
#             ),
#             MessageTemplateAction(
#                 label='飯糰 輸入(3空格$)',
#                 text='riceroll'
#             ),
#         ]
#         reply_token = event.reply_token
#         send_button_message(reply_token,btn_action,"早餐",indic)
#     #next breakfast
#     def is_going_to_nextbreakfast(self, event):
#         text = event.message.text
#         return True
#     def on_enter_nextbreakfast(self, event):
#         text = event.message.text
#         input = text.split()
#         print(input)
#         if input[0] == '1':
#             TocMachine.breakfast['calorie'] = 270
#             TocMachine.breakfast['starch']  = 20
#             TocMachine.breakfast['protein'] = 13
#             TocMachine.breakfast['money']   = int(input[1])
#             TocMachine.breakfast['meal'] = '火腿蛋土司'
#             print(TocMachine.breakfast['money'],"breakfast")
#             print(TocMachine.lunch['money'],"lunch")
#             print(TocMachine.dinner['money'],"dinner")
#             print("in hamegg")
#         elif input[0] == '2':
#             TocMachine.breakfast['calorie'] = 230
#             TocMachine.breakfast['starch']  = 25
#             TocMachine.breakfast['protein'] = 6
#             TocMachine.breakfast['money']   = int(input[1])
#             TocMachine.breakfast['meal'] = '蛋餅'
#             print(TocMachine.breakfast['money'],"breakfast")
#             print(TocMachine.lunch['money'],"lunch")
#             print(TocMachine.dinner['money'],"dinner")
#             print("in chiomelet")
#         elif input[0] == '3':
#             TocMachine.breakfast['calorie'] = 220
#             TocMachine.breakfast['starch']  = 40
#             TocMachine.breakfast['protein'] = 5
#             TocMachine.breakfast['money']   = int(input[1])
#             TocMachine.breakfast['meal'] = '飯糰'
#             print(TocMachine.breakfast['money'],"breakfast")
#             print(TocMachine.lunch['money'],"lunch")
#             print(TocMachine.dinner['money'],"dinner")
#             print("in riceroll")
            
#         self.go_money(event,"breakfast")

#     #lunch
#     def is_going_to_lunch(self, event):
#         text = event.message.text
#         return text.lower() == "lunch"
#     def on_enter_lunch(self, event,indic=""):
#         btn_action=[
#             MessageTemplateAction(
#                 label='subway 輸入(1空格$)',
#                 text='subway'
#             ),
#             MessageTemplateAction(
#                 label='炒飯 輸入(2空格$)',
#                 text='friedrice'
#             ),
#             MessageTemplateAction(
#                 label='乾麵 輸入(3空格$)',
#                 text='noodles'
#             ),
#             MessageTemplateAction(
#                 label='雞腿便當 輸入(4空格$)',
#                 text='boxedlunch'
#             )
#         ]
#         reply_token = event.reply_token
#         send_button_message(reply_token,btn_action,"午餐",indic)
#     #next lunch
#     def is_going_to_nextlunch(self, event):
#         text = event.message.text
#         return True
#     def on_enter_nextlunch(self, event):
#         text = event.message.text
#         input = text.split()
#         print(input)
#         if input[0] == '1':
#             TocMachine.lunch['calorie'] = 500
#             TocMachine.lunch['starch']  = 55
#             TocMachine.lunch['protein'] = 35
#             TocMachine.lunch['money']   = int(input[1])
#             TocMachine.lunch['meal'] = 'subway'
#             print(TocMachine.breakfast['money'],"breakfast")
#             print(TocMachine.lunch['money'],"lunch")
#             print(TocMachine.dinner['money'],"dinner")
#             print("in subway")
#         elif input[0] == '2':
#             TocMachine.lunch['calorie'] = 600
#             TocMachine.lunch['starch']  = 80
#             TocMachine.lunch['protein'] = 10
#             TocMachine.lunch['money'] = int(input[1])
#             TocMachine.lunch['meal'] = '炒飯'
            
#             print(TocMachine.breakfast['money'],"breakfast")
#             print(TocMachine.lunch['money'],"lunch")
#             print(TocMachine.dinner['money'],"dinner")
#             print("in friedrice")

#         elif input[0] == '3':
#             TocMachine.lunch['calorie'] = 600
#             TocMachine.lunch['starch']  = 60
#             TocMachine.lunch['protein'] = 10
#             TocMachine.lunch['money']   = int(input[1])
#             TocMachine.lunch['meal'] = '乾麵'
            
#             print(TocMachine.breakfast['money'],"breakfast")
#             print(TocMachine.lunch['money'],"lunch")
#             print(TocMachine.dinner['money'],"dinner")
#             print("in noodles")
#         elif input[0] == '4':
#             TocMachine.lunch['calorie'] = 800
#             TocMachine.lunch['starch']  = 80
#             TocMachine.lunch['protein'] = 40
#             TocMachine.lunch['money']   = int(input[1])
#             TocMachine.lunch['meal'] = '便當'
            
#             print(TocMachine.breakfast['money'],"breakfast")
#             print(TocMachine.lunch['money'],"lunch")
#             print(TocMachine.dinner['money'],"dinner")
#             print("in boxedlunch")
#         self.go_money(event,"lunch")
    
#     #dinner
#     def is_going_to_dinner(self, event):
#         text = event.message.text        
#         return text.lower() == "dinner"
#     def on_enter_dinner(self, event,indic=""):
#         btn_action=[
#             MessageTemplateAction(
#                 label='海南雞飯 輸入(1空格$)',
#                 text= 'chickenrice'
#             ),
#             MessageTemplateAction(
#                 label='關東煮 輸入(2空格$)',
#                 text='oden'
#             ),
#             MessageTemplateAction(
#                 label='涼麵 輸入(3空格$)',
#                 text='coldnoodle'
#             ),
#             MessageTemplateAction(
#                 label='打拋豬飯 輸入(4空格$)',
#                 text='chilipork'
#             )
#         ]
#         reply_token = event.reply_token
#         send_button_message(reply_token,btn_action,"晚餐",indic)
#     #next dinner
#     def is_going_to_nextdinner(self, event):
#         text = event.message.text
#         return True
#     def on_enter_nextdinner(self, event):
#         text = event.message.text
#         input = text.split()
#         print(input)
#         # print(text,"check the nextdinner")
#         if input[0] == '1':
#             TocMachine.dinner['calorie'] = 800
#             TocMachine.dinner['starch']  = 80
#             TocMachine.dinner['protein'] = 50
#             TocMachine.dinner['money']   = int(input[1])
#             TocMachine.dinner['meal'] = '海南雞飯'

#             print(TocMachine.breakfast['money'],"breakfast")
#             print(TocMachine.lunch['money'],"lunch")
#             print(TocMachine.dinner['money'],"dinner")
#             print("in chickenrice")
#         elif input[0] == '2':
#             TocMachine.dinner['calorie'] = 800
#             TocMachine.dinner['starch']  = 90
#             TocMachine.dinner['protein'] = 30
#             TocMachine.dinner['money']   = int(input[1])
#             TocMachine.dinner['meal'] = '關東煮'

#             print(TocMachine.breakfast['money'],"breakfast")
#             print(TocMachine.lunch['money'],"lunch")
#             print(TocMachine.dinner['money'],"dinner")
#             print("in oden")

#         elif input[0] == '3':
#             TocMachine.dinner['calorie'] = 450
#             TocMachine.dinner['starch']  = 50
#             TocMachine.dinner['protein'] = 15
#             TocMachine.dinner['money']   = int(input[1])
#             TocMachine.dinner['meal'] = '涼麵'

#             print(TocMachine.breakfast['money'],"breakfast")
#             print(TocMachine.lunch['money'],"lunch")
#             print(TocMachine.dinner['money'],"dinner")
#             print("in coldnoodle")
#         elif input[0] == '4':
#             TocMachine.dinner['calorie'] = 600
#             TocMachine.dinner['starch']  = 90
#             TocMachine.dinner['protein'] = 30
#             TocMachine.dinner['money']   = int(input[1])
#             TocMachine.dinner['meal'] = '打拋豬飯'

#             print(TocMachine.breakfast['money'],"breakfast")
#             print(TocMachine.lunch['money'],"lunch")
#             print(TocMachine.dinner['money'],"dinner")
#             print("in chilipork")
#         self.go_money(event,"dinner")
        




from transitions.extensions import GraphMachine
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction, PostbackTemplateAction
from utils import send_button_message,send_text_message,send_fsm

class TocMachine(GraphMachine):
    breakfast = {'calorie':0,'starch':0,'protein':0,'money':0,'meal':'none'} #starch:澱粉
    lunch     = {'calorie':0,'starch':0,'protein':0,'money':0,'meal':'none'}   
    dinner    = {'calorie':0,'starch':0,'protein':0,'money':0,'meal':'none'}
    height = 160
    weight = 60
    Totalmoney = 0
    Totalcalorie = 0
    Totalstarch = 0
    Totalprotein = 0
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(model=self, **machine_configs)
    #start
    def is_going_to_start(self, event):
        text = event.message.text
        return text.lower() == "start"
    def on_enter_start(self, event):
        TocMachine.breakfast['calorie'] = 0
        TocMachine.breakfast['starch'] = 0
        TocMachine.breakfast['protein'] = 0
        TocMachine.breakfast['money'] = 0
        TocMachine.breakfast['meal'] = 'none'
        
        TocMachine.lunch['calorie'] = 0
        TocMachine.lunch['starch'] = 0
        TocMachine.lunch['protein'] = 0
        TocMachine.lunch['money'] = 0
        TocMachine.lunch['meal'] = 'none'
        
        TocMachine.dinner['calorie'] = 0
        TocMachine.dinner['starch'] = 0
        TocMachine.dinner['protein'] = 0
        TocMachine.dinner['money'] = 0
        TocMachine.dinner['meal'] = 'none'
        
        btn_action=[
            MessageTemplateAction(
                label='更新個人資訊',
                text='information'
            ),
            MessageTemplateAction(
                label='檢驗  早/午/晚餐熱量',
                text='regfood'
            ),
            MessageTemplateAction(
                label='顯示   建議營養比例',
                text='showsuggest'
            ),
            MessageTemplateAction(
                label='顯示 fsm圖',
                text='showfsm'
            ),
        ]
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"功能表單","提供以下功能")

    #input the food
    def is_going_to_regfood(self, event):
        text = event.message.text
        return text.lower() == "regfood"
    def on_enter_regfood(self, event):
        btn_action=[
            MessageTemplateAction(
                label='早餐',
                text='breakfast'
            ),
            MessageTemplateAction(
                label='午餐',
                text='lunch'
            ),
            MessageTemplateAction(
                label='晚餐',
                text='dinner'
            ),
            MessageTemplateAction(
                label='顯示     營養比例/熱量',
                text='showeat'
            ),
        ]
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"選擇餐點","返回功能選單請按1")
    
    #input the information
    def is_going_to_information(self, event):
        text = event.message.text
        if(text.lower() == "start" or text.lower() == "information"):
            return True
        else:
            return False
        # return text.lower() == "information"
    def on_enter_information(self, event):
        reply_token = event.reply_token
        send_text_message(reply_token, "歡迎使用維持體脂小幫手\n******請先輸入基本資訊******\n\n輸入身高(cm)")
    #input the height
    def is_going_to_height(self, event):
        text = event.message.text
        return True
    def on_enter_height(self, event):
        print("in height")
        text = event.message.text
        TocMachine.height = int(text)
        reply_token = event.reply_token
        send_text_message(reply_token, "輸入體重(kg)")
    #input the weight
    def is_going_to_weight(self, event):
        text = event.message.text
        return True
    def on_enter_weight(self, event):
        text = event.message.text
        TocMachine.weight = int(text)
        print("in weight")
        reply_token = event.reply_token
        send_text_message(reply_token, "輸入每日預算(dollar)")

    #input the money
    def is_going_to_money(self, event):
        text = event.message.text
        return True
    def on_enter_money(self, event):
        text = event.message.text
        TocMachine.Totalmoney = int(text)
        print("in money")
        reply_token = event.reply_token
        send_text_message(reply_token, "輸入年齡")
    #input the age
    def is_going_to_age(self, event):
        text = event.message.text
        return True
    def on_enter_age(self, event):
        text = event.message.text
        TocMachine.age = int(text)
        # bmr = (13.7 x 體重) + (5.0 x 身高) – (6.8 x 年齡) + 66
        bmr = (13.7*TocMachine.weight) + (5*TocMachine.height) - (6.8*TocMachine.age) + 66
        tdee = bmr * 1.375 - 300
        TocMachine.Totalstarch = tdee * 0.3/4 #starch=tdee*0.3/4
        TocMachine.Totalcalorie = tdee
        TocMachine.Totalprotein = TocMachine.weight #(1 kg need 1g protein)
        print(TocMachine.Totalmoney,"totalmoney")
        print(tdee,'tdee')
        print(TocMachine.Totalcalorie,"Totalcalorie")
        print(TocMachine.Totalstarch,"Totalstarch")
        print(TocMachine.Totalprotein,"Totalprotein")
        self.go_regtostart(event)

    #check
    def on_enter_examine(self, event, strback):
        print("in examine")
        print(strback)
        self.go_money(event,strback)
    
    def on_enter_money_check(self, event, strback):
        print("in money check")
        sum = TocMachine.dinner['money'] +TocMachine.breakfast['money'] + TocMachine.lunch['money'] 
        print(TocMachine.breakfast['money'],"breakfast")
        print(TocMachine.lunch['money'],"lunch")
        print(TocMachine.dinner['money'],"dinner")
        print(sum,"sum = ")
        if sum <= TocMachine.Totalmoney:
            self.go_calorie(event,strback)
        else:
            self.go_money_deny(event,strback,sum)

    def on_enter_calorie_check(self, event,strback):
        print("in calorie check")
        sum = TocMachine.dinner['calorie'] + TocMachine.breakfast['calorie'] + TocMachine.lunch['calorie'] 
        print(TocMachine.breakfast['calorie'],"breakfast")
        print(TocMachine.lunch['calorie'],"lunch")
        print(TocMachine.dinner['calorie'],"dinner")
        print(sum,"sum = ")

        if sum < TocMachine.Totalcalorie:
            self.go_starch(event,strback)
        else:
            self.go_calorie_deny(event,strback,sum)
        
    def on_enter_starch_check(self, event,strback):
        print("in starch check")
        sum = TocMachine.dinner['starch'] +TocMachine.breakfast['starch'] + TocMachine.lunch['starch'] 
        print(TocMachine.breakfast['starch'],"breakfast")
        print(TocMachine.lunch['starch'],"lunch")
        print(TocMachine.dinner['starch'],"dinner")
        print(sum,"sum = ")
        if sum < TocMachine.Totalstarch:
            self.go_regfood(event)
        else:
            self.go_starch_deny(event,strback,sum)

    def on_enter_protein_check(self, event,strback):
        print("in protein check")
        sum = TocMachine.dinner['protein'] +TocMachine.breakfast['protein'] + TocMachine.lunch['protein'] 
        print(TocMachine.breakfast['protein'],"breakfast")
        print(TocMachine.lunch['protein'],"lunch")
        print(TocMachine.dinner['protein'],"dinner")
        print(sum,"sum = ")
        if sum < TocMachine.Totalprotein:
            self.go_regfood(event)
        else:
            self.go_protein_deny(event,strback,sum)
    
    #deny
    def on_enter_money_deny(self, event, strback,sum):
        reply_token = event.reply_token
        msg0="餘額不足\n輸入1返回功能表單"
        send_text_message(reply_token,msg0)
        print("in money deny")
        
        if strback == "breakfast":
            sum -= TocMachine.breakfast['money']
            self.go_regfood(event)
        elif strback == "lunch":
            sum -= TocMachine.lunch['money']
            self.go_regfood(event)
        else:
            sum -= TocMachine.dinner['money']
            self.go_regfood(event)
        
    def on_enter_calorie_deny(self, event,strback,sum):
        reply_token = event.reply_token
        msg0="熱量太高\n輸入1返回功能表單"
        send_text_message(reply_token,msg0)
        print("in calorie deny")
        if strback == "breakfast":
            sum -= TocMachine.breakfast['calorie']
            self.go_regfood(event)
        elif strback == "lunch":
            sum -= TocMachine.lunch['calorie']
            self.go_regfood(event)
        else:
            sum -= TocMachine.dinner['calorie']
            self.go_regfood(event)
        
    def on_enter_starch_deny(self, event,strback,sum):
        reply_token = event.reply_token
        msg0="澱粉太多\n輸入1返回功能表單"
        send_text_message(reply_token,msg0)
        print("in starch deny")
        if strback == "breakfast":
            sum -= TocMachine.breakfast['starch']
            self.go_regfood(event)
        elif strback == "lunch":
            sum -= TocMachine.lunch['starch']
            self.go_regfood(event)
        else:
            sum -= TocMachine.dinner['starch']
            self.go_regfood(event)

    def on_enter_protein_deny(self, event,strback,sum):
        reply_token = event.reply_token
        msg0="澱粉太多\n輸入1返回功能表單"
        send_text_message(reply_token,msg0)
        print("in protein deny")
        if strback == "breakfast":
            sum -= TocMachine.breakfast['protein']
            self.go_regfood(event)
        elif strback == "lunch":
            sum -= TocMachine.lunch['protein']
            self.go_regfood(event)
        else:
            sum -= TocMachine.dinner['protein']
            self.go_regfood(event)
 
    #showeat
    def is_going_to_showeat(self, event,indic=""):
        text = event.message.text
        return text.lower() == "showeat"
    def on_enter_showeat(self, event ,indic=""):  
        msg0 = '餐點:\n       早餐%10s\n       午餐%10s\n       晚餐%10s\n' % (TocMachine.breakfast['meal'],TocMachine.lunch['meal'],TocMachine.dinner['meal'])
        msg1 = '卡路里:\n       早餐%20d卡\n       午餐%20d卡\n       晚餐%20d卡\n' % (TocMachine.breakfast['calorie'],TocMachine.lunch['calorie'],TocMachine.dinner['calorie'])
        msg2 = '澱粉:\n       早餐%20d克\n       午餐%20d克\n       晚餐%20d克\n' % (TocMachine.breakfast['starch'],TocMachine.lunch['starch'],TocMachine.dinner['starch'])
        msg3 = '蛋白質:\n       早餐%20d克\n       午餐%20d克\n       晚餐%20d克\n' % (TocMachine.breakfast['protein'],TocMachine.lunch['protein'],TocMachine.dinner['protein'])
        msg4 = '金額:\n       早餐%20d元\n       午餐%20d元\n       晚餐%20d元\n' % (TocMachine.breakfast['money'],TocMachine.lunch['money'],TocMachine.dinner['money'])
        msg5 = '返回請輸入1'
        reply_token = event.reply_token
        send_text_message(reply_token,msg0+msg1+msg2+msg3+msg4+msg5)
    #show back
    def is_going_to_showback(self, event,indic=""):
        text = event.message.text
        return text.lower() == "1"
    def on_enter_showback(self, event ,indic=""):  
        self.go_regfood(event)

    #showsuggest
    def is_going_to_showsuggest(self, event,indic=""):
        text = event.message.text
        return text.lower() == "showsuggest"
    def on_enter_showsuggest(self, event ,indic=""):
        print("in show suggest")  
        print(TocMachine.Totalmoney,"totalmoney")
        print(TocMachine.Totalcalorie,"Totalcalorie")
        print(TocMachine.Totalstarch,"Totalstarch")
        print(TocMachine.Totalprotein,"Totalprotein")
        
        msg0 = '設定完身高體重即可換算\n\n'
        msg1 = '建議攝取熱量:%20d大卡\n' % (TocMachine.Totalcalorie)
        msg2 = '建議攝取澱粉:%20d公克\n' % (TocMachine.Totalstarch)
        msg3 = '建議攝取蛋白質:%20d公克\n' % (TocMachine.Totalprotein)
        msg4 = '每日金額:         %20d元\n\n' % (TocMachine.Totalmoney)
        msg5 = '返回請輸入1'
        reply_token = event.reply_token
        send_text_message(reply_token,msg0+msg1+msg2+msg3+msg4+msg5)
    
    #showfsm
    def is_going_to_showfsm(self, event,indic=""):
        text = event.message.text
        return text.lower() == "showfsm"

    def on_enter_showfsm(self, event ,indic=""):
        reply_token = event.reply_token
        send_fsm(reply_token)

    #regfood back to start
    def is_going_to_regtostart(self, event,indic=""):
        text = event.message.text
        reply_token = event.reply_token
        if text.lower() != "1":
            send_text_message(reply_token,"輸入1回到上一個階段")
        return text.lower() == "1"
    def on_enter_regtostart(self, event ,indic=""):  
        print(" go to start")
        self.go_regtostart(event)
    
    #breakfast
    def is_going_to_breakfast(self, event,indic=""):
        text = event.message.text
        return text.lower() == "breakfast"
    def on_enter_breakfast(self, event ,indic=""):
        btn_action=[
            MessageTemplateAction(
                label='三明治 輸入(1空格$)',
                text='hamegg'
            ),
            MessageTemplateAction(
                label='蛋餅 輸入(2空格$)',
                text='chiomelet'
            ),
            MessageTemplateAction(
                label='飯糰 輸入(3空格$)',
                text='riceroll'
            ),
        ]
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"早餐",indic)
    #next breakfast
    def is_going_to_nextbreakfast(self, event):
        text = event.message.text
        return True
    def on_enter_nextbreakfast(self, event):
        text = event.message.text
        input = text.split()
        print(input)
        if input[0] == '1':
            TocMachine.breakfast['calorie'] = 270
            TocMachine.breakfast['starch']  = 20
            TocMachine.breakfast['protein'] = 13
            TocMachine.breakfast['money']   = int(input[1])
            TocMachine.breakfast['meal'] = '火腿蛋土司'
            print(TocMachine.breakfast['money'],"breakfast")
            print(TocMachine.lunch['money'],"lunch")
            print(TocMachine.dinner['money'],"dinner")
            print("in hamegg")
        elif input[0] == '2':
            TocMachine.breakfast['calorie'] = 230
            TocMachine.breakfast['starch']  = 25
            TocMachine.breakfast['protein'] = 6
            TocMachine.breakfast['money']   = int(input[1])
            TocMachine.breakfast['meal'] = '蛋餅'
            print(TocMachine.breakfast['money'],"breakfast")
            print(TocMachine.lunch['money'],"lunch")
            print(TocMachine.dinner['money'],"dinner")
            print("in chiomelet")
        elif input[0] == '3':
            TocMachine.breakfast['calorie'] = 220
            TocMachine.breakfast['starch']  = 40
            TocMachine.breakfast['protein'] = 5
            TocMachine.breakfast['money']   = int(input[1])
            TocMachine.breakfast['meal'] = '飯糰'
            print(TocMachine.breakfast['money'],"breakfast")
            print(TocMachine.lunch['money'],"lunch")
            print(TocMachine.dinner['money'],"dinner")
            print("in riceroll")
            
        self.go_money(event,"breakfast")

    #lunch
    def is_going_to_lunch(self, event):
        text = event.message.text
        return text.lower() == "lunch"
    def on_enter_lunch(self, event,indic=""):
        btn_action=[
            MessageTemplateAction(
                label='subway 輸入(1空格$)',
                text='subway'
            ),
            MessageTemplateAction(
                label='炒飯 輸入(2空格$)',
                text='friedrice'
            ),
            MessageTemplateAction(
                label='乾麵 輸入(3空格$)',
                text='noodles'
            ),
            MessageTemplateAction(
                label='雞腿便當 輸入(4空格$)',
                text='boxedlunch'
            )
        ]
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"午餐",indic)
    #next lunch
    def is_going_to_nextlunch(self, event):
        text = event.message.text
        return True
    def on_enter_nextlunch(self, event):
        text = event.message.text
        input = text.split()
        print(input)
        if input[0] == '1':
            TocMachine.lunch['calorie'] = 500
            TocMachine.lunch['starch']  = 55
            TocMachine.lunch['protein'] = 35
            TocMachine.lunch['money']   = int(input[1])
            TocMachine.lunch['meal'] = 'subway'
            print(TocMachine.breakfast['money'],"breakfast")
            print(TocMachine.lunch['money'],"lunch")
            print(TocMachine.dinner['money'],"dinner")
            print("in subway")
        elif input[0] == '2':
            TocMachine.lunch['calorie'] = 600
            TocMachine.lunch['starch']  = 80
            TocMachine.lunch['protein'] = 10
            TocMachine.lunch['money'] = int(input[1])
            TocMachine.lunch['meal'] = '炒飯'
            
            print(TocMachine.breakfast['money'],"breakfast")
            print(TocMachine.lunch['money'],"lunch")
            print(TocMachine.dinner['money'],"dinner")
            print("in friedrice")

        elif input[0] == '3':
            TocMachine.lunch['calorie'] = 600
            TocMachine.lunch['starch']  = 60
            TocMachine.lunch['protein'] = 10
            TocMachine.lunch['money']   = int(input[1])
            TocMachine.lunch['meal'] = '乾麵'
            
            print(TocMachine.breakfast['money'],"breakfast")
            print(TocMachine.lunch['money'],"lunch")
            print(TocMachine.dinner['money'],"dinner")
            print("in noodles")
        elif input[0] == '4':
            TocMachine.lunch['calorie'] = 800
            TocMachine.lunch['starch']  = 80
            TocMachine.lunch['protein'] = 40
            TocMachine.lunch['money']   = int(input[1])
            TocMachine.lunch['meal'] = '便當'
            
            print(TocMachine.breakfast['money'],"breakfast")
            print(TocMachine.lunch['money'],"lunch")
            print(TocMachine.dinner['money'],"dinner")
            print("in boxedlunch")
        self.go_money(event,"lunch")
    
    #dinner
    def is_going_to_dinner(self, event):
        text = event.message.text        
        return text.lower() == "dinner"
    def on_enter_dinner(self, event,indic=""):
        btn_action=[
            MessageTemplateAction(
                label='海南雞飯 輸入(1空格$)',
                text= 'chickenrice'
            ),
            MessageTemplateAction(
                label='關東煮 輸入(2空格$)',
                text='oden'
            ),
            MessageTemplateAction(
                label='涼麵 輸入(3空格$)',
                text='coldnoodle'
            ),
            MessageTemplateAction(
                label='打拋豬飯 輸入(4空格$)',
                text='chilipork'
            )
        ]
        reply_token = event.reply_token
        send_button_message(reply_token,btn_action,"晚餐",indic)
    #next dinner
    def is_going_to_nextdinner(self, event):
        text = event.message.text
        return True
    def on_enter_nextdinner(self, event):
        text = event.message.text
        input = text.split()
        print(input)
        # print(text,"check the nextdinner")
        if input[0] == '1':
            TocMachine.dinner['calorie'] = 800
            TocMachine.dinner['starch']  = 80
            TocMachine.dinner['protein'] = 50
            TocMachine.dinner['money']   = int(input[1])
            TocMachine.dinner['meal'] = '海南雞飯'

            print(TocMachine.breakfast['money'],"breakfast")
            print(TocMachine.lunch['money'],"lunch")
            print(TocMachine.dinner['money'],"dinner")
            print("in chickenrice")
        elif input[0] == '2':
            TocMachine.dinner['calorie'] = 800
            TocMachine.dinner['starch']  = 90
            TocMachine.dinner['protein'] = 30
            TocMachine.dinner['money']   = int(input[1])
            TocMachine.dinner['meal'] = '關東煮'

            print(TocMachine.breakfast['money'],"breakfast")
            print(TocMachine.lunch['money'],"lunch")
            print(TocMachine.dinner['money'],"dinner")
            print("in oden")

        elif input[0] == '3':
            TocMachine.dinner['calorie'] = 450
            TocMachine.dinner['starch']  = 50
            TocMachine.dinner['protein'] = 15
            TocMachine.dinner['money']   = int(input[1])
            TocMachine.dinner['meal'] = '涼麵'

            print(TocMachine.breakfast['money'],"breakfast")
            print(TocMachine.lunch['money'],"lunch")
            print(TocMachine.dinner['money'],"dinner")
            print("in coldnoodle")
        elif input[0] == '4':
            TocMachine.dinner['calorie'] = 600
            TocMachine.dinner['starch']  = 90
            TocMachine.dinner['protein'] = 30
            TocMachine.dinner['money']   = int(input[1])
            TocMachine.dinner['meal'] = '打拋豬飯'

            print(TocMachine.breakfast['money'],"breakfast")
            print(TocMachine.lunch['money'],"lunch")
            print(TocMachine.dinner['money'],"dinner")
            print("in chilipork")
        self.go_money(event,"dinner")
        