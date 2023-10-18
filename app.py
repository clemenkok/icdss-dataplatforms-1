#!/usr/bin/env python3

import aws_cdk as cdk

from cdkworkshoppy.cdkworkshoppy_stack import CdkworkshoppyStack


app = cdk.App()
CdkworkshoppyStack(app, "CdkworkshoppyStack")

app.synth()
