#
# spec file for package libkrun
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


%define sev 1

%define descr \
libkrun is a dynamic library that allows programs to easily acquire the\
ability to run processes in a partially isolated environment using KVM Virtualization.\
It integrates a VMM (Virtual Machine Monitor, the userspace side of an Hypervisor) with\
the minimum amount of emulated devices required to its purpose, abstracting most of the\
complexity that comes from Virtual Machine management, offering users a simple C API.

# However sev has been defined, reset it if we're not on x86
%ifnarch x86_64
%define sev 0
%endif

%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
Name:           libkrun
Version:        1.4.8
Release:        0
Summary:        A dynamic library providing KVM-based process isolation capabilities
License:        Apache-2.0
URL:            https://github.com/containers/libkrun
Source0:        libkrun-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config
Patch1:         new-kvm-ioctl.patch
ExclusiveArch:  x86_64 aarch64
BuildRequires:  cargo >= 1.43.0
BuildRequires:  gcc
BuildRequires:  glibc-static
BuildRequires:  libkrunfw-devel >= 3.6.3
BuildRequires:  libopenssl-devel
BuildRequires:  patchelf
BuildRequires:  rust
%if %{sev}
BuildRequires:  libkrunfw-sev-devel >= 3.6.3
%endif
%ifarch aarch64
BuildRequires:  libfdt-devel >= 1.6.0
%endif
# For handling the transition from (very) old versions of the packages
Conflicts:      libkrun-devel <= 0.1.7
Conflicts:      libkrun0 <= 0.1.7

%description
%{summary}

%package -n %{name}1
Summary:        A dynamic library providing KVM-based process isolation capabilities
Obsoletes:      libkrun <= 1.4.1

%description -n %{name}1
%{descr}

%package devel
Summary:        Header files and libraries for libkrun development
Requires:       %{name}1 = %{version}-%{release}

%description devel
%{descr}

This package containes the libraries and headers needed to develop programs
that use libkrun Virtualization-based process isolation capabilities.

%if %{sev}
%package sev1
Summary:        Dynamic library providing Virtualization-based process isolation capabilities (SEV variant)
Obsoletes:      libkrun <= 1.4.1

%description sev1
%{descr}

This package contains the library that enables using AMD SEV to create a
microVM-based Trusted Execution Environment (TEE).

%package sev-devel
Summary:        Header files and libraries for libkrun development
Requires:       %{name}-devel = %{version}-%{release}
Requires:       %{name}-sev1 = %{version}-%{release}
Provides:       %{name}:%{_libdir}/libkrun-sev.so
Obsoletes:      %{name} < %{version}

%description sev-devel
%{descr}

This package containes the libraries and headers needed to develop programs that
use libkrun-sev Virtualization-based process isolation capabilities.
%endif

%prep
%autosetup -p1 -a1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
export RUSTFLAGS=%{rustflags}

%make_build

%if %{sev}
%make_build SEV=1
%endif

%install
export RUSTFLAGS=%{rustflags}

%make_install PREFIX=%{_prefix}

%if %{sev}
%make_install SEV=1 PREFIX=%{_prefix}
%endif

%files -n %{name}1
%license LICENSE
%doc README.md
%{_libdir}/libkrun.so.%{version}
%{_libdir}/libkrun.so.1

%files devel
%{_libdir}/libkrun.so
%{_includedir}/libkrun.h

%post -n %{name}1 -p /sbin/ldconfig

%postun -n %{name}1 -p /sbin/ldconfig

%if %{sev}
%files sev1
%license LICENSE
%doc README.md
%{_libdir}/libkrun-sev.so.%{version}
%{_libdir}/libkrun-sev.so.1

%files sev-devel
%{_libdir}/libkrun-sev.so

%post sev1 -p /sbin/ldconfig

%postun sev1 -p /sbin/ldconfig
%endif

%if %{with check}
%check
%cargo_test
%endif

%changelog
