#
# spec file for package fcitx-zhuyin
#
# Copyright (c) 2020 SUSE LLC
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


%define sover 7

Name:           fcitx-zhuyin
Version:        0.1.0+git20150626.36064e1
Release:        0
Summary:        Libzhuyin Wrapper for Fcitx
License:        GPL-2.0-only
Group:          System/I18n/Chinese
URL:            https://github.com/fcitx/fcitx-zhuyin
Source:         %{name}-%{version}.tar.xz
#PATCH-FIX-UPSTREAM marguerite@opensuse.org in 1.0.91, zhuyin_guess_candidates
# was replaced by zhuyin_guess_candidates_after_cursor
Patch:          libzhuyin-1.0.91-zhuyin_guess_candidates.patch
#PATCH-FIX-UPSTREAM marguerite@opensuse.org libzhuyin has merged to libpinyin
# libpinyin doesn't provide pkgdata dir in libzhuyin.pc
Patch1:         fcitx-zhuyin-libpinyin.patch
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libpinyin-devel
Provides:       locale(fcitx:zh_TW;zh_HK)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The libzhuyin project aims to provide the algorithms core
for intelligent sentence-based Chinese zhuyin input methods.

This is a libzhuyin wrapper for fcitx.


%prep
%setup -q
%patch -p1
%patch1 -p1

%build
export PKG_CONFIG_PATH=$PKG_CONFIG_PATH:%{_libdir}/libzhuyin-1.1.1/pkgconfig
mkdir build && cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      ..
make %{?_smp_mflags}

%install
%cmake_install

%find_lang %{name}
%fdupes %{buildroot}/%{_prefix}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README COPYING
%{_fcitx_libdir}/%{name}.so
%{_fcitx_addondir}/%{name}.conf
%{_fcitx_descdir}/%{name}.desc
%{_fcitx_imicondir}/zhuyin.png
%{_fcitx_inputmethoddir}/zhuyin.conf
%{_datadir}/icons/hicolor/*/status/%{name}.png

%changelog
