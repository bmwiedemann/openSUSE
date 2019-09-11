#
# spec file for package wv
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


%global lname	libwv-1_2-4
Name:           wv
Version:        1.2.9
Release:        0
Summary:        Tools for Importing Microsoft Word (tm) Documents
License:        GPL-2.0+
Group:          Productivity/Publishing/Word
Url:            http://wvware.sourceforge.net/
Source0:        https://www.abisource.com/downloads/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch0:         wv-1.2.2-automake.patch
Patch5:         wv-1.0.3-wvText.patch
Patch9:         wv-1.2.2-fiximplicit.patch
Patch10:        wv-strcasecmp.patch
Patch11:        wv-gsf.patch
Patch12:        wv-noansi.patch
BuildRequires:  libtool
BuildRequires:  libwmf-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(zlib)
Requires:       w3m

%description
WV is a program that can understand the Microsoft Word 8 binary file
format (Office97). It currently converts Word into HTML, which can then
be read with a web browser.

%package -n %{lname}
Summary:        Library for importing Microsoft Word documents
Group:          System/Libraries

%description -n %{lname}
libwv can parse the Microsoft Word 8 binary file format (Office97).

%package devel
Summary:        Header files for wv
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       libgsf-devel
Requires:       libwmf-devel

%description devel
Header files for wv.

%prep
%setup -q
%patch0
%patch5
%patch9 -p1
%patch10 -p1
%if 0%{?suse_version} > 1230
%patch11 -p1
%endif
%patch12 -p1

%build
autoreconf -f -i --verbose
%define warn_flags -Wall -Wstrict-prototypes -Wpointer-arith -Wformat -Wformat-security
CFLAGS="%{optflags} %{warn_flags} -fno-strict-aliasing -fstack-protector" \
%configure \
    --with-libwmf \
    --with-expat \
    --disable-dependency-tracking \
    --disable-static

make %{?_smp_mflags}

%install
%make_install manonedir=%{_mandir}/man1
find %{buildroot} -type f -name "*.la" -delete -print

%check
make %{?_smp_mflags} check

%post -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%doc COPYING README
%{_bindir}/wvAbw
%{_bindir}/wvCleanLatex
%{_bindir}/wvConvert
%{_bindir}/wvDVI
%{_bindir}/wvHtml
%{_bindir}/wvLatex
%{_bindir}/wvMime
%{_bindir}/wvPDF
%{_bindir}/wvPS
%{_bindir}/wvRTF
%{_bindir}/wvSummary
%{_bindir}/wvText
%{_bindir}/wvVersion
%{_bindir}/wvWare
%{_bindir}/wvWml
%{_bindir}/wvDocBook
%{_datadir}/wv
%{_mandir}/*/*

%files -n %{lname}
%{_libdir}/libwv-1.2.so.*

%files devel
%{_includedir}/wv
%{_libdir}/libwv.so
%{_libdir}/pkgconfig/%{name}-1.0.pc

%changelog
