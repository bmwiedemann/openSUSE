#
# spec file for package intel-cmt-cat
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2016 Intel Corporation
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


# Since they ship libpqos and the binaries in one package but do not simultatious
# updates libversion can differ from binaries version.
%define libpqosMajor 4
%global make_flags EXTRA_CFLAGS="%{optflags}" SHARED=y PREFIX=%{buildroot}/%{_prefix} MAN_DIR=%{buildroot}/%{_mandir}/man8 LIB_INSTALL_DIR=%{buildroot}%{_libdir}/
Name:           intel-cmt-cat
Version:        4.4.1
Release:        0
Summary:        Command line interface to CMT, MBM, CAT and CDP technologies
License:        BSD-3-Clause
Group:          Development/Tools/Other
URL:            https://github.com/01org/%{name}
Source0:        https://github.com/intel/intel-cmt-cat/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         fix-bad-env-shebang.patch
BuildRequires:  doxygen
ExclusiveArch:  x86_64 %{ix86}

%description
This software package provides basic support for
Cache Monitoring Technology (CMT), Memory Bandwidth Monitoring (MBM),
Cache Allocation Technology (CAT) and Code Data Prioratization (CDP).

CMT, MBM and CAT are configured using Model Specific Registers (MSRs)
to measure last level cache occupancy, set up the class of service masks and
manage the association of the cores/logical threads to a class of service.
The software executes in user space, and access to the MSRs is
obtained through a standard Linux* interface. The virtual file system
provides an interface to read and write the MSR registers but
it requires root privileges.

%package     -n libpqos%{libpqosMajor}
Summary:        Runtime pqos library
Group:          System/Libraries

%description -n libpqos%{libpqosMajor}
PQoS library provides API to detect and configure Intel(R) RDT including:
Cache Monitoring Technology (CMT), Memory Bandwidth Monitoring (MBM),
Cache Allocation Technology (CAT), Code and Data Prioritization (CDP) Technology.

%package     -n libpqos-devel
Summary:        Development package for libpqos%{libpqosMajor}
Group:          Development/Libraries/C and C++
Requires:       libpqos%{libpqosMajor} = %{version}
#Version number should stay constant here, because devel package had a version number in the name previously
Obsoletes:      libpqos1-devel < %{version}
Provides:       libpqos1-devel = %{version}

%description    -n libpqos-devel
PQoS library provides API to detect and configure Intel(R) RDT including:
Cache Monitoring Technology (CMT), Memory Bandwidth Monitoring (MBM),
Cache Allocation Technology (CAT), Code and Data Prioritization (CDP) Technology.

This package contains all that is needed to develop/compile
applications that use PQoS.

%prep
%setup -q
%patch1 -p1

%build
%make_build %{make_flags}

%install
make %{make_flags} NOLDCONFIG=y install

%post -n libpqos%{libpqosMajor} -p /sbin/ldconfig
%postun -n libpqos%{libpqosMajor} -p /sbin/ldconfig

%files
%doc ChangeLog
%license LICENSE
%{_bindir}/membw
%{_mandir}/man8/membw.8%{?ext_man}
%{_bindir}/pqos
%{_mandir}/man8/pqos.8%{?ext_man}
%{_bindir}/rdtset
%{_mandir}/man8/rdtset.8%{?ext_man}
%{_bindir}/pqos-msr
%{_mandir}/man8/pqos-msr.8%{?ext_man}
%{_bindir}/pqos-os
%{_mandir}/man8/pqos-os.8%{?ext_man}

%files -n libpqos-devel
%{_includedir}/pqos.h
%{_libdir}/*.so

%files -n libpqos%{libpqosMajor}
%{_libdir}/*.so.*

%changelog
