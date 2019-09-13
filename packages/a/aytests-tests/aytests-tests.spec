#
# spec file for package aytests-tests
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           aytests-tests
Version:        1.2.40
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        aytests-tests-%{version}.tar.bz2

BuildArch:      noarch

Summary:        Integration tests for AutoYaST2
License:        GPL-3.0-only
Group:          System/YaST
Url:            https://github.com/yast/aytests-tests

# Depends on defining classes/rules in an own directory.
Recommends:     rubygem-aytests >= 1.0.53

%description
Profiles and test scripts for AutoYaST2 integration tests.
For internal testing purposes only! Not useful on a real system!

%prep
%setup -n %{name}-%{version}

%build

%install

# Installation files

install -d $RPM_BUILD_ROOT/var/lib/autoinstall
mv aytests $RPM_BUILD_ROOT/var/lib/autoinstall/

%files
%defattr(-,root,root)
%dir /var/lib/autoinstall
/var/lib/autoinstall/aytests
%attr(755, -, root) /var/lib/autoinstall/aytests/*.sh

%changelog
