# -*- coding: utf-8 -*-

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###

from .api.queue_status import QueueStatus
from .api.qmanager import Qmanager
from .api.qmanager_status import QmanagerStatus
from .api.queue import Queue
from .api.channel import Channel
from .api.connection import Connection
from .api.channel_status import ChannelStatus
from .api.cluster_qmanager import ClusterQmanager


routes = [
    dict(resource=QueueStatus, urls=['/queue_status'], endpoint='queue_status'),
    dict(resource=Qmanager, urls=['/qmanager'], endpoint='qmanager'),
    dict(resource=QmanagerStatus, urls=['/qmanager_status'], endpoint='qmanager_status'),
    dict(resource=Queue, urls=['/queue'], endpoint='queue'),
    dict(resource=Channel, urls=['/channel'], endpoint='channel'),
    dict(resource=Connection, urls=['/connection'], endpoint='connection'),
    dict(resource=ChannelStatus, urls=['/channel_status'], endpoint='channel_status'),
    dict(resource=ClusterQmanager, urls=['/cluster_qmanager'], endpoint='cluster_qmanager'),
]