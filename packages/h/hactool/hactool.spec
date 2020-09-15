#
# spec file for package hactool
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


Name:           hactool
Version:        1.4.0
Release:        0
Summary:        Tool to view/extract information about Nintendo Switch Archives
License:        ISC
Group:          Hardware/Other
URL:            https://github.com/SciresM/hactool
Source:         https://github.com/SciresM/hactool/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
hactool is a tool to view information about, decrypt, and extract
common file formats for the Nintendo Switch, especially Nintendo
Content Archives.

%prep
%setup -q
mv config.mk.template config.mk

%build
make %{?_smp_mflags}

%install
install -D -m0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}

%changelog
