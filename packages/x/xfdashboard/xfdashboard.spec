#
# spec file for package xfdashboard
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define so_ver 0

Name:           xfdashboard
Version:        0.7.5
Release:        0
Summary:        GNOME shell like dashboard for Xfce
License:        GPL-2.0+
Group:          System/GUI/XFCE
Url:            http://xfdashboard.froevel.de
Source0:        http://archive.xfce.org/src/apps/xfdashboard/0.7/xfdashboard-%{version}.tar.bz2
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
BuildRequires:  libxfce4util-devel >= 4.10.0
BuildRequires:  xfce4-dev-tools
BuildRequires:  pkgconfig(garcon-1)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(libwnck-3.0)
BuildRequires:  pkgconfig(libxfce4ui-2) >= 4.10.0
BuildRequires:  pkgconfig(libxfce4util-1.0) >= 4.10.0
BuildRequires:  pkgconfig(libxfconf-0)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xinerama)
Requires:       libcanberra-gtk-module-common
Requires(post): update-desktop-files
Requires(pre):  update-desktop-files
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
Requires:       %{name}
BuildArch:      noarch

%description themes
Additional themes for use with Xfdashboard.

%package -n libxfdashboard%{so_ver}
Summary:        Xfdashboard library

%description -n libxfdashboard%{so_ver}
A library providing authenticators for Xfdashboard.

%prep
%setup -q
%patch0 -p1
%patch2 -p1

%build
export CFLAGS="%{optflags}"
%configure
make V=1 %{?_smp_mflags}

%install
make V=1 %{?_smp_mflags} DESTDIR=%{buildroot} install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_mandir}/man1
gzip -c9 %{SOURCE8} | tee -a %{buildroot}%{_mandir}/man1/%{name}.1.gz
gzip -c9 %{SOURCE9} | tee -a %{buildroot}%{_mandir}/man1/%{name}-settings.1.gz
%fdupes -s %{buildroot}%{_datadir}/themes/%{name}-*
%find_lang %{name} %{?no_lang_C}

%post
%icon_theme_cache_post
%desktop_database_post

%postun
%icon_theme_cache_postun
%desktop_database_postun

%post -n libxfdashboard%{so_ver} -p /sbin/ldconfig
%postun -n libxfdashboard%{so_ver} -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc AUTHORS README
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
%defattr(-,root,root)

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/libxfdashboard.pc

%files themes
%defattr(-,root,root)
%{_datadir}/themes/%{name}-*

%files -n libxfdashboard%{so_ver}
%defattr(-,root,root)
%{_libdir}/lib%{name}.so.*

%changelog
