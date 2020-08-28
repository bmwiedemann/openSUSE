#
# spec file for package m17n-lib
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


%define	appdefdir  %{_datadir}/X11
Name:           m17n-lib
Version:        1.8.0
Release:        0
Summary:        Multilingual Text Processing Library for the C Language
License:        LGPL-2.1-or-later AND GPL-2.0-or-later
Group:          System/I18n/Japanese
URL:            https://www.m17n.org/m17n-lib/
Source0:        http://download.savannah.gnu.org/releases/m17n/%{name}-%{version}.tar.gz
Source1:        m17n-lib-rpmlintrc
Source2:        baselibs.conf
BuildRequires:  fdupes
BuildRequires:  libotf-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(fribidi)
BuildRequires:  pkgconfig(gdlib)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(m17n-db)
BuildRequires:  pkgconfig(wordcut)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xft)

%description
A multilingual text processing library for the C language.
This package contains m17n-* programs.

%package -n libm17n0
Summary:        Multilingual text processing library for the C language
Group:          System/Libraries
Requires:       pkgconfig(m17n-db)

%description -n libm17n0
A multilingual text processing library for the C language.
This package contains shared libraries.

%package devel
Summary:        Multilingual text processing library for the C language
Group:          Development/Libraries/C and C++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xft)
Requires:       %{name} = %{version}
Requires:       glibc-devel

%description devel
A multilingual text processing library for the C language

%prep
%setup -q

%build
%configure \
  --disable-static
# Not thread safe at all
%make_build -j1

%check
export MALLOC_CHECK_=2
%make_build -j1 check
unset MALLOC_CHECK_

%install
%make_install INSTALL="install -p"
# Japanese app-defaults:
mkdir -p %{buildroot}%{appdefdir}/{ja,ja_JP,ja_JP.eucJP,ja_JP.SJIS,ja_JP.UTF-8}/app-defaults
iconv -f EUC-JP -t EUC-JP < example/M17NEdit.ja \
      > %{buildroot}%{appdefdir}/ja/app-defaults/M17NEdit
iconv -f EUC-JP -t EUC-JP < example/M17NEdit.ja \
      > %{buildroot}%{appdefdir}/ja_JP/app-defaults/M17NEdit
iconv -f EUC-JP -t EUC-JP < example/M17NEdit.ja \
      > %{buildroot}%{appdefdir}/ja_JP.eucJP/app-defaults/M17NEdit
iconv -f EUC-JP -t SJIS < example/M17NEdit.ja \
      > %{buildroot}%{appdefdir}/ja_JP.SJIS/app-defaults/M17NEdit
iconv -f EUC-JP -t UTF-8 < example/M17NEdit.ja \
      > %{buildroot}%{appdefdir}/ja_JP.UTF-8/app-defaults/M17NEdit
find %{buildroot} -type f -name "*.la" -delete -print
find %{buildroot} -type f -name "*.la" -delete -print

%fdupes %{buildroot}

%post -n libm17n0 -p /sbin/ldconfig
%postun -n libm17n0 -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README ChangeLog
%{_bindir}/*
%dir %{appdefdir}/??
%dir %{appdefdir}/??_*
%dir %{appdefdir}/*/app-defaults
%{appdefdir}/*/app-defaults/M17NEdit

%files -n libm17n0
%{_libdir}/lib*.so.*
%{_libdir}/m17n

%files devel
%{_includedir}/*
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc

%changelog
