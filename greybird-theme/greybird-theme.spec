#
# spec file for package greybird-theme
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


%define _name Greybird

Name:           greybird-theme
Version:        3.22.10~git3.c0b8881
Release:        0
Url:            https://github.com/shimmerproject/Greybird
Summary:        A grey theme for GNOME, XFCE, GTK+ 2 and 3
License:        GPL-2.0-or-later OR CC-BY-SA-3.0
Group:          System/GUI/GNOME
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  gdk-pixbuf-loader-rsvg
BuildRequires:  glib2-devel
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
The Greybird Theme for GTK2/3 and xfwm4/emerald/metacity started out on the
basis of Bluebird, but aims at reworking the intense blue tone to a more
neutral grey-ish look.

This package provides the GTK+ 2 support of Greybird.

%package -n gtk3-metatheme-greybird
Summary:        GTK+ 3 support for the Greybird theme
Group:          System/GUI/GNOME
Requires:       metatheme-greybird-common = %{version}
Supplements:    packageand(metatheme-greybird-common:gtk3)

%description -n gtk3-metatheme-greybird
The Greybird Theme for GTK2/3 and xfwm4/emerald/metacity started out on the
basis of Bluebird, but aims at reworking the intense blue tone to a more
neutral grey-ish look.

This package provides the GTK+ 3 support of Greybird.

%prep
%autosetup

%build
./autogen.sh
%configure
%make_build

%install
%make_install
# remove stuff that's unlikely to be used
rm -r %{buildroot}%{_datadir}/themes/%{_name}/unity
rm -r %{buildroot}%{_datadir}/themes/%{_name}/plank
rm    %{buildroot}%{_datadir}/themes/%{_name}/ubiquity-panel-bg.png
# the convulted fdupes call is necessary, else a gtk-2.0 icon will be linked to gtk-3.0
# which will not work if only one subpackage is installed.
%fdupes -s %{buildroot}/%{_datadir}/themes/%{_name}*/{[^g]*,gtk-3.0}

%files -n metatheme-greybird-common
%doc README.md 
%license LICENSE.CC LICENSE.GPL
%dir %{_datadir}/themes/%{_name}/
%{_datadir}/themes/%{_name}/metacity-1
%{_datadir}/themes/%{_name}/xfce-notify-4.0
%{_datadir}/themes/%{_name}/xfwm4
%{_datadir}/themes/%{_name}/Greybird.emerald
%{_datadir}/themes/%{_name}/index.theme
%dir %{_datadir}/themes/%{_name}-accessibility
%{_datadir}/themes/%{_name}-accessibility/xfwm4
%dir %{_datadir}/themes/%{_name}-compact
%{_datadir}/themes/%{_name}-compact/xfwm4
%dir %{_datadir}/themes/%{_name}-bright
%{_datadir}/themes/%{_name}-bright/xfce-notify-4.0
%dir %{_datadir}/themes/%{_name}/gnome-shell
%{_datadir}/themes/%{_name}/gnome-shell/gnome-shell.css

%files -n gtk2-metatheme-greybird
%{_datadir}/themes/%{_name}/gtk-2.0

%if 0%{?suse_version} >= 1210
%files -n gtk3-metatheme-greybird
%{_datadir}/themes/%{_name}/gtk-3.0
%endif

%changelog
