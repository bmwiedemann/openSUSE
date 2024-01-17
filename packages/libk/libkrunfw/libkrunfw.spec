#
# spec file for package libkrunfw
#
# Copyright (c) 2023 SUSE LLC
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


%define sev 1

%global kernel linux-6.0.6

%ifnarch x86_64
%define sev 0
%endif

%define descr \
libkrunfw is a library bundling a Linux kernel in a dynamic library \
in a way that can be easily consumed by libkrun. \
By having the kernel bundled in a dynamic library, libkrun can leave to \
the linker the work of mapping the sections into the process, and then \
directly inject those mappings into the guest without any kind of additional \
work nor processing.

Name:           libkrunfw
Version:        3.8.1
Release:        0
Summary:        A dynamic library bundling a Linux kernel in a convenient storage format
License:        GPL-2.0-only AND LGPL-2.1-only
URL:            https://github.com/containers/libkrunfw
Source0:        https://github.com/containers/libkrunfw/archive/v%{version}.tar.gz#/libkrunfw-%{version}.tar.gz
Source1:        https://www.kernel.org/pub/linux/kernel/v6.x/%{kernel}.tar.xz
ExclusiveArch:  x86_64 aarch64
# For building libkrunfw itself, we need:
BuildRequires:  gcc
BuildRequires:  git-core
BuildRequires:  openssl-devel
BuildRequires:  python3-pyelftools
# For building the embedded kernel, we need:
BuildRequires:  bc
BuildRequires:  binutils
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  libelf-devel
# Handling transitions from (very) old versions of the package
Conflicts:      libkrunfw-devel <= 0.7
Conflicts:      libkrunfw0 <= 0.7

%description
%{summary}

%package -n %{name}3
Summary:        A dynamic library bundling a Linux kernel in a convenient storage format
Obsoletes:      libkrunfw <= 3.6.3

%description -n %{name}3
%{descr}

%package devel
Summary:        Header files and libraries for libkrunfw development
Requires:       %{name}3 = %{version}-%{release}

%description devel
%{descr}

This package contains the libraries needed to develop programs
that consume the guest payload integrated in libkrunfw.

%if %{sev}
%package sev3
Summary:        A dynamic library bundling the guest payload consumed by libkrun-sev
Obsoletes:      libkrunfw <= 3.6.3

%description sev3
%{descr}

This package contains the library bundling the guest payload consumed
by libkrun-sev.

%package sev-devel
Summary:        Header files and libraries for libkrunfw-sev development
Requires:       %{name}-sev3 = %{version}-%{release}
Provides:       %{name}:%{_libdir}/libkrunfw-sev.so
Obsoletes:      %{name} < %{version}-%{release}

%description sev-devel
%{descr}

This package contains the libraries needed to develop programs that
consume the guest payload integrated in libkrunfw-sev.
%endif

%prep
%autosetup -S git
mkdir tarballs
cp %{SOURCE1} tarballs/

%build
test -n "$SOURCE_DATE_EPOCH" || export SOURCE_DATE_EPOCH=`date +%s`
cat > .kernel-binary.spec.buildenv <<EOF
export KBUILD_BUILD_TIMESTAMP="$(LANG=C date -u -d "@$SOURCE_DATE_EPOCH")"
export KBUILD_BUILD_USER=geeko
export KBUILD_BUILD_HOST=buildhost
EOF
source ./.kernel-binary.spec.buildenv

%make_build

%if %{sev}
rm -rf %{kernel}
rm kernel.c
%make_build SEV=1
pushd utils
%if 0%{?suse_version} > 1500
make
%else
# Workaround an issue of "undefined reference to symbol 'dlsym@@GLIBC_2.2.5'"
# in older distros.
gcc -o krunfw_measurement krunfw_measurement.c -lcrypto -ldl
%endif
popd
%endif

%install
source ./.kernel-binary.spec.buildenv
%make_install PREFIX=%{_prefix}

%if %{sev}
%make_install SEV=1 PREFIX=%{_prefix}
install -D -p -m 0755 utils/krunfw_measurement %{buildroot}%{_bindir}/krunfw_measurement
%endif

%post -n %{name}3 -p /sbin/ldconfig

%postun -n %{name}3 -p /sbin/ldconfig

%files -n %{name}3
%{_libdir}/libkrunfw.so.3
%{_libdir}/libkrunfw.so.%{version}

%files devel
%{_libdir}/libkrunfw.so

%if %{sev}
%files sev3
%{_libdir}/libkrunfw-sev.so.3
%{_libdir}/libkrunfw-sev.so.%{version}
%{_bindir}/krunfw_measurement

%files sev-devel
%{_libdir}/libkrunfw-sev.so

%post sev3 -p /sbin/ldconfig

%postun sev3 -p /sbin/ldconfig

%endif

%changelog
