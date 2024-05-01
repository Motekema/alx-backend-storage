#!/usr/bin/env python3
"""
Log Stats
"""
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    '''Prints stats about Nginx request logs.
    '''
    total_logs = nginx_collection.count_documents({})
    print('{} logs'.format(total_logs))

    methods = {
        'GET': 0,
        'POST': 0,
        'PUT': 0,
        'PATCH': 0,
        'DELETE': 0
    }
    status_checks_count = 0

    for log in nginx_collection.find():
        method = log.get('method', '')
        if method in methods:
            methods[method] += 1
        if method == 'GET' and log.get('path', '') == '/status':
            status_checks_count += 1

    print('Methods:')
    for method, count in methods.items():
        print('\tmethod {}: {}'.format(method, count))

    print('{} status check'.format(status_checks_count))


def run():
    '''Provides some stats about Nginx logs stored in MongoDB.
    '''
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
