#
# spec file for package ibus-sunpinyin
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ibus-sunpinyin
Version:        2.0.99
Release:        0
Summary:        Sunpinyin module for ibus
License:        LGPL-2.1 or CDDL-1.0
Group:          System/I18n/Chinese
Url:            https://github.com/sunpinyin/sunpinyin
Source:         https://github.com/sunpinyin/sunpinyin/archive/v3.0.0-rc1/sunpinyin-3.0.0-rc1.tar.gz
# PATCH-FIX-UPSTREAM ibus-sunpinyin-scons-on-py3.patch dimstar@opensuse.org -- Fix build with scons using python3 as interpreter
Patch0:         ibus-sunpinyin-scons-on-py3.patch
# PATCH-FIX-UPSTREAM ibus-sunpinyin-migrate-to-python3.patch hillwood@opensuse.org -- Use python3, python2 is EOF
Patch1:         ibus-sunpinyin-migrate-to-python3.patch
# PATCH-FIX-UPSTREAM ibus-sunpinyin-fix-libexecdir.patch hillwood@opensuse.org -- libexecdir should be in %{_libdir}/ibus/
Patch2:         ibus-sunpinyin-fix-libexecdir.patch
BuildRequires:  gcc-c++
BuildRequires:  intltool
BuildRequires:  scons >= 1.2.0
BuildRequires:  pkgconfig(ibus-1.0)
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
%setup -q -n sunpinyin-3.0.0-rc1
%patch0 -p1
%patch1 -p1
%patch2 -p1
sed -i "s/LIBEXECDIR'\].*ibus-sunpinyin.*/LIBEXECDIR'\]/" SConstruct

%build
cd wrapper/ibus/
scons --prefix=%{_prefix} \
      --libdir=%{_libdir} \
      --libexecdir=%{_libdir}/ibus

%install
pushd wrapper/ibus/
scons install --prefix=%{_prefix} \
              --libdir=%{_libdir} \
              --libexecdir=%{_libdir}/ibus \
              --install-sandbox=%{buildroot}
popd

chmod 755 %{buildroot}%{_datadir}/%{name}/setup/main.py

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc wrapper/ibus/README 
%license wrapper/ibus/COPYING wrapper/ibus/LGPL.LICENSE wrapper/ibus/OPENSOLARIS.LICENSE
%{_libdir}/ibus/ibus-engine-sunpinyin
%{_libdir}/ibus/ibus-setup-sunpinyin
%{_datadir}/%{name}
%{_datadir}/ibus/component/sunpinyin.xml

%changelog
