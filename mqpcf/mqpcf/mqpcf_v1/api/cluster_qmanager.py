# -*- coding: utf-8 -*-
from flask import request, g

from . import Resource
import CMQC
from . import mq_cache
import pymqi
import mq_defs
import json

class ClusterQmanager(Resource):

    def get(self):
        try:
            if 'name' in g.args:
                name_match = str(g.args['name'])
            else:
                name_match = '*'

            args = {CMQC.MQCA_CLUSTER_Q_MGR_NAME: name_match}

            print("cluster_qmanager args: "+json.dumps(args))

            conn = mq_cache.get(g.args['qmgr_name'])
            pcf = pymqi.PCFExecute(conn)
            cluster_qmanager = pcf.MQCMD_INQUIRE_CLUSTER_Q_MGR(args)

        except pymqi.MQMIError, e:
            return {"reason": e.reason, "code": e.comp, "message": e.errorAsString()}, 500

        except Exception, ex:
            return {"message": ex.message}, 500

        cluster_qmanager = map(lambda x: mq_defs.mqcons_to_string(x), cluster_qmanager)
        print cluster_qmanager
        mq_defs.make_swagger_defs("cluster_qmanager", cluster_qmanager[0])
        return cluster_qmanager, 200, None