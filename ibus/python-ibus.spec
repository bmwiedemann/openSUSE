#
# spec file for package python-ibus
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


%define _name ibus
Name:           python-ibus
Version:        1.5.20
Release:        0
Summary:        Python2 module for ibus
License:        LGPL-2.1-or-later
Group:          System/I18n/Chinese
URL:            https://github.com/ibus/
Source:         https://github.com/ibus/ibus/releases/download/%{version}/%{_name}-%{version}.tar.gz
# Source:         %{_name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE ibus-python-install-dir.patch ftake@geeko.jp
Patch0:         ibus-python-install-dir.patch
BuildRequires:  dbus-1-glib-devel
BuildRequires:  dbus-1-python-devel >= 0.83.0
BuildRequires:  dconf-devel >= 0.7.5
BuildRequires:  fdupes
BuildRequires:  gettext-devel
BuildRequires:  glib2-devel >= 2.34.0
BuildRequires:  gobject-introspection-devel >= 0.9.6
BuildRequires:  gtk-doc >= 1.9
BuildRequires:  gtk2-devel
BuildRequires:  intltool
BuildRequires:  iso-codes-devel
BuildRequires:  libnotify-devel >= 0.7
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  python-devel
BuildRequires:  python-gobject-devel
BuildRequires:  unicode-ucd
BuildRequires:  update-desktop-files
# copy_deep method is supported since 0.31.1
BuildRequires:  vala >= 0.31.1
BuildRequires:  x11-tools
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(vapigen)
BuildRequires:  pkgconfig(xkbcommon)
Requires:       %{_name} = %{version}
Requires:       python-gobject

%description
IBus, short for Intelligent Input Bus, is an input framework. IBus
plugins then provide the particular logic how to translate keypresses
to input characters and possibly show disambiguation windows around
the text cursor.

%prep
%setup -q -n %{_name}-%{version}
%patch0 -p1

%build
autoreconf -fi
%configure --disable-static \
           --enable-gtk3 \
           --enable-vala \
           --disable-emoji-dict \
           --enable-python-library \
           --enable-introspection \
           --disable-gconf \
           --enable-dconf \
           --enable-gtk-doc \
           --enable-surrounding-text \
           --enable-appindicator_engine_icon \
           --libexecdir=%{_libdir}/ibus
make %{?_smp_mflags}

%install
%make_install

#remove needless files
rm -rf %{buildroot}%{_bindir} %{buildroot}%{_datadir} %{buildroot}%{_libdir}/ibus \
       %{buildroot}%{_libdir}/gtk-* %{buildroot}%{_sysconfdir} %{buildroot}%{_includedir} \
       %{buildroot}%{_libdir}/libibus* %{buildroot}%{_libdir}/pkgconfig \
       %{buildroot}%{_libdir}/girepository-1.0

%fdupes %{buildroot}%{python_sitearch}

%files
%defattr(-,root,root)
%{python_sitearch}/ibus
%{python_sitearch}/gi/overrides/*

%changelog
