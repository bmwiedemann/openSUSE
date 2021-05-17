#
# spec file for package fcitx-libpinyin
#
# Copyright (c) 2021 SUSE LLC
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


%define sover 12

Name:           fcitx-libpinyin
Version:        0.5.4
Release:        0
Summary:        Libpinyin Wrapper for Fcitx
License:        GPL-2.0-or-later
Group:          System/I18n/Chinese
URL:            https://fcitx-im.org/wiki/Libpinyin
Source0:        https://github.com/fcitx/fcitx-libpinyin/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://download.fcitx-im.org/data/model.text.20161206.tar.gz
#PATCH-FIX-UPSTREAM downgrade qt5 requirement to 5.4 since qtwebengine is available
# starting from that release
Patch0:         dictmanager-qt5.4.patch
BuildRequires:  cmake >= 3.6
BuildRequires:  fcitx-devel
BuildRequires:  fcitx-qt5-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  pkgconfig(Qt5WebEngine)
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libpinyin) >= 2.6
Provides:       locale(fcitx:zh_CN;zh_SG)
%{fcitx_requires}

%description
Fcitx-libpinyin is a Frontend of the Intelligent Pinyin IME Backend.

%prep
%setup -q
%patch0 -p1
cp %{SOURCE1} data

%build
%cmake
%make_build

%install
%cmake_install
%find_lang %{name}
%fdupes %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%license COPYING
%dir %{_fcitx_libdir}/qt
%{_fcitx_libdir}/%{name}.so
%{_fcitx_libdir}/qt/lib%{name}-dictmanager.so
%{_fcitx_addondir}/%{name}.conf
%{_fcitx_descdir}/%{name}.desc
%{_fcitx_imicondir}/*.png
%{_fcitx_inputmethoddir}/pinyin-libpinyin.conf
%{_fcitx_inputmethoddir}/shuangpin-libpinyin.conf
%{_fcitx_inputmethoddir}/zhuyin-libpinyin.conf
%{_datadir}/icons/hicolor/48x48/status/*.png
%{_fcitx_datadir}/libpinyin

%changelog
