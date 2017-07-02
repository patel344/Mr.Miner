#!/usr/bin/env python

import pexpect

child = pexpect.spawn('./geth account new')
child.delaybeforesend = None
child.expect('.*')
child.sendline('dhruvandraiya999')
child.expect('.*')
child.sendline('dhruvandraiya999')
child.expect(pexpect.EOF, timeout=None)
cmd_show_data = child.before
cmd_output = cmd_show_data.decode('utf-8').split()
print(cmd_output[-1][1:-1])
#for data in cmd_output:
    # print(data)