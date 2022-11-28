#
# spec file for package fcitx5-skk
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


Name:           fcitx5-skk
Version:        5.0.14
Release:        0
Summary:        Libskk input method engine for Fcitx5
License:        GPL-3.0-or-later
URL:            https://github.com/fcitx/fcitx5-skk
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fcitx5-qt-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libskk-devel
BuildRequires:  pkgconfig
Requires:       fcitx5
Provides:       fcitx-skk = %{version}
Obsoletes:      fcitx-skk <= 0.1.4
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
fcitx-skk is an input method engine for Fcitx, which uses libskk as its backend.

%prep
%setup -q

%build
%cmake
%make_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES
%doc README.md
%dir %{_fcitx5_libdir}/qt5
%{_fcitx5_libdir}/skk.so
%{_fcitx5_libdir}/qt5/libfcitx5-skk-config.so
%{_fcitx5_addondir}/skk.conf
%{_fcitx5_imconfdir}/skk.conf
%{_fcitx5_datadir}/skk
%{_datadir}/icons/hicolor/*/apps/fcitx-skk*
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-skk*
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Skk.metainfo.xml

%changelog
