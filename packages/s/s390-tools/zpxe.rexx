/* zPXE: REXX PXE Client for System z

zPXE is a PXE client used with Cobbler or a just a plain TFTP server.
It must be run under z/VM.  zPXE uses TFTP to first download a
user-specific profile (if one exists), or a list of available profiles.
From the profile a specific kernel, initial RAMdisk, and PARM file are
then downloaded and these files are then punched to start the install
process.

zPXE does not require a writeable 191 A disk.  Files are downloaded to a
temporary disk (VDISK).

zPXE can also IPL from a DASD volume by default.  You can specify the
default DASD device in ZPXE CONF, as well as the hostname or IP address
of the Cobbler or TFTP server.
---

Copyright 2006-2009, Red Hat, Inc
Brad Hinson <bhinson@redhat.com>

Copyright 2012, 2017, SUSE Linux,
Mark Post <mpost@suse.com>

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA
02110-1301  USA
*/


/* Set the default environment for "safety" reasons. */
ADDRESS COMMAND

/* Save the value of the trace state */
tvar_o=trace()
tvar_c=tvar_o

/* Was this script invoked with "debug" as one of the parameters? */
debug=0
if arg() then
  do
    parse upper arg uparg
    do sub=1 to words(uparg)
      if word(uparg,sub) = "DEBUG" then
        do
          debug=1;
          trace i;
          tvar_c=trace()
        end;
      else do  /* This is a do/end in case we want to add to it later */
             trace e
             tvar_c=trace()
           end
     end
  end

/* Set some defaults */
/* These values are intended to be modified by the site using this */
/* script to match their environment. */
userid=''
server=''
iplDisk=''
server_def = 'internal.tftp.server'     /* define default TFTP server */
iplDisk_def = '150'                        /* define default IPL DASD */
FM='T'                                      /* Default file mode is T */
profilelist = 'PROFILE LIST' FM  /* Disk will be accessed as FM later */
profiledetail = 'PROFILE DETAIL' FM
zpxeparm = 'ZPXE PARM' FM
zpxeconf = 'ZPXE CONF' FM
config = 'ZPXE CONF A'
seconds=10    /* The default amount of time to wait for console input */

workDiskType='VFB-512'
workDiskSize=200000           /* This is approximately 97MB of space. */
/* For TDISK instead of VDISK, comment out the previous two lines and */
/* uncomment the following two lines.*/
/* workDisk='T3390' */
/* workDiskSize=138 */

/* Make it possible to interrupt zPXE and to enter CMS no matter how
   the guest was started, if there is a system-specific profile
   or not, etc.
*/
if debug then say 'Debugging, so we will skip the wait and just run.'
else do
        say
        say 'Enter a non-blank character and ENTER (or two ENTERs)',
            'within' seconds 'seconds to interrupt zPXE.'
        ADDRESS CMS 'WAKEUP +00:'seconds '(CONS'
/* Check for the interrupt code */
        if rc = 6 then do
          say 'Interrupt received: exiting to CMS...'
          ADDRESS CMS 'DESBUF'                     /* Clear the stack */
          exit
        end
     end

/* For translating strings to lowercase */
lower = xrange('a','i')xrange('j','r')xrange('s','z')
upper = xrange('A','I')xrange('J','R')xrange('S','Z')

/* Query user ID.  This is used to determine:
     1. Whether a user-specific PXE profile exists.
     2. Whether user is disconnected.
   The logic that gets followed will vary based on the results.
*/
ADDRESS CMS 'QUERY USER' userid() '(STACK'
parse pull userid_def dash dsc
if dsc = 'DSC' then disconnected=1            /* user is disconnected */
else disconnected=0

/* Yeah, this call to translate looks backward, but it's not. Sorry.  */
userid_def = translate(userid_def, lower, upper)

/* Useful settings normally found in PROFILE EXEC */
'CP SET RUN ON'
'CP SET PF11 RETRIEVE FORWARD'
'CP SET PF12 RETRIEVE'

/* Useful setting for a script that may run unattended */
'CP TERM HOLD OFF'

/* We want to have a way to figure out what went wrong if something
   isn't working. */

'CP SPOOL CONSOLE STOP CLOSE'  /* Close any existing spooled console. */
'CP SPOOL CONSOLE START'  /* Start spooling the console for this run. */

if \ debug then ADDRESS CMS 'VMFCLEAR'                /* clear screen */

/* The following two commands that were in the original script are    */
/* almost certainly not going to work for anyone that only has CP     */
/* privilege class G */
/* 'set vdisk syslim infinite' */
/* 'set vdisk userlim infinite' */

/* Define a temporary disk to store files and CMS FORMAT it           */
/* If your site doesn't allow this, but does allow TDISKs, change the */
/* DEFINE command to T3390 instead */
'CP SET EMSG OFF'
if \ debug then trace off
'CP DETACH FFFF'                            /* detach ffff if present */
trace value tvar_c
'CP SET EMSG ON'
'CP DEFINE' workDiskType' AS FFFF' workDiskSize
queue '1'
queue 'tmpdsk'
if \ debug then                   /* If debug was not specified, then */
  ADDRESS CMS 'set cmstype ht'              /* suppress format output */
ADDRESS CMS 'format ffff' FM          /* format VDISK as file mode FM */
ADDRESS CMS 'set cmstype rt'          /* Resume seeing command output */
say 'DASD FFFF has been CMS formatted'

/* Check for the ZPXE CONF A config file and use whatever is there in
   preference over the defaults in this script */
call GetZPXECONF

/* For any values not found in ZPXE CONF A, or if it doesn't exist, use
   the default values specified in this script. */
if server = '' then do
  say 'Setting TFTP server to 'server_def
  server = server_def
end
if iplDisk = '' then do
  say 'Setting IPL disk to default of 'iplDisk_def
  iplDisk = iplDisk_def
end
if userid = '' then do
  say 'Setting userid to default of 'userid_def
  userid = userid_def
end

/* Link to TCPMAINT's 592 disk for access to the TFTP command */
say
ADDRESS CMS 'exec vmlink tcpmaint 592'

say
say 'Connecting to server 'server                /* print server name */

/* Check whether a user-specific PXE profile exists. */
call GetTFTP '/s390x/s_'userid 'profile.detail.'FM
if lines(profiledetail) > 0 then call ProcessUserProfile
else do                         /* no user-specific profile was found */
  say 'No profile found for' userid
  if disconnected then do                     /* user is disconnected */
    ADDRESS CMS 'release' FM '(detach'
    ADDRESS CMS 'exec vmlink tcpmaint 592 <detach>'
    say 'User is disconnected.  Booting from DASD 'iplDisk'...'
    'CP IPL' iplDisk
  end
  else call ProcessGenericProfiles   /* user is interactive -> prompt */
end  /* no user-specific profile was found */

trace value tvar_o

exit
/*                                         */
/* Subroutines called from the main script */
/*                                         */


/* Procedure GetZPXECONF
*/
GetZPXECONF:

if lines(config) > 0 then do
  say config "was found"
  do while lines(config) > 0
    inputline = linein(config)
    parse upper var inputline keyword value .
    select
      when (keyword = 'HOST') then do   /* line is server hostname/IP */
        server = value
        if server = '' then say config "didn't have an IP address for",
                               "the TFTP server."
        else say '  Setting TFTP server to 'server
      end

      when (keyword = 'IPLDISK') then do  /* line is default IPL disk */
        iplDisk = value
        if iplDisk = '' then say config "didn't have an IPL Disk parm."
        else say '  Setting IPL disk to 'iplDisk
      end

      otherwise do    /* line is userid to use instead of the default */
        userid = translate(keyword,lower,upper) /* Still not backward */
        say '  Setting userid to 'userid
      end

    end /* select */
  end /* do while lines(config) > 0 */
end /* if lines(config) > 0 */
return /* GetZPXECONF */


/* Procedure ProcessUserProfile
*/
ProcessUserProfile:

say 'Profile for 'userid' found'
say
bootRc = ParseSystemRecord()            /* parse file for boot action */
if bootRc = 0 then do
  say 'The profile said we should boot from local disk.'
  ADDRESS CMS 'release' FM '(detach'
  ADDRESS CMS 'exec vmlink tcpmaint 592 <detach>'
  say 'IPLing from' iplDisk
  'CP IPL' iplDisk                          /* boot from default DASD */
end /* if bootRc = 0 */
else do         /* The profile should contain pointers to kernel, etc.*/
  abort=0

  /* Get the user PARM file that contains network info */
  say 'Downloading parameter file [/s390x/s_'userid'_parm]...'
  call GetTFTP '/s390x/s_'userid'_parm' 'zpxe.parm.'FM
  if CheckDownload('s_'userid'_parm' zpxeparm)  <> 0 then
    abort=1

  /* Get the user CONF file that currently isn't used for anything */
  say 'Downloading conf file [/s390x/s_'userid'_conf]...'
  call GetTFTP '/s390x/s_'userid'_conf' 'zpxe.conf.'FM
  if CheckDownload('s_'userid'_conf' zpxeconf) <> 0 then
    abort=1

  if abort then do
    say 'Aborting PXE boot.'
    exit 99
  end

  call DownloadBinaries                 /* download kernel and initrd */
  say 'Starting install...'
  say
  call PunchFiles                     /* punch files to begin install */
  exit
end /* he profile should contain pointers to kernel, etc */


/* ProcessGenericProfiles
*/
ProcessGenericProfiles:
/* Download the list of generic profiles available */
say 'Downloading the profile list [/s390x/profile_list]...'
call GetTFTP '/s390x/profile_list' 'profile.list.'FM
if CheckDownload('profile_list' profilelist) <> 0 then do
  say '**                                      **'
  say '** No profile list found                **'
  say '** Possible error connecting to server? **'
  say '**                                      **'
  exit 99
end

/* Display a menu of the generic profiles */
say
say 'zPXE MENU'
say '---------'

/* Display one profile per line */
do count = 1 by 1 while lines(profilelist) > 0
  inputline = linein(profilelist)
  parse var inputline profile.count
  say count'. 'profile.count
end

/* Add two non-profile selections to the menu */
say count'. Don''t continue, exit to CMS'
say
say
say 'Enter Choice -->'
say 'or press <Enter> to boot from disk [DASD 'iplDisk']'

parse pull answer .
select
  when answer = count then do             /* Exit to CMS was selected */
    say
    say 'Exiting to CMS...'
    exit
  end

  when answer = '' then do                   /* IPL from default disk */
    ADDRESS CMS 'release' FM '(detach'
    ADDRESS CMS 'exec vmlink tcpmaint 592 <detach>'
    say 'Booting from DASD 'iplDisk'...'
    'CP IPL' iplDisk
  end

  when (answer > 0) & (answer < count) then do      /* valid response */
    abort=0

    say 'Downloading generic profile [/s390x/p_'profile.answer']...'
    call GetTFTP '/s390x/p_'profile.answer 'profile.detail.'FM
    if CheckDownload('p_'profile.answer profiledetail) <> 0 then
      abort=1

    say 'Downloading generic parameter file',
        '[/s390x/p_'profile.answer'_parm]...'
    call GetTFTP '/s390x/p_'profile.answer'_parm' 'zpxe.parm.'FM
    if CheckDownload('p_'profile.answer'_parm' zpxeparm) <> 0 then
      abort=1

    say 'Downloading generic conf file',
        '[/s390x/p_'profile.answer'_conf]...'
    call GetTFTP '/s390x/p_'profile.answer'_conf' 'zpxe.conf.'FM
    if CheckDownload('p_'profile.answer'_conf' zpxeconf) <> 0 then
      abort=1

    if abort then do
      say 'Aborting PXE boot.'
      exit 99
    end

/* We have to add the HostIP parameter to the parm file, since that is
   going to vary for each guest, so we can't hard-code it in the generic
   profiles.  We use the numeric part of the guest name, which starts in
   column 6, after "LINUX".  But we have to watch out for leading zeros,
   since that will appear as an octal number to Linux.  So, we use the
   fact that Rexx/Regina doesn't care about leading zeros, but will
   remove them when used in an arithmetic statement, such as follows. */
    lastoctet=substr(userid,6)
    lastoctet=lastoctet+0     /* Adding a zero won't change the value */
    hostipparm=' HostIP=10.121.157.'lastoctet
    call lineout zpxeparm, hostipparm
    call lineout zpxeparm                    /* close the output file */

    if \ debug then ADDRESS CMS 'VMFCLEAR'            /* clear screen */
    say
    say 'Using profile 'answer' ['profile.answer']'
    say
    call DownloadBinaries               /* download kernel and initrd */

    say 'Starting install...'
    say

    call PunchFiles

  end /* valid response */

  otherwise do  /* The user entered something that wasn't in the list */
    say 'Invalid choice, exiting to CMS...'
    exit
  end

end /* Select */


/* Procedure GetTFTP
   Use CMS TFTP client to download files
     path: remote file location
     filename: local file name
     transfermode [optional]: 'ascii' or 'octet'
*/
GetTFTP:

  parse arg path filename transfermode

  if transfermode <> '' then
    queue 'mode' transfermode

  queue 'get 'path filename
  queue 'quit'

  if \ debug then
    ADDRESS CMS 'set cmstype ht'              /* suppress TFTP output */

  ADDRESS CMS 'tftp' server
  ADDRESS CMS 'set cmstype rt'

return /* GetTFTP */


/* Procedure CheckDownload
  TFTP is dumb, so you can't ever tell if a file was actually retrieved
  or not from the return code.
    path: The filename (including path) that was to be retrieved
          via TFTP
    filename: The local CMS filename that should have received it.
*/
CheckDownload:

  parse arg path filename
  if lines(filename) = 0 then do
    say 'The' path 'file was not successfully retrieved'
    return 99
    end
  else return 0

/* End CheckDownload */


/* Procedure DownloadBinaries
   Download kernel and initial RAMdisk.  Convert both
   to fixed record length 80.
*/
DownloadBinaries:

  inputline = linein(profiledetail)           /* first line is kernel */
  parse var inputline kernelpath
  if kernelpath = '' then do
    say 'The path to the kernel is null.  Aborting...'
    exit 99
  end
  say 'Downloading kernel ['kernelpath']...'
  call GetTFTP kernelpath 'kernel.img.'FM octet
  if CheckDownload(kernelpath kernel img FM) <> 0 then do
    say 'Aborting PXE boot.'
    exit 99
  end

  inputline = linein(profiledetail)          /* second line is initrd */
  parse var inputline initrdpath
  if initrdpath = '' then do
    say 'The path to the initrd is null.  Aborting...'
    exit 99
  end
  say 'Downloading initrd ['initrdpath']...'
  call GetTFTP initrdpath 'initrd.img.'FM octet
  if CheckDownload(initrdpath initrd img FM) <> 0 then do
    say 'Aborting PXE boot.'
    exit 99
  end

  inputline = linein(profiledetail)     /* third line is kernel parms */
  parse var inputline kparms
  if kparms <> '' then do  /* If there are parms, add them to the end */
    call lineout zpxeparm, kparms       /* add ks line to end of parm */
    call lineout zpxeparm                               /* close file */
  end

  /* Convert to fixed record length since they're going to be run
     through the virtual card reader. */
  ADDRESS CMS 'pipe < KERNEL IMG 'FM' | fblock 80 00 | > KERNEL IMG' FM
  ADDRESS CMS 'pipe < INITRD IMG 'FM' | fblock 80 00 | > INITRD IMG' FM
  ADDRESS CMS 'pipe < ' zpxeparm ' | fblock 80 SPACE | > ' zpxeparm

return /* DownloadBinaries */


/* Procedure PunchFiles
   Punch the kernel, initial RAMdisk, and PARM file.
   Then IPL to start the install process.
*/
PunchFiles:

  'CP SPOOL PUNCH *'
  'CP CLOSE READER'
  'CP PURGE READER ALL'                      /* clear reader contents */

  ADDRESS CMS 'punch kernel img' FM '( noheader'         /* punch kernel */
  ADDRESS CMS 'punch zpxe parm' FM '( noheader'       /* punch PARM file */
  ADDRESS CMS 'punch initrd img' FM '( noheader'         /* punch initrd */
  ADDRESS CMS 'release' FM '(detach'     /* release and detach the VDISK */
  ADDRESS CMS 'exec vmlink tcpmaint 592 <detach>'    /* and this disk */

  'CP CHANGE READER ALL KEEP NOHOLD'          /* keep files in reader */
  'CP IPL 00C CLEAR'                                /* IPL the reader */

return /* PunchFiles */


/* Procedure ParseSystemRecord
   Open system record file to look for local boot flag.
   Return 0 if local flag found (guest will IPL default DASD).
   Return 1 otherwise (guest will download kernel/initrd and install).
*/
ParseSystemRecord:

  inputline = linein(profiledetail)                 /* get first line */
  parse var inputline systemaction .
  /* Close the file to reset the read pointer to the beginning. Yes I
     know that calling lineout to close a file seems weird, but it's
     how Rexx/Regina works. */
  call lineout profiledetail

  if systemaction = 'local' then
    return 0
  else
    return 1

/* End ParseSystemRecord */
