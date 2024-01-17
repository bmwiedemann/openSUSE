#
# spec file for package greybird-theme
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


%define _name Greybird

Name:           greybird-theme
Version:        3.23.2+git0.25f312f
Release:        0
URL:            https://github.com/shimmerproject/Greybird
Summary:        A grey theme for GNOME, XFCE, GTK+ 2 and 3
License:        CC-BY-SA-3.0 OR GPL-2.0-or-later
Group:          System/GUI/GNOME
Source:         %{_name}-%{version}.tar.xz
# PATCH-FIX-OPENSUSE link-selected-is-optional.patch manfred.h@gmx.net -- work around too old gtk4 libs on Leap 15.4 and 15.5
Patch0:         link-selected-is-optional.patch
BuildRequires:  fdupes
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  gdk-pixbuf-loader-rsvg
BuildRequires:  glib2-devel
BuildRequires:  meson
BuildRequires:  sassc
BuildArch:      noarch

%description
This theme for GTK2/3 and xfwm4/emerald/metacity started out on the basis of
Bluebird, but aims at reworking the intense blue tone to a more neutral
grey-ish look.

%package -n metatheme-greybird-common
Summary:        Common files for the Greybird theme
Group:          System/GUI/GNOME
Suggests:       gtk2-metatheme-greybird
Suggests:       gtk3-metatheme-greybird

%description -n metatheme-greybird-common
The Greybird theme for GTK2/3 and xfwm4/emerald/metacity started out on the
basis of Bluebird, but aims at reworking the intense blue tone to a more
neutral grey-ish look.

This package provides the files common to the GTK+ themes and the window
manager themes as well as background images.

%package -n gtk2-metatheme-greybird
Summary:        GTK+ 2 support for the Greybird theme
Group:          System/GUI/GNOME
Requires:       gtk2-engine-murrine
Requires:       metatheme-greybird-common = %{version}
Supplements:    packageand(metatheme-greybird-common:gtk2)

%description -n gtk2-metatheme-greybird
This package provides the GTK+ 2 support of Greybird.

%package -n gtk3-metatheme-greybird
Summary:        GTK+ 3 support for the Greybird theme
Group:          System/GUI/GNOME
Requires:       metatheme-greybird-common = %{version}
Supplements:    packageand(metatheme-greybird-common:gtk3)

%description -n gtk3-metatheme-greybird
This package provides the GTK+ 3 support of Greybird.

%package -n gtk4-metatheme-greybird
Summary:        GTK+ 3 support for the Greybird theme
Group:          System/GUI/GNOME
Requires:       metatheme-greybird-common = %{version}
Supplements:    packageand(metatheme-greybird-common:gtk3)

%description -n gtk4-metatheme-greybird
This package provides the GTK+ 4 support of Greybird

%prep
%setup -q -n %{_name}-%{version}
%if 0%{?sle_version} >= 150400 && 0%{?is_opensuse}
%patch0 -p1
%endif

%build
%meson
%meson_build

%install
%meson_install
# remove stuff that's unlikely to be used
rm -r %{buildroot}%{_datadir}/themes/%{_name}{,-dark}/unity
rm -r %{buildroot}%{_datadir}/themes/%{_name}{,-dark}/plank

# the convulted fdupes call is necessary, else a gtk-2.0 icon will be linked to gtk-3.0
# which will not work if only one subpackage is installed.
%fdupes -s %{buildroot}/%{_datadir}/themes/%{_name}*/{[^g]*,gtk-3.0}
%fdupes -s %{buildroot}/%{_datadir}/themes/%{_name}*/gtk-2.0/*

%files -n metatheme-greybird-common
%doc README.md
%license LICENSE.CC LICENSE.GPL
%dir %{_datadir}/themes/%{_name}{,-dark}/
%{_datadir}/themes/%{_name}{,-dark}/metacity-1
%{_datadir}/themes/%{_name}/xfce-notify-4.0
%{_datadir}/themes/%{_name}{,-dark}/xfwm4
%{_datadir}/themes/%{_name}{,-dark}/*.emerald
%{_datadir}/themes/%{_name}{,-dark}/index.theme
%dir %{_datadir}/themes/%{_name}{,-dark}-accessibility
%{_datadir}/themes/%{_name}{,-dark}-accessibility/xfwm4
%dir %{_datadir}/themes/%{_name}-compact
%{_datadir}/themes/%{_name}-compact/xfwm4
%dir %{_datadir}/themes/%{_name}-bright
%{_datadir}/themes/%{_name}-bright/xfce-notify-4.0
%dir %{_datadir}/themes/%{_name}{,-dark}/gnome-shell
%{_datadir}/themes/%{_name}{,-dark}/gnome-shell/gnome-shell.css
%dir %{_datadir}/themes/%{_name}{,-dark}/openbox-3
%{_datadir}/themes/%{_name}{,-dark}/openbox-3/*

%files -n gtk2-metatheme-greybird
%{_datadir}/themes/%{_name}{,-dark}/gtk-2.0

%if 0%{?suse_version} >= 1210
%files -n gtk3-metatheme-greybird
%{_datadir}/themes/%{_name}{,-dark}/gtk-3.0
%endif

%files -n gtk4-metatheme-greybird
%{_datadir}/themes/%{_name}{,-dark}/gtk-4.0

%changelog
