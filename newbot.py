import discord
import os
from discord.ext import commands 
import datetime
import requests                  # 웹 페이지의 HTML을 가져오는 모듈    
import time
import copy

timetable = {
                '1반': [['1.창체', '2.프로', '3.프로', '4.과학', '5.사회', '6.음악', '7.영어'],
                        ['1.컴구', '2.컴구', '3.수학', '4.체육', '5.국어', '6.프로', '7.프로'],
                        ['1.영어', '2.사회', '3.컴구', '4.음악', '5.수학', '6.과학', '7.국어'],
                        ['1.국어', '2.음악', '3.프로', '4.프로', '5.창체', '6.창체', '7.창체'],
                        ['1.수학', '2.과학', '3.체육', '4.사회', '5.영어', '6.프로']],
                '2반': [['1.창체', '2.프로', '3.프로', '4.프로', '5.수학', '6.영어', '7.과학'],
                        ['1.국어', '2.음악', '3.컴구', '4.컴구', '5.체육', '6.수학', '7.사회'],
                        ['1.프로', '2.프로', '3.프로', '4.프로', '5.국어', '6.음악', '7.영어'],
                        ['1.컴구', '2.체육', '3.사회', '4.과학', '5.창체', '6.창체', '7.창체'],
                        ['1.음악', '2.수학', '3.사회', '4.영어', '5.국어', '6.과학']],
                '3반': [['1.창체', '2.수학', '3.컴구', '4.컴구', '5.영어', '6.국어', '7.프로'],
                        ['1.과학', '2.수학', '3.음악', '4.영어', '5.사회', '6.프로', '7.프로'],
                        ['1.수학', '2.음악', '3.사회', '4.체육', '5.프로', '6.영어', '7.과학'],
                        ['1.프로', '2.국어', '3.과학', '4.사회', '5.창체', '6.창체', '7.창체'],
                        ['1.국어', '2.프로', '3.프로', '4.컴구', '5.음악', '6.체육']],
                '4반': [['1.창체', '2.영어', '3.프로', '4.프로', '5.컴구', '6.컴구', '7.사회'],
                        ['1.음악', '2.사회', '3.과학', '4.국어', '5.수학', '6.체육', '7.영어'],
                        ['1.컴구', '2.수학', '3.음악', '4.영어', '5.프로', '6.프로', '7.프로'],
                        ['1.과학', '2.수학', '3.체육', '4.국어', '5.창체', '6.창체', '7.창체'],
                        ['1.사회', '2.국어', '3.과학', '4.음악', '5.프로', '6.프로']]
            }
Backup = copy.deepcopy(timetable)

def timeset():
    now= datetime.datetime.now()+datetime.timedelta(hours=9)
    nowday=now.weekday() 
    print(nowday)       #0: 월요일, 1:화요일, 2:수요일, 3:목요일, 4:금요일, 5:토요일, 6:일요일
    return nowday,now

def foods(now):
  ymd = now.strftime('%Y-%m-%d')
  print(ymd)
  url='https://api.dsm-dms.com/meal/'+ymd+''
  data = requests.get(url).json()
  food = data[ymd]
  breakfast = ""
  lunch = ""
  dinner = ""

  for i in food['breakfast'] :
    breakfast=breakfast+str(i)+' '
  for i in food['lunch'] :
    lunch=lunch+str(i)+' '
  for i in food['dinner'] :
    dinner=dinner+str(i)+' '
  
  return ymd,breakfast,lunch,dinner






game = discord.Game("!사용방법")    #디스코드 게임활동 메시지 설정
bot = commands.Bot(command_prefix='!',activity=game,help_command=None) # !가 앞에 있을 때 명령어를 받아드림. 게임중 상태 설정. 추가적으로 설정할 도움명령 없음.
nowday,nowtime=timeset()
nextday = (nowday+1)%6
print(nextday)
if nowday == 1:
  timetable = copy.deepcopy(Backup)

""" 봇 명령어"""
command = {
            "!시간표 O반":"각반 오늘의시간표를 출력해줍니다.\n",
            "!내일시간표 O반":"각반 내일의 시간표를 출력해줍니다.\n",
            "!오늘급식":"오늘의 급식을 출력해줍니다.\n",
            "!시간표수정":"봇 관리자(도비)를 멘션합니다."
          }

@bot.command()
async def 시간표(ctx,ban):
    onebantime = "\n"
    if nowday==5 or nowday==6:
      await ctx.send('```주말에는 좀 쉬세요```')
    else :
      onebantime="\n".join(timetable.get(ban)[nowday])
      await ctx.send('```오늘 {}의 시간표\n'.format(ban)+ onebantime+'```')

@bot.command()
async def 내일시간표(ctx,ban):
    onebantime = "\n"
    if nextday==5 or nextday==6:
      await ctx.send('```내일은 신나는 주말인 거시와요!```')
    else :
      onebantime="\n".join(timetable.get(ban)[nextday])
      await ctx.send('```내일 {}의 시간표\n'.format(ban)+ onebantime+'```')

@bot.command(name = "오늘급식")
async def 급식표(ctx):
  ymd,b,l,d=foods(nowtime)
  await ctx.send('```{} 급식표\n아침급식 : '.format(ymd)+b+'\n점심급식 : '+l+'\n저녁급식 : '+d+'```')
 
@bot.command(name = "시간표수정")
async def 시간표수정(ctx):
  id = '587083600063889423'
  await ctx.send(f'<@!{id}>, 시간표 수정좀 해달래요.')

@bot.command(name = "사용방법")
async def 사용방법(ctx):
  com = ""
  for key,value in command.items():
    com+=(str(key)+':'+str(value)+'\n')
  await ctx.send('```'+com+'```')

@bot.command()
async def 안녕(ctx):
  await ctx.send('```살려주세요```')
        
access_token = os.environ["BOT_TOKEN"]
bot.run('BOT_TOKEN')
