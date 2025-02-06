#
# spec file for package fcitx5-sayura
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


Name:           fcitx5-sayura
Version:        5.1.3
Release:        0
Summary:        Sinhala input method for Fcitx5
License:        GPL-2.0-or-later
URL:            https://github.com/fcitx/fcitx5-sayura
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
BuildRequires:  zstd
Requires:       fcitx5
Provides:       fcitx-sayura = %{version}
Obsoletes:      fcitx-sayura <= 0.1.2
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
Fcitx5-Sayura is a Sinhala input method for Fcitx5 input method framework ported from IBus-Sayura.

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
%{_fcitx5_libdir}/libsayura.so
%{_fcitx5_addondir}/sayura.conf
%{_fcitx5_imconfdir}/sayura.conf
%{_datadir}/icons/hicolor/*/apps/fcitx-sayura*
%{_datadir}/icons/hicolor/*/apps/org.fcitx.Fcitx5.fcitx-sayura*
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Sayura.metainfo.xml

%changelog
