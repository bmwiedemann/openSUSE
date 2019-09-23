#
# spec file for package mkdud
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


Name:           mkdud
BuildRequires:  xz
Requires:       gpg2
Summary:        Create driver update from rpms
License:        GPL-3.0+
Group:          Hardware/Other
Version:        1.45
Release:        0
Source:         %{name}-%{version}.tar.xz
Url:            https://github.com/openSUSE/mkdud
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Create a driver update from rpms.

Authors:
--------
    Steffen Winterfeldt

%prep
%setup

%build

%install
  make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/bin/mkdud
/usr/share/bash-completion
%doc README.md COPYING

%changelog
