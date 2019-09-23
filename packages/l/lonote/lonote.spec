#
# spec file for package lonote
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


Name:           lonote
Version:        3.2.13
Release:        0
Summary:        A personal note-taking application
License:        GPL-3.0 AND Apache-2.0
Group:          Productivity/Office/Organizers
Url:            https://bitbucket.org/civalin/lonote
Source0:        https://bitbucket.org/civalin/lonote/get/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python3-devel
BuildRequires:  update-desktop-files
Requires:       python3-dbm
Requires:       python3-xml
BuildArch:      noarch

%description
Lonote is a personal note-taking application based on python3
and modern browsers.
It features in well interact UI, minimal design, structural notes,
auto reloading, archiving and versioning.

%prep
%setup -q -c -T
tar xzf %{SOURCE0} --strip-components=1

sed -i "s|#!/usr/bin/python3||" lonotelib/diff_match_patch.py # Fix non-executable script
sed -i '/^#!\/usr\/bin\/env/d' lonotelib/bottle.py
chmod -x server/static/diff-match-patch/diff_match_patch.js \
         server/static/glyphicons/fonts/glyphiconshalflings-regular.svg

%build
python3 setup.py build

%install
python3 setup.py install --prefix=%{_prefix} --root=%{buildroot}
# Remove wrongly installed docs
rm -rf %{buildroot}%{_datadir}/doc/%{name}/
# Fix Categories in desktop file
sed -i "s/Development;//" %{buildroot}%{_datadir}/applications/%{name}.desktop
%suse_update_desktop_file %{name} Office ProjectManagement
# Fix locale
find %{buildroot}%{_datadir}/locale -type f -name "*.po" -delete
%find_lang %{name}
# Fix pixmaps
rm -rf %{buildroot}%{_datadir}/pixmaps/%{name}.ico
# Hidden file for dir
find %{buildroot} -type f -name "*.swp" -delete
find %{buildroot} -type f -name ".DS_Store" -delete
find %{buildroot} -type f -name ".hgempty" -delete

%fdupes %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README.rst doc/{Apache_License,CHANGELOG.rst,LICENSE.rst}
%{_bindir}/lonote
%{python3_sitelib}/*
%{_datadir}/applications/%{name}.desktop
%{_mandir}/man1/lonote.*
%{_datadir}/%{name}/
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.png

%changelog
