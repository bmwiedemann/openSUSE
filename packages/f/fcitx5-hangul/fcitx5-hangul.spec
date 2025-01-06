#
# spec file for package fcitx5-hangul
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


Name:           fcitx5-hangul
Version:        5.1.5
Release:        0
Summary:        Hangul Wrapper for Fcitx5
License:        LGPL-2.1-only
URL:            https://github.com/fcitx/fcitx5-hangul
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libhangul-devel
BuildRequires:  pkgconfig
BuildRequires:  zstd
Requires:       fcitx5
Provides:       fcitx-hangul = %{version}
Obsoletes:      fcitx-hangul <= 0.3.1
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
Hangul Wrapper for Fcitx5.

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
%{_fcitx5_libdir}/libhangul.so
%{_fcitx5_addondir}/hangul.conf
%{_fcitx5_imconfdir}/hangul.conf
%{_fcitx5_datadir}/hangul
%{_datadir}/icons/hicolor/*/apps/fcitx-hangul.png
%{_datadir}/icons/hicolor/*/apps/fcitx-hanja*.png
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-han*.png
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Hangul.metainfo.xml

%changelog
