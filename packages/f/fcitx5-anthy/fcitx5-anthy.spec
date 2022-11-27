#
# spec file for package fcitx5-anthy
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


Name:           fcitx5-anthy
Version:        5.0.13
Release:        0
Summary:        Anthy Wrapper for Fcitx5
License:        GPL-2.0-or-later
URL:            https://github.com/fcitx/fcitx5-anthy
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.xz
BuildRequires:  anthy-devel
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  pkgconfig
Requires:       anthy
Requires:       fcitx5
Provides:       fcitx-anthy = %{version}
Obsoletes:      fcitx-anthy <= 0.2.3
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
Anthy Wrapper for Fcitx5.

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
%{_fcitx5_libdir}/anthy.so
%{_fcitx5_addondir}/anthy.conf
%{_fcitx5_imconfdir}/anthy.conf
%{_fcitx5_datadir}/anthy
%{_datadir}/icons/hicolor/*/status/org.fcitx.Fcitx5.fcitx-anthy*
%{_datadir}/icons/hicolor/*/status/fcitx-anthy*
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.Anthy.metainfo.xml

%changelog
