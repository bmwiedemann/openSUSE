#
# spec file for package jbigkit
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define ver_maj 2
%define ver_min 2
%define libname libjbig
%define soversion %{ver_maj}
%define libpkg %{libname}%{soversion}
%define devpkg %{libname}-devel
Name:           jbigkit
Version:        %{ver_maj}.%{ver_min}
Release:        0
Summary:        JBIG1 lossless image compression tools
License:        GPL-2.0-or-later
URL:            https://www.cl.cam.ac.uk/~mgk25/jbigkit/
Source0:        https://www.cl.cam.ac.uk/~mgk25/download/%{name}-%{version}.tar.gz
Source42:       baselibs.conf
Patch0:         jbigkit-2.1-shlib.patch
BuildRequires:  gcc
BuildRequires:  make

%package -n %{libpkg}
Summary:        JBIG1 lossless image compression library
Provides:       %{libname} = %{version}

%package -n %{devpkg}
Summary:        JBIG1 lossless image compression library -- development files
Requires:       %{libpkg} = %{version}

%description -n %{libpkg}
JBIG-KIT provides a portable library of compression and decompression
functions with a documented interface that you can include very easily
into your image or document processing software. In addition, JBIG-KIT
provides ready-to-use compression and decompression programs with a
simple command line interface (similar to the converters found in
netpbm).

JBIG-KIT implements the specification:
    ISO/IEC 11544:1993 and ITU-T Recommendation T.82(1993):
     Information technology — Coded representation of picture and audio
     information — Progressive bi-level image compression

which is commonly referred to as the “JBIG1 standard”

%description -n %{devpkg}
The libjbig-devel package contains files needed for development using
the JBIG-KIT image compression library.

%description
The jbigkit package contains tools for converting between PBM and JBIG1
formats.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} -I../libjbig" CXXFLAGS="%{optflags}"
%make_build

%check
%make_build test

%install
install -d %{buildroot}/%{_libdir}
install -m 0755 libjbig/libjbig.so.%{version} %{buildroot}/%{_libdir}
install -m 0755 libjbig/libjbig85.so.%{version} %{buildroot}/%{_libdir}
ln -s -f libjbig.so.%{version} %{buildroot}/%{_libdir}/libjbig.so.%{soversion}
ln -s -f libjbig85.so.%{version} %{buildroot}/%{_libdir}/libjbig85.so.%{soversion}
ln -s -f libjbig.so.%{version} %{buildroot}/%{_libdir}/libjbig.so
ln -s -f libjbig85.so.%{version} %{buildroot}/%{_libdir}/libjbig85.so

install -d %{buildroot}%{_includedir}
install -m 0644 libjbig/jbig*.h %{buildroot}%{_includedir}

install -d %{buildroot}%{_bindir}
install -m 0755 pbmtools/pbmtojbg %{buildroot}%{_bindir}
install -m 0755 pbmtools/jbgtopbm %{buildroot}%{_bindir}
install -m 0755 pbmtools/pbmtojbg85 %{buildroot}%{_bindir}
install -m 0755 pbmtools/jbgtopbm85 %{buildroot}%{_bindir}

install -d %{buildroot}%{_mandir}/man1
install -m 0644 pbmtools/*.1 %{buildroot}%{_mandir}/man1
ln -s -f pbmtojbg.1 %{buildroot}%{_mandir}/man1/pbmtojbg85.1
ln -s -f jbgtopbm.1 %{buildroot}%{_mandir}/man1/jbgtopbm85.1

%ldconfig_scriptlets -n %{libpkg}

%files
%{_bindir}/*
%{_mandir}/man1/*
%license COPYING
%doc ANNOUNCE TODO CHANGES pbmtools/*.txt

%files -n %{libpkg}
%{_libdir}/%{libname}*.so.*

%files -n %{devpkg}
%{_libdir}/%{libname}*.so
%{_includedir}/jbig*.h
%license COPYING
%doc ANNOUNCE TODO CHANGES libjbig/*.txt

%changelog
