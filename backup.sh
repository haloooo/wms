#!/bin/sh
basepath1=$(cd `dirname $0`; pwd)
file=`date +"%Y-%m-%d"`
pg_dump -U postgres -F t -f $basepath1/backup/mos_db_$file.tar MOS_DB













