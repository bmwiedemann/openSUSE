#
# spec file for package xfdashboard
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%define so_ver 0
Name:           xfdashboard
Version:        1.1.0
Release:        0
Summary:        GNOME shell like dashboard for Xfce
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/apps/xfdashboard/start
Source0:        https://archive.xfce.org/src/apps/%{name}/1.1/%{name}-%{version}.tar.xz
Source8:        xfdashboard.1
Source9:        xfdashboard-settings.1
Source10:       xfdashboard-rpmlintrc

# WARNING! Please don't add OnlyShowIn key to the desktop file
# to save possibility to be run from under different desktop environments.

# PATCH-FIX-OPENSUSE gh#gmc-holle/xfdashboard#70 xfdashboard-desktop-category.diff dap.darkness@gmail.com -- fixes not-sufficient desktop file category.
Patch0:         xfdashboard-desktop-category.diff

# PATCH-FIX-OPENSUSE xfdashboard-desktopfile-without-binary.diff dap.darkness@gmail.com -- fixes "W: desktopfile-without-binary".
Patch2:         xfdashboard-desktopfile-without-binary.diff

# PATCH-FIX-OPENSUSE xfdashboard-relax-some-package-versions.diff manfred.h@gmx.net -- live with some older packages in Leap 15.6
Patch3:         xfdashboard-relax-some-package-versions.diff

BuildRequires:  appstream-glib
BuildRequires:  clutter-devel
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  meson >= 0.54.0
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(clutter-1.0) >= 1.24.0
BuildRequires:  pkgconfig(clutter-cogl-1.0) >= 1.24.0
BuildRequires:  pkgconfig(clutter-gdk-1.0) >= 1.24.0
BuildRequires:  pkgconfig(cogl-1.0) >= 1.18.0
BuildRequires:  pkgconfig(garcon-1) >= 4.16.0
BuildRequires:  pkgconfig(libwnck-3.0) >= 3.0
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.16.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.16.0
BuildRequires:  pkgconfig(libxfconf-0) >= 4.16.0
BuildRequires:  pkgconfig(x11) >= 1.6.7
BuildRequires:  pkgconfig(xcomposite) >= 0.2
BuildRequires:  pkgconfig(xdamage) >= 1.1.4
BuildRequires:  pkgconfig(xinerama) >= 1.1.3
Requires:       libcanberra-gtk-module-common
Recommends:     %{name}-lang
Recommends:     %{name}-themes

%description
Xfdashboard provides a GNOME shell dashboard like interface for use with Xfce
desktop. It can be configured to run to any keyboard shortcut and when executed
provides an overview of applications currently open enabling the user to switch
between different applications. The search feature works like Xfce's app finder
which makes it convenient to search for and start applications.

%lang_package

%package devel
Summary:        Xfdashboard Development Files
Group:          Development/Libraries/Other
Requires:       libxfdashboard%{so_ver} = %{version}

%description devel
This package provides files required for development for Xfdashboard.

%package themes
Summary:        Themes for Xfdashboard
Group:          System/GUI/XFCE
Requires:       %{name}
BuildArch:      noarch

%description themes
Additional themes for use with Xfdashboard.

%package -n libxfdashboard%{so_ver}
Summary:        Xfdashboard library
Group:          System/GUI/XFCE

%description -n libxfdashboard%{so_ver}
A library providing authenticators for Xfdashboard.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} > 0 && 0%{?suse_version} < 1600
# Need to explicitly link with the match library
export CFLAGS="%{optflags} -lm"
%else
export CFLAGS="%{optflags}"
%endif
%meson
%meson_build

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_mandir}/man1
gzip -c9 %{SOURCE8} >> %{buildroot}%{_mandir}/man1/%{name}.1.gz
gzip -c9 %{SOURCE9} >> %{buildroot}%{_mandir}/man1/%{name}-settings.1.gz
%fdupes -s %{buildroot}%{_datadir}/themes/%{name}-*
%find_lang %{name} %{?no_lang_C}

appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/*.metainfo.xml

%post -n libxfdashboard%{so_ver} -p /sbin/ldconfig
%postun -n libxfdashboard%{so_ver} -p /sbin/ldconfig

%files
%doc AUTHORS README.md
%license COPYING
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*.1.gz
%{_datadir}/%{name}
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/org.xfce.%{name}.metainfo.xml
%{_datadir}/applications/org.xfce.%{name}.desktop
%{_datadir}/applications/org.xfce.%{name}-settings.desktop
%{_sysconfdir}/xdg/autostart/org.xfce.%{name}-autostart.desktop
%{_datadir}/icons/hicolor/*/apps/org.xfce.xfdashboard.*
%{_datadir}/themes/%{name}
%{_libdir}/%{name}

%files lang -f %{name}.lang

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/libxfdashboard.pc

%files themes
%{_datadir}/themes/%{name}-*

%files -n libxfdashboard%{so_ver}
%{_libdir}/lib%{name}.so.*

%changelog
