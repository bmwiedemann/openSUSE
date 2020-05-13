#
# spec file for package scat
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


Name:           scat
Version:        0.0.1
Release:        0
Url:            https://github.com/asdil12/scat
Summary:        Syntax highlight for terminal 
License:        GPL-3.0-only
Group:          Productivity/Text/Utilities
Source:         https://github.com/asdil12/scat/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       python3-Pygments
BuildArch:      noarch

%description
Cat-like tool with syntax highlighting for terminals.

%prep
%setup -q -n scat-%{version}

%build

%install
install -Dm755 scat %{buildroot}/%{_prefix}/bin/scat 

%files
%defattr(-,root,root,-)
%doc README.md
%license LICENSE
/usr/bin/scat

%changelog
