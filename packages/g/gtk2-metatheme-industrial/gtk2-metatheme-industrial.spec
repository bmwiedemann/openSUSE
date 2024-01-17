#
# spec file for package gtk2-metatheme-industrial
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


%define _name metatheme-industrial
Name:           gtk2-metatheme-industrial
Version:        0.6.5
Release:        0
Summary:        Industrial Metatheme for GNOME
License:        GPL-2.0-only
Group:          System/GUI/GNOME
Source:         %{_name}-%{version}.tar.bz2
BuildRequires:  automake
BuildRequires:  gtk2-devel
BuildRequires:  gtk2-engines-devel
BuildRequires:  intltool
# For Industrial engine and theme:
Requires:       gtk2-engine-industrial
# For Gilouche icon theme:
Requires:       gtk2-metatheme-gilouche
Requires:       gtk2-theme-industrial
Enhances:       gtk2
Enhances:       metacity
Supplements:    gtk2-engine-industrial
Supplements:    gtk2-theme-industrial
# Industrial metatheme was a part of gnome-themes in openSUSE < 11.0
Conflicts:      gnome-themes < 2.22.0-28
# for openSUSE <= 10.3 SLE <= 10
Provides:       gnome-themes:%{_datadir}/themes/Industrial/index.theme
BuildArch:      noarch

%description
Metatheme for GNOME: Industrial strength WM theme for Metacity and
Industrial icon theme for GNOME.

%prep
%setup -q -n %{_name}-%{version}

%build
autoreconf -f -i
%configure
make %{?_smp_mflags}

%install
%make_install
#find_lang %{_name}

%files
# AUTHORS NEWS README are empty
%license COPYING
%doc ChangeLog
%{_datadir}/themes/*

%changelog
