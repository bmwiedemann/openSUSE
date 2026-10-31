#
# spec file for package ibus-sunpinyin
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           ibus-sunpinyin
Version:        3.1.0
Release:        0
Summary:        Sunpinyin module for ibus
License:        CDDL-1.0 OR LGPL-2.1-only
Group:          System/I18n/Chinese
URL:            https://github.com/openSUSE/ibus-sunpinyin
Source:         https://github.com/openSUSE/ibus-sunpinyin/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(opencc)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(sunpinyin-2.0)
Requires:       sunpinyin-data
Provides:       locale(ibus:zh_CN;zh_SG)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ibus-sunpinyin is a wrapper around SunPinyin which enables user to use
SunPinyin with IBus framework.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%meson
%meson_build

%install
%meson_install

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README.md
%license COPYING LGPL.LICENSE OPENSOLARIS.LICENSE
%dir %{_libexecdir}/%{name}/
%{_libexecdir}/%{name}/ibus-engine-sunpinyin
%{_libexecdir}/%{name}/ibus-setup-sunpinyin
%{_datadir}/%{name}
%{_datadir}/ibus/component/sunpinyin.xml

%changelog
