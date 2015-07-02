#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import os
import tempfile

DOCUMENTATION="""
---
module: iptables
author:
	- Daniel Osielczak (Daniel.Osielczak@opitz-consulting.com)
	
short_description: Manipulates iptables entries by rewriting /etc/sysconfig/iptables
"""

def write_header(module, conffile):
	HEADER = '##############################################################\n#\n#This file is maintained by Ansible\n#Please refrain from making any changes manually as those WILL BE OVERWRITTEN WITH NEXT UPDATE!\n#Instead, plaese make your changes in Ansible playbook/host_vars file\n##############################################################\n'
	tmpfd, tmpfile = tempfile.mkstemp()
	f = os.fdopen(tmpfd,'wb')
	f.write(HEADER)
	f.close()
	
	if validate:
		module.atomic_move(tmpfile, conffile)
	else:
		module.atomic_move(tmpfile, conffile)

def write_entry(module, chain, state, prot, port, action):
	pass
def main():
	module = AnsibleModule(
		argument_spec=dict(
			enabled=dict(required=True, default=True, choices=['True', 'False']),
			file=dict(default='/etc/sysconfig/iptables.test', type='str'),
			chain=dict(default=None, type='str'),
			state=dict(default='NEW', type='str'),
			prot=dict(default='tcp', type='str'),
			port=dict(default=None, type='str'),
			action=dict(default='ACCEPT', type='str')
			),
		add_file_common_args=True,
		supports_check_mode=True
	)
	
	params = module.params
	file = module.params.get('file')
	write_header(module, file)
    

# import module snippets
from ansible.module_utils.basic import *
from ansible.module_utils.splitter import *
if __name__ == '__main__':
    main()
