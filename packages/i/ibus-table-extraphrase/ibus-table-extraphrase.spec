#
# spec file for package ibus-table-extraphrase
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


Name:           ibus-table-extraphrase
Version:        1.3.9.20110826
Release:        0
Summary:        Extra phrases for IBus-table based IME
License:        GPL-3.0-or-later
Group:          System/I18n/Chinese
URL:            http://code.google.com/p/ibus/
Source:         %{name}-%{version}.tar.gz
BuildRequires:  ibus-table-devel
BuildRequires:  pkgconfig
BuildArch:      noarch

%description
provide Chinese extra phrases for ibus-table based IME,
such as ibus-table-zhengma, ibus-table-wubi, ibus-table-cangjie5,
ibus-table-erbi and etc.

%package devel
Summary:        Development package for ibus-table-extraphrase
Group:          System/I18n/Chinese
Requires:       %{name} = %{version}-%{release}

%description devel
This package contains the files required for the development of
ibus-table-extraphrase.

%prep
%setup -q
sed -i "/^libdir=/d" %{name}.pc.in

%build
%configure
%make_build

%install
%make_install
# move pkgconfig file to /usr/share/pkgconfig
mkdir -p %{buildroot}%{_datadir}/pkgconfig
mv %{buildroot}%{_libdir}/pkgconfig/%{name}.pc \
   %{buildroot}%{_datadir}/pkgconfig

%files
%{_datadir}/ibus-table/data/extra_phrase.txt
%license COPYING

%files devel
%{_datadir}/pkgconfig/%{name}.pc

%changelog
