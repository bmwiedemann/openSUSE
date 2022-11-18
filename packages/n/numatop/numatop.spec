#
# spec file for package numatop
#
# Copyright (c) 2022 SUSE LLC
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


Name:           numatop
Version:        2.3
Release:        0
Summary:        A top-like tool for runtime memory locality monitoring on NUMA systems
License:        BSD-3-Clause
Group:          System/Monitoring
URL:            https://01.org/numatop
Source0:        https://github.com/intel/%{name}/archive/refs/tags/v%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  check-devel
BuildRequires:  libnuma-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
ExclusiveArch:  x86_64 ppc64le

%description
NumaTOP is an observation tool for runtime memory locality characterization
and analysis of processes and threads running on a NUMA system. It helps the
user characterize the NUMA behavior of processes and threads and identify
where the NUMA-related performance bottlenecks reside.
Numatop is supported on Intel Xeon processors: 5500-series, 6500/7500-series,
5600 series, E7-x8xx-series, and E5-16xx/24xx/26xx/46xx-series.
E5-16xx/24xx/26xx/46xx-series should be updated to latest CPU microcode
(microcode must be 0x618+ or 0x70c+). Kernel 3.9 or higher is required.

%prep
%setup -q -n %{name}-%{version}

%build
autoreconf -i
%configure
# there seems to be wrong order of libnumatop.la and $(NCURSES_LIBS) in Makefile.am
make %{?_smp_mflags} LDFLAGS="-lncursesw -lncurses"

%install
%make_install

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%{_mandir}/man8/%{name}.8%{ext_man}

%changelog
