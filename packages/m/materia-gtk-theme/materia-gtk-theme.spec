#
# spec file for package materia-gtk-theme
#
# Copyright (c) 2020 SUSE LLC
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


%define         _name    materia-theme
Name:           materia-gtk-theme
Version:        20200320
Release:        0
Summary:        A Material Design theme for GNOME/GTK+ based desktop environments
License:        GPL-2.0-only
URL:            https://github.com/nana-4/materia-theme
Source:         https://github.com/nana-4/%{_name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  bc
BuildRequires:  fdupes
Requires:       gnome-themes-extras
Recommends:     gtk2-engine-murrine
BuildArch:      noarch

%description
Materia (formerly Flat-Plat) is a Material Design theme for GNOME/GTK+ based desktop environments.
It supports GTK+ 3, GTK+ 2, GNOME Shell, Budgie, Cinnamon, MATE, Unity, LightDM, GDM, Chrome theme, etc.

%prep
%autosetup -n %{_name}-%{version}

%build

%install
./install.sh --dest %{buildroot}%{_datadir}/themes

%fdupes %{buildroot}

#fix permissions
find %{buildroot}/%{_datadir}/themes -type f -exec chmod -x {} \;
#remove duplicate COPYING files
find %{buildroot}%{_datadir}/themes -name COPYING -delete

%files
%license COPYING
%doc README.md
%{_datadir}/themes/*

%changelog
