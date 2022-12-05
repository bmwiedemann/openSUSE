#
# spec file for package courier-unicode
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


%define libname   lib%{name}
%define libsoname %{libname}7

Name:           courier-unicode
Version:        2.2.6
Release:        0
Summary:        Courier Unicode Library
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Email/Servers
URL:            https://www.courier-mta.org/
Source0:        https://download.sourceforge.net/courier/%{name}-%{version}.tar.bz2
Source1:        https://download.sourceforge.net/courier/%{name}-%{version}.tar.bz2.sig
# Keyring downloaded from https://www.courier-mta.org/KEYS.bin#/%%{name}.keyring
Source2:        %{name}.keyring
BuildRequires:  fdupes
BuildRequires:  gcc-c++

%description
The Courier Unicode Library based on the Unicode 13.0.0 standard.
This package holds all man pages.

%package -n %{libsoname}
Summary:        Courier Unicode Library
Group:          System/Libraries

%description -n %{libsoname}
This library implements several algorithms related to the Unicode Standard:
* Look up uppercase, lowercase, and titlecase equivalents of a unicode
  character.
* Implementation of grapheme and work breaking rules.
* Implementation of line breaking rules.
* Several ancillary functions, like looking up the unicode character
  that corresponds to some HTML 4.0 entity (such as “&amp;”, for
  example), and determining the normal width or a double-width status of
  a unicode character. Also, an adaptation of the iconv(3) API for this
  unicode library.
This library also implements C++ bindings for these algorithms.

%package devel
Summary:        Courier Unicode Library - Development files
Group:          Development/Languages/C and C++
Requires:       %{libsoname} = %{version}
Provides:       %{libname}-devel

%description devel
This package contains the files needed to compile programs that use the
libunicode library.

%package doc
Summary:        Courier Unicode Library - Docs and man pages
Group:          Productivity/Networking/Email/Servers
BuildArch:      noarch

%description doc
This package contains the docs and the man pages of the Courier Unicode Library

%prep
%setup -q

%build
%configure \
  --disable-static

make %{?_smp_mflags}

%install
%make_install

# cleanup *.la libs
find %{buildroot} -name %{libname}.la -exec rm {} \;

# fdupes
%fdupes -s %{buildroot}%{_mandir}/man3/

%post   -n %{libsoname} -p /sbin/ldconfig
%postun -n %{libsoname} -p /sbin/ldconfig

%files -n %{libsoname}
%defattr(-,root,root)
%license COPYING
%doc ChangeLog README
%{_libdir}/%{libname}.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS
%dir %{_datadir}/aclocal/
%{_datadir}/aclocal/%{name}*.m4
%{_libdir}/%{libname}.so
%{_includedir}/%{name}*.h

%files doc
%defattr(-,root,root)
%{_mandir}/man?/*

%changelog
