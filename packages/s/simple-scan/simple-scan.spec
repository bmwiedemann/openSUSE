#
# spec file for package simple-scan
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


Name:           simple-scan
Version:        3.36.6
Release:        0
Summary:        Simple Scanning Utility
License:        GPL-3.0-or-later
Group:          System/GUI/GNOME
URL:            https://gitlab.gnome.org/GNOME/simple-scan
Source0:        https://download.gnome.org/sources/simple-scan/3.36/%{name}-%{version}.tar.xz

BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  sane-backends-devel
BuildRequires:  vala >= 0.22.0
BuildRequires:  yelp-tools
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(colord)
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.38
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gusb) >= 0.2.7
BuildRequires:  pkgconfig(libwebp)
BuildRequires:  pkgconfig(libwebpmux)
BuildRequires:  pkgconfig(packagekit-glib2) >= 1.1.5
BuildRequires:  pkgconfig(zlib)
Requires:       xdg-utils

%description
Simple Scan is an easy-to-use application, designed to let users connect
their scanner and quickly have the image/document in an appropriate
format.

Simple Scan is basically a frontend for SANE - which is the same backend
as XSANE uses. This means that all existing scanners will work and the
interface is well tested.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name} %{?no_lang_C}
%fdupes %{buildroot}%{_datadir}

%files
%license COPYING
%doc NEWS README.md
%doc %{_datadir}/help/C/%{name}/
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.SimpleScan.gschema.xml
%{_mandir}/man1/%{name}.1%{?ext_man}
%dir %{_datadir}/metainfo/
%{_datadir}/metainfo/simple-scan.appdata.xml
%{_datadir}/icons/hicolor/*/apps/*.svg

%files lang -f %{name}.lang

%changelog
