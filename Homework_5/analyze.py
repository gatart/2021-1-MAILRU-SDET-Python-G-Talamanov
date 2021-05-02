#!/usr/bin/env python
import argparse
import re
import json
from os.path import isfile


def a(lines):
    return len(lines)


def t(requests):
    methods = ['OPTIONS', 'GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'TRACE', 'CONNECT']
    stats = {}
    for dict_ in requests:
        method = dict_['method']
        if method not in methods:
            continue

        if method not in stats.keys():
            stats[method] = 0

        stats[method] += 1

    ret = []
    for key in stats:
        dict_ = {}
        dict_['method'] = key
        dict_['count'] = stats[key]
        ret.append(dict_)

    return ret

#---------------------------------------------------------------------------------------------------------------------------

def f(requests):
    requests.sort(key=lambda x: x['url'])
    ans = []
    flag = True
    tmp = {}
    for elm in requests:
        if flag:
            tmp['url'] = elm['url']
            tmp['count'] = 0
            flag = False
        if elm['url'] != tmp['url']:
            ans.append(tmp)
            tmp = {}
            tmp['url'] = elm['url']
            tmp['count'] = 1
        else:
            tmp['count'] += 1

    ans.append(tmp)
    ans.sort(key=lambda x: x['count'], reverse=True)
    ans = ans[:10]

    ret = []
    for request in ans:
        dict_ = {}
        dict_['url'] = request['url']
        dict_['count'] = request['count']
        ret.append(dict_)

    return ret

#--------------------------------------------------------------------------------------------------------------------------------

def c(requests):
    requests = list(filter(lambda x: x['code'] in range(400, 500), requests))
    requests.sort(key=lambda x: x['len'], reverse=True)
    ans = requests[:5]

    ret = []
    for request in ans:
        dict_ = {}
        dict_['url'] = request['url']
        dict_['code'] = request['code']
        dict_['len'] = request['len']
        dict_['ip'] = request['ip']
        ret.append(dict_)

    return ret


def s(requests):
    requests = list(filter(lambda x: x['code'] in range(500, 600), requests))
    requests.sort(key=lambda x: x['ip'])
    ans = []
    flag = True
    tmp = {}
    for elm in requests:
        if flag:
            tmp['ip'] = elm['ip']
            tmp['count'] = 0
            flag = False
        if elm['ip'] != tmp['ip']:
            ans.append(tmp)
            tmp = {}
            tmp['ip'] = elm['ip']
            tmp['count'] = 1
        else:
            tmp['count'] += 1

    ans.append(tmp)
    ans.sort(key=lambda x: x['count'], reverse=True)
    ans = ans[:5]

    ret = []
    for request in ans:
        dict_ = {}
        dict_['ip'] = request['ip']
        dict_['count'] = request['count']
        ret.append(dict_)

    return ret


def to_requests(lines):
    requests = []
    for line in lines:
        dict_ = {}
        splited = re.split('[ "]', line)
        dict_['ip'] = splited[0]
        dict_['method'] = splited[6]
        dict_['url'] = splited[7]
        dict_['code'] = int(splited[10])
        if splited[11] == '-':
            dict_['len'] = 0
        else:
            dict_['len'] = int(splited[11])
        requests.append(dict_)

    return requests


def main():
    outfile = 'analyzed'

    parser = argparse.ArgumentParser(usage='analyze.py  [--json]  a | t | f | c | s  <FILE>',
                                     epilog=f'Имя выходного файла - "{outfile}".')
    parser.add_argument('task', action='store', help='см. в README.md', choices=['a', 't', 'f', 'c', 's'])
    parser.add_argument('file', action='store', metavar='FILE', help='входной файл')
    parser.add_argument('--json', action='store_true', help='записать вывод в формате JSON')

    args = parser.parse_args()

    if isfile(outfile):
        print(f"File '{outfile}' exists, overwrite? (yes/NO): ", end='')
        in_ = input()
        if not (in_ == 'y' or in_ == 'yes'):
            raise FileExistsError()

    with open(args.file) as fl:
        lines = fl.read().split('\n')

    method = '^(OPTIONS|GET|HEAD|POST|PUT|DELETE|TRACE|CONNECT)$'
    for line in lines:
        if not re.search(method, line):
            del line

    if lines[-1] == '':
        del lines[-1]

    task = args.task
    if task == 'a':
        res = a(lines)
    else:
        requests = to_requests(lines)
        if task == 't':
            res = t(requests)
        elif task == 'f':
            res = f(requests)
        elif task == 'c':
            res = c(requests)
        elif task == 's':
            res = s(requests)
        else:
            raise Exception()

    with open(outfile, 'w') as fl:
        if args.json:
            fl.write(json.dumps(res))
        else:
            if isinstance(res, list):
                for line in res:
                    for key in line:
                        fl.write(str(line[key]) + ' ')
                    fl.write('\n')
            elif isinstance(res, int):
                fl.write(str(res))
            else:
                raise Exception()


if __name__ == '__main__':
    main()
