#
# spec file for package ibus-table-extraphrase
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           ibus-table-extraphrase
BuildRequires:  ibus-table-devel
BuildRequires:  pkg-config
Version:        1.3.9.20110826
Release:        0
Url:            http://code.google.com/p/ibus/
Source:         %{name}-%{version}.tar.gz
Summary:        Extra phrases for IBus-table based IME
License:        GPL-3.0+
Group:          System/I18n/Chinese
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
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

%build
%configure
make

%install
%makeinstall
# move pkgconfig file to /usr/share/pkgconfig
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pkgconfig
mv $RPM_BUILD_ROOT%{_libdir}/pkgconfig/*.pc \
   $RPM_BUILD_ROOT%{_datadir}/pkgconfig

%files
%defattr(-,root,root)
%{_datadir}/ibus-table/data/extra_phrase.txt
%doc COPYING

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/*.pc

%changelog
