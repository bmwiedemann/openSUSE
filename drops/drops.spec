#
# spec file for package opmsg
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define gittag rel-0.12s
Name:           drops
Version:        0.12s
Release:        0
Summary:        Peer to Peer networking implementation for opmsg
License:        GPL-3.0+
Group:          Productivity/Security
Url:            https://github.com/stealth/drops
Source0:        https://github.com/stealth/drops/archive/%{gittag}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(openssl)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
[dr]:ops -- dead drops for ops

A p2p transport network for opmsg end2end encrypted messages.


%prep
%setup -q -n %{name}-%{gittag}

%build
pushd src
make %{?_smp_mflags} INC="%optflags"

%install
pushd src
mkdir -p %{buildroot}/%{_bindir}
install dropsd %{buildroot}/%{_bindir}/

%files
%defattr(-,root,root)
%doc README.md src/GPL3
%{_bindir}/dropsd

%changelog
