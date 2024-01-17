#
# spec file for package uget
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


Name:           uget
Version:        2.2.3
Release:        0
Summary:        Download Manager with a GTK+ user interface
License:        LGPL-2.1-or-later
Group:          Productivity/Networking/Web/Utilities
URL:            http://ugetdm.com
Source:         http://downloads.sourceforge.net/project/urlget/uget%20%28stable%29/%{version}/%{name}-%{version}-1.tar.gz
# PATCH-FIX-UPSTREAM uget-gcc10.patch dimstar@opensuse.org -- Fix build with GCC10, taken from upstream git 148909
Patch0:         uget-gcc10.patch
BuildRequires:  intltool
%if 0%{?WITH_APPINDICATOR}
BuildRequires:  pkgconfig(appindicator3-0.1)
%endif
BuildRequires:  libcurl-devel
BuildRequires:  libgcrypt-devel
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(glib-2.0) >= 2.32
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.4
BuildRequires:  pkgconfig(libnotify)
Requires:       aria2

%description
Uget is a download manager written with GTK+. It supports
pause and resume, and the ability to classify download, with every
category having an independent configuration.

%lang_package
%prep
%autosetup -p1

%build
%configure \
    --with-gnutls \
    --enable-unix-socket \
%if 0%{?WITH_APPINDICATOR}
    --enable-appindicator=yes
%endif

make %{?_smp_mflags} V=1

%install
%make_install
%suse_update_desktop_file %{name}-gtk
%find_lang %{name} %{?no_lang_C}

%if 0%{?suse_version} < 1500
%post
%desktop_database_post
%icon_theme_cache_post

%postun
%desktop_database_postun
%icon_theme_cache_postun
%endif

%files
%doc AUTHORS README COPYING
%{_bindir}/%{name}-gtk
%{_bindir}/uget-gtk-1to2
%{_datadir}/applications/%{name}-gtk.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}-icon.*
%{_datadir}/icons/hicolor/*/apps/%{name}-tray-*
%dir %{_datadir}/pixmaps/%{name}/
%{_datadir}/pixmaps/%{name}/logo.png
%dir %{_datadir}/sounds/%{name}/
%{_datadir}/sounds/%{name}/notification.wav

%files lang -f %{name}.lang

%changelog
