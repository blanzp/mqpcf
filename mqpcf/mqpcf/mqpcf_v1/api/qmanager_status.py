# -*- coding: utf-8 -*-
from flask import request, g

from . import Resource
from .. import schemas
from . import mq_cache
import pymqi
import mq_defs

class QmanagerStatus(Resource):

    def get(self):
        try:
            conn = mq_cache.get(g.args['qmgr_name'])
            pcf = pymqi.PCFExecute(conn)
            qmgr = pcf.MQCMD_INQUIRE_Q_MGR_STATUS()
        except pymqi.MQMIError, e:
            return {"reason": e.reason, "code": e.comp, "message": e.errorAsString()}, 500
        except Exception, ex:
            return {"message": ex.message }, 500
        qmgr = map(lambda x: mq_defs.mqcons_to_string(x), qmgr)[0]
        #mq_defs.make_swagger_defs("qmanager_status", qmgr)
        return qmgr, 200, None