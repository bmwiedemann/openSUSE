#
# spec file for package nautilus-sendto
#
# Copyright (c) 2025 SUSE LLC
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


Name:           nautilus-sendto
Version:        3.8.6
Release:        0
Summary:        Integrate Nautilus and E-Mail clients
License:        GPL-2.0-or-later
Group:          Productivity/File utilities
URL:            http://www.es.gnome.org/~telemaco/
Source:         https://download.gnome.org/sources/nautilus-sendto/3.8/%{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM nautilus-sendto-fix-meson-061.patch bjorn.lie@gmail.com -- Fix build with meson 0.61 and newer
Patch0:         nautilus-sendto-fix-meson-061.patch

BuildRequires:  intltool >= 0.35.0
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.25.0
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.6.7
Obsoletes:      nautilus-sendto-devel < %{version}
Obsoletes:      nautilus-sendto-plugin-evolution < %{version}
Obsoletes:      nautilus-sendto-plugin-pidgin < %{version}
Obsoletes:      nautilus-sendto-plugin-upnp < %{version}

%description
This package provides the functionality to the Nautilus file browser to
send files over e-mail via Evolution, Thunderbird, Sylpheed or Balsa.

%lang_package

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %{name}

%files
%license COPYING
%doc AUTHORS NEWS
%{_bindir}/nautilus-sendto
%{_mandir}/man1/nautilus-sendto.1%{?ext_man}
%{_datadir}/appdata/nautilus-sendto.metainfo.xml

%files lang -f %{name}.lang

%changelog
