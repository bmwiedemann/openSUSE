#
# spec file for package fcitx-pylogger 
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           fcitx-pylogger
Version:	1.0
Release:	0
License:	GPL-2.0
Summary:	A Fcitx Typo Tracking Tool
Url:		https://github.com/yuyichao/fcitx-pylogger
Group:	System/I18n/Chinese
Source:	%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	gcc-c++
BuildRequires:	fcitx-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{fcitx_requires}

%description
fcitx-pylogger collects typo statitics data of pinyin with Fcitx.
It records the cases you use `backspace` for typo correction.
It won't upload any data in background but hosts them at
~/.config/fcitx/pylog/pyedit.log
Once you've collected 1000 items, you can send it to fcitx@gmx.com

It can work with Sunpinyin/Libpinyin/GooglePinyin. Thanks for your
contribution to make fcitx a better world.

%prep
%setup -q

%build
mkdir build
cd build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} ..
make %{?_smp_mflags}

%install
cd build
%makeinstall
cd ..
%find_lang %{name}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(-,root,root)
%{_fcitx_libdir}/%{name}.so
%{_fcitx_addondir}/%{name}.conf
%{_fcitx_descdir}/%{name}.desc

%changelog

