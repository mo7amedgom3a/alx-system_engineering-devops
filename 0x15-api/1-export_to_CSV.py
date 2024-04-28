#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


if __name__ == '__main__':
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get('name')

    todoUrl = url + "/todos"
    response = requests.get(todoUrl)
    tasks = response.json()
    with open('{}.csv'.format(employeeId), 'w') as f:
        for task in tasks:
            f.write('"{}","{}","{}","{}"\n'.format(employeeId, employeeName,
                                                   task.get('completed'),
                                                   task.get('title')))
