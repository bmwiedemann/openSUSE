<?php

#   This program is free software; you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 2 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program; if not, write to the Free Software
#   Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

#   PNP Template for check_bind.sh
#   Author: Mike Adolphs (http://www.matejunkie.com/)

$opt[1] = "--vertical-label \"DNS Requests \" -l 0 -r --title \"DNS Requests for $hostname / $servicedesc\" ";

$def[1]  = "DEF:success=$rrdfile:$DS[1]:AVERAGE " ;
$def[1] .= "DEF:referral=$rrdfile:$DS[2]:AVERAGE " ;
$def[1] .= "DEF:nxrrset=$rrdfile:$DS[3]:AVERAGE " ;
$def[1] .= "DEF:nxdomain=$rrdfile:$DS[4]:AVERAGE " ;
$def[1] .= "DEF:recursion=$rrdfile:$DS[5]:AVERAGE " ;
$def[1] .= "DEF:failure=$rrdfile:$DS[6]:AVERAGE " ;
$def[1] .= "DEF:duplicate=$rrdfile:$DS[7]:AVERAGE " ;
$def[1] .= "DEF:dropped=$rrdfile:$DS[8]:AVERAGE " ;

$def[1] .= "COMMENT:\"\\t\\t\\t\\tLAST\\t\\tAVERAGE\\t\\tMAX\\n\" " ;

$def[1] .= "LINE2:success#008000:\"user\\t\\t \" " ;
$def[1] .= "GPRINT:success:LAST:\"%6.0lf\\t\" " ;
$def[1] .= "GPRINT:success:AVERAGE:\" %6.0lf\\t\" " ;
$def[1] .= "GPRINT:success:MAX:\" %6.0lf\\n\" " ;

$def[1] .= "LINE2:referral#0C64E8:\"referral\\t\\t \" " ;
$def[1] .= "GPRINT:referral:LAST:\"%6.0lf\\t\" " ;
$def[1] .= "GPRINT:referral:AVERAGE:\" %6.0lf\\t\" " ;
$def[1] .= "GPRINT:referral:MAX:\" %6.0lf\\n\" " ;

$def[1] .= "LINE2:nxrrset#E80C3E:\"nxrrset\\t\\t \" " ;
$def[1] .= "GPRINT:nxrrset:LAST:\"%6.0lf\\t\" " ;
$def[1] .= "GPRINT:nxrrset:AVERAGE:\" %6.0lf\\t\" " ;
$def[1] .= "GPRINT:nxrrset:MAX:\" %6.0lf\\n\" " ;

$def[1] .= "LINE2:nxdomain#FFA500:\"nxdomain\\t\\t \" " ;
$def[1] .= "GPRINT:nxdomain:LAST:\"%6.0lf\\t\" " ;
$def[1] .= "GPRINT:nxdomain:AVERAGE:\" %6.0lf\\t\" " ;
$def[1] .= "GPRINT:nxdomain:MAX:\" %6.0lf\\n\" " ;

$def[1] .= "LINE2:recursion#1CC8E8:\"recursion\\t\\t \" " ;
$def[1] .= "GPRINT:recursion:LAST:\"%6.0lf\\t\" " ;
$def[1] .= "GPRINT:recursion:AVERAGE:\" %6.0lf\\t\" " ;
$def[1] .= "GPRINT:recursion:MAX:\" %6.0lf\\n\" " ;

$def[1] .= "LINE2:failure#E80C8C:\"failure\\t\\t \" " ;
$def[1] .= "GPRINT:failure:LAST:\"%6.0lf\\t\" " ;
$def[1] .= "GPRINT:failure:AVERAGE:\" %6.0lf\\t\" " ;
$def[1] .= "GPRINT:failure:MAX:\" %6.0lf\\n\" " ;

$def[1] .= "LINE2:duplicate#00FF3F:\"duplicate\\t\\t \" " ;
$def[1] .= "GPRINT:duplicate:LAST:\"%6.0lf\\t\" " ;
$def[1] .= "GPRINT:duplicate:AVERAGE:\" %6.0lf\\t\" " ;
$def[1] .= "GPRINT:duplicate:MAX:\" %6.0lf\\n\" " ;

$def[1] .= "LINE2:dropped#FFFF00:\"dropped\\t\\t \" " ;
$def[1] .= "GPRINT:dropped:LAST:\"%6.0lf\\t\" " ;
$def[1] .= "GPRINT:dropped:AVERAGE:\" %6.0lf\\t\" " ;
$def[1] .= "GPRINT:dropped:MAX:\" %6.0lf\\n\" " ;
?>
