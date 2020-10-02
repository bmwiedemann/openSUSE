#
# spec file for package libnvidia-container
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


%define sover 1
%define modprobe_version 396.51

Name:           libnvidia-container
Version:        1.1.1
Release:        0
Summary:        NVIDIA container runtime library
# elftoolchain is licensed under BSD-3-Clause
#  https://github.com/elftoolchain/elftoolchain#copyright-and-license
# libnvidia-container is licensed under apache-2.0
#  https://github.com/NVIDIA/libnvidia-container/blob/master/LICENSE
# libnvidia-container includes the GLPv3 license
#  https://github.com/NVIDIA/libnvidia-container/blob/master/COPYING
# libnvidia-container includes the LGPLv3 license
#  https://github.com/NVIDIA/libnvidia-container/blob/master/COPYING.LESSER
# nvidia-modprobe is licensed under GPLv2
#  https://github.com/NVIDIA/nvidia-modprobe/blob/master/COPYING
# several nvidia-modprobe files contain the MIT license header
#  https://github.com/NVIDIA/nvidia-modprobe/blob/master/utils.mk
License:        BSD-3-Clause AND Apache-2.0 AND GPL-3.0-or-later AND LGPL-3.0-or-later AND MIT AND GPL-2.0-only
URL:            https://github.com/NVIDIA/libnvidia-container
Source:         https://github.com/NVIDIA/libnvidia-container/archive/v%{version}.tar.gz#/libnvidia-container-%{version}.tar.gz
Source1:        https://github.com/NVIDIA/nvidia-modprobe/archive/%{modprobe_version}.tar.gz#/nvidia-modprobe-%{modprobe_version}.tar.gz
Patch0:         libnvidia-container-fix-revision.patch
Patch1:         libnvidia-container-fix-makefile.patch
Patch2:         no-manual-debuginfo.patch
BuildRequires:  bmake
BuildRequires:  distribution-release
BuildRequires:  groff
BuildRequires:  libcap-devel
BuildRequires:  libelf-devel
BuildRequires:  libseccomp-devel
BuildRequires:  libtirpc-devel
BuildRequires:  lsb-release
BuildRequires:  m4
BuildRequires:  rpcgen
ExcludeArch:    i586

%description
The nvidia-container library provides an interface to configure GNU/Linux
containers leveraging NVIDIA hardware. The implementation relies on several
kernel subsystems and is designed to be agnostic of the container runtime.

%package -n %{name}%{sover}
Summary:        NVIDIA container runtime library

%description -n %{name}%{sover}
The nvidia-container library provides an interface to configure GNU/Linux
containers leveraging NVIDIA hardware. The implementation relies on several
kernel subsystems and is designed to be agnostic of the container runtime.

This package requires the NVIDIA driver (>= 340.29) to be installed separately.

%package devel
Summary:        NVIDIA container runtime library (development files)
Requires:       %{name}%{sover} = %{version}-%{release}

%description devel
The nvidia-container library provides an interface to configure GNU/Linux
containers leveraging NVIDIA hardware. The implementation relies on several
kernel subsystems and is designed to be agnostic of the container runtime.

This package contains the files required to compile programs with the library.

%package static
Summary:        NVIDIA container runtime library (static library)
Requires:       %{name}-devel = %{version}-%{release}

%description static
The nvidia-container library provides an interface to configure GNU/Linux
containers leveraging NVIDIA hardware. The implementation relies on several
kernel subsystems and is designed to be agnostic of the container runtime.

This package requires the NVIDIA driver (>= 340.29) to be installed separately.

%package tools
Summary:        NVIDIA container runtime library (command-line tools)
Requires:       %{name}%{sover} >= %{version}-%{release}

%description tools
The nvidia-container library provides an interface to configure GNU/Linux
containers leveraging NVIDIA hardware. The implementation relies on several
kernel subsystems and is designed to be agnostic of the container runtime.

This package contains command-line tools that facilitate using the library.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
# META_NOECHO=echo is required to work around a bug in Leap 15's version of bmake,
# see also https://github.com/ptt/pttbbs/issues/30
export META_NOECHO="echo"
export REVISION=%{version}
REVISION=%{version} make distclean

mkdir -p deps/src/nvidia-modprobe-%{modprobe_version}
tar -C deps/src/nvidia-modprobe-%{modprobe_version} --strip-components=1 -xzf %{SOURCE1}
touch deps/src/nvidia-modprobe-%{modprobe_version}/.download_stamp

%make_build REVISION=%{version} WITH_LIBELF=yes

%install
# META_NOECHO=echo is required to work around a bug in Leap 15's version of bmake,
# see also https://github.com/ptt/pttbbs/issues/30
export META_NOECHO="echo"
make install DESTDIR=%{buildroot} REVISION=%{version} WITH_LIBELF=yes \
             LDCONFIG=/bin/true \
             prefix=%{_prefix} \
             exec_prefix=%{_exec_prefix} \
             bindir=%{_bindir} \
             libdir=%{_libdir} \
             includedir=%{_includedir} \
             docdir=%{_licensedir}

# Add the missing link
ln -s libnvidia-container.so.%{version} %{buildroot}%{_libdir}/libnvidia-container.so.1

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%doc README.md
%license %{_licensedir}/*
%{_libdir}/libnvidia-container.so.*

%files devel
%{_includedir}/nvc.h
%{_includedir}/nvidia-modprobe-utils.h
%{_includedir}/pci-enum.h
%{_libdir}/libnvidia-container.so
%{_libdir}/pkgconfig/libnvidia-container.pc

%files static
%{_libdir}/libnvidia-container.a
%{_libdir}/libnvidia-modprobe-utils.a

%files tools
%{_bindir}/nvidia-container-cli

%changelog
