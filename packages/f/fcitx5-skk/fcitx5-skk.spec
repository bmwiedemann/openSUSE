#
# spec file for package fcitx5-skk
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


%global flavor @BUILD_FLAVOR@%{nil}
%global sname fcitx5-skk
%if "%{flavor}" == ""
%global pname %sname
%else
%global pname %{sname}-%{flavor}
%endif

Name:           %{pname}
Version:        5.1.5
Release:        0
Summary:        Libskk input method engine for Fcitx5
License:        GPL-3.0-or-later
Group:          System/I18n/Japanese
URL:            https://github.com/fcitx/fcitx5-skk
Source:         https://download.fcitx-im.org/fcitx5/%{sname}/%{sname}-%{version}.tar.zst
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  fcitx5-qt-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libskk-devel
BuildRequires:  pkgconfig
%if "%{flavor}" == ""
BuildRequires:  libqt5-qtbase-devel
Conflicts:      %{sname}-qt6
Provides:       fcitx-skk = %{version}
Obsoletes:      fcitx-skk <= 0.1.4
%endif
%if "%{flavor}" == "qt6"
BuildRequires:  qt6-base-devel
Conflicts:      %{sname}
Supplements:    (fcitx5 and skkdic and plasma6-workspace)
%endif
BuildRequires:  zstd
Requires:       fcitx5
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
fcitx-skk is an input method engine for Fcitx, which uses libskk as its backend.

%prep
%setup -q -n %{sname}-%{version}

%build
%if "%{flavor}" == "qt6"
%if 0%{?suse_version} == 1500
%cmake -DCMAKE_CXX_COMPILER=%{_bindir}/g++-13
%else
%cmake
%endif
%endif
%if "%{flavor}" == ""
%cmake -DUSE_QT6=OFF
%endif
%make_build

%install
%cmake_install
%find_lang %{sname}

%files -f %{sname}.lang
%license LICENSES
%doc README.md
%{_fcitx5_libdir}/skk.so
%if "%{flavor}" == ""
%{_fcitx5_qt5dir}/libfcitx5-skk-config.so
%endif
%if "%{flavor}" == "qt6"
%{_libdir}/fcitx5/qt6/libfcitx5-skk-config.so
%endif
%{_fcitx5_addondir}/skk.conf
%{_fcitx5_imconfdir}/skk.conf
%{_fcitx5_datadir}/skk
%{_datadir}/icons/hicolor/*/apps/fcitx_skk*
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx_skk*
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Skk.metainfo.xml

%changelog
