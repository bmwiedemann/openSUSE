#
# spec file for package slingshot
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           slingshot
Version:        0.9
Release:        0
Url:            https://github.com/ryanakca/slingshot
Summary:        A two dimensional, turn based simulation-strategy game
License:        GPL-2.0
Group:          Amusements/Games/Strategy/Turn Based
Source:         https://github.com/ryanakca/slingshot/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FEATURE-UPSTREAM https://github.com/ryanakca/slingshot/pull/4
Source3:        %{name}.appdata.xml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gnu-free-fonts
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-devel
BuildRequires:  update-desktop-files
Requires:       gnu-free-fonts
Requires:       python-pygame
%py_requires
BuildArch:      noarch

%description
Slingshot is a two dimensional, turn based simulation-strategy game
set in the gravity fields of several planets. It is never the same
from round to round due to its randomly generated playing fields.

%prep
%setup -q

%build
python setup.py build

%install
# use system fonts
rm -f slingshot/data/FreeSansBold.ttf
ln -sf %{_datadir}/fonts/truetype/FreeSansBold.ttf src/slingshot/data/FreeSansBold.ttf

python setup.py install --prefix=%{_prefix} --root=%{buildroot}

mv src/slingshot/data/icon64x64.png src/slingshot/data/slingshot.png
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/64x64/apps
install -p -m 644 src/slingshot/data/slingshot.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps

mkdir -p %{buildroot}%{_datadir}/applications
install -p -m 644 data/slingshot.desktop %{buildroot}%{_datadir}/applications

# https://en.opensuse.org/openSUSE:AppStore
mkdir -p %{buildroot}%{_datadir}/appdata
install -p -m 664 %{SOURCE3} %{buildroot}%{_datadir}/appdata

%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun

%files
%defattr(-,root,root)
%doc README LICENSE
%{_bindir}/%{name}
%{python_sitelib}/
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/slingshot.xpm
%{_datadir}/icons/hicolor/64x64/apps/%{name}.png
%{_datadir}/appdata/slingshot.appdata.xml

%changelog
