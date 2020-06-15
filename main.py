import discord
import os
from discord.ext import commands 
import datetime
import requests                  # 웹 페이지의 HTML을 가져오는 모듈    
import time

t1=[['1.창체','2.프로','3.프로','4.과학','5.사회','6.음악','7.영어'],
['1.컴구', '2.컴구', '3.수학', '4.체육', '5.국어', '6.프로', '7.프로'],
['1.영어', '2.사회', '3.컴구', '4.음악', '5.수학', '6.과학', '7.국어'],
['1.국어', '2.음악', '3.프로', '4.프로', '5.창체', '6.창체', '7.창체'],
['1.수학', '2.과학', '3.체육', '4.사회', '5.영어', '6.프로'],
['있겠냐 1반'],
['있겠냐 바부야']]

t2=[['1.창체', '2.프로', '3.프로', '4.프로', '5.수학', '6.영어', '7.과학'],
['1.국어', '2.음악', '3.컴구', '4.컴구', '5.체육', '6.수학', '7.사회'],
['1.프로', '2.프로', '3.프로', '4.프로', '5.국어', '6.음악', '7.영어'],
['1.컴구', '2.체육', '3.사회', '4.과학', '5.창체', '6.창체', '7.창체'],
['1.음악', '2.수학->사회', '3.사회->수학', '4.영어', '5.국어', '6.과학'],
['있겠냐 2반'],['있겠냐 잠좀자']]

t3=[['1.창체', '2.수학', '3.컴구', '4.컴구', '5.영어', '6.국어', '7.프로'],
['1.과학', '2.수학', '3.음악','4.영어','5.사회', '6.프로', '7.프로'],
['1.수학', '2.음악', '3.사회', '4.체육', '5.프로', '6.영어', '7.과학'],
['1.프로->체육', '2.국어', '3.과학', '4.사회', '5.창체', '6.창체', '7.창체'],
['1.국어', '2.프로', '3.프로', '4.컴구', '5.음악', '6.체육->사회'],
['있겠냐 3반'],['있겠냐 심심하다']]

t4=[['1.창체', '2.영어', '3.프로', '4.프로', '5.컴구', '6.컴구', '7.사회'],
['1.음악', '2.사회', '3.과학', '4.국어', '5.수학','6.체육', '7.영어'],
['1.컴구', '2.수학', '3.음악', '4.영어', '5.프로', '6.프로', '7.프로'],
['1.과학', '2.수학', '3.체육', '4.국어', '5.창체', '6.창체', '7.창체'],
['1.사회', '2.국어', '3.과학', '4.음악', '5.프로', '6.프로'],
['있겠냐 4반'],['있겠냐 역시 지민이가문제야']]
save=[0,0,0,0,0,0,0]

now= datetime.datetime.now()
nownine =now+datetime.timedelta(hours=9)
print(nownine)
n=nownine.weekday()
if n==6:
  m=0
else :
  m=n+1
print(n)

game = discord.Game("!사용방법")
bot = commands.Bot(command_prefix='!',activity=game,help_command=None)

ymd = nownine.strftime('%Y-%m-%d')
print(ymd)
url='https://api.dsm-dms.com/meal/'+ymd+''
#soup = BeautifulSoup(res.content, 'html.parser')
data = requests.get(url).json()

ndata = data[ymd]
breakfast = []
lunch = []
dinner = []
j=0;
for i in ndata['breakfast'] :
  print(i)
  breakfast.append(str(i))
  j+=1

for i in ndata['lunch'] :
  print(i)
  lunch.append(str(i))

  j+=1
print(lunch)

for i in ndata['dinner'] :
  print(i)
  dinner.append(str(i))
  j+=1
print(dinner)

@bot.command(name='아침급식')
async def 급식(ctx):
  await ctx.send('```아침급식은 \n{} 입니다.```'.format('\n'.join(breakfast)))

@bot.command(name='점심급식')
async def 급식(ctx):
  await ctx.send('```점심급식은 \n{} 입니다.```'.format('\n'.join(lunch)))

@bot.command(name='저녁급식')
async def 급식(ctx):
  await ctx.send('```저녁급식은 \n{} 입니다.```'.format('\n'.join(dinner)))


@bot.command(name='점심시간')
async def 점심시간(ctx):
  await ctx.send('```1학년 점심시간은 12:40분에 먹으러가세요\n 점심시간은 12:10~13:30분입니다.```')

  
@bot.command(name='저녁시간')
async def 저녁시간(ctx):
  await ctx.send('```1학년 저녁시간은 17:50분에 먹으러가세요\n 저녁시간은 17:20~18:40분입니다.```')
  
@bot.command(name='대마고대표커요미')
async def 커요미(ctx):
  await ctx.send('```그건바로너(?)```')

@bot.command(name='지민이바보')
async def 커요미(ctx):
  await ctx.send('```인정```')

@bot.command(name='혜준이능지')
async def 커요미(ctx):
  await ctx.send('```메이플(?)```')


@bot.command(name='1반시간표')
async def 시간표(ctx):
  now= datetime.datetime.now()
  nownine =now+datetime.timedelta(hours=9)
  n=nownine.weekday()
  if n==6:
   m=0
  else :
    m=n+1
  
  i=0
  if n==4:
    while (i<6):
      save[i]=t1[n][i]
      i=i+1
    await ctx.send('```오늘의 시간표는\n'+save[0]+'\n'+save[1]+'\n'+save[2]+'\n'+save[3]+'\n'+save[4]+'\n'+save[5]+'\n'+'틀렸다면 1213이주석에게 제보해주세요 제보는 언제나 환영!```')
  elif(n==5 or n==6):
    await ctx.send('```오늘의 시간표는'+t1[n][0]+'```')
  else:
    while (i<7):
      save[i]=t1[n][i]
      i=i+1
    await ctx.send('```오늘의 시간표는\n'+save[0]+'\n'+save[1]+'\n'+save[2]+'\n'+save[3]+'\n'+save[4]+'\n'+save[5]+'\n'+save[6]+'\n'+'틀렸다면 1213이주석에게 제보해주세요 제보는 언제나 환영!```')

@bot.command(name='2반시간표')
async def 시간표(ctx):
  now= datetime.datetime.now()
  nownine =now+datetime.timedelta(hours=9)
  n=nownine.weekday()
  if n==6:
   m=0
  else :
    m=n+1
  
  i=0
  if n==4:
    while (i<6):
      save[i]=t2[n][i]
      i=i+1
    await ctx.send('```오늘의 시간표는\n'+save[0]+'\n'+save[1]+'\n'+save[2]+'\n'+save[3]+'\n'+save[4]+'\n'+save[5]+'\n'+'틀렸다면 1213이주석에게 제보해주세요 제보는 언제나 환영!```')
  elif(n==5 or n==6):
    await ctx.send('```오늘의 시간표는'+t2[n][0]+'```')
  else:
    while (i<7):
      save[i]=t2[n][i]
      i=i+1
    await ctx.send('```오늘의 시간표는\n'+save[0]+'\n'+save[1]+'\n'+save[2]+'\n'+save[3]+'\n'+save[4]+'\n'+save[5]+'\n'+save[6]+'\n'+'틀렸다면 1213이주석에게 제보해주세요 제보는 언제나 환영!```')

@bot.command(name='3반시간표')
async def 시간표(ctx):
  now= datetime.datetime.now()
  nownine =now+datetime.timedelta(hours=9)
  n=nownine.weekday()
  if n==6:
   m=0
  else :
    m=n+1
  
  i=0
  if n==4:
    while (i<6):
      save[i]=t3[n][i]
      i=i+1
    await ctx.send('```오늘의 시간표는\n'+save[0]+'\n'+save[1]+'\n'+save[2]+'\n'+save[3]+'\n'+save[4]+'\n'+save[5]+'\n'+'틀렸다면 1213이주석에게 제보해주세요 제보는 언제나 환영!```')
  elif(n==5 or n==6):
    await ctx.send('```오늘의 시간표는'+t3[n][0]+'```')
  else:
    while (i<7):
      save[i]=t3[n][i]
      i=i+1
    await ctx.send('```오늘의 시간표는\n'+save[0]+'\n'+save[1]+'\n'+save[2]+'\n'+save[3]+'\n'+save[4]+'\n'+save[5]+'\n'+save[6]+'\n'+'틀렸다면 1213이주석에게 제보해주세요 제보는 언제나 환영!```')

@bot.command(name='4반시간표')
async def 시간표(ctx):
  now= datetime.datetime.now()
  nownine =now+datetime.timedelta(hours=9)
  n=nownine.weekday()
  if n==6:
   m=0
  else :
    m=n+1
  
  i=0
  if n==4:
    while (i<6):
      save[i]=t4[n][i]
      i=i+1
    await ctx.send('```오늘의 시간표는\n'+save[0]+'\n'+save[1]+'\n'+save[2]+'\n'+save[3]+'\n'+save[4]+'\n'+save[5]+'\n'+'틀렸다면 1213이주석에게 제보해주세요 제보는 언제나 환영!```')
  elif(n==5 or n==6):
    await ctx.send('```오늘의 시간표는'+t4[n][0]+'```')
  else:
    while (i<7):
      save[i]=t4[n][i]
      i=i+1
    await ctx.send('```오늘의 시간표는\n'+save[0]+'\n'+save[1]+'\n'+save[2]+'\n'+save[3]+'\n'+save[4]+'\n'+save[5]+'\n'+save[6]+'\n'+'틀렸다면 1213이주석에게 제보해주세요 제보는 언제나 환영!```')



@bot.command(name='내일1반시간표')
async def 내일시간표(ctx):
  now= datetime.datetime.now()
  nownine =now+datetime.timedelta(hours=9)
  n=nownine.weekday()
  if n==6:
   m=0
  else :
    m=n+1
    
  
  i=0
  if m==4:
    while (i<6):
      save[i]=t1[m][i]
      i=i+1
    await ctx.send('```내일의 시간표는\n'+save[0]+'\n'+save[1]+'\n'+save[2]+'\n'+save[3]+'\n'+save[4]+'\n'+save[5]+'\n'+'틀렸다면 1213이주석에게 제보해주세요 제보는 언제나 환영!```')
  elif(m==6):
    await ctx.send('```내일의 시간표는'+t1[6][0]+'```')
  else:
    while (i<7):
      save[i]=t1[m][i]
      i=i+1
    await ctx.send('```내일의 시간표는\n'+save[0]+'\n'+save[1]+'\n'+save[2]+'\n'+save[3]+'\n'+save[4]+'\n'+save[5]+'\n'+save[6]+'\n'+'틀렸다면 1213이주석에게 제보해주세요 제보는 언제나 환영!```')

@bot.command(name='내일2반시간표')
async def 내일시간표(ctx):
  now= datetime.datetime.now()
  nownine =now+datetime.timedelta(hours=9)
  n=nownine.weekday()
  if n==6:
   m=0
  else :
    m=n+1
  
  i=0
  if m==4:
    while (i<6):
      save[i]=t2[m][i]
      i=i+1
    await ctx.send('```내일의 시간표는\n'+save[0]+'\n'+save[1]+'\n'+save[2]+'\n'+save[3]+'\n'+save[4]+'\n'+save[5]+'\n'+'틀렸다면 1213이주석에게 제보해주세요 제보는 언제나 환영!```')
  elif(m==6):
    await ctx.send('```내일의 시간표는'+t2[6][0]+'```')
  else:
    while (i<7):
      save[i]=t2[m][i]
      i=i+1
    await ctx.send('```내일의 시간표는\n'+save[0]+'\n'+save[1]+'\n'+save[2]+'\n'+save[3]+'\n'+save[4]+'\n'+save[5]+'\n'+save[6]+'\n'+'틀렸다면 1213이주석에게 제보해주세요 제보는 언제나 환영!```')

@bot.command(name='내일3반시간표')
async def 내일시간표(ctx):
  now= datetime.datetime.now()
  nownine =now+datetime.timedelta(hours=9)
  n=nownine.weekday()
  if n==6:
   m=0
  else :
    m=n+1
  
  i=0
  if m==4:
    while (i<6):
      save[i]=t3[m][i]
      i=i+1
    await ctx.send('```내일의 시간표는\n'+save[0]+'\n'+save[1]+'\n'+save[2]+'\n'+save[3]+'\n'+save[4]+'\n'+save[5]+'\n'+'틀렸다면 1213이주석에게 제보해주세요 제보는 언제나 환영!```')
  elif(m==6):
    await ctx.send('```내일의 시간표는'+t3[6][0]+'```')
  else:
    while (i<7):
      save[i]=t3[m][i]
      i=i+1
    await ctx.send('```내일의 시간표는\n'+save[0]+'\n'+save[1]+'\n'+save[2]+'\n'+save[3]+'\n'+save[4]+'\n'+save[5]+'\n'+save[6]+'\n'+'틀렸다면 1213이주석에게 제보해주세요 제보는 언제나 환영!```')

@bot.command(name='내일4반시간표')
async def 내일시간표(ctx):
  now= datetime.datetime.now()
  nownine =now+datetime.timedelta(hours=9)
  n=nownine.weekday()
  if n==6:
   m=0
  else :
    m=n+1
  
  i=0
  if m==4:
    while (i<6):
      save[i]=t4[m][i]
      i=i+1
    await ctx.send('```내일의 시간표는\n'+save[0]+'\n'+save[1]+'\n'+save[2]+'\n'+save[3]+'\n'+save[4]+'\n'+save[5]+'\n'+'틀렸다면 1213이주석에게 제보해주세요 제보는 언제나 환영!```')
  elif(m==6):
    await ctx.send('```내일의 시간표는'+t4[6][0]+'```')
  else:
    while (i<7):
      save[i]=t4[m][i]
      i=i+1
    await ctx.send('```내일의 시간표는\n'+save[0]+'\n'+save[1]+'\n'+save[2]+'\n'+save[3]+'\n'+save[4]+'\n'+save[5]+'\n'+save[6]+'\n'+'틀렸다면 1213이주석에게 제보해주세요 제보는 언제나 환영!```')



"""
@bot.command(name='실행시간')
async def 안녕(ctx):
  await ctx.send('주인님이 일어났을 때부터~ P.M 6시까지')
"""

@bot.command(name='사용방법')
async def 사용방법(ctx):
  await ctx.send('``` !1or2or3or4반시간표 :각반시간표를 보여줍니다. 띄어쓰기 없음\n!내일1or2or3or4반시간표 :각반시간표를 보여줍니다.\n!안녕 : 봇이 응답해줍니다.\n!대마고대표커요미 : 알죠?ㅋㅋ\n!혜준이능지 :\n!점심시간:점심먹는 시간을 알려줍니다.\n!저녁시간:저녁먹는 시간을 알려줍니다.\n!아침&점심&저녁급식 : 아침,점심,저녁 급식 메뉴를 출력합니다.```')

@bot.command(name='안녕')
async def 안녕(ctx):
  await ctx.send('살려주세요')
access_token = os.environ["BOT_TOKEN"]
#bot.run('NzA2MTIxMzc3MDIzMDAwNTc3.Xt89HQ.qyn__xrYopLKi3sFm7c_gT-pXiI')
bot.run('BOT_TOKEN')
