#
# spec file for package wv
#
# Copyright (c) 2024 SUSE LLC
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


%global lname	libwv-1_2-4
Name:           wv
Version:        1.2.9
Release:        0
Summary:        Tools for Importing Microsoft Word (tm) Documents
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/Word
URL:            http://wvware.sourceforge.net/
Source0:        https://www.abisource.com/downloads/%{name}/%{version}/%{name}-%{version}.tar.gz
Patch1:         detect-imagick.patch
Patch2:         man-refs.patch
Patch3:         man-wvrtf-name.patch
Patch4:         man-wvware-options.patch
Patch5:         non-latin-latex.patch
Patch6:         wvdvi-output-ext.patch
Patch7:         wvmime.patch
Patch8:         wvtext-no-graphics.patch
Patch9:         wvware-no-placeholder.patch
Patch10:        man-wvware-typo.patch
Patch11:        hardening-format.patch
Patch12:        man-remove-PU.patch
Patch13:        cross.patch
Patch14:        0014-Add-missing-include.patch
BuildRequires:  libexpat-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
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
%autosetup -p1

%build
perl -i -lpe 's{AM_INIT_AUTOMAKE.*}{AM_INIT_AUTOMAKE([foreign subdir-objects])}g' configure.ac
autoreconf -f -i --verbose
%define warn_flags -Wall -Wstrict-prototypes -Wpointer-arith -Wformat -Wformat-security
CFLAGS="%{optflags} %{warn_flags} -fno-strict-aliasing -fstack-protector" \
%configure \
    --with-libwmf \
    --with-expat \
    --disable-dependency-tracking \
    --disable-static

%make_build

%install
%make_install manonedir=%{_mandir}/man1
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%ldconfig_scriptlets -n %{lname}

%files
%license COPYING
%doc README
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
