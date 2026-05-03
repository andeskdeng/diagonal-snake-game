import pygame
from random import randint

pygame.init()
screen = pygame.display.set_mode((501,501))
pygame.display.set_caption("Snake")
snake=[[0,0]]
fruit=[[9,9]]
x=0
y=0
grow=0
end=False
clock=pygame.time.Clock()
while True:
  #key_detect
  for event in pygame.event.get():
    if event.type==pygame.KEYDOWN:
      if event.key==pygame.K_m:
        y=1
      elif event.key==pygame.K_j:
        y=0 
      elif event.key==pygame.K_u:
        y=-1
      elif event.key==pygame.K_d:
        x=1
      elif event.key==pygame.K_s:
        x=0
      elif event.key==pygame.K_a:
        x=-1
    elif event.type==pygame.QUIT:
      end=True
      break
  #collision?
  for i in enumerate(fruit):
    if snake[-1]==i[1]:
      fruit.pop(i[0])
      grow+=1
      while True:
        if len(snake+fruit)==100:
          break
        newpos=[randint(0,9),randint(0,9)]
        if newpos not in snake+fruit:
          fruit.append(newpos)
          break
      break
  #move?
  snake.append([snake[-1][0]+x,snake[-1][1]+y])
  if grow:
    grow-=1
  else:
    snake.pop(0)
  #update
  screen.fill("Black")
  for i in range(11):
    pygame.draw.line(screen,"white",(50*i,0),(50*i,500))
    pygame.draw.line(screen,"white",(0,50*i),(500,50*i))
  for i in fruit:
    pygame.draw.rect(screen,"red",pygame.Rect(50*i[0]+1,50*i[1]+1,49,49))
  for i in snake:
    pygame.draw.rect(screen,"green",pygame.Rect(50*i[0]+1,50*i[1]+1,49,49))
  pygame.display.flip()
  #end?
  if any([end,snake[-1][1]>9,
          snake[-1][1]<0,
          snake[-1][0]>9,
          snake[-1][0]<0,
          snake[-1] in snake[:-1]]):
    pygame.display.quit()
    break
  #tick
  clock.tick(3)