#
# spec file for package xfdashboard
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


%define so_ver 0

Name:           xfdashboard
Version:        0.7.8
Release:        0
Summary:        GNOME shell like dashboard for Xfce
License:        GPL-2.0-or-later
Group:          System/GUI/XFCE
URL:            https://docs.xfce.org/apps/xfdashboard/start
Source0:        https://archive.xfce.org/src/apps/%{name}/0.7/%{name}-%{version}.tar.bz2
Source8:        xfdashboard.1
Source9:        xfdashboard-settings.1

# WARNING! Please don't add OnlyShowIn key to the desktop file
# to save possibility to be run from under different desktop environments.

# PATCH-FIX-OPENSUSE gh#gmc-holle/xfdashboard#70 xfdashboard-desktop-category.diff dap.darkness@gmail.com -- fixes not-sufficient desktop file category.
Patch0:         xfdashboard-desktop-category.diff

# PATCH-FIX-OPENSUSE xfdashboard-desktopfile-without-binary.diff dap.darkness@gmail.com -- fixes "W: desktopfile-without-binary".
Patch2:         xfdashboard-desktopfile-without-binary.diff

BuildRequires:  clutter-devel
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  libxfce4util-devel >= 4.12.0
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(garcon-1)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.12.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.12.0
BuildRequires:  pkgconfig(libxfconf-0)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xinerama)
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
%setup -q
%patch0 -p1
%patch2 -p1

%build
export CFLAGS="%{optflags}"
%configure
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_mandir}/man1
gzip -c9 %{SOURCE8} | tee -a %{buildroot}%{_mandir}/man1/%{name}.1.gz
gzip -c9 %{SOURCE9} | tee -a %{buildroot}%{_mandir}/man1/%{name}-settings.1.gz
%fdupes -s %{buildroot}%{_datadir}/themes/%{name}-*
%find_lang %{name} %{?no_lang_C}

%post -n libxfdashboard%{so_ver} -p /sbin/ldconfig
%postun -n libxfdashboard%{so_ver} -p /sbin/ldconfig

%files
%doc AUTHORS README.md
%license COPYING
%{_bindir}/%{name}*
%{_mandir}/man1/%{name}*.1.gz
%{_datadir}/%{name}
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}-settings.desktop
%{_sysconfdir}/xdg/autostart/%{name}-autostart.desktop
%{_datadir}/icons/hicolor/*/*/%{name}.png
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
