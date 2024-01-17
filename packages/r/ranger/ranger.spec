#
# spec file for package ranger
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


%define short_version 1.9.3

Name:           ranger
Version:        1.9.3+git20230416.478d5b6
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
BuildRequires:  python3-setuptools
BuildRequires:  update-desktop-files
Requires:       file
Requires:       python3-curses
Recommends:     atool
Recommends:     highlight
Recommends:     mediainfo
Recommends:     python3-Pillow
Recommends:     w3m
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

mv "%{buildroot}%{_datadir}/doc/ranger" _doc
find _doc -type f -exec chmod -x '{}' +

%if 0%{?suse_version} < 1500
%post
%desktop_database_post

%postun
%desktop_database_postun
%endif

%files
%license LICENSE
%doc _doc/*
%{_bindir}/ranger
%{_bindir}/rifle
%{python3_sitelib}/ranger_fm-%{short_version}-*.egg-info
%{python3_sitelib}/ranger
%{_mandir}/man1/ranger.1%{ext_man}
%{_mandir}/man1/rifle.1%{ext_man}
%{_datadir}/applications/%{name}.desktop

%changelog
