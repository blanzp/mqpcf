# -*- coding: utf-8 -*-

# TODO: datetime support

###
### DO NOT CHANGE THIS FILE
### 
### The code is auto generated, your change will be overwritten by 
### code generating.
###


DefinitionsQueue_status = {'properties': {'oldest_msg_age': {'type': 'integer'}, 'monitoring_q': {'type': 'integer'}, 'q_status_type': {'type': 'integer'}, 'open_input_count': {'type': 'integer'}, 'open_output_count': {'type': 'integer'}, 'last_get_date': {'type': 'string'}, 'media_log_extent_name': {'type': 'string'}, 'q_name': {'type': 'string'}, 'uncommitted_msgs': {'type': 'integer'}, 'q_time_indicator': {'type': 'integer'}, 'last_put_date': {'type': 'string'}, 'current_q_depth': {'type': 'integer'}, 'last_put_time': {'type': 'string'}, 'last_get_time': {'type': 'string'}}}
DefinitionsQueue = {'properties': {'alteration_date': {'type': 'string'}, 'open_input_count': {'type': 'integer'}, 'clwl_q_priority': {'type': 'integer'}, 'creation_time': {'type': 'string'}, 'property_control': {'type': 'integer'}, 'accounting_q': {'type': 'integer'}, 'def_read_ahead': {'type': 'integer'}, 'backout_req_q_name': {'type': 'string'}, 'harden_get_backout': {'type': 'integer'}, 'clwl_q_rank': {'type': 'integer'}, 'clwl_useq': {'type': 'integer'}, 'def_input_open_option': {'type': 'integer'}, 'msg_delivery_sequence': {'type': 'integer'}, 'q_desc': {'type': 'string'}, 'statistics_q': {'type': 'integer'}, 'backout_threshold': {'type': 'integer'}, 'trigger_depth': {'type': 'integer'}, 'max_msg_length': {'type': 'integer'}, 'def_priority': {'type': 'integer'}, 'custom': {'type': 'string'}, 'cluster_name': {'type': 'string'}, 'shareability': {'type': 'integer'}, 'alteration_time': {'type': 'string'}, 'q_depth_high_event': {'type': 'integer'}, 'initiation_q_name': {'type': 'string'}, 'max_q_depth': {'type': 'integer'}, 'q_depth_max_event': {'type': 'integer'}, 'scope': {'type': 'integer'}, 'current_q_depth': {'type': 'integer'}, 'def_bind': {'type': 'integer'}, 'npm_class': {'type': 'integer'}, 'inhibit_put': {'type': 'integer'}, 'monitoring_q': {'type': 'integer'}, 'q_depth_low_event': {'type': 'integer'}, 'open_output_count': {'type': 'integer'}, 'q_service_interval_event': {'type': 'integer'}, 'process_name': {'type': 'string'}, 'trigger_msg_priority': {'type': 'integer'}, 'dist_lists': {'type': 'integer'}, 'usage': {'type': 'integer'}, 'cluster_namelist': {'type': 'string'}, 'q_service_interval': {'type': 'integer'}, 'trigger_control': {'type': 'integer'}, 'creation_date': {'type': 'string'}, 'retention_interval': {'type': 'integer'}, 'q_type': {'type': 'integer'}, 'def_persistence': {'type': 'integer'}, 'definition_type': {'type': 'integer'}, 'trigger_type': {'type': 'integer'}, 'q_depth_high_limit': {'type': 'integer'}, 'def_put_response_type': {'type': 'integer'}, 'q_name': {'type': 'string'}, 'clus-chl-name': {'type': 'string'}, 'inhibit_get': {'type': 'integer'}, 'q_depth_low_limit': {'type': 'integer'}, 'trigger_data': {'type': 'string'}}}
DefinitionsChannel = {'properties': {'alteration_date': {'type': 'string'}, 'hdr_compression': {'type': 'integer'}, 'rcv_exit_user_data': {'type': 'string'}, 'max_msg_length': {'type': 'integer'}, 'npm_speed': {'type': 'integer'}, 'mr_exit_name': {'type': 'string'}, 'statistics_channel': {'type': 'integer'}, 'rcv_exit_name': {'type': 'string'}, 'put_authority': {'type': 'integer'}, 'mca_user_id': {'type': 'string'}, 'send_exit_name': {'type': 'string'}, 'channel_name': {'type': 'string'}, 'monitoring_channel': {'type': 'integer'}, 'msg_exit_user_data': {'type': 'string'}, 'use-dead-letter-q': {'type': 'integer'}, 'mr_count': {'type': 'integer'}, 'msg_exit_name': {'type': 'string'}, 'alteration_time': {'type': 'string'}, 'mr_exit_user_data': {'type': 'string'}, 'ssl_cipher_spec': {'type': 'string'}, 'ssl_peer_name': {'type': 'string'}, 'msg_compression': {'type': 'integer'}, 'keep_alive_interval': {'type': 'integer'}, 'hb_interval': {'type': 'integer'}, 'batch_size': {'type': 'integer'}, 'send_exit_user_data': {'type': 'string'}, 'desc': {'type': 'string'}, 'sequence_number_wrap': {'type': 'integer'}, 'sec_exit_user_data': {'type': 'string'}, 'sec_exit_name': {'type': 'string'}, 'ssl_client_auth': {'type': 'integer'}, 'channel_type': {'type': 'integer'}, 'mr_interval': {'type': 'integer'}, 'reset_requested': {'type': 'integer'}, 'first': {'type': 'integer'}}}
DefinitionsQmanager_status = {'properties': {'current_log_extent_name': {'type': 'string'}, 'installation_desc': {'type': 'string'}, 'installation_path': {'type': 'string'}, 'chinit_status': {'type': 'integer'}, 'q_mgr_name': {'type': 'string'}, 'q_mgr_status': {'type': 'integer'}, 'log_path': {'type': 'string'}, 'restart_log_extent_name': {'type': 'string'}, 'installation-name': {'type': 'string'}, 'media_log_extent_name': {'type': 'string'}, 'permit-standby': {'type': 'integer'}, 'q_mgr_start_date': {'type': 'string'}, 'cmd_server_status': {'type': 'integer'}, 'connection_count': {'type': 'integer'}, 'q_mgr_start_time': {'type': 'string'}}}
DefinitionsConnection = {'properties': {'generic_connection_id': {'type': 'string'}, 'async_state': {'type': 'integer'}, 'connection_id': {'type': 'string'}, 'q_mgr_uow_id': {'type': 'string'}, 'thread_id': {'type': 'integer'}, 'uow_log_start_date': {'type': 'string'}, 'process_id': {'type': 'integer'}, 'uow_log_extent_name': {'type': 'string'}, 'external_uow_id': {'type': 'string'}, 'uow_state': {'type': 'integer'}, 'conn_info_type': {'type': 'integer'}, 'uow_start_time': {'type': 'string'}, 'appl_tag': {'type': 'string'}, 'uow_type': {'type': 'integer'}, 'uow_start_date': {'type': 'string'}, 'uow_log_start_time': {'type': 'string'}, 'connection_name': {'type': 'string'}, 'appl_desc': {'type': 'string'}, 'user_identifier': {'type': 'string'}, 'channel_name': {'type': 'string'}, 'appl_type': {'type': 'integer'}, 'connect_options': {'type': 'integer'}}}
DefinitionsCluster_qmanager = {'properties': {'name': {'type': 'string'}}}
DefinitionsQmanager = {'properties': {'alteration_date': {'type': 'string'}, 'xr_capability': {'type': 'integer'}, 'clwl_mru_channels': {'type': 'integer'}, 'configuration_event': {'type': 'integer'}, 'last_used': {'type': 'integer'}, 'statistics_auto_clussdr': {'type': 'integer'}, 'command_level': {'type': 'integer'}, 'channel_event': {'type': 'integer'}, 'cluster_workload_data': {'type': 'string'}, 'ip_address_version': {'type': 'integer'}, 'pubsub_maxmsg_retry_count': {'type': 'integer'}, 'statistics_mqi': {'type': 'integer'}, 'pubsub_np_resp': {'type': 'integer'}, 'trigger_interval': {'type': 'integer'}, 'channel_auto_def_event': {'type': 'integer'}, 'custom': {'type': 'string'}, 'platform': {'type': 'integer'}, 'alteration_time': {'type': 'string'}, 'max_uncommitted_msgs': {'type': 'integer'}, 'accounting_conn_override': {'type': 'integer'}, 'cluster_workload_exit': {'type': 'string'}, 'repository_namelist': {'type': 'string'}, 'max_priority': {'type': 'integer'}, 'activity_trace': {'type': 'integer'}, 'monitoring_auto_clussdr': {'type': 'integer'}, 'q_mgr_desc': {'type': 'string'}, 'mq_249': {'type': 'integer'}, 'pubsub_np_msg': {'type': 'integer'}, 'dist_lists': {'type': 'integer'}, 'channel_auto_def': {'type': 'integer'}, 'command_event': {'type': 'integer'}, 'remote_event': {'type': 'integer'}, 'chlauth_records': {'type': 'integer'}, 'inhibit_event': {'type': 'integer'}, 'start_stop_event': {'type': 'integer'}, 'prot_policy_capability': {'type': 'integer'}, 'q_mgr_identifier': {'type': 'string'}, 'logger_event': {'type': 'integer'}, 'ssl_reset_count': {'type': 'integer'}, 'authority_event': {'type': 'integer'}, 'local_event': {'type': 'integer'}, 'creation_time': {'type': 'string'}, 'accounting_q': {'type': 'integer'}, 'clwl_useq': {'type': 'integer'}, 'activity_conn_override': {'type': 'integer'}, 'statistics_channel': {'type': 'integer'}, 'coded_char_set_id': {'type': 'integer'}, 'statistics_interval': {'type': 'integer'}, 'ssl_fips_required': {'type': 'integer'}, 'accounting_mqi': {'type': 'integer'}, 'chinit_control': {'type': 'integer'}, 'monitoring_channel': {'type': 'integer'}, 'command_input_q_name': {'type': 'string'}, 'max_msg_length': {'type': 'integer'}, 'trace_route_recording': {'type': 'integer'}, 'version': {'type': 'string'}, 'ssl_key_repository': {'type': 'string'}, 'accounting_interval': {'type': 'integer'}, 'monitoring_q': {'type': 'integer'}, 'dead_letter_q_name': {'type': 'string'}, 'activity_recording': {'type': 'integer'}, 'parent': {'type': 'string'}, 'ssl_crl_namelist': {'type': 'string'}, 'creation_date': {'type': 'string'}, 'statistics_q': {'type': 'integer'}, 'ssl_crypto_hardware': {'type': 'string'}, 'channel_auto_def_exit': {'type': 'string'}, 'ssl_event': {'type': 'integer'}, 'pubsub_sync_pt': {'type': 'integer'}, 'max_handles': {'type': 'integer'}, 'pubsub_mode': {'type': 'integer'}, 'max_properties_length': {'type': 'integer'}, 'repository_name': {'type': 'string'}, 'performance_event': {'type': 'integer'}, 'suite_b_strength': {'type': 'integer'}, 'q_mgr_name': {'type': 'string'}, 'cmd_server_control': {'type': 'integer'}, 'def_xmit_q_name': {'type': 'string'}, 'syncpoint': {'type': 'integer'}, 'cluster_workload_length': {'type': 'integer'}, 'def_cluster_xmit_q_type': {'type': 'integer'}, 'tree_life_time': {'type': 'integer'}, 'msg_mark_browse_interval': {'type': 'integer'}}}
DefinitionsChannel_status = {'properties': {'last_used': {'type': 'string'}, 'hdr_compression': {'type': 'integer'}, 'msgs': {'type': 'integer'}, 'compression_rate': {'type': 'integer'}, 'remote_product': {'type': 'string'}, 'stop_requested': {'type': 'integer'}, 'mca_job_name': {'type': 'string'}, 'buffers_received': {'type': 'integer'}, 'buffers_sent': {'type': 'integer'}, 'channel_status': {'type': 'integer'}, 'ssl_cert_issuer_name': {'type': 'string'}, 'mca_user_id': {'type': 'string'}, 'channel_substate': {'type': 'integer'}, 'ssl_key_reset_date': {'type': 'string'}, 'monitoring_channel': {'type': 'integer'}, 'compression_time': {'type': 'integer'}, 'exit_time_indicator': {'type': 'integer'}, 'last_msg_time': {'type': 'string'}, 'local_address': {'type': 'string'}, 'remote_appl_tag': {'type': 'string'}, 'msg_compression': {'type': 'integer'}, 'last_msg_date': {'type': 'string'}, 'hb_interval': {'type': 'integer'}, 'channel_start_date': {'type': 'string'}, 'channel_instance_type': {'type': 'integer'}, 'channel_start_time': {'type': 'string'}, 'remote_version': {'type': 'string'}, 'max_sharing_convs': {'type': 'integer'}, 'current_sharing_convs': {'type': 'integer'}, 'bytes_sent': {'type': 'integer'}, 'connection_name': {'type': 'string'}, 'channel_type': {'type': 'integer'}, 'channel_name': {'type': 'string'}, 'mca_status': {'type': 'integer'}, 'bytes_rcvd': {'type': 'integer'}, 'ssl_key_resets': {'type': 'integer'}, 'ssl_short_peer_name': {'type': 'string'}}}
DefinitionsError = {'properties': {'message': {'type': 'string'}, 'code': {'type': 'integer', 'format': 'int32'}, 'reason': {'type': 'integer', 'format': 'int32'}}}

validators = {
    ('queue_status', 'GET'): {'args': {'required': ['qmgr_name'], 'properties': {'qmgr_name': {'type': 'string', 'description': 'The name of the qmgr to retreive'}, 'name': {'required': False, 'type': 'string', 'description': 'queue name to query'}}}},
    ('qmanager', 'GET'): {'args': {'required': ['qmgr_name'], 'properties': {'qmgr_name': {'type': 'string', 'description': 'The name of the qmgr to retreive'}}}},
    ('qmanager_status', 'GET'): {'args': {'required': ['qmgr_name'], 'properties': {'qmgr_name': {'type': 'string', 'description': 'The name of the qmgr to retreive'}}}},
    ('queue', 'GET'): {'args': {'required': ['qmgr_name'], 'properties': {'qmgr_name': {'type': 'string', 'description': 'The name of the qmgr to retreive'}, 'type': {'required': False, 'type': 'string', 'description': 'type of queue'}, 'name': {'required': False, 'type': 'string', 'description': 'queue name to query'}}}},
    ('channel', 'GET'): {'args': {'required': ['qmgr_name'], 'properties': {'qmgr_name': {'type': 'string', 'description': 'The name of the qmanager to retreive'}, 'type': {'required': False, 'type': 'string', 'description': 'type of channel'}, 'name': {'required': False, 'type': 'string', 'description': 'channel name to query'}}}},
    ('connection', 'GET'): {'args': {'required': ['qmgr_name'], 'properties': {'qmgr_name': {'type': 'string', 'description': 'The name of the qmgr to retreive'}, 'channel_name': {'required': False, 'type': 'string', 'description': 'channel name to query'}}}},
    ('channel_status', 'GET'): {'args': {'required': ['qmgr_name'], 'properties': {'qmgr_name': {'type': 'string', 'description': 'The name of the qmgr to retreive'}, 'type': {'required': False, 'type': 'string', 'description': 'type of channel'}, 'name': {'required': False, 'type': 'string', 'description': 'channel name to query'}}}},
    ('cluster_qmanager', 'GET'): {'args': {'required': ['qmgr_name'], 'properties': {'qmgr_name': {'type': 'string', 'description': 'The name of the qmgr to retreive'}, 'name': {'description': 'cluster name to query', 'default': '*', 'required': False, 'type': 'string'}}}},
}

filters = {
    ('queue_status', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsQueue_status, 'type': 'array'}}, 500: {'headers': None, 'schema': DefinitionsError}},
    ('qmanager', 'GET'): {200: {'headers': None, 'schema': DefinitionsQmanager}, 500: {'headers': None, 'schema': DefinitionsError}},
    ('qmanager_status', 'GET'): {200: {'headers': None, 'schema': DefinitionsQmanager_status}, 500: {'headers': None, 'schema': DefinitionsError}},
    ('queue', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsQueue, 'type': 'array'}}, 500: {'headers': None, 'schema': DefinitionsError}},
    ('channel', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsChannel, 'type': 'array'}}, 500: {'headers': None, 'schema': DefinitionsError}},
    ('connection', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsConnection, 'type': 'array'}}, 500: {'headers': None, 'schema': DefinitionsError}},
    ('channel_status', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsChannel_status, 'type': 'array'}}, 500: {'headers': None, 'schema': DefinitionsError}},
    ('cluster_qmanager', 'GET'): {200: {'headers': None, 'schema': {'items': DefinitionsCluster_qmanager, 'type': 'array'}}, 500: {'headers': None, 'schema': DefinitionsError}},
}

scopes = {
}


class Security(object):

    def __init__(self):
        super(Security, self).__init__()
        self._loader = lambda: []

    @property
    def scopes(self):
        return self._loader()

    def scopes_loader(self, func):
        self._loader = func
        return func

security = Security()


def merge_default(schema, value):
    # TODO: more types support
    type_defaults = {
        'integer': 9573,
        'string': 'something',
        'object': {},
        'array': [],
        'boolean': False
    }

    return normalize(schema, value, type_defaults)[0]


def normalize(schema, data, required_defaults=None):

    if required_defaults is None:
        required_defaults = {}
    errors = []

    class DataWrapper(object):

        def __init__(self, data):
            super(DataWrapper, self).__init__()
            self.data = data

        def get(self, key, default=None):
            if isinstance(self.data, dict):
                return self.data.get(key, default)
            if hasattr(self.data, key):
                return getattr(self.data, key)
            else:
                return default

        def has(self, key):
            if isinstance(self.data, dict):
                return key in self.data
            return hasattr(self.data, key)

    def _normalize_dict(schema, data):
        result = {}
        data = DataWrapper(data)
        for key, _schema in schema.get('properties', {}).iteritems():
            # set default
            type_ = _schema.get('type', 'object')
            if ('default' not in _schema
                    and key in schema.get('required', [])
                    and type_ in required_defaults):
                _schema['default'] = required_defaults[type_]

            # get value
            if data.has(key):
                result[key] = _normalize(_schema, data.get(key))
            elif 'default' in _schema:
                result[key] = _schema['default']
            elif key in schema.get('required', []):
                errors.append(dict(name='property_missing',
                                   message='`%s` is required' % key))
        return result

    def _normalize_list(schema, data):
        result = []
        if isinstance(data, (list, tuple)):
            for item in data:
                result.append(_normalize(schema.get('items'), item))
        elif 'default' in schema:
            result = schema['default']
        return result

    def _normalize_default(schema, data):
        if data is None:
            return schema.get('default')
        else:
            return data

    def _normalize(schema, data):
        if not schema:
            return None
        funcs = {
            'object': _normalize_dict,
            'array': _normalize_list,
            'default': _normalize_default,
        }
        type_ = schema.get('type', 'object')
        if not type_ in funcs:
            type_ = 'default'

        return funcs[type_](schema, data)

    return _normalize(schema, data), errors

