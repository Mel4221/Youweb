#!/bin/bash
#defining variables start
WWW_YOU=wwwroot/you
DEBUG_YOU=net7.0/you
#defining variables ends

#getting dependencys
bash get_deps.sh &&

#cleaning project
dotnet clean &&
#getting new dependencys




print red "Deleting..: ${WWW_YOU}" &&
rm -rfv $WWW_YOU &&
print red "Deleting..: ${DEBUG_YOU}" &&
rm -rfv $DEBUG_YOU &&

print yellow "Creatting Directory..: ${WWW_YOU} ${DEBUG_YOU}" &&
mkdir -p $WWW_YOU &&
mkdir -p $DEBUG_YOU &&

print cyan "Coping..: ${WWW_YOU}" &&
cp -rfv you/* $WWW_YOU &&
print cyan "Coping..: ${DEBUG_YOU}" &&
cp -rfv you/* $DEBUG_YOU

#building project
dotnet build