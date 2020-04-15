import sys
import argparse

parser = argparse.ArgumentParser(prog='My Script')
parser.add_argument('-i', '--integer', type=int, action='store', dest='intarg', help='an integer', required=True)
parser.add_argument('-s', '--string', dest='strarg', action='store', default='hello',
                    help='string argument')

def run(num, string):
  print('%s %d' % (string, num))

if __name__ == '__main__':
  # print(sys.argv)
  # if sys.argv[1] == 'say_hello':
  #   print('hello world')

  args = parser.parse_args() 
  print(args.intarg)
  run(args.intarg, args.strarg)
  # print(args.intarg)
  run(args.intarg, args.strarg)
  # Git hehe
