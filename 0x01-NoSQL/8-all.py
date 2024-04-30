#!/usr/bin/env python3
""" 8-main """


def list_all(mongo_collection):
  '''list all docs'''
  return [doc for doc in mongo_collection.find()]
