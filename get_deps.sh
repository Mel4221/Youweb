#!/bin/bash

print yellow 'Copying..: Newtonsoft.Json.dll' && 
cp -rfv ../Newtonsoft.Json-13.0.3/bin/Bin/net6.0/Newtonsoft.Json.dll Newtonsoft.Json-13.0.3_net6.0/Newtonsoft.Json.dll &&
print yellow 'Copying..: QuickTools.dll' &&
cp -rfv ../QuickTools/bin/Release/QuickTools.dll QuickTools/QuickTools.dll
