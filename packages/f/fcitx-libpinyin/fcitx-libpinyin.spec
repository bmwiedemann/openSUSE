#
# spec file for package fcitx-libpinyin
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.5.3
Release:        0
Summary:        Libpinyin Wrapper for Fcitx
License:        GPL-2.0-or-later
Group:          System/I18n/Chinese
Url:            https://github.com/fcitx/fcitx-libpinyin
Source:         http://download.fcitx-im.org/fcitx-libpinyin/%{name}-%{version}_dict.tar.xz
#PATCH-FIX-UPSTREAM downgrade qt5 requirement to 5.4 since qtwebengine is available
# starting from that release
Patch0:         dictmanager-qt5.4.patch
#PATCH-FIX-UPSTREAM linking against fcitx
Patch1:         fcitx-libpinyin-linking.patch
BuildRequires:  cmake
BuildRequires:  fcitx-devel
BuildRequires:  fcitx-qt5-devel
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  intltool
BuildRequires:  libqt5-qtbase-devel
BuildRequires:  libqt5-qtwebengine-devel
BuildRequires:  xz
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(libpinyin)
Provides:       locale(fcitx:zh_CN;zh_SG)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{fcitx_requires}

%description
Fcitx-libpinyin is a Frontend of the Intelligent Pinyin IME Backend.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%cmake
make %{?_smp_mflags}

%install
%cmake_install
%find_lang %{name}
%fdupes %{buildroot}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%doc COPYING
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
