#
# spec file for package libidn2
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define lname	libidn2-0
Name:           libidn2
Version:        2.3.8
Release:        0
Summary:        Support for Internationalized Domain Names (IDN) based on IDNA2008
License:        (GPL-2.0-or-later OR LGPL-3.0-or-later) AND GPL-3.0-or-later
URL:            https://www.gnu.org/software/libidn/#libidn2
Source0:        https://ftp.gnu.org/gnu/libidn/%{name}-%{version}.tar.gz
Source1:        https://ftp.gnu.org/gnu/libidn/%{name}-%{version}.tar.gz.sig
Source2:        https://josefsson.org/key-20190320.txt#/%{name}.keyring
Source3:        baselibs.conf
BuildRequires:  libunistring-devel
BuildRequires:  pkgconfig

%description
An implementation of the IDNA2008 specifications (RFCs 5890, 5891, 5892, 5893)

%package tools
Summary:        Command line utility to convert Int. Domain Names
License:        GPL-3.0-or-later

%description tools
An implementation of the IDNA2008 specifications (RFCs 5890, 5891, 5892, 5893)

%package -n %{lname}
Summary:        Support for Internationalized Domain Names (IDN)
# for lang package
License:        GPL-2.0-or-later OR LGPL-3.0-or-later
Provides:       %{name} = %{version}

%description -n %{lname}
An implementation of the IDNA2008 specifications (RFCs 5890, 5891, 5892, 5893)

%package devel
Summary:        Include Files and Libraries mandatory for Development
License:        (GPL-2.0-or-later OR LGPL-3.0-or-later) AND GPL-3.0-or-later
Requires:       %{lname} = %{version}

%description devel
An implementation of the IDNA2008 specifications (RFCs 5890, 5891, 5892, 5893)

%lang_package

%prep
%autosetup -p1

%build
%configure \
    --disable-rpath \
    --disable-silent-rules \
    --disable-static \
    --disable-gtk-doc

%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
# Do not bother with partial gtkdoc
rm -rf %{buildroot}/%{_datadir}/gtk-doc/
%find_lang %{name}

%check
%make_build check

%ldconfig_scriptlets -n %{lname}

%files tools
%license COPYING*
%doc AUTHORS ChangeLog NEWS README.md
%{_infodir}/libidn*
%{_bindir}/idn2
%{_mandir}/man1/idn2.1%{?ext_man}

%files -n %{lname}
%license COPYING*
%{_libdir}/libidn2.so.*

%files devel
%license COPYING*
%{_libdir}/libidn2.so
%{_libdir}/pkgconfig/libidn2.pc
%{_includedir}/*.h
%{_mandir}/man3/*

%files lang -f %{name}.lang
%license COPYING*

%changelog
