import asyncio,discord
from discord.ext import commands 
from datetime import datetime

t1=[['1.창체','2.프로','3.프로','4.수학','5.국어','6.국어','7.영어'],
['1.컴구', '2.컴구', '3.과학', '4.체육', '5.프로', '6.프로', '7.프로'],
['1.영어', '2.영어', '3.컴구', '4.음악', '5.국어', '6.수학', '7.수학'],
['1.사회', '2.사회', '3.프로', '4.프로', '5.창체', '6.창체', '7.창체'],
['1.과학', '2.과학', '3.체육', '4.사회', '5.음악', '6.음악'],
['있겠냐 1반'],
['있겠냐 바부야']]

t2=[['1.창체', '2.프로', '3.프로', '4.프로', '5.과학', '6.영어', '7.수학'],
['1.국어', '2.국어', '3.컴구', '4.컴구', '5.체육', '6.사회', '7.사회'],
['1.프로', '2.프로', '3.프로', '4.프로', '5.음악', '6.영어', '7.영어'],
['1.컴구', '2.체육', '3.과학', '4.과학', '5.창체', '6.창체', '7.창체'],
['1.수학', '2.수학', '3.음악', '4.음악', '5.사회', '6.국어'],
['있겠냐 2반'],['있겠냐 잠좀자']]

t3=[['1.창체', '2.음악', '3.컴구', '4.컴구', '5.영어', '6.사회', '7.프로'],
['1.음악', '2.음악', '3.수학','4.수학','5.국어', '6.프로', '7.프로'],
['1.과학', '2.사회', '3.사회', '4.체육', '5.프로', '6.국어', '7.국어'],
['1.프로', '2.컴구', '3.영어', '4.영어', '5.창체', '6.창체', '7.창체'],
['1.프로', '2.프로', '3.과학', '4.과학', '5.수학', '6.체육'],
['있겠냐 3반'],['있겠냐 심심하다']]

t4=[['1.창체', '2.영어', '3.프로', '4.프로', '5.컴구', '6.컴구', '7.사회'],
['1.수학', '2.수학', '3.사회', '4.사회', '5.음악','6.체육', '7.과학->국어'],
['1.컴구', '2.음악', '3.음악', '4.국어->과학', '5.프로', '6.프로', '7.프로'],
['1.과학', '2.과학', '3.체육', '4.수학', '5.창체', '6.창체', '7.창체'],
['1.영어', '2.영어', '3.국어', '4.국어', '5.프로', '6.프로'],
['있겠냐 4반'],['있겠냐 역시 지민이가문제야']]
save=[0,0,0,0,0,0,0]
client = discord.Client()
n=datetime.today().weekday()
if n==6:
  m=0
else :
  m=datetime.today().weekday()+1
print(n)
game = discord.Game("!사용방법")
bot = commands.Bot(command_prefix='!',activity=game,help_command=None)

@bot.event
async def on_ready():
  await bot.change_presence(name="반갑습니다 :D", type=1)


@bot.command(name='대마고대표커요미')
async def 커요미(ctx):
  await ctx.send('```그건바로너(?)```')

@bot.command(name='지민이바보')
async def 커요미(ctx):
  await ctx.send('```인정```')

@bot.command(name='혜준이능지')
async def 커요미(ctx):
  await ctx.send('```메이플(?)```')

@bot.command(name='1반대표능지처참')
async def 커요미(ctx):
  await ctx.send('```:15번```')

@bot.command(name='4반대표능지처참')
async def 커요미(ctx):
  await ctx.send('```:김지민```')
  await ctx.send('```미안하다 이거 보여줄라고 어그로 끌었다 나루토가 던지는 나선정환킴실화냐?```')

@bot.command(name='1반시간표')
async def 시간표(ctx):
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




@bot.command(name='실행시간')
async def 안녕(ctx):
  await ctx.send('주인님이 일어났을 때부터~ P.M 6시까지')

@bot.command(name='사용방법')
async def 사용방법(ctx):
  await ctx.send('``` !1or2or3or4반시간표 :각반시간표를 보여줍니다. 띄어쓰기 없음\n!실행시간 : 실행시간을 보여줍니다\n!내일1or2or3or4반시간표 :각반시간표를 보여줍니다.\n!안녕 : 봇이 응답해줍니다.\n!대마고대표커요미 : 알죠?ㅋㅋ\n!지민이바보 :\n!혜준이능지 :\n!1반대표능지처참\n!4반대표능지처참```')

@bot.command(name='안녕')
async def 안녕(ctx):
  await ctx.send('살려주세요')

bot.run('NzA2MTIxMzc3MDIzMDAwNTc3.Xrvhgg.Flxrg6JK8efb8lSUfRqQX1UBm_M')