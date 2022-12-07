#
# spec file for package ibus-libzhuyin
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


%define sover 13

Name:           ibus-libzhuyin
Version:        1.10.1
Release:        0
Summary:        Zhuyin engine based on libzhuyin for IBus
License:        GPL-2.0-only
Group:          System/I18n/Chinese
URL:            https://github.com/libzhuyin/ibus-libzhuyin
Source:         https://github.com/libzhuyin/ibus-libzhuyin/releases/download/%{version}/ibus-libzhuyin-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  libpinyin-tools >= 2.0.91
BuildRequires:  libzhuyin%{sover}
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(ibus-1.0) >= 1.4.99
BuildRequires:  pkgconfig(libpinyin) >= 2.2.0
BuildRequires:  pkgconfig(opencc) >= 1.0.0
Provides:       locale(ibus:zh_TW;zh_HK)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package includes a Chinese Zhuyin (Bopomofo) input method based
on libzhuyin for IBus.

%prep
%setup -q
#NOCONFIGURE=1 ./autogen.sh

%build
%configure
make %{?_smp_mflags}

%install
%make_install

rm -rf %{buildroot}%{_datadir}/doc
%find_lang %{name}
%fdupes %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%license COPYING
%{_libexecdir}/ibus-engine-libzhuyin
%{_libexecdir}/ibus-setup-libzhuyin
%{_datadir}/%{name}
%{_libdir}/ibus-libzhuyin/
%dir %{_datadir}/appdata
%{_datadir}/appdata/libzhuyin.appdata.xml
%{_datadir}/ibus/component/libzhuyin.xml
%{_datadir}/applications/ibus-setup-libzhuyin.desktop
%{_datadir}/glib-2.0/schemas/com.github.libzhuyin.ibus-libzhuyin.gschema.xml

%changelog
