#
# spec file for package cups-filters
#
# Copyright (c) 2024 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Summary:        OpenPrinting CUPS filters 2.x for CUPS 2.x
License:        Apache-2.0
Group:          Hardware/Printing
URL:            https://github.com/OpenPrinting/cups-filters
Name:           cups-filters2
Version:        2.0.1
Release:        0
# To get Source0 go to https://github.com/OpenPrinting/cups-filters/releases or use e.g.
# wget https://github.com/OpenPrinting/cups-filters/releases/download/2.0.1/cups-filters-2.0.1.tar.gz
Source0:        cups-filters-%{version}.tar.gz
BuildRequires:  cups-devel >= 2.2.2
BuildRequires:  libcupsfilters-devel >= 2.1.1
BuildRequires:  libppd-devel >= 2.1.1
BuildRequires:  ghostscript >= 10.0.0
# Provide the 'cups-filters' RPM capability for backward compatibility
# with RPMs which "Requires: cups-filters" or "Recommends: cups-filters":
Provides:       cups-filters = %{version}
# Conflict with the old 'cups-filters' version 1.x RPM because file conflicts happen
# when two packages attempt to install files with the same name but different contents.
Conflicts:      cups-filters < 2.0.0
# cups-filters2 is useless without CUPS and libcupsfilters and libppd:
Requires:       cups >= 2.2.2
Requires:       libcupsfilters >= 2.1.1
Requires:       libppd >= 2.1.1
# Ghostscript and poppler are usually needed but not strictly required:
Recommends:     ghostscript >= 10.0.0
Recommends:     poppler-tools

%description
This package contains backends, filters, and other software
that was once part of CUPS, but during the time when CUPS
was developed at Apple, Apple stopped maintaining these
parts as they were not needed by Mac OS.
In addition it contains more filters and software developed
independently of Apple, especially filters for the PDF-centric
printing workflow introduced by OpenPrinting.
Since CUPS 1.6.0 cups-filters is required for using printer
drivers (and also driverless printing) with CUPS under Linux.
This version 2.x of cups-filters is only for CUPS 2.2.2 or newer
(for older CUPS versions use cups-filters version 1.x).

%package driverless
# Because automated driverless printer setup is as generic security issue
# we provide the driverless parts as separated sub-package
# so users who do not need it can keep it away from their systems.
# We do not specify "Recommends: cups-filters2-driverless" here
# because a recommended package gets automatically (and silently) installed
# when it is available to be installed so software which is a generic security issue
# would get automatically installed in most cases without an explicit user request.
Summary: OpenPrinting automated driverless printer setup for CUPS 2.x
# cups-filters2-driverless is useless without its main package cups-filters2.
# Require the exact matching version-release of the cups-filters2 main package
# because all gets built simulaneously from the same cups-filters2 sources and
# there could be interdependencies in the sources so the driverless parts
# only work with the exact matching version-release of its main package:
Requires:       %{name} = %{version}-%{release}

%description driverless
Automated driverless printer setup requires IPP communication with the printer
for polling capability information from the printer to generate a PPD file
from what the printer responds to set up a print queue with that PPD file.
Automated printer setup from what a (possibly fake) printer responds
is a generic security issue: You must trust the printer because
the printer's response controlls what print queue gets set up.
Cf. https://en.opensuse.org/SDB:CUPS_and_SANE_Firewall_settings

%prep
%autosetup -n cups-filters-%{version} -p1

%build
# No need to set our preferred architecture-specific flags for the compiler and linker
# via export CFLAGS="$RPM_OPT_FLAGS" and export CXXFLAGS="$RPM_OPT_FLAGS"
# because the RPM macro configure does that.
# --disable-mutool : disable mupdf processing because we use gostcript
# --disable-foomatic : disable Foomatic-based filters because Foomatic is old and outdated
#   and has generic security issues in particular FoomaticRIPCommandLine in PPD files
#   which can execute basically arbitary commands indirectly via the foomatic-rip tool
#   cf. https://github.com/OpenPrinting/cups-filters/security/advisories/GHSA-p9rh-jxmq-gq47
#   and https://github.com/OpenPrinting/cups-filters/issues/599
# --enable-universal-cups-filter : use a single, universal CUPS filter executable for all filter functions
%configure --disable-static \
           --enable-shared \
           --disable-silent-rules \
           --disable-mutool \
           --disable-foomatic \
           --enable-universal-cups-filter \
           --docdir=%{_defaultdocdir}/%{name}
make %{?_smp_mflags}

%check
make check %{?_smp_mflags}

%install
%make_install
# Don't ship libtool la files:
rm -f %{buildroot}%{_libdir}/lib*.la
# Do no longer ship the parallel and serial backends for CUPS
# because parallel port printers and serial port printers are outdated:
rm -f %{buildroot}/usr/lib/cups/backend/parallel
rm -f %{buildroot}/usr/lib/cups/backend/serial

%files
%dir /usr/lib/cups
%dir /usr/lib/cups/backend
# The wrapper backend beh would need 0700 permissions so that cupsd runs it as root
# (backends with root-only permissions are run as root by cupsd)
# because otherwise wrapper backends cannot run other backends that need to run as root.
# In particular the ipp backend runs as root so that it can support Kerberos authentication
# see https://github.com/OpenPrinting/cups-filters/issues/183#issuecomment-570196216
# so when beh should be used for the ipp backend beh needs 0700 permissions to run as root.
# But running something as root in any case is a generic security issue
# which we avoid by not setting 0700 permissions for beh in any case here
# so the user must set such permissions manually only when really needed.
# See also https://bugzilla.opensuse.org/show_bug.cgi?id=1178604
# which was about as similar case where the implicitclass wrapper backend
# runs the ipp backend to print via queues that are generated by cupsd-browsed
# but cupsd-browsed is no longer included in cups-filters version 2.x
# because cupsd-browsed became a separated project at OpenPrinting
# see https://github.com/OpenPrinting/cups-browsed
# and cupsd-browsed is a generic security issue, see the section
# "Automated print queue setup via cups-browsed"
# in https://en.opensuse.org/SDB:CUPS_and_SANE_Firewall_settings
# cf. above the driverless sub-package description about the
# generic security issue "Automated driverless printer setup".
/usr/lib/cups/backend/beh
%dir /usr/lib/cups/filter
/usr/lib/cups/filter/*
%dir %{_datadir}/cups
%dir %{_datadir}/cups/drv
%{_datadir}/cups/drv/*
%dir %{_datadir}/cups/mime
%{_datadir}/cups/mime/*
%dir %{_datadir}/ppd
%dir %{_datadir}/ppd/cupsfilters
%{_datadir}/ppd/cupsfilters/*
%dir %{_datadir}/ppdc
%{_datadir}/ppdc/*
%doc %{_defaultdocdir}/%{name}

%files driverless
%{_bindir}/driverless
%{_bindir}/driverless-fax
%dir /usr/lib/cups
%dir /usr/lib/cups/backend
/usr/lib/cups/backend/driverless
/usr/lib/cups/backend/driverless-fax
%dir /usr/lib/cups/driver
/usr/lib/cups/driver/*
%{_mandir}/man1/driverless.1.gz

%changelog
