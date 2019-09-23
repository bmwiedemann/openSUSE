#
# spec file for package jbigkit
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           jbigkit
%define ver_maj 2
%define ver_min 1
Version:        %{ver_maj}.%{ver_min}
Release:        0
Summary:        JBIG1 lossless image compression tools
License:        GPL-2.0+
Group:          Productivity/Graphics/Convertors
Url:            http://www.cl.cam.ac.uk/~mgk25/jbigkit/
Source0:        http://www.cl.cam.ac.uk/~mgk25/download/%{name}-%{version}.tar.gz
Source42:       baselibs.conf
Patch0:         %{name}-%{version}-shlib.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%define libname libjbig
%define soversion %ver_maj
%define libpkg %{libname}%soversion
%define devpkg %{libname}-devel

%package -n %libpkg
Summary:        JBIG1 lossless image compression library
Group:          System/Libraries
Provides:       %libname = %version

%package -n %devpkg
Summary:        JBIG1 lossless image compression library -- development files
Group:          Development/Libraries/C and C++
Requires:       %libpkg = %version

%description -n %libpkg
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

%description -n %devpkg
The libjbig-devel package contains files needed for development using 
the JBIG-KIT image compression library.

%description
The jbigkit package contains tools for converting between PBM and JBIG1
formats.

%prep
%setup
%patch0 -p1

%build
export CFLAGS="%optflags -I../libjbig" CXXFLAGS="%optflags"
%__make %{?_smp_mflags}

%check
%__make test

%install
%__install -d %{buildroot}/%_libdir
%__install -m 0755 libjbig/libjbig.so.%version %{buildroot}/%_libdir
%__install -m 0755 libjbig/libjbig85.so.%version %{buildroot}/%_libdir
%__ln_s -f libjbig.so.%version %{buildroot}/%{_libdir}/libjbig.so.%soversion
%__ln_s -f libjbig85.so.%version %{buildroot}/%{_libdir}/libjbig85.so.%soversion
%__ln_s -f libjbig.so.%version %{buildroot}/%{_libdir}/libjbig.so
%__ln_s -f libjbig85.so.%version %{buildroot}/%{_libdir}/libjbig85.so

%__install -d %{buildroot}%_includedir
%__install -m 0644 libjbig/jbig*.h %{buildroot}%_includedir

%__install -d %{buildroot}%_bindir
%__install -m 0755 pbmtools/pbmtojbg %{buildroot}%_bindir
%__install -m 0755 pbmtools/jbgtopbm %{buildroot}%_bindir
%__install -m 0755 pbmtools/pbmtojbg85 %{buildroot}%_bindir
%__install -m 0755 pbmtools/jbgtopbm85 %{buildroot}%_bindir

%__install -d %{buildroot}%{_mandir}/man1
%__install -m 0644 pbmtools/*.1 %{buildroot}%{_mandir}/man1
%__ln_s -f pbmtojbg.1 %{buildroot}%{_mandir}/man1/pbmtojbg85.1
%__ln_s -f jbgtopbm.1 %{buildroot}%{_mandir}/man1/jbgtopbm85.1

%post -n %libpkg -p /sbin/ldconfig

%postun -n %libpkg -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/*
%doc %{_mandir}/man1/*
%doc COPYING ANNOUNCE TODO CHANGES pbmtools/*.txt

%files -n %libpkg
%defattr(-,root,root)
%{_libdir}/%{libname}*.so.*

%files -n %devpkg
%defattr(-,root,root)
%{_libdir}/%{libname}*.so
%{_includedir}/jbig*.h
%doc COPYING ANNOUNCE TODO CHANGES libjbig/*.txt

%changelog
