#
# spec file for package ranger
#
# Copyright (c) 2022 SUSE LLC
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

%define short_version 1.9.3

Name:           ranger
Version:        1.9.3+git20221124.f8b304f
Release:        0
Summary:        Console File Manager
License:        GPL-3.0-or-later
Group:          Productivity/File utilities
URL:            https://github.com/ranger/ranger
Source:         %{name}-%{version}.tar.gz
Source99:       ranger-rpmlintrc
# PATCH-FIX-UPSTREAM ranger.desktop.patch -- Add missing GenericName
Patch0:         ranger.desktop.diff
BuildRequires:  python3-devel
BuildRequires:	python3-setuptools
BuildRequires:  update-desktop-files
Requires:       file
Requires:       python3-curses
Recommends:     atool
Recommends:     highlight
Recommends:     mediainfo
Recommends:     w3m
Recommends:     python3-Pillow
BuildArch:      noarch

%description
Ranger is a console file manager that gives you greater flexibility and a
good overview of your files without having to leave your text console. It
visualizes the directory tree in two dimensions: the directory hierarchy on
one, lists of files on the other, with a preview to the right.

The default keys are similar to those of Vim, Emacs and Midnight Commander,
though ranger is easily controllable with just the arrow keys or the mouse.

%prep
%setup -q
%patch0 -p1
sed -e 's|#!/usr/bin/env python|#!%{_bindir}/python3|' -i doc/tools/*.py
sed -e 's|#!/usr/bin/env bash|#!/bin/bash|' -i ranger/data/scope.sh

%build
python3 ./setup.py build

%install
python3 ./setup.py install \
  --prefix="%{_prefix}" \
  --root=%{buildroot}

rm -rf "%{buildroot}%{_datadir}/doc/ranger"

%if 0%{?suse_version} < 1500
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%license LICENSE
%doc AUTHORS CHANGELOG.md README.md HACKING.md
%doc doc/colorschemes.md
%doc doc/tools
%doc examples
%{_bindir}/ranger
%{_bindir}/rifle
%{python3_sitelib}/ranger_fm-%{short_version}-*.egg-info
%{python3_sitelib}/ranger
%{_mandir}/man1/ranger.1%{ext_man}
%{_mandir}/man1/rifle.1%{ext_man}
%{_datadir}/applications/%{name}.desktop

%changelog
