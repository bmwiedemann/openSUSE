#
# spec file for package schroedinger
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


Name:           schroedinger
Version:        1.0.11
Release:        0
Summary:        Library for decoding and encoding video in the Dirac format
License:        GPL-2.0-only AND LGPL-2.0-only AND MPL-1.1 AND MIT
Group:          Productivity/Multimedia/Other
URL:            http://schrodinger.sourceforge.net/schrodinger_faq.php
# DEAD: http://diracvideo.org/download/schroedinger/%{name}-%{version}.tar.gz
Source:         %{name}-%{version}.tar.gz
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  gtk-doc
BuildRequires:  orc >= 0.4.16
BuildRequires:  pkgconfig

%description
The Schroedinger project implements portable libraries for the high
quality Dirac video codec created by BBC Research and Development.
Dirac is a free and open source codec producing very high image quality
video. The project produces two libraries in ANSI C89, one for decoding
and one for encoding.

%package -n libschroedinger-1_0-0
Summary:        Library for decoding and encoding video in the Dirac format
Group:          Productivity/Multimedia/Other
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}

%description -n libschroedinger-1_0-0
The Schroedinger project implements portable libraries for the high
quality Dirac video codec created by BBC Research and Development.
Dirac is a free and open source codec producing very high image quality
video. The project produces two libraries in ANSI C89, one for decoding
and one for encoding.

%package devel
Summary:        Library for decoding and encoding video in the Dirac format
Group:          Development/Libraries/Other
Requires:       glib2-devel
Requires:       libschroedinger-1_0-0 = %{version}
Requires:       orc
Provides:       libschroedinger-devel = %{version}-%{release}

%description devel
The Schroedinger project implements portable libraries for the high
quality Dirac video codec created by BBC Research and Development.
Dirac is a free and open source codec producing very high image quality
video. The project produces two libraries in ANSI C89, one for decoding
and one for encoding.

%package doc
Summary:        Library for decoding and encoding video in the Dirac format
Group:          Productivity/Multimedia/Other
Requires:       libschroedinger-1_0-0 = %{version}

%description doc
The Schroedinger project implements portable libraries for the high
quality Dirac video codec created by BBC Research and Development.
Dirac is a free and open source codec producing very high image quality
video. The project produces two libraries in ANSI C89, one for decoding
and one for encoding.

%prep
%setup -q
sed -i -e 's:testsuite::g' Makefile.{am,in}

%build
%configure\
	--disable-static
make %{?_smp_mflags} docdir=%{_docdir}/%{name}

%install
%make_install docdir=%{_docdir}/%{name}
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libschroedinger-1_0-0 -p /sbin/ldconfig
%postun -n libschroedinger-1_0-0 -p /sbin/ldconfig

%files -n libschroedinger-1_0-0
%license COPYING COPYING.MIT COPYING.GPL COPYING.LGPL COPYING.MPL
%doc AUTHORS
%{_libdir}/*.so.0*

%files devel
%{_includedir}/schroedinger-1.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%{_datadir}/gtk-doc/html/schroedinger

%changelog
