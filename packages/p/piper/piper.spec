#
# spec file for package piper
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2019 Matthias Bach <marix@marix.org>.
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


Name:           piper
Version:        0.7
Release:        0
Summary:        Configuration UI for gaming mice
License:        GPL-2.0-only
Group:          Hardware/Other
URL:            https://github.com/libratbag/piper
Source:         %{name}-%{version}.tar.xz
Patch1:         shebang-env.patch
BuildRequires:  AppStream
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-cairo
BuildRequires:  python3-evdev
BuildRequires:  python3-flake8
BuildRequires:  python3-gobject-devel
BuildRequires:  python3-lxml
BuildRequires:  ratbagd >= 0.14
BuildRequires:  update-desktop-files
Requires:       python3-cairo
Requires:       python3-evdev
Requires:       python3-gobject
Requires:       python3-gobject-Gdk
Requires:       python3-lxml
Requires:       ratbagd >= 0.14
BuildArch:      noarch

%description
Piper is a GTK+ application to configure gaming mice. It is a graphical frontent
to the ratbagd DBUS daemon which provides the actual configuration support for the
devices.

%prep
%autosetup -p1

%build
PATH="${PATH}:%{_sbindir}" %meson
%meson_build

%check
%meson_test

%install
%meson_install
%fdupes %{buildroot}/%{_prefix}
%suse_update_desktop_file -r org.freedesktop.Piper Settings HardwareSettings
%find_lang %{name}

%files -f %{name}.lang
%license COPYING
%{_bindir}/piper
%{_datadir}/applications/org.freedesktop.Piper.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.freedesktop.Piper.svg
%{_datadir}/icons/hicolor/symbolic/apps/org.freedesktop.Piper-symbolic.svg
%{_datadir}/metainfo/org.freedesktop.Piper.appdata.xml
%{_datadir}/piper
%{python3_sitelib}/*
%{_mandir}/man1/piper.1%{?ext_man}

%changelog
