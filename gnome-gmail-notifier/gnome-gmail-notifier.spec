#
# spec file for package gnome-gmail-notifier
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


Name:           gnome-gmail-notifier
Version:        0.10.1
Release:        0
Summary:        Gmail Notifier for GNOME
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            http://code.google.com/p/gnome-gmail-notifier/
Source:         %{name}-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM gnome-gmail-notifier-libnotify-0.7.patch issue#86 dimstar@opensuse.org -- Fix build with libnotify 0.7.
Patch0:         gnome-gmail-notifier-libnotify-0.7.patch
# PATCH-FIX-UPSTREAM gnome-gmail-notifier-glib-2.31.patch issue#95 dimstar@opensuse.org -- Fix build with glib 2.31.
Patch1:         gnome-gmail-notifier-glib-2.31.patch
# PATCH-FIX-UPSTREAM gnome-gmail-notifier-gstreamer-1.0.patch issue#99 dimstar@opensuse.org -- Port to GStreamer 1.0
Patch2:         gnome-gmail-notifier-gstreamer-1.0.patch
# PATCH-FIX-UPSTREAM gnome-gmail-notifier-automake.patch issue#104 dimstar@opensuse.org -- Fix build with automake >= 1.14
Patch3:         gnome-gmail-notifier-automake.patch
BuildRequires:  fdupes
# Needed for patch2
BuildRequires:  gnome-common
BuildRequires:  gstreamer-plugins-good
BuildRequires:  gstreamer-utils
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(gnome-keyring-1)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
Recommends:     %{name}-lang

%description
GNOME Gmail Notifier is an application that provides periodic updates
that pertain to the user's gmail inbox. The Notifier presents itself
as a system tray icon displaying a small balloon popup when the user
receives new mail.

%lang_package

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
# Needed for patch2 and patch3
NOCONFIGURE=1 ./autogen.sh
%configure
make %{?_smp_mflags}

%install
%make_install
%find_lang %{name} %{?no_lang_C}
%suse_update_desktop_file %{name}
%fdupes %{buildroot}%{_datadir}

%if 0%{?suse_version} > 1130
%post
%desktop_database_post
%endif

%if 0%{?suse_version} > 1130
%postun
%desktop_database_postun
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README THANKS
%dir %{_datadir}/gnome-control-center/
%dir %{_datadir}/gnome-control-center/default-apps/
%{_bindir}/gnome-gmail-notifier
%{_datadir}/applications/gnome-gmail-notifier.desktop
%{_datadir}/gnome-gmail-notifier/
%{_datadir}/gnome-control-center/default-apps/gnome-gmail-notifier.xml
%{_datadir}/pixmaps/gnome-gmail-notifier.svg

%files lang -f %{name}.lang

%changelog
