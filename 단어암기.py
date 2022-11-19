import random as rnd

#List를 입력받아 Dict 형태로 반환함
def convert(lst):
  dct = {lst[i]: lst[i + 1] for i in range(0, len(lst), 2)}
  return dct

#.txt파일을 읽어와 스페이스를 기준으로 split한 뒤 List를 반환
def readFile(file_directory):
  file=open(file_directory, "rt", encoding='UTF-8')
  file_Content = file.read().split(' ')
  words=convert(file_Content)
  file.close()
  return words

#Dict를 입력받아 Dict의 key/value 를 유지하며 무작위로 섞인 Dict를 반환
def shuffleDct(dct):
  lst = list(dct.items())
  rnd.shuffle(lst)
  dct = dict(lst)
  return dct

def main(pairs):

  #입력 받은 Dict를 섞음
  pairs = shuffleDct(pairs)

  #맞은 문제 수와 틀린 문제 수 초기화
  right_Answer_count=0
  wrong_Answer_count=0

  #틀린 단어를 저장할 List
  wrong_Pair=[]

  #입력 받은 Dict의 key를 프린트 한 뒤 value와 같으면 "맞았습니다"를 프린트 하고 맞은 단어 수를 1 증가, 틀리면 틀린 단어 수를 1 증가.
  for i in pairs:
    print(i)
    print('위 단어의 뜻을 적어주세요')
    answer = input()
    if answer == pairs[i]:
      print('맞았습니다.')
      right_Answer_count+=1
    else:
      print('틀렸습니다.')
      wrong_Answer_count+=1
      wrong_Pair.append(i)

  #맞은 문제 수와 틀린 문제 수를 프린트
  print(f"총 {right_Answer_count+wrong_Answer_count}개의 문제 중 {right_Answer_count}개를 맞췄고 {wrong_Answer_count}개를 틀렸습니다.")

  #한 개 이상의 문제를 틀렸다면 텍스트 파일로 출력할지 물음
  if wrong_Answer_count > 0:
    print('틀린 문제를 텍스트 파일로 출력할까요? (y/n)')

    #y나 Y를 입력 받으면 틀린 문제를 텍스트 파일로 출력
    while True:
      output_Answer=input()
      if output_Answer =='y' or output_Answer =='Y':
        output=open('Wrong_Answers.txt', 'w')
        output.write(' '.join(wrong_Pair))
        output.close()
        break
      elif output_Answer =='n' or output_Answer =='N':
        break
      else:
        print('y 혹은 n을 입력해주세요.')

  #y나 Y를 입력 받으면 새로운 파일을 불러옴
  print('새로운 파일을 불러올까요? (y/n)')
  while True:
    redo=input()
    if redo =='y' or redo =='Y' or redo =='n' or redo =='N':
      break
    else:
      print('y 혹은 n을 입력해주세요.')
  return redo

#코드 작동부
redo='y'
while redo == 'y' or redo == 'Y':
  redo = main(readFile(input('파일 경로명을 입력해주세요')))