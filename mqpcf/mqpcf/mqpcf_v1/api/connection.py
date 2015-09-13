# -*- coding: utf-8 -*-
from flask import request, g

from . import Resource
from .. import schemas
import CMQC
from . import mq_cache, mq_defs
import pymqi
import CMQCFC
import json

class Connection(Resource):

    def get(self):
        try:
            if 'connection_id' in g.args:
                args = {CMQCFC.MQBACF_CONNECTION_ID: g.args['connection_id']}
            else:
                args = {CMQCFC.MQBACF_GENERIC_CONNECTION_ID: pymqi.ByteString(''),
                        CMQCFC.MQIACF_CONNECTION_ATTRS: CMQCFC.MQIACF_ALL}

            print args

            conn = mq_cache.get(g.args['qmgr_name'])
            pcf = pymqi.PCFExecute(conn)
            connections = pcf.MQCMD_INQUIRE_CONNECTION(args)

          #  print connections

        except pymqi.MQMIError, e:
            print "got mq error"
            return {"reason": e.reason, "code": e.comp, "message": e.errorAsString()}, 500

        except Exception, ex:
            print ex
            return {"message": ex.message}, 500

        connections = map(lambda x: mq_defs.mqcons_to_string(x), connections)

        if 'channel_name' in g.args:
            connections = filter(lambda x: x['channel_name'] == g.args['channel_name'], connections)

        for c in connections:
            print c
        #mq_defs.make_swagger_defs("connection", connections[0])
        #import json
        #xj = json.dumps(connections)
        #print xj
        return connections, 200, None