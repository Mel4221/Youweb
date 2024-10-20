#!/bin/bash

bash build.sh &&
open http://localhost:4251
dotnet run && print green "Task Exited Sucessfully!!!"
echo 'LGTM'