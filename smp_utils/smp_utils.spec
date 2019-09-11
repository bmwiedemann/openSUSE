#
# spec file for package smp_utils
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           smp_utils
%define lname   libsmputils1-1
Version:        0.98
Release:        0
Summary:        Utilities for the SAS Management Protocol (SMP)
License:        BSD-3-Clause AND GPL-2.0-only
Group:          Hardware/Other

Source:         http://sg.danny.cz/sg/p/%name-%version.tar.xz
Patch:          sysmacros.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  xz
Provides:       scsi:/usr/bin/smp_conf_general
Provides:       scsi:/usr/bin/smp_conf_route_info
Provides:       scsi:/usr/bin/smp_discover
Provides:       scsi:/usr/bin/smp_discover_list
Provides:       scsi:/usr/bin/smp_phy_control
Provides:       scsi:/usr/bin/smp_phy_test
Provides:       scsi:/usr/bin/smp_read_gpio
Provides:       scsi:/usr/bin/smp_rep_exp_route_tbl
Provides:       scsi:/usr/bin/smp_rep_general
Provides:       scsi:/usr/bin/smp_rep_manufacturer
Provides:       scsi:/usr/bin/smp_rep_phy_err_log
Provides:       scsi:/usr/bin/smp_rep_phy_sata
Provides:       scsi:/usr/bin/smp_rep_route_info
Provides:       scsi:/usr/bin/smp_write_gpio

%description
The smp_utils package contains utilities for the Serial Attached SCSI
(SAS) Management Protocol (SMP).  Most utilities correspond to a single
SMP function, sending out a request, checking for errors and if all is
well processing the response. The response is either decoded, printed
out in ASCII hexadecimal or sent as binary to stdout.

%package -n %lname
Summary:        Library for SAS SMP control of expanders
Group:          System/Libraries

%description -n %lname
The smp_utils package contains utilities for the Serial Attached SCSI
(SAS) Management Protocol (SMP).

This subpackage holds the library of shared functions.

%package -n libsmputils-devel
Summary:        Development files for the SAS SMP Expander Control Library
Group:          Development/Libraries/C and C++
Requires:       %lname = %version

%description -n libsmputils-devel
The smp_utils package contains utilities for the Serial Attached SCSI
(SAS) Management Protocol (SMP).

This subpackage contains libraries and header files for developing
applications that want to make use of libsmputils.

%prep
%setup -q
%patch -p1

%build
# None of these is performance-critical, so use -Os rather than -O2:
export CFLAGS=$(echo "%optflags" | sed 's/\-O2/-Os/')
%configure --disable-static
make %{?_smp_mflags}

%install
make install DESTDIR="%buildroot"
rm -f "%buildroot/%_libdir"/*.la

%files
%defattr(-,root,root)
# smp_utils
%doc README ChangeLog
%_bindir/smp_*
%_mandir/man8/*.8*

%files -n %lname
%defattr(-,root,root)
%_libdir/libsmputils1.so.1*

%files -n libsmputils-devel
%defattr(-,root,root)
%_includedir/scsi/
%_libdir/libsmputils1.so

%changelog
