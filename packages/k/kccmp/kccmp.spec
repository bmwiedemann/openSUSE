#
# spec file for package kccmp
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

Name:           kccmp
Version:        1.0.0
Release:        0
Summary:        Tool for kernel configurations comparison
License:        GPL-2.0-only
Group:          Productivity/Text/Utilities
URL:            https://github.com/hanzyd/kccmp
Source0:        kccmp-%{version}.tar.xz
BuildRequires:  gcc-c++

%description
kccmp is a simple tool for comparing two linux kernel ".config" files.

%prep
%setup -q

%build
make

%install
install -D -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%defattr(-,root,root)
%license LICENSE.GPL
%doc README
%{_bindir}/%{name}

%changelog
