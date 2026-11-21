#
# spec file for package krohnkite
#
# Copyright (c) 2026 SUSE LLC and contributors
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

%define plasma6_version 6.0.0

Name:           krohnkite
Version:        0.9.10.0
Release:        0
Summary:        A dynamic tiling extension for KWin 6
License:        MIT
Url:            https://codeberg.org/anametologin/Krohnkite
Source:         %{name}-%{version}.tar.gz
BuildRequires:  typescript >= 3.1
BuildRequires:  p7zip-full
BuildRequires:  cmake(Plasma) >= %{plasma6_version}
BuildArch:      noarch

%description
Kröhnkite is mainly inspired by dwm from suckless folks, and aims to provide 
rock solid stability while fully integrating into KWin.

%prep
%autosetup
sed -i 's/PROJECT_REV  =.*/PROJECT_REV  = %{version}/' Makefile
sed -i '/npm install --save-dev/d' Makefile
sed -i 's/npm run tsc --/tsc/' Makefile
sed -i 's|#!/usr/bin/env python3|#!/usr/bin/python3|' tools/install-icons.py

%build
make package
make pkg/metadata.json

%install
mkdir -p %{buildroot}%{_datadir}/kwin/scripts/%{name}
cp -ra pkg/* %{buildroot}%{_datadir}/kwin/scripts/%{name}/

%check
test -d pkg

%files
%license LICENSE
%doc README.md
%{_datadir}/kwin/scripts/%{name}
%dir %{_datadir}/kwin
%dir %{_datadir}/kwin/scripts

%changelog

