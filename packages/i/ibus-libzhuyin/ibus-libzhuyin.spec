#
# spec file for package ibus-libzhuyin
#
# Copyright (c) 2024 SUSE LLC
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


Name:           ibus-libzhuyin
Version:        1.10.3
Release:        0
Summary:        Zhuyin engine based on libzhuyin for IBus
License:        GPL-2.0-only
Group:          System/I18n/Chinese
URL:            https://github.com/libzhuyin/ibus-libzhuyin
Source:         %{url}/releases/download/%{version}/ibus-libzhuyin-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  intltool
BuildRequires:  libpinyin-tools >= 2.0.91
BuildRequires:  python3-devel
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(ibus-1.0) >= 1.4.99
BuildRequires:  pkgconfig(libpinyin) >= 2.2.0
BuildRequires:  pkgconfig(opencc) >= 1.0.0
Provides:       locale(ibus:zh_TW;zh_HK)

%description
This package includes a Chinese Zhuyin (Bopomofo) input method based
on libzhuyin for IBus.

%prep
%autosetup -p1
#NOCONFIGURE=1 ./autogen.sh

%build
%configure --libexecdir=%{_ibus_libexecdir}
%make_build

%install
%make_install

rm -rf %{buildroot}%{_datadir}/doc
%find_lang %{name}
%fdupes %{buildroot}%{_prefix}

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%license COPYING
%{_ibus_libexecdir}/ibus-engine-libzhuyin
%{_ibus_libexecdir}/ibus-setup-libzhuyin
%{_datadir}/%{name}
%{_libdir}/ibus-libzhuyin/
%{_datadir}/metainfo/*.appdata.xml
%{_datadir}/ibus/component/libzhuyin.xml
%{_datadir}/applications/ibus-setup-libzhuyin.desktop
%{_datadir}/glib-2.0/schemas/com.github.libzhuyin.ibus-libzhuyin.gschema.xml

%changelog
