#
# spec file for package libdatrie
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


Name:           libdatrie
Version:        0.2.10
Release:        0
Summary:        Double-Array Trie Library
License:        LGPL-2.1
Group:          Development/Libraries/C and C++
Url:            https://linux.thai.net/~thep/datrie/datrie.html
Source:         https://linux.thai.net/pub/thailinux/software/libthai/%{name}-%{version}.tar.xz
Source99:       baselibs.conf
BuildRequires:  autoconf-archive
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xz

%description
This is an implementation of double-array structure for representing
trie, as proposed by Junichi Aoe.

%package -n libdatrie1
Summary:        Double-Array Trie Library
Group:          System/Libraries

%description -n libdatrie1
This is an implementation of double-array structure for representing
trie, as proposed by Junichi Aoe.

%package devel
Summary:        Development files for the Double-Array Trie library
Group:          Development/Libraries/C and C++
Requires:       libdatrie1 = %{version}

%description devel
This is an implementation of double-array structure for representing
trie, as proposed by Junichi Aoe.

This package contains the development files for libdatrie.

%prep
%setup -q

%build
autoreconf -fiv
%configure \
        --disable-static \
        --with-html-docdir=%{_docdir}/libdatrie/html
make %{?_smp_mflags}

%install
%make_install
rm -f %{buildroot}%{_libdir}/libdatrie.la
# This is not installed where it should
mv %{buildroot}%{_datadir}/doc/libdatrie/README.migration %{buildroot}%{_docdir}/libdatrie/

%post -n libdatrie1 -p /sbin/ldconfig
%postun -n libdatrie1 -p /sbin/ldconfig

%files -n libdatrie1
%doc AUTHORS ChangeLog COPYING README
%{_libdir}/libdatrie.so.1*

%files devel
%{_bindir}/trietool*
%{_mandir}/man*/trietool*.1%{ext_man}
%{_includedir}/datrie/
%{_libdir}/libdatrie.so
%{_libdir}/pkgconfig/datrie-0.2.pc
%doc %{_docdir}/libdatrie/

%changelog
