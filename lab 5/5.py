import re
str = "AFajfnabssf,manflkV<Mbn,mvNZXV<NZCX<nz<bXNclzkxjclzkxjczx,nc,zxmcnasiljbxzcn,mxczzx,mvnfmnb"
x = re.findall("a.*b$", str)
print(x)