#
# spec file for package cuishark
#
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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


Name:           cuishark
Version:        0.1.2
Release:        0
Summary:        A protocol analyzer like a wireshark on CUI
License:        MIT
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/slankdev/cuishark
Source:         https://github.com/slankdev/cuishark/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- Fix build on 32bit platform
Patch0:         cuishark-0.1.2-fix-32bit-build.patch
BuildRequires:  gcc-c++
BuildRequires:  libpcap-devel
BuildRequires:  ncurses-devel

%description
A console based wireshark like protocol analyzer.
It is using libwireshark for the protocol dissection.

%prep
%setup -q
%patch0 -p1

%build
make %{?_smp_mflags}

%install
install -D -m 0755 cuishark %{buildroot}/%{_bindir}/cuishark

%files
%doc README.md
%license LICENSE
%{_bindir}/cuishark

%changelog
