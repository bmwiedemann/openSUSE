#
# spec file for package wardstone
#
# Copyright (c) 2024 SUSE LLC
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


Name:           wardstone
#               This will be set by osc services, that will run after this.
Version:        0.2.0~0
Release:        0
Summary:        Assess compliance for cryptographic keys
License:        ISC
#               Select a group from this link:
#               https://en.opensuse.org/openSUSE:Package_group_guidelines
Group:          Productivity/Security
URL:            https://github.com/openSUSE/wardstone
Source0:        %{name}-%{version}.tar.zst
Source1:        vendor.tar.zst
Source2:        cargo_config
BuildRequires:  cargo-packaging >= 1.2.0
BuildRequires:  openssl-devel

%description
The wardstone project aims to create a library that can be used across different programming languages via a foreign function interface and a command line utility that users can run against their existing keys to detect conformance to varying cryptographic key standards and research publications.

%package        devel
Summary:        FFI bindings for wardstone
Group:          Productivity/Security

%description    devel
A version of wardstone_core that exports a foreign function interface for using the library from C and other languages that support it.

%prep
%autosetup -a1
install -D -m 644 %{SOURCE2} .cargo/config

%build
%{cargo_build} --all

%install
# CLI program
%{cargo_install -p crates/cmd}

# FFI devel
install -D -d -m 0755 %{buildroot}%{_libdir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/libwardstone.so %{buildroot}%{_libdir}/libwardstone.so
install -D -d -m 0755 %{buildroot}%{_includedir}
install -m 0644 %{_builddir}/%{name}-%{version}/target/wardstone.h %{buildroot}%{_includedir}/wardstone.h

%check
%{cargo_test}

%files
%{_bindir}/%{name}

%files devel
%{_includedir}/wardstone.h
%{_libdir}/libwardstone.so

%changelog
