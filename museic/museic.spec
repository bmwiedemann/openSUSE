#
# spec file for package museic
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


Name:           museic
Version:        2.1.3
Release:        0
Summary:        Audio player with remote control
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Sound/Players
URL:            https://github.com/bcedu
Source:         https://github.com/bcedu/MuseIC/archive/%{version}.tar.gz#/MuseIC-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  elementary-cmake-modules
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  vala
BuildRequires:  pkgconfig(dbus-glib-1)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gmodule-2.0)
BuildRequires:  pkgconfig(granite) >= 0.5
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)

%description
MuseIC is a fast and simple music player with remote control from any
device through internet browser.

%prep
%setup -q -n MuseIC-%{version}

%build
%cmake \
    -DGSETTINGS_COMPILE=OFF

make %{?_smp_mflags}

%install
%cmake_install

rm %{buildroot}%{_datadir}/icons/hicolor/*.??g

%suse_update_desktop_file -r com.github.bcedu.museic GTK AudioVideo Music Player
%fdupes %{buildroot}/%{_datadir}

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/com.github.bcedu.museic
%{_datadir}/applications/com.github.bcedu.museic.desktop
%{_datadir}/com.github.bcedu.museic/
%{_datadir}/glib-2.0/schemas/com.github.bcedu.museic.gschema.xml
%{_datadir}/icons/hicolor/*/apps/com.github.bcedu.museic.??g
%{_datadir}/metainfo/com.github.bcedu.museic.appdata.xml

%changelog
