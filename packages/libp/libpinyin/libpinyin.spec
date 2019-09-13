#
# spec file for package libpinyin
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           libpinyin
Version:        2.3.0
Release:        0
Summary:        Intelligent Pinyin IME
License:        GPL-3.0-or-later
Group:          System/I18n/Chinese
Url:            https://github.com/libpinyin/libpinyin
Source:         https://github.com/libpinyin/libpinyin/releases/download/%{version}/%{name}-%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM marguerite@opensuse.org - AX_CXX_COMPILE_CXX([11])
# breaks Leap 42.1 builds while of no actual use
Patch1:         libpinyin-1.7.0-no-AX_CXX_COMPILE_STDCXX_11.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(kyotocabinet)

%description
libpinyin is an intelligent (and universal) sentence-based Pinyin IME
backend supporting many language models and frontends.

%package -n %{name}%{sover}
Summary:        Intelligent Pinyin IME
Group:          System/Libraries
Requires:       %{name}-data

%description -n %{name}%{sover}
libpinyin is a staging joint effort of many Chinese Pinyin IME development
teams. It is an intelligent (and universal) sentence-based Pinyin IME backend
supporting many language models and frontends.

This package provides runtime library for libpinyin.

%package -n libzhuyin%{sover}
Summary:        Intelligent Pinyin IME
Group:          System/Libraries
Requires:       %{name}-data

%description -n libzhuyin%{sover}
libpinyin is a staging joint effort of many Chinese Pinyin IME development
teams. It is an intelligent (and universal) sentence-based Pinyin IME backend
supporting many language models and frontends.

This package provides runtime library for libpinyin.

%package data
Summary:        Data files for the libpinyin IME
Group:          System/I18n/Chinese

%description data
libpinyin is an intelligent (and universal) sentence-based Pinyin IME
backend supporting many language models and frontends.

This package provides language model table data for libpinyin.

%package devel
Summary:        Development files for the libpinyin IME
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
Requires:       %{name}-tools = %{version}
Provides:       libzhuyin-devel = %{version}

%description devel
libpinyin is an intelligent (and universal) sentence-based Pinyin IME
backend supporting many language models and frontends.

This subpackage contains the development files.

%package tools
Summary:        Tools for libpinyin
Group:          System/I18n/Chinese

%description tools
libpinyin is an intelligent (and universal) sentence-based Pinyin IME
backend supporting many language models and frontends.

This package provides the tools used to make data files.

%prep
%setup -q
%patch1 -p1

%build
autoreconf -ifv
# NOCONFIGURE=1 ./autogen.sh
%configure \
    --disable-static \
    --with-dbm=KyotoCabinet \
    --disable-silent-rules \
    --enable-libzhuyin
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
%fdupes %{buildroot}/%{_prefix}

%check
make %{?_smp_mflags} check

%post -n %{name}%{sover} -p /sbin/ldconfig
%postun -n %{name}%{sover} -p /sbin/ldconfig
%post -n libzhuyin%{sover} -p /sbin/ldconfig
%postun -n libzhuyin%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%doc COPYING
%{_libdir}/%{name}.so.*

%files -n libzhuyin%{sover}
%defattr(-,root,root)
%doc ChangeLog AUTHORS README
%license COPYING
%{_libdir}/libzhuyin.so.*

%files data
%defattr(-,root,root)
%{_libdir}/%{name}

%files tools
%defattr(-,root,root)
%{_bindir}/gen_binary_files
%{_bindir}/gen_unigram
%{_bindir}/import_interpolation

%files devel
%defattr(-,root,root)
%doc ChangeLog AUTHORS README
%{_includedir}/%{name}-*/
%{_libdir}/%{name}.so
%{_libdir}/libzhuyin.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/libzhuyin.pc
%{_mandir}/man1/libpinyin.1%{ext_man}

%changelog
