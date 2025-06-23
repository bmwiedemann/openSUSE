#
# spec file for package fcitx5-unikey
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


Name:           fcitx5-unikey
Version:        5.1.7
Release:        0
Summary:        Unikey engine support for Fcitx5
License:        GPL-2.0-or-later AND LGPL-2.0-or-later
Group:          System/Localization
URL:            https://github.com/fcitx/fcitx5-unikey
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fcitx5-qt-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  qt6-base-devel
BuildRequires:  zstd
Requires:       fcitx5
Provides:       fcitx-unikey = %{version}
Obsoletes:      fcitx-unikey <= 0.2.7
Obsoletes:      fcitx5-unikey-qt6 <= 5.1.6
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
Chewing Wrapper for Fcitx5.

%prep
%setup -q -n %{name}-%{version}

%build
%if 0%{?suse_version} == 1500
%cmake -DCMAKE_CXX_COMPILER=%{_bindir}/g++-13
%else
%cmake
%endif
%make_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES
%doc README
%{_fcitx5_libdir}/libunikey.so
%{_libdir}/fcitx5/qt6/libfcitx5-unikey-keymap-editor.so
%{_libdir}/fcitx5/qt6/libfcitx5-unikey-macro-editor.so
%{_fcitx5_addondir}/unikey.conf
%{_fcitx5_imconfdir}/unikey.conf
%{_datadir}/icons/hicolor/*/apps/fcitx-unikey*
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-unikey*
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Unikey.metainfo.xml

%changelog
