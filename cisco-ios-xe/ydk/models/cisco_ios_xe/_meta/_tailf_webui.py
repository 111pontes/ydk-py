


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Webui.Schematics.Panels.Panel.Properties' : {
        'meta_info' : _MetaInfoClass('Webui.Schematics.Panels.Panel.Properties',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'description',
                'tailf-webui', False),
            _MetaInfoClassMember('height', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'height',
                'tailf-webui', False),
            _MetaInfoClassMember('title', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'title',
                'tailf-webui', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'width',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'properties',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui.Schematics.Panels.Panel.Components.Component.Properties.Image' : {
        'meta_info' : _MetaInfoClass('Webui.Schematics.Panels.Panel.Components.Component.Properties.Image',
            False, 
            [
            _MetaInfoClassMember('image', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'image',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'image',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui.Schematics.Panels.Panel.Components.Component.Properties.Link' : {
        'meta_info' : _MetaInfoClass('Webui.Schematics.Panels.Panel.Components.Component.Properties.Link',
            False, 
            [
            _MetaInfoClassMember('link', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'link',
                'tailf-webui', False),
            _MetaInfoClassMember('text', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'text',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'link',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui.Schematics.Panels.Panel.Components.Component.Properties' : {
        'meta_info' : _MetaInfoClass('Webui.Schematics.Panels.Panel.Components.Component.Properties',
            False, 
            [
            _MetaInfoClassMember('height', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'height',
                'tailf-webui', False),
            _MetaInfoClassMember('image', REFERENCE_CLASS, 'Image' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.Schematics.Panels.Panel.Components.Component.Properties.Image', 
                [], [], 
                '''                ''',
                'image',
                'tailf-webui', False),
            _MetaInfoClassMember('left', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'left',
                'tailf-webui', False),
            _MetaInfoClassMember('link', REFERENCE_CLASS, 'Link' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.Schematics.Panels.Panel.Components.Component.Properties.Link', 
                [], [], 
                '''                ''',
                'link',
                'tailf-webui', False),
            _MetaInfoClassMember('top', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'top',
                'tailf-webui', False),
            _MetaInfoClassMember('width', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ''',
                'width',
                'tailf-webui', False),
            _MetaInfoClassMember('z-index', ATTRIBUTE, 'int' , None, None, 
                [('-32768', '32767')], [], 
                '''                ''',
                'z_index',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'properties',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui.Schematics.Panels.Panel.Components.Component' : {
        'meta_info' : _MetaInfoClass('Webui.Schematics.Panels.Panel.Components.Component',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'id',
                'tailf-webui', True),
            _MetaInfoClassMember('properties', REFERENCE_CLASS, 'Properties' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.Schematics.Panels.Panel.Components.Component.Properties', 
                [], [], 
                '''                ''',
                'properties',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'component',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui.Schematics.Panels.Panel.Components' : {
        'meta_info' : _MetaInfoClass('Webui.Schematics.Panels.Panel.Components',
            False, 
            [
            _MetaInfoClassMember('component', REFERENCE_LIST, 'Component' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.Schematics.Panels.Panel.Components.Component', 
                [], [], 
                '''                ''',
                'component',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'components',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui.Schematics.Panels.Panel' : {
        'meta_info' : _MetaInfoClass('Webui.Schematics.Panels.Panel',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'name',
                'tailf-webui', True),
            _MetaInfoClassMember('components', REFERENCE_CLASS, 'Components' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.Schematics.Panels.Panel.Components', 
                [], [], 
                '''                ''',
                'components',
                'tailf-webui', False),
            _MetaInfoClassMember('properties', REFERENCE_CLASS, 'Properties' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.Schematics.Panels.Panel.Properties', 
                [], [], 
                '''                ''',
                'properties',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'panel',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui.Schematics.Panels' : {
        'meta_info' : _MetaInfoClass('Webui.Schematics.Panels',
            False, 
            [
            _MetaInfoClassMember('panel', REFERENCE_LIST, 'Panel' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.Schematics.Panels.Panel', 
                [], [], 
                '''                ''',
                'panel',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'panels',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui.Schematics.Assets.Asset.TypeEnum' : _MetaInfoEnum('TypeEnum', 'ydk.models.cisco_ios_xe.tailf_webui',
        {
            'jpeg':'jpeg',
            'png':'png',
            'gif':'gif',
        }, 'tailf-webui', _yang_ns._namespaces['tailf-webui']),
    'Webui.Schematics.Assets.Asset' : {
        'meta_info' : _MetaInfoClass('Webui.Schematics.Assets.Asset',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'name',
                'tailf-webui', True),
            _MetaInfoClassMember('base-64-image', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'base_64_image',
                'tailf-webui', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'TypeEnum' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.Schematics.Assets.Asset.TypeEnum', 
                [], [], 
                '''                ''',
                'type',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'asset',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui.Schematics.Assets' : {
        'meta_info' : _MetaInfoClass('Webui.Schematics.Assets',
            False, 
            [
            _MetaInfoClassMember('asset', REFERENCE_LIST, 'Asset' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.Schematics.Assets.Asset', 
                [], [], 
                '''                ''',
                'asset',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'assets',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui.Schematics' : {
        'meta_info' : _MetaInfoClass('Webui.Schematics',
            False, 
            [
            _MetaInfoClassMember('assets', REFERENCE_CLASS, 'Assets' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.Schematics.Assets', 
                [], [], 
                '''                ''',
                'assets',
                'tailf-webui', False),
            _MetaInfoClassMember('panels', REFERENCE_CLASS, 'Panels' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.Schematics.Panels', 
                [], [], 
                '''                ''',
                'panels',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'schematics',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui.DataStores.UserProfile.Profile' : {
        'meta_info' : _MetaInfoClass('Webui.DataStores.UserProfile.Profile',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'key',
                'tailf-webui', True),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'value',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'profile',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui.DataStores.UserProfile.SavedQuery' : {
        'meta_info' : _MetaInfoClass('Webui.DataStores.UserProfile.SavedQuery',
            False, 
            [
            _MetaInfoClassMember('list-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'list_path',
                'tailf-webui', True),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'name',
                'tailf-webui', True),
            _MetaInfoClassMember('serialized-query', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'serialized_query',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'saved-query',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui.DataStores.UserProfile' : {
        'meta_info' : _MetaInfoClass('Webui.DataStores.UserProfile',
            False, 
            [
            _MetaInfoClassMember('username', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'username',
                'tailf-webui', True),
            _MetaInfoClassMember('profile', REFERENCE_LIST, 'Profile' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.DataStores.UserProfile.Profile', 
                [], [], 
                '''                ''',
                'profile',
                'tailf-webui', False),
            _MetaInfoClassMember('saved-query', REFERENCE_LIST, 'SavedQuery' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.DataStores.UserProfile.SavedQuery', 
                [], [], 
                '''                ''',
                'saved_query',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'user-profile',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui.DataStores.DataStore' : {
        'meta_info' : _MetaInfoClass('Webui.DataStores.DataStore',
            False, 
            [
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'key',
                'tailf-webui', True),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'value',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'data-store',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui.DataStores.SavedQuery' : {
        'meta_info' : _MetaInfoClass('Webui.DataStores.SavedQuery',
            False, 
            [
            _MetaInfoClassMember('list-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'list_path',
                'tailf-webui', True),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'name',
                'tailf-webui', True),
            _MetaInfoClassMember('serialized-query', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'serialized_query',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'saved-query',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui.DataStores' : {
        'meta_info' : _MetaInfoClass('Webui.DataStores',
            False, 
            [
            _MetaInfoClassMember('data-store', REFERENCE_LIST, 'DataStore' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.DataStores.DataStore', 
                [], [], 
                '''                ''',
                'data_store',
                'tailf-webui', False),
            _MetaInfoClassMember('saved-query', REFERENCE_LIST, 'SavedQuery' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.DataStores.SavedQuery', 
                [], [], 
                '''                ''',
                'saved_query',
                'tailf-webui', False),
            _MetaInfoClassMember('user-profile', REFERENCE_LIST, 'UserProfile' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.DataStores.UserProfile', 
                [], [], 
                '''                ''',
                'user_profile',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'data-stores',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
    'Webui' : {
        'meta_info' : _MetaInfoClass('Webui',
            False, 
            [
            _MetaInfoClassMember('data-stores', REFERENCE_CLASS, 'DataStores' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.DataStores', 
                [], [], 
                '''                ''',
                'data_stores',
                'tailf-webui', False),
            _MetaInfoClassMember('schematics', REFERENCE_CLASS, 'Schematics' , 'ydk.models.cisco_ios_xe.tailf_webui', 'Webui.Schematics', 
                [], [], 
                '''                ''',
                'schematics',
                'tailf-webui', False),
            ],
            'tailf-webui',
            'webui',
            _yang_ns._namespaces['tailf-webui'],
        'ydk.models.cisco_ios_xe.tailf_webui'
        ),
    },
}
_meta_table['Webui.Schematics.Panels.Panel.Components.Component.Properties.Image']['meta_info'].parent =_meta_table['Webui.Schematics.Panels.Panel.Components.Component.Properties']['meta_info']
_meta_table['Webui.Schematics.Panels.Panel.Components.Component.Properties.Link']['meta_info'].parent =_meta_table['Webui.Schematics.Panels.Panel.Components.Component.Properties']['meta_info']
_meta_table['Webui.Schematics.Panels.Panel.Components.Component.Properties']['meta_info'].parent =_meta_table['Webui.Schematics.Panels.Panel.Components.Component']['meta_info']
_meta_table['Webui.Schematics.Panels.Panel.Components.Component']['meta_info'].parent =_meta_table['Webui.Schematics.Panels.Panel.Components']['meta_info']
_meta_table['Webui.Schematics.Panels.Panel.Properties']['meta_info'].parent =_meta_table['Webui.Schematics.Panels.Panel']['meta_info']
_meta_table['Webui.Schematics.Panels.Panel.Components']['meta_info'].parent =_meta_table['Webui.Schematics.Panels.Panel']['meta_info']
_meta_table['Webui.Schematics.Panels.Panel']['meta_info'].parent =_meta_table['Webui.Schematics.Panels']['meta_info']
_meta_table['Webui.Schematics.Assets.Asset']['meta_info'].parent =_meta_table['Webui.Schematics.Assets']['meta_info']
_meta_table['Webui.Schematics.Panels']['meta_info'].parent =_meta_table['Webui.Schematics']['meta_info']
_meta_table['Webui.Schematics.Assets']['meta_info'].parent =_meta_table['Webui.Schematics']['meta_info']
_meta_table['Webui.DataStores.UserProfile.Profile']['meta_info'].parent =_meta_table['Webui.DataStores.UserProfile']['meta_info']
_meta_table['Webui.DataStores.UserProfile.SavedQuery']['meta_info'].parent =_meta_table['Webui.DataStores.UserProfile']['meta_info']
_meta_table['Webui.DataStores.UserProfile']['meta_info'].parent =_meta_table['Webui.DataStores']['meta_info']
_meta_table['Webui.DataStores.DataStore']['meta_info'].parent =_meta_table['Webui.DataStores']['meta_info']
_meta_table['Webui.DataStores.SavedQuery']['meta_info'].parent =_meta_table['Webui.DataStores']['meta_info']
_meta_table['Webui.Schematics']['meta_info'].parent =_meta_table['Webui']['meta_info']
_meta_table['Webui.DataStores']['meta_info'].parent =_meta_table['Webui']['meta_info']
