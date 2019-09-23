#
# spec file for package manufacturer-PPDs
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           manufacturer-PPDs
BuildRequires:  cups
Summary:        PPD Files from Printer Manufacturers
License:        GPL-2.0+ and MIT
Group:          Hardware/Printing
BuildArch:      noarch
# Howto make Source0:
# Visit http://www.linuxprinting.org/download/PPD/HP/ and note the directories
# which contain PPD files - for example:
#   http://www.linuxprinting.org/download/PPD/HP/all_in_one/
#   http://www.linuxprinting.org/download/PPD/HP/business_inkjet/
#   http://www.linuxprinting.org/download/PPD/HP/color_laser/
#   http://www.linuxprinting.org/download/PPD/HP/designjet/
#   http://www.linuxprinting.org/download/PPD/HP/mono_laser/
# Download only *.ppd files and ignore the Robot Exclusion Standard via /robots.txt
# and without --user-agent="" www.linuxprinting.org rejects it with "ERROR 403: Forbidden":
#   for d in all_in_one business_inkjet color_laser designjet mono_laser
#   do wget --user-agent="" --execute robots=off \
#           --recursive --level=1 \
#           --no-host-directories --no-directories --no-parent \
#           --accept "*.ppd*,*.PPD*" --directory-prefix=hp \
#           http://www.linuxprinting.org/download/PPD/HP/$d/
#   done
# Now all PPDs are in the same sub-directory "hp" (duplicates with *.ppd.1, *.ppd.2, ...).
# Remove old version PPDs (according to the file or directory-date at LinuxPrinting.org).
# Rename all PPDs to have the suffix .ppd (and not .ppd.1, .ppd.2, ...).
# Some PPDs may have MAC style cr line breaks. Recode or translate them to nl.
# Make a bzip2 compressed tar-archive of the remaining PPDs:
#   tar -cjvf hp.ppd.tar.bz2 hp/*.ppd
Source0:        hp.ppd.tar.bz2
# Howto make Source1:
# Visit http://www.linuxprinting.org/download/PPD/Oce/ and note the directory structure
# which contain PPD files - for example:
#    http://www.linuxprinting.org/download/PPD/Oce/*/1/
#    http://www.linuxprinting.org/download/PPD/Oce/Others/
# Download them (see Source0):
#   wget --user-agent="" --execute robots=off \
#        --recursive --level=3 \
#        --no-host-directories --no-directories --no-parent \
#        --accept "*.ppd*,*.PPD*" --directory-prefix=oce \
#        http://www.linuxprinting.org/download/PPD/Oce/
# Accept "*.ppd*" and "*.PPD*" otherwise newer vesions like "*.ppd.1" would be deleted.
# Now all PPDs are in the same sub-directory "oce".
# Newer versions of *.ppd are stored as *.ppd.1
# and some old versions of *.ppd are stored as *.PPD
# Some PPDs may have non-latin1 encoding. Recode them to lat1 (e.g.: "recode ibmpc..lat1").
# The "Others" PPDs are older versions.
# Keep only those "Others" PPDs for which there is no newer PPD.
# Make a bzip2 compressed tar-archive of them:
#   tar -cjvf oce.ppd.tar.bz2 oce/*.ppd
Source1:        oce.ppd.tar.bz2
# Howto make Source2:
# We got the initial PPDs as attachments in mails from Jens Stark <j.stark@esbc.sharp-eu.com>.
# After unpacking them store all PPDs in the same sub-directory "sharp".
# Some of the PPDs have identical NickName entries (i.e. are for the same models)
# and identical other entries except that the default media size options are different:
# Letter for the normal PPD and A4 for a Japanese version (with a "j" somehow in the file name).
# As the default media size options are changed to A4 during build, the Japanese version is removed
# if there is another PPD with identical NickName.
# New PPDs and updates of existing PPDs are at LinuxPrinting.org.
# Download the PPDs from LinuxPrinting.org:
#   wget --user-agent="" --execute robots=off \
#        --recursive --level=1 \
#        --no-host-directories --no-directories --no-parent \
#        --accept "*.ppd*,*.PPD*" --directory-prefix=sharp.new \
#        http://www.linuxprinting.org/foomatic-db/db/source/PPD//Sharp/
# Some PPDs may have non-latin1 encoding. Recode them to lat1 (e.g.: "recode ibmpc..lat1").
# Some PPDs may have CR LF line break. Remove the CR (e.g.: "tr -d '\r'").
# Copy the new PPDs into the directory "sharp".
# Check that all NickName entries are different to avoid duplicate PPDs
# (e.g. PPDs with same NickName entries but slightly different file names).
# Make a bzip2 compressed tar-archive of them:
#   tar -cjvf sharp.ppd.tar.bz2 sharp/*.ppd
Source2:        sharp.ppd.tar.bz2
# Howto make Source3:
# We got the PPDs as attachment in two mails from Vipa Nichapanich:
# 1. mail (new release because before they had a modified non-free MIT license):
#   From: vipa <vipa@eitc.epson.com>
#   Date: Wed, 3 Mar 2004 11:44:14 -0800
#   Subject: New Release of PostScriptTM printer description (PPD) files for Epson laser printers 
# 2. mail:
#   From: "Nichapanich, Vipaporn" <vipaporn.nichapanich@eitc.epson.com>
#   Date: Mon, 27 Jun 2005 15:57:55 -0700
#   Subject: New Epson PPD Files Available for Your Linux Distribution
# Additionally the epalc420.ppd was downloaded from
#   http://www.avasys.jp/english/linux_e/dl_laser.html
# as http://lx1.avasys.jp/ppd/v111/epson_ppd-1.1.1.run which must be run as root,
# then it installs PPDs into /usr/share/cups/model/epson_ppd/ where only epalc420.ppd was new.
# After unpacking them and storing all PPDs in the same sub-directory "epson":
# Add a trailing blank to "are " in the license text in epalc260.ppd to have it same in all PPDs. 
# Make a bzip2 compressed tar-archive of them:
#   tar -cjvf epson.ppd.tar.bz2 epson/*.ppd
Source3:        epson.ppd.tar.bz2
# Howto make Source4:
# We got the initial PPDs as attachment in a mail from Markus Brauer <markus.brauer@ktde.de>.
# After unpacking them store all PPDs in the same sub-directory "kyocera".
# New PPDs and updates of existing PPDs are at LinuxPrinting.org.
# Download the PPDs from LinuxPrinting.org:
#   wget --user-agent="" --execute robots=off \
#        --recursive --level=1 \
#        --no-host-directories --no-directories --no-parent \
#        --accept "*.ppd*,*.PPD*" --directory-prefix=kyocera.new \
#        http://www.linuxprinting.org/foomatic-db/db/source/PPD/Kyocera/en/
# Copy the new PPDs into the directory "kyocera".
# Check that all NickName entries are different to avoid duplicate PPDs
# (e.g. PPDs with same NickName entries but slightly different file names).
# Make a bzip2 compressed tar-archive of them:
#   tar -cjvf kyocera.ppd.tar.bz2 kyocera/*.ppd
Source4:        kyocera.ppd.tar.bz2
# Howto make Source5:
# We got this PPDs as attachment in a mail from Toshiyuki Ito <jrito@oki.com>.
# The archive contains the PPDs and a COPYING file which contains the GPL.
# After unpacking them and storing all PPDs in the same sub-directory "oki":
# Make a bzip2 compressed tar-archive of them:
#   tar -cjvf oki.ppd.tar.bz2 oki/*.ppd
Source5:        oki.ppd.tar.bz2
# Howto make Source6, Source7, Source8, Source9, Source10, Source11:
# All those PPDs are in fact Ricoh PPDs (but using different printer brand names).
# The PostScript PPDs are in the sub-directory "PS",
# the PCLXL PPDs are in the sub-directory "PXL".
# Almost all those PPDs require the foomatic-rip filter
# (even the PostScript PPDs to support usercode and secure print features).
# In http://www.linuxprinting.org/download/oldPPDs/ there are plain PostScript PPDs
# which do not require the foomatic-rip filter.
# Download the PPDs from LinuxPrinting.org:
#   for d in Ricoh Gestetner Infotec Lanier NRG Savin
#   do dp=$( echo $d | tr '[:upper:]' '[:lower:]' )
#      for sd in PS PXL
#      do wget --user-agent="" --execute robots=off \
#              --recursive --level=1 \
#              --no-host-directories --no-directories --no-parent \
#              --accept "*.ppd*,*.PPD*" --directory-prefix=$dp \
#              http://www.linuxprinting.org/download/PPD/$d/$sd/
#      done
#      wget --user-agent="" --execute robots=off \
#           --recursive --level=1 \
#           --no-host-directories --no-directories --no-parent \
#           --accept "*.ppd*,*.PPD*" --directory-prefix=$dp.old \
#           http://www.linuxprinting.org/download/oldPPDs/$d/PS/
#   done
# Now all PPDs are in the sub-directories ricoh, gestetner, infotec, lanier, nrg, savin
# and ricoh.old, gestetner.old, infotec.old, lanier.old, nrg.old, savin.old.
# Almost all PostScript PPDs have same file names.
# Rename the *.ppd files in the *.old sub-directories to *.plainPS.ppd files.
# Make a bzip2 compressed tar-archive of them:
#   for d in ricoh gestetner infotec lanier nrg savin
#   do tar -cjvf $d.ppd.tar.bz2 $d/*.ppd
#   done
Source6:        ricoh.ppd.tar.bz2
Source7:        gestetner.ppd.tar.bz2
Source8:        infotec.ppd.tar.bz2
Source9:        lanier.ppd.tar.bz2
Source10:       nrg.ppd.tar.bz2
Source11:       savin.ppd.tar.bz2
# Howto make Source12:
# Download the PPDs from LinuxPrinting.org:
#   wget --user-agent="" --execute robots=off \
#        --recursive --level=1 \
#        --no-host-directories --no-directories --no-parent \
#        --accept "*.ppd*,*.PPD*" --directory-prefix=brother \
#        http://www.linuxprinting.org/download/PPD/Brother/
# Now all PPDs are in the sub-directory brother.
# Some PPDs may have non-latin1 encoding. Recode them to lat1 (e.g.: "recode ibmpc..lat1").
# Make a bzip2 compressed tar-archive of them:
#  tar -cjvf brother.ppd.tar.bz2 brother/*.ppd
Source12:       brother.ppd.tar.bz2
# Howto make Source13:
# Download the PPDs from LinuxPrinting.org:
#   wget --user-agent="" --execute robots=off \
#        --recursive --level=1 \
#        --no-host-directories --no-directories --no-parent \
#        --accept "*.ppd*,*.PPD*" --directory-prefix=toshiba \
#        http://www.linuxprinting.org/download/PPD/Toshiba/
# Now all PPDs are in the sub-directory toshiba.
# Some PPDs may have non-latin1 encoding. Recode them to lat1 (e.g.: "recode ibmpc..lat1").
# Make a bzip2 compressed tar-archive of them:
#  tar -cjvf toshiba.ppd.tar.bz2 toshiba/*.ppd
Source13:       toshiba.ppd.tar.bz2
# Source1000,...Source1999 are for license testing.
# There may be several licenses for one manufacturer therefore the numbering is:
#   Source1000,...,Source1009 for licenses which belong to Source0
#   ...
#   Source1990,...,Source1999 for licenses which belong to Source99
# The *license files are extracted from the PPD files in the matching Source[0-99].
# If new PPD files have a different license then the license test below should detect them.
Source1000:     hp.license
Source1010:     oce.license
Source1020:     sharp.license
Source1030:     epson.license
Source1040:     kyocera.license
Source1050:     oki.license
# The Ricoh license applies also for Gestetner, Infotec, Lanier, NRG, Savin:
Source1060:     ricoh.license
Source1120:     brother.license
Source1130:     toshiba.license
# The package version matches to the openSUSE version:
Version:        10.2
Release:        0
# Install into this non-root directory (required when norootforbuild is used):
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%prep
# Create the build directory and change into it without unpacking anything
# then unpack the Sources one by one:
%setup -c -n %{name}-%{version} -T -a 0 -a 1 -a 2 -a 3 -a 4 -a 5 -a 6 -a 7 -a 8 -a 9 -a 10 -a 11 -a 12 -a 13

%build
# There is nothing to "make" as the sources contain plain PPD files.
# Neverteless some conversion and testing must be done.
# Only keep files where the license is o.k.:
# Test the license of HP's PPDs:
for p in hp/*.ppd
do grep -A 21 'Copyright [12][90][90][24]-200[356] Hewlett-Packard' $p | tail -n 20 | diff -q - %{SOURCE1000} || rm -v $p
done
# Test the license of OCE's PPDs:
for p in oce/*.ppd
do grep -A 19 'Permission is hereby granted' $p | diff -q - %{SOURCE1010} || rm -v $p
done
# Test the license of Sharp's PPDs:
for p in sharp/*.ppd
do grep -A 13 'This software is free software; you can redistribute it and/or' $p | diff -q - %{SOURCE1020} || rm -v $p
done
# Test the license of EPSON's PPDs:
for p in epson/*.ppd
do grep -A 25 'Copyright (C) 2003 Seiko Epson Corporation' $p | diff -q --strip-trailing-cr - %{SOURCE1030} || rm -v $p
done
# Test the licenses of Kyocera's PPDs:
for p in kyocera/*.ppd
do grep -A 24 "Copyright (C) 2000 KYOCERA CORPORATION" $p | tail -n 22 | diff -q - %{SOURCE1040} || rm -v $p
done
# Test the license of Oki's PPDs:
for p in oki/*.ppd
do grep -A 20 'This PostScript Printer Description(PPD) file is free software' $p | diff -q - %{SOURCE1050} || rm -v $p
done
# Test the license of Ricoh's PPDs:
for d in ricoh gestetner infotec lanier nrg savin
do for p in $d/*.ppd
   do grep -A 19 'Permission is hereby granted, free of charge, to any person obtaining' $p | diff -q - %{SOURCE1060} || rm -v $p
   done
done
# Test the license of Brother's PPDs:
for p in brother/*.ppd
do grep -A 8 'This program is free software' $p | diff -q - %{SOURCE1120} || rm -v $p
done
# Test the licenses of Toshiba's PPDs:
for p in toshiba/*.ppd
do grep -A 24 "Copyright (c) 2006 TOSHIBA TEC Corporation" $p | tail -n 23 | diff -q - %{SOURCE1130} || rm -v $p
done
# Make some general tests and adjustments for all PPDs:
# - Add a line-feed to the end of all PPDs to fix those PPDs where it is missing.
#   See Novell/Suse Bugzilla bug #309832: Unix/Linux text files must end with a line-feed.
#   Otherwise reading the last line results EOF and then some programs may ignore the last line.
# - Only keep files which are really PPD files (test file's output).
# - Only keep files which are of '*LanguageVersion: English'.
# - Remove whitespaces (except \n) from lines which contain only whitespaces
#   ('\n \n' is not allowed but '\n\n' is),
# - Change default media size to A4 if this is an available choice in the PPD and then
#   set DefaultPageSize, DefaultPageRegion, DefaultImageableArea, DefaultPaperDimension to A4.
for d in hp oce sharp epson kyocera oki ricoh gestetner infotec lanier nrg savin brother toshiba
do for p in $d/*.ppd
   do echo -en '\n' >>$p
      file $p | grep -q 'PPD file, ve' || { rm -v $p ; continue ; }
      grep -q '^\*LanguageVersion:[[:space:]]*English' $p || { rm -v $p ; continue ; }
      perl -pi -e 's/^[ \t]+$//' $p
      for i in PageSize PageRegion ImageableArea PaperDimension
      do if grep -q "^\*$i[[:space:]]*A4[:/]" $p
         then grep -q "^\*Default$i:[[:space:]]*A4\$" $p || perl -pi -e "s/^\*Default$i:.*/\*Default$i: A4/" $p
         fi
      done
   done
done
# Fix trivial bugs for particular PPDs:
# Fix bugs in HP PPDs:
# Some PPDs contain "1284DeviceId" which must be "1284DeviceID".
# Some PPDs contain "* PageRegion" which must be "*PageRegion".
for p in hp/*.ppd
do perl -pi -e 's/1284DeviceId/1284DeviceID/;' $p
   perl -pi -e 's/\* PageRegion/*PageRegion/;' $p
done
# Correct problematic HP PPDs:
# HP_LaserJet_5Si.ppd works only when this printer has the optional PostScript module:
sed -i -e '/^\*NickName:/s/ (recommended)//' hp/HP_LaserJet_5Si.ppd
sed -i -e '/^\*ModelName:/s/5Si/5Si MX/' hp/HP_LaserJet_5Si.ppd
# HP_LaserJet_5MP.ppd works only for the model with the built-in PostScript module ("MP"):
sed -i -e '/^\*ModelName:/s/5P/5MP/' hp/HP_LaserJet_5MP.ppd
# For Epson PPDs:
# In epson/epl5800.ppd there is "DefaultMediaType: Normal" but no "MediaType Normal"
# but there is "MediaType None/Plain":
perl -pi -e 's/^\*MediaType None(.*)$/\*MediaType Normal$1/;' epson/epl5800.ppd
# For Kyocera PPDs:
# Some have an entry  *1284DeviceID: "MFG:Kyocera Mita:Model:...
# which should be     *1284DeviceID: "MFG:Kyocera Mita;Model:...
# (i.e. wrong field seperator ':' instead of ';')
for p in kyocera/*.ppd
do sed -i -e 's/^\*1284DeviceID: "MFG:Kyocera Mita:Model:/*1284DeviceID: "MFG:Kyocera Mita;Model:/' $p
done
# For Ricoh PPDs:
for p in ricoh/Ricoh-DDP_92_PS.ppd ricoh/Ricoh-DDP_92_PS.plainPS.ppd
do sed -i -e 's/^\*UIConstraints: \*HKTrimming \*Option2 OneContainerStackerwithAdvancedFinisher \*HKTrimming$/*UIConstraints: *HKTrimming *Option2 OneContainerStackerwithAdvancedFinisher/' $p
done
# For Ricoh family PPDs:
# Add some info which kind of "driver" is used by the PPD.
# Mark all PCLXL PPDs to be "(recommended)" so that YaST selects them preferred
# because those models do not understand PostScript by default but only optionally.
# Mark a Foomatic PS.ppd to be "(recommended)" only if there is no matching PCLXL PPD
# so that YaST prefers the Foomatic PS.ppd with its additional features.
for d in ricoh gestetner infotec lanier nrg savin
do
   for p in $d/*_PXL.ppd
   do grep -q -i '^\*NickName:.*recommended' $p || perl -pi -e 's/^(\*NickName:.*)"$/$1 Foomatic\/pxlmono (recommended)"/;' $p
   done
   for p in $d/*_PS.plainPS.ppd
   do grep -q -i '^\*NickName:.*PostScript' $p || perl -pi -e 's/^(\*NickName:.*)"$/$1 plain PostScript"/;' $p
   done
   for p in $d/*_PS.ppd
   do if test -e $( echo $p | sed -e 's/_PS.ppd/_PXL.ppd/' )
      then grep -q -i '^\*NickName:.*Foomatic' $p || perl -pi -e 's/^(\*NickName:.*)"$/$1 PostScript+Foomatic"/;' $p
      else grep -q -i '^\*NickName:.*Foomatic' $p || perl -pi -e 's/^(\*NickName:.*)"$/$1 PostScript+Foomatic (recommended)"/;' $p
      fi
   done
done
# Final test by cupstestppd:
# Only keep files which don't FAIL for cupstestppd (therefore cups is needed for build),
# to save disk space gzip the files (gzipped PPDs can also be used by CUPS).
# Ignore FAILs because of errors in UIConstraints and/or NonUIConstraints
# which are detected since cupstestppd in CUPS > 1.2.7 (i.e. in openSUSE 10.3).
# See Novell/Suse Bugzilla bug #309822: When this bug is fixed, cupstestppd would
# no longer result zero exit code.
# In the long run the PPDs should be fixed but as far as we know there have been
# no problems because of such UIConstraints errors so that it should be o.k.
# let those PPDs pass even if they are not strictly compliant.
# Keep all PPDs even if cupstestppd FAILs.
# Reason:
# With each CUPS version upgrade cupstestppd finds more and more errors
# so that more and more PPDs would be no longer included in the RPM
# which have been included before which results a regression.
# As far as we know there have been no problems at all because of
# not strictly compliant PPDs so that it is much better
# to provide all PPDs so that the matching printers can be used
# than to be rigorous regarding enforcing compliance to the PPD specification:
for d in hp oce epson kyocera oki ricoh gestetner infotec lanier nrg savin brother toshiba
do for p in $d/*.ppd
   do egrep -v '^\*UIConstraints:|^\*NonUIConstraints:' $p | cupstestppd - || true
      gzip -n -9 $p
   done
done
# Apply a special test for Sharp PPDs:
# Several Sharp PPDs include additional special Duplex option choices
# DuplexBookletLeft and DuplexBookletRight which are not in compliance
# to the Adobe PPD specification (section 5.17) which lists the
# allowed Duplex option choices.
# As those additional choices should not cause real problems
# (perhaps some printing frontends may not show them to the user),
# we let those PPDs pass even if they are not strictly compliant.
# Keep all PPDs even if cupstestppd FAILs.
# Reason:
# With each CUPS version upgrade cupstestppd finds more and more errors
# so that more and more PPDs would be no longer included in the RPM
# which have been included before which results a regression.
# As far as we know there have been no problems at all because of
# not strictly compliant PPDs so that it is much better
# to provide all PPDs so that the matching printers can be used
# than to be rigorous regarding enforcing compliance to the PPD specification:
for p in sharp/*.ppd
do egrep -v '^\*UIConstraints:|^\*NonUIConstraints:|DuplexBooklet' $p | cupstestppd - || true
   gzip -n -9 $p
done
# For each manufacturer check and warn for duplicate NickName entries.
# Usually the NickName entry is shown to the user to let him select a PPD
# and then PPDs with same NickName entries are undistinguishable for the user.
# Nevertheless we keep them because e.g. in YaST or when using "lpadmin"
# the user can alternatively select a PPD via its file name.
for d in hp oce sharp epson kyocera oki ricoh gestetner infotec lanier nrg savin brother toshiba
do zgrep -h '^\*NickName:' $d/*.ppd.gz | grep -o '"[^"]*"' | sort -f | uniq -dci | grep '.*' && echo "duplicate NickName entries for $d" || :
done

%install
# Make the install directories and install the matching PPDs:
for d in hp oce sharp epson kyocera oki ricoh gestetner infotec lanier nrg savin brother toshiba
do mkdir -p %{buildroot}/usr/share/cups/model/%{name}/$d
   install -m 644 $d/*.ppd.gz %{buildroot}/usr/share/cups/model/%{name}/$d
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%dir /usr/share/cups
%dir /usr/share/cups/model
/usr/share/cups/model/%{name}

%description
PPD files from printer manufacturers that are under a free license.

For example, the original MIT license, shown for example under
http://www.opensource.org/licenses/mit-license.php, is okay but not an
often used modified MIT license, which does not allow redistribution if
the file was altered in any way from its original form.

If you have a PostScript printer and there is no PPD file included in
this package, ask your printer manufacturer for a PPD file or visit
http://www.linuxprinting.org/ppd-doc.html.




%changelog
