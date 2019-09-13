#
# spec file for package OpenPrintingPPDs
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           OpenPrintingPPDs
BuildRequires:  cups
# All printer driver packages should have "BuildRequires: python-cups"
# because python-cups installs special rpm macros that adds Provides tags
# for the printer drivers supported by the package,
# see https://bugzilla.novell.com/show_bug.cgi?id=735865
# but python-cups is not available for SLE10, regarding the suse_version value for SLE10
# see http://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto
%if 0%{?suse_version} > 1010
BuildRequires:  python-cups
%endif
Summary:        PPD files from OpenPrinting.org
License:        GPL-2.0+ and MIT
Group:          Hardware/Printing
# The package version is the PPD-O-MATIC version mentioned in the PPD files
# which is currently "PPD-O-MATIC (4.0.0 or newer)"
# and/or the required minimal foomatic-rip version by the PPD files
# which is currently "Foomatic 4.0.0"
# (macro name can be only alphanumeric and '_' i.e. "foomatic-rip_version" does not work)
%define foomatic_rip_version 4.0.0
# plus an additional trailing version number by openSUSE
# so that openSUSE package upgrades get a strictly increasing sequence of versions:
Version:        4.0.0.2
Release:        0
Url:            http://www.linuxfoundation.org/collaborate/workgroups/openprinting/database/query
BuildArch:      noarch
# The main-package OpenPrintingPPDs alone is useless because it does not contain any PPD files.
# The PPD files are provided via its sub-packages depending on which kind of driver software
# is needed so that the appropriate RPM requirements can be specified for each sub-package.
# Nevertheless when a user selects only the main-package to be installed, he probably
# wants "all the OpenPrintingPPDs" and therefore all sub-packages are recommended:
Recommends:     OpenPrintingPPDs-ghostscript
Recommends:     OpenPrintingPPDs-hpijs
Recommends:     OpenPrintingPPDs-postscript
# Howto make Source0:
# See the HOWTO file in the sources.
Source0:        OpenPrintingPPDs-%{version}.tar.bz2
# Install into this non-root directory (required when norootforbuild is used):
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
To set up a printer configuration a printer description file
(PPD file) is required.

A printer description file is not a driver.

For non-PostScript printers a driver is needed
together with a PPD file which matches exactly
to the particular driver.

For PostScript printers, a PPD file alone is sufficient
(except for older PostScript level 1 printer models).

The PPD files are provided in the following sub-packages
depending on which kind of driver software is needed:

OpenPrintingPPDs-ghostscript provides PPDs
which use Ghostscript built-in drivers.

OpenPrintingPPDs-hpijs provides PPDs
which use the hpijs driver from HPLIP.

OpenPrintingPPDs-postscript provides PPDs
which need no driver.


%package ghostscript
Summary:        PPD files from OpenPrinting.org which use Ghostscript built-in drivers
Group:          Hardware/Printing
# This version is no typo because the PPDs are created at OpenPrinting.org
# by PPD-O-MATIC version X.Y.Z which is the version of this package
# and usually those PPDs require at least the same version of the foomatic-rip filter:
Requires:       foomatic-filters >= %{foomatic_rip_version}
Requires:       ghostscript-library

%description ghostscript
PPD files for non-PostScript printers
which use a Ghostscript built-in driver
and PPD files for PostScript level 1 printers
which use the Ghostscript driver pswrite.


%package hpijs
Summary:        PPD files from OpenPrinting.org which use the hpijs driver
Group:          Hardware/Printing
# This version is no typo because the PPDs are created at OpenPrinting.org
# by PPD-O-MATIC version X.Y.Z which is the version of this package
# and usually those PPDs require at least the same version of the foomatic-rip filter:
Requires:       foomatic-filters >= %{foomatic_rip_version}
Requires:       ghostscript-library
Requires:       hplip-hpijs

%description hpijs
PPD files for non-PostScript printers
which use the Ghostscript IJS driver
/usr/bin/hpijs from HPLIP.


%package postscript
Summary:        PPD files from OpenPrinting.org for PostScript printers
Group:          Hardware/Printing
# Regardless that PPD files for PostScript printers do not require a driver
# many PPD files from OpenPrinting.org for PostScript printers still
# require the foomatic-rip filter which does not call 'gs' or another real driver program
# but inserts PostScript snippets from the PPD at the beginning of the PostScript data.
# This version is no typo because the PPDs are created at OpenPrinting.org
# by PPD-O-MATIC version X.Y.Z which is the version of this package
# and usually those PPDs require at least the same version of the foomatic-rip filter:
Requires:       foomatic-filters >= %{foomatic_rip_version}

%description postscript
PPD files for PostScript printers
which do not use a driver but
may use the foomatic-rip filter.


%prep
# Be quiet when unpacking:
%setup -q -n OpenPrintingPPDs

%build
# There is nothing to "make" as the sources contain plain PPD files.
# Neverteless some conversion and testing must be done.
PPDs_DIRs="PPDs_for_printers_for_ghostscript_drivers \
           PPDs_for_printers_for_hpijs_drivers \
           PPDs_for_printers_for_postscript_drivers"
set +x
# Make some general tests and adjustments for all PPDs:
# - Add a line-feed to the end of all PPDs to fix those PPDs where it is missing.
#   See Novell/Suse Bugzilla bug #309832: Unix/Linux text files must end with a line-feed.
#   Otherwise reading the last line results EOF and then some programs may ignore the last line.
# - Only keep files which are really PPD files (test file's output).
# - Only keep files which are of '*LanguageVersion: English'.
# - Remove PPDs which use an non-Ghostscript external driver filter program.
# - Remove whitespaces (except \n) from lines which contain only whitespaces
#   ('\n \n' is not allowed but '\n\n' is).
# Some of the manufactuer's PPD files contain a non-free redistribution license
# which demands that "the contents of the file are not altered"
# but adding only a line-feed to the end of a PPD file and
# removing lines which contain only whitespaces
# is considered to be still allowed:
for d in $PPDs_DIRs
do echo "Making general tests and adjustments for the PPDs in $d"
   for p in $d/*.ppd
   do echo -en '\n' >>$p
      file $p | grep -q 'PPD file, ve' || { rm -v $p ; continue ; }
      grep -q '^\*LanguageVersion:[[:space:]]*English' $p || { rm -v $p ; continue ; }
      grep -q '^\*driverType F/Filter:' $p && { rm -v $p ; continue ; }
      sed -i -e 's/^[[:space:]]*$//' $p
   done
   echo "Finished general tests and adjustments for the PPDs in $d"
done
# Fix trivial bugs for particular PPDs:
# Some Lexmark PPDs contain "* DefaultColorSep:", "* DefaultOutputOrder:", "* DefaultScreenProc:", "* InkName:"
# which must be "*DefaultColorSep:", "*DefaultOutputOrder:", "*DefaultScreenProc:", "*InkName:"
for p in PPDs_for_printers_for_postscript_drivers/Lexmark-*.Postscript-Lexmark.ppd
do echo "Fixing trivial bugs for Lexmark PPD $p"
   for k in DefaultColorSep DefaultOutputOrder DefaultScreenProc InkName
   do sed -i -e "s/^\* $k:/*$k:/" $p
   done
done
# For Kyocera PPDs:
# Some have an 1284DeviceID entry "MFG:Kyocera Mita:Model:...
# which should be                 "MFG:Kyocera Mita;Model:...
# (i.e. wrong field seperator ':' instead of ';')
for p in PPDs_for_printers_for_postscript_drivers/Kyocera-CS-*.Postscript-Kyocera.ppd
do echo "Fixing trivial bugs for Kyocera PPD $p"
   if grep -q 'MFG:Kyocera Mita:Model:' $p
   then # Some of Kyocera's PostScript PPD files contain a non-free redistribution license
        # which demands that "the contents of the file are not altered in any way from their original form"
        # so that issues in those PPD files cannot be fixed:
        if grep -q 'contents of the file are not altered' $p
        then echo "Kyocera's redistribution license forbids to fix 'MFG:Kyocera Mita:Model:' bug in $p"
        else sed -i -e 's/MFG:Kyocera Mita:Model:/MFG:Kyocera Mita;Model:/' $p
             echo "Fixed 'MFG:Kyocera Mita:Model:' bug in $p"
        fi
   fi
done
# Final test by cupstestppd:
# Keep all PPDs even if cupstestppd FAILs.
# Reason:
# With each CUPS version upgrade cupstestppd finds more and more errors
# so that more and more PPDs would be no longer included in the RPM
# which have been included before which results a regression.
# As far as we know there have been no problems at all because of
# not strictly compliant PPDs so that it is much better
# to provide all PPDs so that the matching printers can be used
# than to be rigorous regarding enforcing compliance to the PPD specification:
for d in $PPDs_DIRs
do echo "Testing with cupstestppd the PPDs in $d"
   for p in $d/*.ppd
   do cupstestppd -q -W all -r $p || echo "cupstestppd failed for $p"
   done
   echo "Finished testing with cupstestppd the PPDs in $d"
done
# Check and warn for duplicate NickName entries.
# Usually the NickName entry is shown to the user to let him select a PPD
# and then PPDs with same NickName entries are undistinguishable for the user.
# Nevertheless we keep them because e.g. in YaST or when using "lpadmin"
# the user can alternatively select a PPD via its file name.
for d in $PPDs_DIRs
do echo "Checking duplicate NickName entries for the PPDs in $d"
   grep -h '^\*NickName:' $d/*.ppd | grep -o '"[^"]*"' | sort -f | uniq -dci | grep '.*' && echo "There are duplicate NickName entries in PPDs in $d"
   echo "Finished checking duplicate NickName entries for the PPDs in $d"
done
# Finally compress the PPDs:
for d in $PPDs_DIRs
do echo "Compressing the PPDs in $d"
   for p in $d/*.ppd
   do gzip -n -9 "$p"
   done
   echo "Finished compressing the PPDs in $d"
done

%install
# Make the install directories and install the matching PPDs:
for d in ghostscript hpijs postscript
do mkdir -p %{buildroot}/usr/share/cups/model/OpenPrintingPPDs/$d
   set +x
   echo "Installing the '$d' PPDs."
   for p in PPDs_for_printers_for_${d}_drivers/*.ppd.gz
   do install -m 644 $p %{buildroot}/usr/share/cups/model/OpenPrintingPPDs/$d
   done
   echo "Finished installing the '$d' PPDs."
   set -x
done
# Do not install the "Generic GDI Printer" PPD because there is no such thing
# as a "Generic GDI Printer", see http://www.cups.org/str.php?L3759
# The particular GDI printer models which are supported have already their
# individual /usr/share/cups/model/OpenPrintingPPDs/ghostscript/*gdi* PPD files.
rm %{buildroot}/usr/share/cups/model/OpenPrintingPPDs/ghostscript/Generic-GDI_Printer.gdi.ppd.gz

%files
%defattr(-,root,root)
%doc HOWTO README gpl-2.0.txt makePPDtest

%files ghostscript
%defattr(-,root,root)
%dir /usr/share/cups
%dir /usr/share/cups/model
%dir /usr/share/cups/model/OpenPrintingPPDs
/usr/share/cups/model/OpenPrintingPPDs/ghostscript

%files hpijs
%defattr(-,root,root)
%dir /usr/share/cups
%dir /usr/share/cups/model
%dir /usr/share/cups/model/OpenPrintingPPDs
/usr/share/cups/model/OpenPrintingPPDs/hpijs

%files postscript
%defattr(-,root,root)
%dir /usr/share/cups
%dir /usr/share/cups/model
%dir /usr/share/cups/model/OpenPrintingPPDs
/usr/share/cups/model/OpenPrintingPPDs/postscript

%changelog
