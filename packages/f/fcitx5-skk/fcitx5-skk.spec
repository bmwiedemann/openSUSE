#
# spec file for package fcitx5-skk
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        5.1.9
Release:        0
Summary:        Libskk input method engine for Fcitx5
License:        GPL-3.0-or-later
Group:          System/I18n/Japanese
URL:            https://github.com/fcitx/fcitx5-skk
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fcitx5-qt-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  libskk-devel
BuildRequires:  pkgconfig
BuildRequires:  qt6-base-devel
Supplements:    (fcitx5 and skkdic and plasma6-workspace)
Provides:       fcitx-skk = %{version}
Obsoletes:      fcitx-skk <= 0.1.4
Obsoletes:      fcitx5-skk-qt6 <= 5.1.6
%if 0%{?suse_version} >= 1550
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc13-c++
%endif
BuildRequires:  zstd
Requires:       fcitx5

%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
fcitx-skk is an input method engine for Fcitx, which uses libskk as its backend.

%prep
%autosetup

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
%doc README.md
%{_fcitx5_libdir}/skk.so
%{_libdir}/fcitx5/qt6/libfcitx5-skk-config.so
%{_fcitx5_addondir}/skk.conf
%{_fcitx5_imconfdir}/skk.conf
%{_fcitx5_datadir}/skk
%{_datadir}/icons/hicolor/*/apps/fcitx_skk*
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx_skk*
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Skk.metainfo.xml

%changelog
