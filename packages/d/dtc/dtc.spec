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
Version:        1.5.1
Release:        0
Summary:        Device-tree compiler
License:        GPL-2.0-or-later
URL:            https://github.com/dgibson/dtc
Source0:        https://mirrors.edge.kernel.org/pub/software/utils/dtc/dtc-%{version}.tar.gz
Source1:        https://mirrors.edge.kernel.org/pub/software/utils/dtc/dtc-%{version}.tar.sign
Source2:        baselibs.conf
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libyaml-devel
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  swig

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

%description -n libfdt%{sover}
libfdt is a library to process Open Firmware style device trees on various
architectures.

%package -n libfdt-devel
Summary:        Development headers for device tree library
Requires:       libfdt%{sover} = %{version}-%{release}
# Provide previously used incorrectly named devel package
Provides:       libfdt1-devel = %{version}-%{release}
Obsoletes:      libfdt1-devel < %{version}-%{release}

%description -n libfdt-devel
This package provides development files for libfdt


%package -n python3-libfdt
Summary:        Python binding for Device Tree

%description -n python3-libfdt
libfdt is a library to process Open Firmware style device trees on various
architectures.

Python binding part.

%prep
%setup -q

%build
make %{?_smp_mflags} V=1 NO_PYTHON=1
cd pylibfdt
python3 setup.py build_ext
%py3_build

%install
%make_install PREFIX=%{_prefix} LIBDIR=%{_libdir} NO_PYTHON=1
install -p -m 644 libfdt/libfdt_env.h %{buildroot}/%{_includedir}
rm -f %{buildroot}/%{_libdir}/*.a
cd pylibfdt
%python3_install

%check
make %{?_smp_mflags} check

%files
%license README.license
%doc Documentation/manual.txt
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
%{_libdir}/libfdt-1.5.0.so
%{_libdir}/libfdt.so.*

%files -n libfdt-devel
%{_libdir}/libfdt.so
%{_includedir}/*

%files -n python3-libfdt
%{python3_sitearch}/*.so
%{python3_sitearch}/*.egg-info
%{python3_sitearch}/__pycache__/*.pyc
%{python3_sitearch}/libfdt.py

%changelog
