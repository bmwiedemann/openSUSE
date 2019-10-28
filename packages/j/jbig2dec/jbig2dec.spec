#
# spec file for package jbig2dec
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           jbig2dec
Version:        0.14
Release:        0
Summary:        JBIG2 Decoder Utility
License:        AGPL-3.0+
Group:          Productivity/Other
URL:            https://www.ghostscript.com/jbig2dec.html
Source:         http://downloads.ghostscript.com/public/jbig2dec/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  pkgconfig(libpng)

%description
jbig2dec is a decoder utility implementing the JBIG2 bi-level image compression
spec. Also known as ITU T.88 and ISO IEC 14492, and included by reference in
Adobe's PDF version 1.4 and later.

%package -n libjbig2dec0
Summary:        JBIG2 Decoder Library
Group:          System/Libraries

%description -n libjbig2dec0
jbig2dec is a decoder utility implementing the JBIG2 bi-level image compression
spec. Also known as ITU T.88 and ISO IEC 14492, and included by reference in
Adobe's PDF version 1.4 and later.

%package devel
Summary:        JBIG2 decoder development files
Group:          Development/Libraries/C and C++
Requires:       libjbig2dec0 = %{version}

%description devel
This package contains development files needed for developing applications
based on libjbig2dec.

%prep
%setup -q

%build
export CFLAGS="%{optflags} -fPIC"
export LDFLAGS="-pie"
%configure \
  --disable-static \
  --with-libpng
make %{?_smp_mflags}

%install
%make_install
# Install missing header
install -c -m 644 memento.h %{buildroot}%{_includedir}/memento.h
rm %{buildroot}%{_libdir}/libjbig2dec.la

%post -n libjbig2dec0 -p /sbin/ldconfig
%postun -n libjbig2dec0 -p /sbin/ldconfig

%files
%doc CHANGES README
%license COPYING LICENSE
%{_bindir}/jbig2dec
%{_mandir}/man1/jbig2dec.1%{ext_man}

%files -n libjbig2dec0
%{_libdir}/libjbig2dec.so.*

%files devel
%{_includedir}/jbig2.h
%{_includedir}/memento.h
%{_libdir}/libjbig2dec.so

%changelog
