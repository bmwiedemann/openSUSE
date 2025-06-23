#
# spec file for package fcitx5-libthai
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


Name:           fcitx5-libthai
Version:        5.1.6
Release:        0
Summary:        Libthai input method engine for Fcitx5
License:        GPL-2.0-or-later
URL:            https://github.com/fcitx/fcitx5-libthai
Source:         https://download.fcitx-im.org/fcitx5/%{name}/%{name}-%{version}.tar.zst
Patch0:         %{name}-iconv.patch
BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  fcitx5-devel
%if 0%{?suse_version} >= 1550
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc13-c++
%endif
BuildRequires:  libthai-devel
BuildRequires:  pkgconfig
BuildRequires:  zstd
Requires:       fcitx5
Requires:       libthai-data
%if 0%{?suse_version} <= 1520
BuildRequires:  appstream-glib-devel
%endif

%description
fcitx-libthai is an input method engine for Fcitx, which uses libthai as its backend.

%prep
%setup -q
%autopatch -p1

%build
%if 0%{?suse_version} < 1550
export CXX=%{_bindir}/g++-13
%endif
%cmake
%make_build

%install
%cmake_install
%find_lang %{name}

%files -f %{name}.lang
%license LICENSES
%doc README.md
%{_fcitx5_libdir}/libthai.so
%{_fcitx5_addondir}/libthai.conf
%{_fcitx5_imconfdir}/libthai.conf
%{_datadir}/metainfo/org.fcitx.Fcitx5.Addon.LibThai.metainfo.xml

%changelog
