#
# spec file for package gnome-dictionary
#
# Copyright (c) 2022 SUSE LLC
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


Name:           gnome-dictionary
Version:        40.0
Release:        0
Summary:        Utility to look up words in dictionary sources
License:        GPL-2.0-or-later
Group:          System/GUI/GNOME
URL:            https://wiki.gnome.org/Apps/Dictionary
Source:         https://download.gnome.org/sources/gnome-dictionary/40/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM gnome-dictionary-fix-meson-061.patch -- Fix build with meson 0.61 and newer
Patch:          gnome-dictionary-fix-meson-061.patch

BuildRequires:  appstream-glib
BuildRequires:  desktop-file-utils
BuildRequires:  fdupes
BuildRequires:  gobject-introspection-devel
BuildRequires:  gtk-doc
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(glib-2.0) >= 2.39.0
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.16
Conflicts:      gnome-utils < 3.3.1
# libgdict is no longer a public library, and thus no external tool can make use of the data
# Merge the package back into the main package, obsoleting libgdict-data
Obsoletes:      libgdict-data < %{version}
Conflicts:      libgdict-1_0-6 < %{version}

%description
The Dictionary application enables you to search words and terms on a
dictionary source.

%lang_package

%prep
%autosetup -p1

%build
%meson \
        -D use_ipv6=true \
        -D build_man=true \
        %{nil}
%meson_build

%install
%meson_install
%fdupes %{buildroot}%{_datadir}/help
%find_lang %{name} %{?no_lang_C}

%check
%meson_test

%files
%license COPYING
%doc NEWS
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/org.gnome.Dictionary.desktop
%{_datadir}/dbus-1/services/org.gnome.Dictionary.service
%{_datadir}/gdict-1.0
%{_datadir}/glib-2.0/schemas/org.gnome.dictionary.gschema.xml
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Dictionary.Devel.svg
%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Dictionary.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.gnome.Dictionary-symbolic.svg
%{_datadir}/metainfo/org.gnome.Dictionary.appdata.xml
%{_mandir}/man1/%{name}.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
