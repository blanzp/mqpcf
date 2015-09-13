# -*- coding: utf-8 -*-
from flask import request, g

from . import Resource
from .. import schemas
import mq_defs
from . import mq_cache
import pymqi
import CMQC

class Queue(Resource):

    def get(self):
        try:
            if 'name' in g.args:
                queue_match = str(g.args['name'])
            else:
                queue_match = '*'

            if 'type' in g.args:
                qtype = g.args['type']
                if qtype == "local":
                    queue_type = CMQC.MQQT_LOCAL
                elif qtype == "remote":
                    queue_type = CMQC.MQQT_REMOTE
                elif qtype == "alias":
                    queue_type = CMQC.MQQT_ALIAS
                elif qtype == 'model':
                    queue_type = CMQC.MQQT_MODEL
                elif qtype == 'cluster':
                    queue_type = CMQC.MQQT_CLUSTER
                else:
                    queue_type = CMQC.MQQT_ALL
            else:
                queue_type = CMQC.MQQT_ALL

            args = {CMQC.MQCA_Q_NAME: queue_match,
                    CMQC.MQIA_Q_TYPE: queue_type}

            conn = mq_cache.get(g.args['qmgr_name'])
            pcf = pymqi.PCFExecute(conn)
            queues = pcf.MQCMD_INQUIRE_Q(args)
        except pymqi.MQMIError, e:
            return {"reason": e.reason, "code": e.comp, "message": e.errorAsString()}, 500
        except Exception, ex:
            return {"message": ex.message }, 500
        queues = map(lambda x: mq_defs.mqcons_to_string(x), queues)
        #print queues
        #mq_defs.make_swagger_defs("queue", queues[0])
        return queues, 200, None