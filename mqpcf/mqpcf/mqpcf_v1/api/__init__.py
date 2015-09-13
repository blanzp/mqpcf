# -*- coding: utf-8 -*-
import flask_restful as restful

from ..validators import request_validate, response_filter

import pymqi
import CMQC, CMQCFC
from pymqi import MQMIError


class Resource(restful.Resource):
    method_decorators = [request_validate, response_filter]


class MQConnectionCache(object):
    servers=[{"qmgr":'TESTQM1', "channel":'SYSTEM.DEF.SVRCONN', "ip":"127.0.0.1(1414)"},
         {"qmgr":'TESTQM2', "channel":'SYSTEM.DEF.SVRCONN', "ip":"127.0.0.1(1415)"},
         {"qmgr":'TESTQM3', "channel":'SYSTEM.DEF.SVRCONN', "ip":"127.0.0.1(1416)"}]

    def __init__(self):
        self.cache = dict()

    def get(self, qmgr_name):
        if qmgr_name in self.cache.keys():
            print "cache hit"
            conn = self.cache[qmgr_name]
            if conn._is_connected:
                return conn
            else:
                print "cache reconnect"
                return self.connect(qmgr_name)
        else:
            print "cache miss"
            return self.connect(qmgr_name)

    def connect(self, qmgr_name):
        conn = MQConnectionCache.get_connection(qmgr_name)
        self.cache[qmgr_name] = conn
        return conn

    @staticmethod
    def get_connection(qmgr_name):
        hit = filter(lambda x: x['qmgr'] == qmgr_name, MQConnectionCache.servers)
        if len(hit):
            hit = hit[0]
            print "connecting to", qmgr_name
            try:
                conn = pymqi.connect(hit['qmgr'],hit['channel'],hit['ip'])
            except pymqi.MQMIError, e:
                if e.reason == CMQC.MQRC_CONNECTION_BROKEN:
                    print "Connection to qmgr broken attempting reconnect"
                    return pymqi.connect(hit['qmgr'],hit['channel'],hit['ip'])
                else:
                    print "Connection failed with ", e.reason
                    raise e
            print "successfully connected to", qmgr_name
            return conn
        else:
            raise Exception("No such server")

mq_cache = MQConnectionCache()
