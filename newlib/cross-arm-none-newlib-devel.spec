#
# spec file for package cross-arm-none-newlib-devel
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


%define cross_arch arm-none

%define gcc_cross_arch %{cross_arch}
%if "%{cross_arch}" == "riscv64"
%define gcc_cross_arch %{cross_arch}-elf
%endif

Name:           cross-%{cross_arch}-newlib-devel
Version:        3.1.0
Release:        0
Summary:        C library intended for use on %{cross_arch} embedded systems
License:        BSD-3-Clause AND MIT AND LGPL-2.0-or-later AND ISC
Group:          Development/Tools
Url:            https://sourceware.org/newlib/
Source0:        ftp://sourceware.org/pub/newlib/newlib-%{version}.tar.gz

Patch1:         epiphany-fixes.diff

%if "%{cross_arch}" == "riscv64"
BuildRequires:  cross-%{gcc_cross_arch}-gcc8-bootstrap
%else
BuildRequires:  cross-%{gcc_cross_arch}-gcc%{gcc_version}-bootstrap
%endif
%if %{suse_version} > 1220
BuildRequires:  makeinfo
%else
BuildRequires:  texinfo
%endif

%description
Newlib is a C library intended for use on embedded systems. It is a
conglomeration of several library parts.

%define target %{cross_arch}
%if "%{cross_arch}" == "epiphany" || "%{cross_arch}" == "riscv32" || "%{cross_arch}" == "riscv64" || "%{cross_arch}" == "rl78" || "%{cross_arch}" == "rx"
%define target %{cross_arch}-elf
%endif
%if "%{cross_arch}" == "arm-none"
%define target %{cross_arch}-eabi
%endif
%if "%{cross_arch}" == "spu"
%define sysroot /usr/spu
%else
%define sysroot %{_prefix}/%{target}/sys-root
%endif

%prep
%setup -q -n newlib-%{version}
%patch1 -p1

%build
mkdir build-dir
cd build-dir
../configure \
	--prefix=%{_prefix} --libdir=%{_libdir} --mandir=%{_mandir} --infodir=%{_infodir} \
	--target=%{target} \
%if "%{cross_arch}" == "arm-none"
	--with-multilib-list=armv6-m,armv7-m,armv7e-m,cortex-m7,armv7-r \
%endif
	--with-build-sysroot=%{sysroot}
make %{?_smp_mflags}

%install
# All binaries built are for the target architecture - don't damage them.
export NO_BRP_STRIP_DEBUG=true
export NO_DEBUGINFO_STRIP_DEBUG=true
%define __debug_install_post %{nil}
: >debugfiles.list
: >debugsourcefiles.list
: >debugsources.list

cd build-dir
make install DESTDIR=%{buildroot}

%files
%defattr(-,root,root,-)
%{_prefix}/%{target}/

%changelog
