import sys
import argparse
import requests


parser = argparse.ArgumentParser(prog='My Postman')
parser.add_argument('-X', '--request', type=str, action='store', dest='request',
                    help='HTTP method', default='GET')
parser.add_argument('-H', '--header', type=str, action='store', dest='header',
                    default=None, help='HTTP headers')
parser.add_argument('-d', '--data', type=str, action='store', dest='data',
                    default=None, help='HTTP POST data')

# req_dispatcher = {
#   'get': requests.get,
#   'post': requests.post,
#   'delete': requests.delete
# }

# Linux: crontab

def curl(method, headers, data, url):
  # print('%s %s %s %s' % (method, url, headers, data))
  if method.lower() == 'get':
    return requests.get(url=url, headers=headers, data=data)
  elif method.lower() == 'post':
    return requests.post(url=url, headers=headers, data=data)
  elif method.lower() == 'delete':
    return requests.delete(url=url, headers=headers, data=data)

  # return req_dispatcher.get(method.lower())(url=url, headers=headers, data=data)


# script -X post/get -H 'accept:application/json;Content-Type:application/json' -d data http://120.72.106.56:9000/v1/documents

if __name__ == '__main__':
  args, argv = parser.parse_known_args()

  headers = None
  if args.header:
    headers = [item.split(':') for item in args.header.split(';')]
    headers = dict(headers)

  res = curl(args.request, headers, args.data, argv[0])
  if res:
    print(res.json())