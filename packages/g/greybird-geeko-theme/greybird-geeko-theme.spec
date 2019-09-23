#
# spec file for package greybird-geeko-theme
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define name_light Greybird-Geeko-Light
%define name_dark Greybird-Geeko-Dark

Name:           greybird-geeko-theme
Version:        3.22.10.1+git39.ffde076
Release:        0
Url:            https://github.com/shimmerproject/Greybird-Geeko
Summary:        A grey theme for GNOME, XFCE, GTK+ 2 and 3
License:        GPL-2.0-or-later OR CC-BY-SA-3.0 AND GPL-3.0-or-later
Group:          System/GUI/GNOME
Source:         %{name}-%{version}.tar.xz
BuildRequires:  fdupes
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  gdk-pixbuf-loader-rsvg
BuildRequires:  glib2-devel
BuildRequires:  meson
BuildRequires:  sassc
BuildArch:      noarch

%description
This theme for GTK2/3 and xfwm4/emerald/metacity is a 
fork of Greybird with openSUSE branding elements added.


%package -n metatheme-greybird-geeko-common
Summary:        Common files for the Greybird theme
Group:          System/GUI/GNOME
Suggests:       gtk2-metatheme-greybird-geeko
Suggests:       gtk3-metatheme-greybird-geeko

%description -n metatheme-greybird-geeko-common
The Greybird theme for GTK2/3 and xfwm4/emerald/metacity started out on the
basis of Bluebird, but aims at reworking the intense blue tone to a more
neutral grey-ish look.

This package provides the files common to the GTK+ themes and the window
manager themes as well as background images.

%package -n gtk2-metatheme-greybird-geeko
Summary:        GTK+ 2 support for the Greybird theme
Group:          System/GUI/GNOME
Requires:       gtk2-engine-murrine
Requires:       metatheme-greybird-geeko-common = %{version}
Supplements:    packageand(metatheme-greybird-geeko-common:gtk2)

%description -n gtk2-metatheme-greybird-geeko
The Greybird Theme for GTK2/3 and xfwm4/emerald/metacity started out on the
basis of Bluebird, but aims at reworking the intense blue tone to a more
neutral grey-ish look.

This package provides the GTK+ 2 support of Greybird.

%package -n gtk3-metatheme-greybird-geeko
Summary:        GTK+ 3 support for the Greybird theme
Group:          System/GUI/GNOME
Requires:       metatheme-greybird-geeko-common = %{version}
Supplements:    packageand(metatheme-greybird-geeko-common:gtk3)

%description -n gtk3-metatheme-greybird-geeko
The Greybird Theme for GTK2/3 and xfwm4/emerald/metacity started out on the
basis of Bluebird, but aims at reworking the intense blue tone to a more
neutral grey-ish look.

This package provides the GTK+ 3 support of Greybird.

%prep
%autosetup

%build
%meson
%meson_build

%install
%meson_install

# the convulted fdupes call is necessary, else a gtk-2.0 icon will be linked to gtk-3.0
# which will not work if only one subpackage is installed.
%fdupes -s %{buildroot}/%{_datadir}/themes/{%{name_light},%{name_dark}}*/{[^g]*,gtk-3.0}

%fdupes -s %{buildroot}/%{_datadir}/themes/{%{name_light},%{name_dark}}/gtk-2.0/*

%files -n metatheme-greybird-geeko-common
%doc README.md 
%license LICENSE.CC LICENSE.GPL
%dir %{_datadir}/themes/{%{name_light},%{name_dark}}
%{_datadir}/themes/{%{name_light},%{name_dark}}/{%{name_light},%{name_dark}}.emerald
%{_datadir}/themes/{%{name_light},%{name_dark}}/metacity-1
%{_datadir}/themes/{%{name_light},%{name_dark}}/xfce-notify-4.0
%{_datadir}/themes/{%{name_light},%{name_dark}}/xfwm4
%{_datadir}/themes/{%{name_light},%{name_dark}}/index.theme
%dir %{_datadir}/themes/{%{name_light},%{name_dark}}-{Accessibility,Compact}
%{_datadir}/themes/{%{name_light},%{name_dark}}-{Accessibility,Compact}/*
%dir %{_datadir}/themes/{%{name_light},%{name_dark}}/gnome-shell
%{_datadir}/themes/{%{name_light},%{name_dark}}/gnome-shell/*

%files -n gtk2-metatheme-greybird-geeko
%{_datadir}/themes/{%{name_light},%{name_dark}}/gtk-2.0

%if 0%{?suse_version} >= 1210
%files -n gtk3-metatheme-greybird-geeko
%{_datadir}/themes/{%{name_light},%{name_dark}}/gtk-3.0
%endif

%changelog
