#
# spec file for package gti
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

# norootforbuild

Name:           gti
Version:	1.6.1
Release:	0
License:	MIT
Summary:	ASCII art punishmet for misspelling git
Url:		http://r-wos.org/hacks/gti
Group:		Amusements/Toys/Other
Source:         https://github.com/rwos/gti/archive/v1.6.1.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:	gcc
Recommends:      git-core
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Program which will show you ASCII art car driving across the terminal when you
misspell git command. After animation it will perform git command as well.
Similar to sl (steam locomotive).

%prep
%setup -q

%build

make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
mkdir -p %buildroot/usr/bin
%makeinstall PREFIX=%buildroot/usr/bin

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%files
%defattr(-,root,root)
%doc README.md 
%{_bindir}/gti
%{_mandir}/man*/*

%changelog

