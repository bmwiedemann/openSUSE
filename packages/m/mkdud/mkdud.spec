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
%if 0%?suse_version >= 1500 || 0%?sle_version >= 120400
BuildRequires:  rubygem(asciidoctor)
%else
BuildRequires:  asciidoc
%if 0%?suse_version >= 1310 || 0%?sle_version >= 120000
BuildRequires:  libxslt-tools
%endif
%endif
Requires:       gpg2
Summary:        Create driver update from rpms
License:        GPL-3.0-or-later
Group:          Hardware/Other
Version:        1.49
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
  %make_install
  install -D -m 644 mkdud.1 %{buildroot}%{_mandir}/man1/mkdud.1

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
/usr/bin/mkdud
/usr/share/bash-completion
%doc %{_mandir}/man1/mkdud.*
%doc *.md
%if %suse_version >= 1500
%license COPYING
%else
%doc COPYING
%endif

%changelog
