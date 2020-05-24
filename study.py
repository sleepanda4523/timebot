import asyncio,discord
from discord.ext import commands 
from datetime import datetime
import os
import time

stack = [
  ['김지민',0],['박승준',0],['유정민',0],['전규현',0],['홍태희',0]]
ranking = [0 for i in range(len(stack))]

bantime=[['김지민',0],['박승준',0],['유정민',0],['전규현',0],['홍태희',0]]

game = discord.Game("!사용방법")
bot = commands.Bot(command_prefix='!',activity=game,help_command=None)


n='hi'     
print(n+stack[0][0])
print(time.time())
@bot.command()
async def 벤(ctx,name):
  i=0
  while i<len(bantime):
    if(name==bantime[i][0]):
      banname=bantime[i][0]
      bantime[i][1]=bantime[i][1]+30
      if (bantime[i][1]>60) :
        await ctx.send('```'+banname+'님 영구 벤입니다. ```')
      else:
        await ctx.send('```현재 '+banname+'님 '+str(bantime[i][1])+'분동안 벤입니다. ```')
      
      """max_time = time.time()+(60*bantime[i][1])
      print(max_time)
      while True:
        if max_time < time.time():
          await ctx.send('```'+banname+'님 벤 시간 종료됬습니다. ```')
          break"""
    i=i+1

@bot.commend()
async def 추가(ctx,name):
  stack.append([name,0])
  bantime.append([name,0])
 

@bot.command()
async def push(ctx,name):
  i=0
  n=name
  print(n)
  while i<len(stack):
    if(n==stack[i][0]):
      you = stack[i][0]
      stack[i][1]=stack[i][1]+1
      your=str(stack[i][1])
      print(you)
      print(your)
      await ctx.send('```'+you+'님 1스택 경고. 조심하세요ㅡㅡ\n현재 당신의 스택 현황:'+your+'```')
      break
    i=i+1

@bot.command()
async def pop(ctx,name):
  i=0
  while i<len(stack):
    if(name==stack[i][0]):
      you = stack[i][0]
      print(you)
      if(stack[i][1]>0):
        stack[i][1]=stack[i][1]-1
      your=str(stack[i][1])
      print(your)
      await ctx.send('```'+you+'님 1스택 제거. 축하드려요!\n현재 당신의 스택 현황:'+your+'```')
      break
    i=i+1


@bot.command()
async def 현황(ctx,name):
  i=0
  n=name
  print(n)
  while i<5:
    if(n==stack[i][0]):
      you = stack[i][0]
      your=str(stack[i][1])
      print(you)
      print(your)
      await ctx.send('```'+you+'님의 스택 현황:'+your+'```')
      break
    i=i+1

@bot.command(name='스택순위')
async def 스택순위(ctx):
  i=0
  stack.sort(key=lambda x: x[1])
  print(stack)
  while i<len(stack):
    n=str(i+1)
    ranking[i]=str(n+'. '+stack[i][0]+': '+str(stack[i][1]))
    print(ranking)
    i=i+1
  await ctx.send('```{}```'.format('\n'.join(ranking)) )

@bot.command(name='사용방법')
async def 사용방법(ctx):
  await ctx.send('```!push 이름 : 1스택 적립\n!pop 이름 : 1스택 감소\n!현황 이름 : 그 사람의 스택 현황\n!스택순위 : 스택이 가장 적은 순으로 순위 보여줌\n!추가 이름: 배열에 자기 이름을 추가합니다.\n!안녕 : 봇이 인사합니다.')

@bot.command(name='안녕')
async def 안녕(ctx):
  await ctx.send('```판다컴퍼니의 오신걸 환영합니다!```')

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)

#bot.run('NzEwNzAwNzgxMzU5MjAyMzg1.Xr_odg.0gundmEqFRakLYzh-a3HwmF0PGI')
