#
# spec file for package fcitx-googlepinyin
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#



Name:           fcitx-googlepinyin
Version:        0.1.6
Release:        0
Summary:        Googlepinyin module for fcitx
Group:          System/I18n/Chinese
License:        GPL-3.0+
Url:            http://code.google.com/p/fcitx
BuildRequires:  cmake
BuildRequires:  libgooglepinyin-devel
BuildRequires:  fcitx-devel
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  pkg-config
Source:         %{name}-%{version}.tar.bz2
Provides:       locale(fcitx:zh_CN;zh_SG)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
fcitx-googlepinyin is a Googlepinyin module for fcitx.
 
%prep
%setup -q -n %{name}-%{version}

%build
%{__mkdir} -pv build
pushd build
cmake   -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DLIB_INSTALL_DIR=%{_libdir} \
        ..
make

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/fcitx
%{_datadir}/fcitx/*
%{_datadir}/icons/hicolor/*/apps/fcitx-googlepinyin.png

%changelog
