#!/usr/bin/env python
#-*- coding: utf-8 -*-
# @Filename: connector.py
# @Author: olenji - lionhe0119@hotmail.com
# @Description: ---
# @Create: 2019-05-13 11:56:58
# @Last Modified: 2019-05-13 11:56:58
#


from odps import ODPS, options
options.sql.use_odps2_extension = True
odps = ODPS('LTAItDVDpC9aEMXJ', 'U6iEFCZCzoPUbjou1FW45SQruxIfFt', 'Qkids_V2')
            #endpoint='**your-end-point**')

#project = odps.get_project()  

