__author__ = 'paul'

import threading
import types

import CMQC
import CMQCFC

class MQConst2String:

    def __init__(self, module, prefix, trim):
        self.__module = module;
        self.__prefix = prefix
        self.stringDict = {}
        self.__lock = threading.Lock()
        self.__build()
        self.__trim = trim

    def __build(self):
        # Lazily build the dictionary of consts vs. their
        # mnemonic strings from the given module dict. Only those
        # attribute that begins with the prefix are considered.
        self.__lock.acquire()
        if len(self.stringDict) == 0:
            pfxlen = len(self.__prefix)
            for i in self.__module.__dict__.keys():
                if i[0:pfxlen] == self.__prefix:
                    newKey, newVal = self.__module.__dict__[i], i
                    self.stringDict[newKey] = newVal
        self.__lock.release()

    def __getitem__(self, code):
        return self.stringDict[code][self.__trim:].lower()

    def __setitem__(self, key, value):
        self.stringDict[key] = value
        return

    def has_key(self, key):
        return self.stringDict.has_key(key)


iaStringDict1 = MQConst2String(CMQC, "MQIA_",5)
iaStringDict1[239] = "MQIA_ACTIVITY_CONN_OVERRIDE"
iaStringDict1[240] = "MQIA_ACTIVITY_TRACE"
iaStringDict1[243] = "MQIA_XR_CAPABILITY"
iaStringDict1[247] = "MQIA_SUITE_B_STRENGTH"
iaStringDict1[248] = "MQIA_CHLAUTH_RECORDS"
iaStringDict1[250] = "MQIA_DEF_CLUSTER_XMIT_Q_TYPE"
iaStringDict1[251] = "MQIA_PROT_POLICY_CAPABILITY"
iaStringDict1[252] = "MQIA_LAST_USED"
iaStringDict1[234] = 'MQIA-USE-DEAD-LETTER-Q'

iaStringDict2 = MQConst2String(CMQCFC, "MQIACH_",7)
iaStringDict2[1623] = "MQIACH_RESET_REQUESTED"

iaStringDict3 = MQConst2String(CMQCFC, "MQIACF_",7)
iaStringDict3[1325] = "MQIACF-PERMIT-STANDBY"

caStringDict1 = MQConst2String(CMQC, "MQCA_",5)
caStringDict1[2119] = "MQCA_CUSTOM"
caStringDict1[2120] = "MQCA_VERSION"
caStringDict1[2115] = "MQCA_INSTALLATION_DESC"
caStringDict1[2116] = "MQCA-INSTALLATION-NAME"
caStringDict1[2117] = "MQCA_INSTALLATION_PATH"
caStringDict1[2124] = "MQCA-CLUS-CHL-NAME"

caStringDict2 = MQConst2String(CMQCFC, "MQCACH_",7)
caStringDict2[3560] = "MQCACH_REMOTE_VERSION"
caStringDict2[3561] = "MQCACH_REMOTE_PRODUCT"

caStringDict3 = MQConst2String(CMQCFC, "MQCACF_",7)
caStringDict3[3174] = "MQCACF_APPL_DESC"
caStringDict3[3175] = "MQCACF_Q_MGR_START_DATE"
caStringDict3[3176] = "MQCACF_Q_MGR_START_TIME"

baStringDict1 = MQConst2String(CMQCFC, "MQBACF_", 7)


def mqcons_to_string(d):
    new_dict = {}

    for k in d.keys():

        if not isinstance(d[k], types.StringType):
            if iaStringDict1.has_key(k):
                new_dict[iaStringDict1[k]] = d[k]
            elif iaStringDict2.has_key(k):
                new_dict[iaStringDict2[k]] = d[k]
            elif iaStringDict3.has_key(k):
                new_dict[iaStringDict3[k]] = d[k]
            else:
                new_dict[k] = d[k]
        else:
            if caStringDict1.has_key(k):
                new_dict[caStringDict1[k]] = d[k].rstrip()
            elif caStringDict2.has_key(k):
                new_dict[caStringDict2[k]] = d[k].rstrip()
            elif caStringDict3.has_key(k):
                new_dict[caStringDict3[k]] = d[k].rstrip()
            elif baStringDict1.has_key(k):
                new_dict[baStringDict1[k]] = d[k]
            else:
                new_dict[k] = d[k].rstrip()
    return new_dict


def make_swagger_defs(mq_obj_name, mq_obj):
    print "\t"+mq_obj_name+":"
    print "\t\tproperties:"
    for k in sorted(mq_obj.keys()):
        if type(mq_obj[k]) is types.StringType:
            print "\t\t\t"+str(k)+":\n\t\t\t\ttype: string"
        else:
            print "\t\t\t"+str(k)+':\n\t\t\t\ttype: integer'