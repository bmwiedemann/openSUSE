#
# spec file for package fcitx5-unikey
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


Name:           fcitx5-unikey
Version:        5.0.11
Release:        0
Summary:        Unikey engine support for Fcitx5
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
URL:            https://github.com/fcitx/fcitx5-unikey
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
# Backport from git
#e352da5
Patch1:         backport-commit-on-switchingIM.diff
#b5f70ed
Patch2:         backport-rebuild-surrounding-state.diff
#0eac455
Patch3:         backport-allow-uoh.diff
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fcitx5-qt-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig
Requires:       fcitx5
Provides:       fcitx-unikey = %{version}
Obsoletes:      fcitx-unikey <= 0.2.7
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
Chewing Wrapper for Fcitx5.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%cmake
%make_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES
%doc README
%dir %{_fcitx5_libdir}/qt5
%{_fcitx5_libdir}/libunikey.so
%{_fcitx5_libdir}/qt5/libfcitx5-unikey-keymap-editor.so
%{_fcitx5_addondir}/unikey.conf
%{_fcitx5_imconfdir}/unikey.conf
%{_datadir}/icons/hicolor/*/apps/fcitx-unikey*
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-unikey*
%{_fcitx5_libdir}/qt5/libfcitx5-unikey-macro-editor.so
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Unikey.metainfo.xml

%changelog
