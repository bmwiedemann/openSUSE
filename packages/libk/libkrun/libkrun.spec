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


%global rustflags '-Clink-arg=-Wl,-z,relro,-z,now'
Name:           libkrun
Version:        0.1.8
Release:        0
Summary:        A dynamic library providing KVM-based process isolation capabilities
License:        Apache-2.0
URL:            https://github.com/containers/libkrun
Source0:        libkrun-%{version}.tar.gz
Source1:        vendor.tar.zst
Source2:        cargo_config
ExclusiveArch:  x86_64 aarch64
BuildRequires:  cargo >= 1.43.0
BuildRequires:  gcc
BuildRequires:  glibc-static
BuildRequires:  libkrunfw >= 0.6
BuildRequires:  rust
Requires:       libkrunfw >= 0.6
%ifarch aarch64
BuildRequires:  libfdt-devel >= 1.6.0
%endif
Conflicts:      libkrun-devel <= 0.1.7
Conflicts:      libkrun0 <= 0.1.7

%description
libkrun is a dynamic library that allows programs to easily acquire the ability to run processes in a partially isolated environment using KVM Virtualization.

It integrates a VMM (Virtual Machine Monitor, the userspace side of an Hypervisor) with the minimum amount of emulated devices required to its purpose, abstracting most of the complexity that comes from Virtual Machine management, offering users a simple C API.

%prep
%setup -qa1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
export RUSTFLAGS=%{rustflags}
%make_build

%install
export RUSTFLAGS=%{rustflags}
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_libdir}/libkrun.so
%{_includedir}/libkrun.h

%changelog
