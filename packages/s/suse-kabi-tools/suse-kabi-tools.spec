#
# spec file for package suse-kabi-tools
#
# Copyright (c) 2025 SUSE LLC
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


Name:           suse-kabi-tools
Version:        1.1.0+git0.3857c3a
Release:        0
Summary:        A set of ABI tools for the Linux kernel
Group:          System/Kernel
License:        GPL-2.0-or-later
URL:            https://github.com/SUSE/suse-kabi-tools
Source:         %{name}-%{version}.tar.zst
BuildRequires:  cargo >= 1.88
BuildRequires:  cargo-packaging

%description
suse-kabi-tools is a set of Application Binary Interface (ABI) tools for the
Linux kernel.

%prep
%autosetup -p1

%build
export SUSE_KABI_TOOLS_VERSION="%{version}"
%{cargo_build}

%install
export SUSE_KABI_TOOLS_VERSION="%{version}"
%{cargo_install}
install -D -m 0644 %{_builddir}/%{name}-%{version}/doc/ksymtypes.1 %{buildroot}%{_mandir}/man1/ksymtypes.1
install -D -m 0644 %{_builddir}/%{name}-%{version}/doc/ksymvers.1 %{buildroot}%{_mandir}/man1/ksymvers.1
install -D -m 0644 %{_builddir}/%{name}-%{version}/doc/suse-kabi-tools.5 %{buildroot}%{_mandir}/man5/suse-kabi-tools.5

%check
export SUSE_KABI_TOOLS_VERSION="%{version}"
%{cargo_test}

%files
%license COPYING
%{_bindir}/ksymtypes
%{_bindir}/ksymvers
%{_mandir}/man1/ksymtypes.1%{?ext_man}
%{_mandir}/man1/ksymvers.1%{?ext_man}
%{_mandir}/man5/suse-kabi-tools.5%{?ext_man}

%changelog

