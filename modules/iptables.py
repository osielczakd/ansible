#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import pipes
import tempfile

DOCUMENTATION="""
---
module: iptables
author:
	- Dabiel Osielczak (Daniel.Osielczak@opitz-consulting.com)
	
short_description: Manipulates iptables entries by rewriting /etc/sysconfig/iptables
"""

def write_header(module):
	HEADER = 'This file is maintained by Ansible\nPlease refrain from making any changes manually as those WILL BE OVERWRITTEN WITH NEXT UPDATE!\nInsted, plaese make your changes in Ansible playbook/host_vars file'
	f = os.fopen('/etc/sysconfig/iptables.test', 'wb')
	f.write(HEADER)
	

def write_entry(module, chain, state, prot, port, action):

def main():
    module = AnsibleModule(
        argument_spec=dict(
                enabled=dict(default=True, choices=['True', 'False']),
                chain=dict(default=None, type='str'),
                state=dict(default='NEW', type='str'),
                prot=dict(default='tcp', type='str'),
                port=dict(default=None, type='str'),
                action=dict(default='ACCEPT', type='str'),
                ),
        supports_check_mode=True
    )

    params = module.params

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.splitter import *
if __name__ == '__main__':
    main()
