# -*- coding: utf-8 -*-
from flask import request, g

from . import Resource
from .. import schemas

import mq_defs
import CMQC
import CMQCFC
import pymqi
from . import mq_defs, mq_cache

class ChannelStatus(Resource):

    def get(self):
        try:
            if 'name' in g.args:
                name_match = str(g.args['name'])
            else:
                name_match = '*'

            if 'type' in g.args:
                ctype = g.args['type']
                if ctype == "svrconn":
                    chl_type = CMQC.MQCHT_SVRCONN
                elif ctype == "sender":
                    chl_type = CMQC.MQCHT_SENDER
                elif ctype == "receiver":
                    chl_type = CMQC.MQCHT_RECEIVER
                elif ctype == 'server':
                    chl_type = CMQC.MQCHT_SERVER
                elif ctype == 'requestor':
                    chl_type = CMQC.MQCHT_REQUESTER
                elif ctype == 'clntconn':
                    chl_type = CMQC.MQCHT_CLNTCONN
                elif ctype == 'clusrcvr':
                    chl_type = CMQC.MQCHT_CLUSRCVR
                elif ctype == 'clussndr':
                    chl_type = CMQC.MQCHT_CLUSSDR
                else:
                    chl_type = CMQC.MQCHT_ALL
            else:
                chl_type = CMQC.MQCHT_ALL

            args = {CMQCFC.MQCACH_CHANNEL_NAME: name_match}

            print args

            conn = mq_cache.get(g.args['qmgr_name'])
            pcf = pymqi.PCFExecute(conn)
            channels = pcf.MQCMD_INQUIRE_CHANNEL_STATUS(args)

        except pymqi.MQMIError, e:
            return {"reason": e.reason, "code": e.comp, "message": e.errorAsString()}, 500

        except Exception, ex:
            return {"message": ex.message}, 500

        channels = map(lambda x: mq_defs.mqcons_to_string(x), channels)
        # print queues
        mq_defs.make_swagger_defs("channel_status", channels[0])
        return channels, 200, None