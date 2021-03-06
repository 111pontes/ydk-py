


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SyslogseverityEnum' : _MetaInfoEnum('SyslogseverityEnum', 'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB',
        {
            'emergency':'emergency',
            'alert':'alert',
            'critical':'critical',
            'error':'error',
            'warning':'warning',
            'notice':'notice',
            'info':'info',
            'debug':'debug',
        }, 'CISCO-SYSLOG-MIB', _yang_ns._namespaces['CISCO-SYSLOG-MIB']),
    'CiscoSyslogMib.Clogbasic.ClogoriginidtypeEnum' : _MetaInfoEnum('ClogoriginidtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB',
        {
            'none':'none',
            'other':'other',
            'hostName':'hostName',
            'ipv4Address':'ipv4Address',
            'contextName':'contextName',
            'userDefined':'userDefined',
        }, 'CISCO-SYSLOG-MIB', _yang_ns._namespaces['CISCO-SYSLOG-MIB']),
    'CiscoSyslogMib.Clogbasic' : {
        'meta_info' : _MetaInfoClass('CiscoSyslogMib.Clogbasic',
            False, 
            [
            _MetaInfoClassMember('clogMaxSeverity', REFERENCE_ENUM_CLASS, 'SyslogseverityEnum' , 'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB', 'SyslogseverityEnum', 
                [], [], 
                '''                Indicates which syslog severity levels will be
                processed.  Any syslog message with a severity value
                greater than this value will be ignored by the agent.
                note: severity numeric values increase as their
                severity decreases, e.g. 'error' is more severe than
                'debug'.
                ''',
                'clogmaxseverity',
                'CISCO-SYSLOG-MIB', False),
            _MetaInfoClassMember('clogMsgDrops', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of syslog messages which could not be
                processed due to lack of system resources. Most
                likely this will occur at the same time that syslog
                messages are generated to indicate this lack of
                resources.  Increases in this object's value may serve
                as an indication that system resource levels should be
                examined via other mib objects.  A message that is
                dropped will not appear in the history table and
                no notification will be sent for this message.
                ''',
                'clogmsgdrops',
                'CISCO-SYSLOG-MIB', False),
            _MetaInfoClassMember('clogMsgIgnores', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of syslog messages which were ignored.  A
                message will be ignored if it has a severity value
                greater than clogMaxSeverity.
                ''',
                'clogmsgignores',
                'CISCO-SYSLOG-MIB', False),
            _MetaInfoClassMember('clogNotificationsEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether clogMessageGenerated notifications
                will or will not be sent when a syslog message is
                generated by the device.  Disabling notifications
                does not prevent syslog messages from being added
                to the clogHistoryTable.
                ''',
                'clognotificationsenabled',
                'CISCO-SYSLOG-MIB', False),
            _MetaInfoClassMember('clogNotificationsSent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of clogMessageGenerated notifications that
                have been sent. This number may include notifications
                that were prevented from being transmitted due to
                reasons such as resource limitations and/or
                non-connectivity.  If one is receiving notifications,
                one can periodically poll this object to determine if
                any notifications were missed.  If so, a poll of the
                clogHistoryTable might be appropriate.
                ''',
                'clognotificationssent',
                'CISCO-SYSLOG-MIB', False),
            _MetaInfoClassMember('clogOriginID', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object is used for configuring the
                origin identifier for the syslog messages.
                
                The origin identifier is useful for identifying 
                the source of system logging messages in cases 
                syslog messages from multiple devices are sent 
                to a single syslog host.
                The origin identifier is added to the beginning of
                all system logging (syslog) messages sent to remote 
                hosts.
                
                The type of the identifier is specified
                by clogOriginIDType object.
                
                This object can be written by the SNMP manager
                only when clogOriginIDType is set to 'userDefined'.
                
                For following value(s) of clogOriginIDType,
                this object can not be set; the value of this
                object is derived by the system in these cases:
                   'contextName' 
                   'ipv4Address'
                   'hostName'
                   'other'     
                   'none'     
                
                This object contains the context name
                of the device, when clogOriginIDType is 
                set to 'contextName'.
                
                This object contains IPv4 address
                (in dotted decimal notation) of the sending 
                interface when clogOriginIDType is set to
                'ipv4Address'.
                
                This object contains hostname of the system
                when clogOriginIDType is set to 'hostName'.
                
                This object will contain zero length
                octet string when clogOriginIDType is
                either 'none' or 'other'.
                ''',
                'clogoriginid',
                'CISCO-SYSLOG-MIB', False),
            _MetaInfoClassMember('clogOriginIDType', REFERENCE_ENUM_CLASS, 'ClogoriginidtypeEnum' , 'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB', 'CiscoSyslogMib.Clogbasic.ClogoriginidtypeEnum', 
                [], [], 
                '''                This object identifies the type of value that
                will be contained in clogOriginID object.
                
                The possible value(s) are:
                   'none'       : do not send origin identifier in 
                                  syslog messages.
                   'other'      : type that is not identified by other 
                                  values specified in this object.
                   'hostName'   : Send hostname of the system in syslog
                                  messages.
                   'ipv4Address': Send IP address of the sending interface.
                   'contextName': Send context name of the security device.
                   'userDefined': Send user configured string in
                                  syslog message.
                
                   The value 'other' and 'none' can not be set but
                   can only be read.
                ''',
                'clogoriginidtype',
                'CISCO-SYSLOG-MIB', False),
            ],
            'CISCO-SYSLOG-MIB',
            'clogBasic',
            _yang_ns._namespaces['CISCO-SYSLOG-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB'
        ),
    },
    'CiscoSyslogMib.Cloghistory' : {
        'meta_info' : _MetaInfoClass('CiscoSyslogMib.Cloghistory',
            False, 
            [
            _MetaInfoClassMember('clogHistMsgsFlushed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of entries that have been removed from
                the clogHistoryTable in order to make room for new
                entries. This object can be utilized to determine
                whether your polling frequency on the history table
                is fast enough and/or the size of your history table
                is large enough such that you are not missing
                messages.
                ''',
                'cloghistmsgsflushed',
                'CISCO-SYSLOG-MIB', False),
            _MetaInfoClassMember('clogHistTableMaxLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '500')], [], 
                '''                The upper limit on the number of entries that the
                clogHistoryTable may contain.  A value of 0 will
                prevent any history from being retained. When this
                table is full, the oldest entry will be deleted and
                a new one will be created.
                ''',
                'cloghisttablemaxlength',
                'CISCO-SYSLOG-MIB', False),
            ],
            'CISCO-SYSLOG-MIB',
            'clogHistory',
            _yang_ns._namespaces['CISCO-SYSLOG-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB'
        ),
    },
    'CiscoSyslogMib.Clogserver' : {
        'meta_info' : _MetaInfoClass('CiscoSyslogMib.Clogserver',
            False, 
            [
            _MetaInfoClassMember('clogMaxServers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The maximum number of syslog servers that can be
                configured for the system in clogServerConfigTable.
                
                A value of zero for this object indicates there is
                no specified limit for the system and is only dictated
                by system resources.
                ''',
                'clogmaxservers',
                'CISCO-SYSLOG-MIB', False),
            ],
            'CISCO-SYSLOG-MIB',
            'clogServer',
            _yang_ns._namespaces['CISCO-SYSLOG-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB'
        ),
    },
    'CiscoSyslogMib.Cloghistorytable.Cloghistoryentry' : {
        'meta_info' : _MetaInfoClass('CiscoSyslogMib.Cloghistorytable.Cloghistoryentry',
            False, 
            [
            _MetaInfoClassMember('clogHistIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                A monotonically increasing integer for the sole
                purpose of indexing messages.  When it reaches the
                maximum value the agent flushes the table and wraps
                the value back to 1.
                ''',
                'cloghistindex',
                'CISCO-SYSLOG-MIB', True),
            _MetaInfoClassMember('clogHistFacility', ATTRIBUTE, 'str' , None, None, 
                [(1, 20)], [], 
                '''                Name of the facility that generated this message.
                For example: 'SYS'.
                ''',
                'cloghistfacility',
                'CISCO-SYSLOG-MIB', False),
            _MetaInfoClassMember('clogHistMsgName', ATTRIBUTE, 'str' , None, None, 
                [(1, 30)], [], 
                '''                A textual identification for the message type.
                A facility name in conjunction with a message name
                uniquely identifies a message type.
                ''',
                'cloghistmsgname',
                'CISCO-SYSLOG-MIB', False),
            _MetaInfoClassMember('clogHistMsgText', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The text of the message.  If the text of the message
                exceeds 255 bytes, the message will be truncated to
                254 bytes and a '*' character will be appended -
                indicating that the message has been truncated.
                ''',
                'cloghistmsgtext',
                'CISCO-SYSLOG-MIB', False),
            _MetaInfoClassMember('clogHistSeverity', REFERENCE_ENUM_CLASS, 'SyslogseverityEnum' , 'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB', 'SyslogseverityEnum', 
                [], [], 
                '''                The severity of the message.
                ''',
                'cloghistseverity',
                'CISCO-SYSLOG-MIB', False),
            _MetaInfoClassMember('clogHistTimestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when this message was
                generated.
                ''',
                'cloghisttimestamp',
                'CISCO-SYSLOG-MIB', False),
            ],
            'CISCO-SYSLOG-MIB',
            'clogHistoryEntry',
            _yang_ns._namespaces['CISCO-SYSLOG-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB'
        ),
    },
    'CiscoSyslogMib.Cloghistorytable' : {
        'meta_info' : _MetaInfoClass('CiscoSyslogMib.Cloghistorytable',
            False, 
            [
            _MetaInfoClassMember('clogHistoryEntry', REFERENCE_LIST, 'Cloghistoryentry' , 'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB', 'CiscoSyslogMib.Cloghistorytable.Cloghistoryentry', 
                [], [], 
                '''                A syslog message that was previously generated by this
                device. Each entry is indexed by a message index.
                ''',
                'cloghistoryentry',
                'CISCO-SYSLOG-MIB', False),
            ],
            'CISCO-SYSLOG-MIB',
            'clogHistoryTable',
            _yang_ns._namespaces['CISCO-SYSLOG-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB'
        ),
    },
    'CiscoSyslogMib.Clogserverconfigtable.Clogserverconfigentry' : {
        'meta_info' : _MetaInfoClass('CiscoSyslogMib.Clogserverconfigtable.Clogserverconfigentry',
            False, 
            [
            _MetaInfoClassMember('clogServerAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                The type of Internet address of this syslog server.
                ''',
                'clogserveraddrtype',
                'CISCO-SYSLOG-MIB', True),
            _MetaInfoClassMember('clogServerAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The Internet address of this syslog server.
                The type of this address is determined by the
                value of the clogServerAddrType object.
                ''',
                'clogserveraddr',
                'CISCO-SYSLOG-MIB', True),
            _MetaInfoClassMember('clogServerStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status object used to manage rows in this table.
                
                A row may only be created by setting this object to
                'createAndGo'.
                
                A row may only be deleted by setting this object to
                'destroy'.
                ''',
                'clogserverstatus',
                'CISCO-SYSLOG-MIB', False),
            ],
            'CISCO-SYSLOG-MIB',
            'clogServerConfigEntry',
            _yang_ns._namespaces['CISCO-SYSLOG-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB'
        ),
    },
    'CiscoSyslogMib.Clogserverconfigtable' : {
        'meta_info' : _MetaInfoClass('CiscoSyslogMib.Clogserverconfigtable',
            False, 
            [
            _MetaInfoClassMember('clogServerConfigEntry', REFERENCE_LIST, 'Clogserverconfigentry' , 'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB', 'CiscoSyslogMib.Clogserverconfigtable.Clogserverconfigentry', 
                [], [], 
                '''                An entry containing information about syslog servers
                configured for the system.
                ''',
                'clogserverconfigentry',
                'CISCO-SYSLOG-MIB', False),
            ],
            'CISCO-SYSLOG-MIB',
            'clogServerConfigTable',
            _yang_ns._namespaces['CISCO-SYSLOG-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB'
        ),
    },
    'CiscoSyslogMib' : {
        'meta_info' : _MetaInfoClass('CiscoSyslogMib',
            False, 
            [
            _MetaInfoClassMember('clogBasic', REFERENCE_CLASS, 'Clogbasic' , 'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB', 'CiscoSyslogMib.Clogbasic', 
                [], [], 
                '''                ''',
                'clogbasic',
                'CISCO-SYSLOG-MIB', False),
            _MetaInfoClassMember('clogHistory', REFERENCE_CLASS, 'Cloghistory' , 'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB', 'CiscoSyslogMib.Cloghistory', 
                [], [], 
                '''                ''',
                'cloghistory',
                'CISCO-SYSLOG-MIB', False),
            _MetaInfoClassMember('clogHistoryTable', REFERENCE_CLASS, 'Cloghistorytable' , 'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB', 'CiscoSyslogMib.Cloghistorytable', 
                [], [], 
                '''                A table of syslog messages generated by this device.
                All 'interesting' syslog messages (i.e. severity <=
                clogMaxSeverity) are entered into this table.
                ''',
                'cloghistorytable',
                'CISCO-SYSLOG-MIB', False),
            _MetaInfoClassMember('clogServer', REFERENCE_CLASS, 'Clogserver' , 'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB', 'CiscoSyslogMib.Clogserver', 
                [], [], 
                '''                ''',
                'clogserver',
                'CISCO-SYSLOG-MIB', False),
            _MetaInfoClassMember('clogServerConfigTable', REFERENCE_CLASS, 'Clogserverconfigtable' , 'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB', 'CiscoSyslogMib.Clogserverconfigtable', 
                [], [], 
                '''                This table contains entries that allow application
                to configure syslog servers for the system.
                
                The maximum number of entries that can be created
                for this table is limited by the object
                clogMaxServers.
                ''',
                'clogserverconfigtable',
                'CISCO-SYSLOG-MIB', False),
            ],
            'CISCO-SYSLOG-MIB',
            'CISCO-SYSLOG-MIB',
            _yang_ns._namespaces['CISCO-SYSLOG-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_SYSLOG_MIB'
        ),
    },
}
_meta_table['CiscoSyslogMib.Cloghistorytable.Cloghistoryentry']['meta_info'].parent =_meta_table['CiscoSyslogMib.Cloghistorytable']['meta_info']
_meta_table['CiscoSyslogMib.Clogserverconfigtable.Clogserverconfigentry']['meta_info'].parent =_meta_table['CiscoSyslogMib.Clogserverconfigtable']['meta_info']
_meta_table['CiscoSyslogMib.Clogbasic']['meta_info'].parent =_meta_table['CiscoSyslogMib']['meta_info']
_meta_table['CiscoSyslogMib.Cloghistory']['meta_info'].parent =_meta_table['CiscoSyslogMib']['meta_info']
_meta_table['CiscoSyslogMib.Clogserver']['meta_info'].parent =_meta_table['CiscoSyslogMib']['meta_info']
_meta_table['CiscoSyslogMib.Cloghistorytable']['meta_info'].parent =_meta_table['CiscoSyslogMib']['meta_info']
_meta_table['CiscoSyslogMib.Clogserverconfigtable']['meta_info'].parent =_meta_table['CiscoSyslogMib']['meta_info']
