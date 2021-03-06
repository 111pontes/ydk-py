


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'RttmonrtttypeEnum' : _MetaInfoEnum('RttmonrtttypeEnum', 'ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB',
        {
            'echo':'echo',
            'pathEcho':'pathEcho',
            'fileIO':'fileIO',
            'script':'script',
            'udpEcho':'udpEcho',
            'tcpConnect':'tcpConnect',
            'http':'http',
            'dns':'dns',
            'jitter':'jitter',
            'dlsw':'dlsw',
            'dhcp':'dhcp',
            'ftp':'ftp',
            'voip':'voip',
            'rtp':'rtp',
            'lspGroup':'lspGroup',
            'icmpjitter':'icmpjitter',
            'lspPing':'lspPing',
            'lspTrace':'lspTrace',
            'ethernetPing':'ethernetPing',
            'ethernetJitter':'ethernetJitter',
            'lspPingPseudowire':'lspPingPseudowire',
            'video':'video',
            'y1731Delay':'y1731Delay',
            'y1731Loss':'y1731Loss',
            'mcastJitter':'mcastJitter',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttmplsvpnmonrtttypeEnum' : _MetaInfoEnum('RttmplsvpnmonrtttypeEnum', 'ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB',
        {
            'jitter':'jitter',
            'echo':'echo',
            'pathEcho':'pathEcho',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttmplsvpnmonlpdfailuresenseEnum' : _MetaInfoEnum('RttmplsvpnmonlpdfailuresenseEnum', 'ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB',
        {
            'unknown':'unknown',
            'noPath':'noPath',
            'allPathsBroken':'allPathsBroken',
            'allPathsUnexplorable':'allPathsUnexplorable',
            'allPathsBrokenOrUnexplorable':'allPathsBrokenOrUnexplorable',
            'timeout':'timeout',
            'error':'error',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttresponsesenseEnum' : _MetaInfoEnum('RttresponsesenseEnum', 'ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB',
        {
            'other':'other',
            'ok':'ok',
            'disconnected':'disconnected',
            'overThreshold':'overThreshold',
            'timeout':'timeout',
            'busy':'busy',
            'notConnected':'notConnected',
            'dropped':'dropped',
            'sequenceError':'sequenceError',
            'verifyError':'verifyError',
            'applicationSpecific':'applicationSpecific',
            'dnsServerTimeout':'dnsServerTimeout',
            'tcpConnectTimeout':'tcpConnectTimeout',
            'httpTransactionTimeout':'httpTransactionTimeout',
            'dnsQueryError':'dnsQueryError',
            'httpError':'httpError',
            'error':'error',
            'mplsLspEchoTxError':'mplsLspEchoTxError',
            'mplsLspUnreachable':'mplsLspUnreachable',
            'mplsLspMalformedReq':'mplsLspMalformedReq',
            'mplsLspReachButNotFEC':'mplsLspReachButNotFEC',
            'enableOk':'enableOk',
            'enableNoConnect':'enableNoConnect',
            'enableVersionFail':'enableVersionFail',
            'enableInternalError':'enableInternalError',
            'enableAbort':'enableAbort',
            'enableFail':'enableFail',
            'enableAuthFail':'enableAuthFail',
            'enableFormatError':'enableFormatError',
            'enablePortInUse':'enablePortInUse',
            'statsRetrieveOk':'statsRetrieveOk',
            'statsRetrieveNoConnect':'statsRetrieveNoConnect',
            'statsRetrieveVersionFail':'statsRetrieveVersionFail',
            'statsRetrieveInternalError':'statsRetrieveInternalError',
            'statsRetrieveAbort':'statsRetrieveAbort',
            'statsRetrieveFail':'statsRetrieveFail',
            'statsRetrieveAuthFail':'statsRetrieveAuthFail',
            'statsRetrieveFormatError':'statsRetrieveFormatError',
            'statsRetrievePortInUse':'statsRetrievePortInUse',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttmonreactvarEnum' : _MetaInfoEnum('RttmonreactvarEnum', 'ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB',
        {
            'rtt':'rtt',
            'jitterSDAvg':'jitterSDAvg',
            'jitterDSAvg':'jitterDSAvg',
            'packetLossSD':'packetLossSD',
            'packetLossDS':'packetLossDS',
            'mos':'mos',
            'timeout':'timeout',
            'connectionLoss':'connectionLoss',
            'verifyError':'verifyError',
            'jitterAvg':'jitterAvg',
            'icpif':'icpif',
            'packetMIA':'packetMIA',
            'packetLateArrival':'packetLateArrival',
            'packetOutOfSequence':'packetOutOfSequence',
            'maxOfPositiveSD':'maxOfPositiveSD',
            'maxOfNegativeSD':'maxOfNegativeSD',
            'maxOfPositiveDS':'maxOfPositiveDS',
            'maxOfNegativeDS':'maxOfNegativeDS',
            'iaJitterDS':'iaJitterDS',
            'frameLossDS':'frameLossDS',
            'mosLQDS':'mosLQDS',
            'mosCQDS':'mosCQDS',
            'rFactorDS':'rFactorDS',
            'successivePacketLoss':'successivePacketLoss',
            'maxOfLatencyDS':'maxOfLatencyDS',
            'maxOfLatencySD':'maxOfLatencySD',
            'latencyDSAvg':'latencyDSAvg',
            'latencySDAvg':'latencySDAvg',
            'packetLoss':'packetLoss',
            'iaJitterSD':'iaJitterSD',
            'mosCQSD':'mosCQSD',
            'rFactorSD':'rFactorSD',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttmonlsppingreplymodeEnum' : _MetaInfoEnum('RttmonlsppingreplymodeEnum', 'ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB',
        {
            'replyIpv4Udp':'replyIpv4Udp',
            'replyIpv4UdpRA':'replyIpv4UdpRA',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttresetEnum' : _MetaInfoEnum('RttresetEnum', 'ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB',
        {
            'ready':'ready',
            'reset':'reset',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttmplsvpnmonlpdgrpstatusEnum' : _MetaInfoEnum('RttmplsvpnmonlpdgrpstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB',
        {
            'unknown':'unknown',
            'up':'up',
            'partial':'partial',
            'down':'down',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttmoncodectypeEnum' : _MetaInfoEnum('RttmoncodectypeEnum', 'ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB',
        {
            'notApplicable':'notApplicable',
            'g711ulaw':'g711ulaw',
            'g711alaw':'g711alaw',
            'g729a':'g729a',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttmonprotocolEnum' : _MetaInfoEnum('RttmonprotocolEnum', 'ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB',
        {
            'notApplicable':'notApplicable',
            'ipIcmpEcho':'ipIcmpEcho',
            'ipUdpEchoAppl':'ipUdpEchoAppl',
            'snaRUEcho':'snaRUEcho',
            'snaLU0EchoAppl':'snaLU0EchoAppl',
            'snaLU2EchoAppl':'snaLU2EchoAppl',
            'snaLU62Echo':'snaLU62Echo',
            'snaLU62EchoAppl':'snaLU62EchoAppl',
            'appleTalkEcho':'appleTalkEcho',
            'appleTalkEchoAppl':'appleTalkEchoAppl',
            'decNetEcho':'decNetEcho',
            'decNetEchoAppl':'decNetEchoAppl',
            'ipxEcho':'ipxEcho',
            'ipxEchoAppl':'ipxEchoAppl',
            'isoClnsEcho':'isoClnsEcho',
            'isoClnsEchoAppl':'isoClnsEchoAppl',
            'vinesEcho':'vinesEcho',
            'vinesEchoAppl':'vinesEchoAppl',
            'xnsEcho':'xnsEcho',
            'xnsEchoAppl':'xnsEchoAppl',
            'apolloEcho':'apolloEcho',
            'apolloEchoAppl':'apolloEchoAppl',
            'netbiosEchoAppl':'netbiosEchoAppl',
            'ipTcpConn':'ipTcpConn',
            'httpAppl':'httpAppl',
            'dnsAppl':'dnsAppl',
            'jitterAppl':'jitterAppl',
            'dlswAppl':'dlswAppl',
            'dhcpAppl':'dhcpAppl',
            'ftpAppl':'ftpAppl',
            'mplsLspPingAppl':'mplsLspPingAppl',
            'voipAppl':'voipAppl',
            'rtpAppl':'rtpAppl',
            'icmpJitterAppl':'icmpJitterAppl',
            'ethernetPingAppl':'ethernetPingAppl',
            'ethernetJitterAppl':'ethernetJitterAppl',
            'videoAppl':'videoAppl',
            'y1731dmm':'y1731dmm',
            'y17311dm':'y17311dm',
            'y1731lmm':'y1731lmm',
            'mcastJitterAppl':'mcastJitterAppl',
            'y1731slm':'y1731slm',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
    'RttmonoperationEnum' : _MetaInfoEnum('RttmonoperationEnum', 'ydk.models.cisco_ios_xe.CISCO_RTTMON_TC_MIB',
        {
            'notApplicable':'notApplicable',
            'httpGet':'httpGet',
            'httpRaw':'httpRaw',
            'ftpGet':'ftpGet',
            'ftpPassive':'ftpPassive',
            'ftpActive':'ftpActive',
            'voipDTAlertRinging':'voipDTAlertRinging',
            'voipDTConnectOK':'voipDTConnectOK',
        }, 'CISCO-RTTMON-TC-MIB', _yang_ns._namespaces['CISCO-RTTMON-TC-MIB']),
}
