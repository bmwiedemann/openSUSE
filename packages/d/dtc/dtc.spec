#
# spec file for package dtc
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define         sover 1
Name:           dtc
Version:        1.5.0
Release:        0
Summary:        Device-tree compiler
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
Url:            https://github.com/dgibson/dtc
Source0:        https://mirrors.edge.kernel.org/pub/software/utils/dtc/dtc-%{version}.tar.gz
Source1:        baselibs.conf
Patch3:         dtc-license.patch
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  valgrind-devel

%description
PowerPC kernels are moving towards requiring a small Open
Firmware-style device tree as the only means of passing information
from bootloaders/firmware to the kernel. This does not require a full
Open Firmware implementation. DTC (Device Tree Compiler) is a tool to
create a static device tree, which is adequate for most embedded
systems (since their topology will not vary across reboots). DTC is
available via a git tree: git://ozlabs.org/srv/projects/dtc/dtc.git

%package -n libfdt%{sover}
Summary:        Device tree library
Group:          Development/Libraries/C and C++

%description -n libfdt%{sover}
libfdt is a library to process Open Firmware style device trees on various
architectures.

%package -n libfdt-devel
Summary:        Development headers for device tree library
Group:          Development/Libraries/C and C++
Requires:       libfdt%{sover} = %{version}-%{release}
# Provide previously used incorrectly named devel package
Provides:       libfdt1-devel = %{version}-%{release}
Obsoletes:      libfdt1-devel < %{version}-%{release}

%description -n libfdt-devel
This package provides development files for libfdt

%prep
%setup -q
%patch3

%build
make %{?_smp_mflags} V=1

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir}
install -p -m 644 libfdt/libfdt_env.h %{buildroot}/%{_includedir}
rm -f %{buildroot}/%{_libdir}/*.a

%check
make %{?_smp_mflags} check

%files
%defattr(-,root,root)
%doc README.license Documentation/manual.txt
%{_bindir}/convert-dtsv0
%{_bindir}/dtc
%{_bindir}/dtdiff
%{_bindir}/fdtdump
%{_bindir}/fdtget
%{_bindir}/fdtput
%{_bindir}/fdtoverlay

%post -n libfdt%{sover} -p /sbin/ldconfig
%postun -n libfdt%{sover} -p /sbin/ldconfig

%files -n libfdt%{sover}
%defattr(-,root,root,-)
%doc GPL
%{_libdir}/libfdt-%{version}.so
%{_libdir}/libfdt.so.*

%files -n libfdt-devel
%defattr(-,root,root,-)
%{_libdir}/libfdt.so
%{_includedir}/*

%changelog
