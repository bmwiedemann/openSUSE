#
# spec file for package smp_utils
#
# Copyright (c) 2020 SUSE LLC
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


%define lname   libsmputils1-1
Name:           smp_utils
Version:        0.99
Release:        0
Summary:        Utilities for the SAS Management Protocol (SMP)
License:        BSD-3-Clause AND GPL-2.0-only
Group:          Hardware/Other
Source:         http://sg.danny.cz/sg/p/%{name}-%{version}.tar.xz
Provides:       scsi:%{_bindir}/smp_conf_general
Provides:       scsi:%{_bindir}/smp_conf_route_info
Provides:       scsi:%{_bindir}/smp_discover
Provides:       scsi:%{_bindir}/smp_discover_list
Provides:       scsi:%{_bindir}/smp_phy_control
Provides:       scsi:%{_bindir}/smp_phy_test
Provides:       scsi:%{_bindir}/smp_read_gpio
Provides:       scsi:%{_bindir}/smp_rep_exp_route_tbl
Provides:       scsi:%{_bindir}/smp_rep_general
Provides:       scsi:%{_bindir}/smp_rep_manufacturer
Provides:       scsi:%{_bindir}/smp_rep_phy_err_log
Provides:       scsi:%{_bindir}/smp_rep_phy_sata
Provides:       scsi:%{_bindir}/smp_rep_route_info
Provides:       scsi:%{_bindir}/smp_write_gpio

%description
The smp_utils package contains utilities for the Serial Attached SCSI
(SAS) Management Protocol (SMP).  Most utilities correspond to a single
SMP function, sending out a request, checking for errors and if all is
well processing the response. The response is either decoded, printed
out in ASCII hexadecimal or sent as binary to stdout.

%package -n %{lname}
Summary:        Library for SAS SMP control of expanders
Group:          System/Libraries

%description -n %{lname}
The smp_utils package contains utilities for the Serial Attached SCSI
(SAS) Management Protocol (SMP).

This subpackage holds the library of shared functions.

%package -n libsmputils-devel
Summary:        Development files for the SAS SMP Expander Control Library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description -n libsmputils-devel
The smp_utils package contains utilities for the Serial Attached SCSI
(SAS) Management Protocol (SMP).

This subpackage contains libraries and header files for developing
applications that want to make use of libsmputils.

%prep
%setup -q

%build
%configure --disable-static
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
# smp_utils
%doc README ChangeLog
%license COPYING
%{_bindir}/smp_*
%{_mandir}/man8/*.8%{?ext_man}

%files -n %{lname}
%{_libdir}/libsmputils1.so.1*

%files -n libsmputils-devel
%{_includedir}/scsi/
%{_libdir}/libsmputils1.so

%changelog
