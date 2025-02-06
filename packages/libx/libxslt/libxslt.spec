#
# spec file for package libxslt
#
# Copyright (c) 2025 SUSE LLC
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


%define libver      1
%define libexver    0

Name:           libxslt
Version:        1.1.42
Release:        0
Summary:        XSL Transformation Library
License:        GPL-2.0-or-later AND MIT
Group:          Development/Libraries/C and C++
URL:            https://gitlab.gnome.org/GNOME/libxslt
Source0:        https://download.gnome.org/sources/%{name}/1.1/%{name}-%{version}.tar.xz
Source1:        baselibs.conf
Source2:        xslt-config.1

# PATCH-FIX-OPENSUSE -- libxslt-1.1.24-no-net-autobuild.patch
#   The xmlGetExternalEntityLoader() tries to fetch/parse some information via
#   internet, which OBS's build environment does not allow it.
Patch0:         libxslt-1.1.24-no-net-autobuild.patch
# PATCH-FIX-UPSTREAM -- libxslt-random-seed.patch
#   https://bugzilla.suse.com/show_bug.cgi?id=934119
#   https://bugzilla.gnome.org/show_bug.cgi?id=758400
#   Initialize the random seed to ensure libxslt's math.random() function
#   produces unpredictable outputs.
Patch1:         libxslt-random-seed.patch
Patch2:         libxslt-reproducible.patch
# PATCH-FIX-UPSTREAM -- libxslt-test-compile-with-older-libxml2-versions.patch
#   https://gitlab.gnome.org/GNOME/libxslt/-/issues/125
Patch3:         libxslt-test-compile-with-older-libxml2-versions.patch
#
### SUSE patches starts on 1000
# PATCH-FIX-SUSE
#Patch1000:
#
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  libgcrypt-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml-2.0) >= 2.9.12
Obsoletes:      libxslt-python

%description
This C library allows you to transform XML files into other XML files
(or HTML, text, and more) using the standard XSLT stylesheet
transformation mechanism.

It is based on libxml (version 2) for XML parsing, tree manipulation,
and XPath support. It is written in plain C, making as few assumptions
as possible and sticks closely to ANSI C/POSIX for easy embedding.
It includes support for the EXSLT set of extension functions as well
as some common extensions present in other XSLT engines.

%package -n libxslt%{libver}
Summary:        XSL Transformation Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libxslt%{libver}
This C library allows you to transform XML files into other XML files
(or HTML, text, and more) using the standard XSLT stylesheet
transformation mechanism.

It is based on libxml (version 2) for XML parsing, tree manipulation,
and XPath support. It is written in plain C, making as few assumptions
as possible and sticks closely to ANSI C/POSIX for easy embedding.
It includes support for the EXSLT set of extension functions as well
as some common extensions present in other XSLT engines.

%package -n libexslt%{libexver}
Summary:        EXSLT Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libexslt%{libexver}
This is the EXSLT C library developed for libxslt.
EXSLT is a community initiative to provide extensions to XSLT.

%package devel
Summary:        Development files for libxslt
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{name}-tools = %{version}
Requires:       glibc-devel
Requires:       libexslt%{libexver} = %{version}
Requires:       libgcrypt-devel
Requires:       libxslt%{libver} = %{version}

%description devel
libxslt allows you to transform XML files into other XML files
(or HTML, text, and more) using the standard XSLT stylesheet
transformation mechanism.

This subpackage contains the header files for developing
applications that want to make use of the XSLT libraries.

%package tools
Summary:        Extended Stylesheet Language (XSL) Transformation utilities
License:        GPL-2.0-or-later AND MIT
Group:          Development/Tools/Other
Provides:       %{name} = %{version}
Provides:       xsltproc = %{version}

%description tools
This package contains xsltproc, a command line interface to the XSLT engine.
xtend the

%prep
%autosetup -p1

%build
%configure \
    --disable-static \
    --without-python \
    --disable-silent-rules
%make_build

%check
find -type f -name "test_bad*" -delete -print
%make_build check

%install
%make_install

# Unwanted doc stuff
rm -fr %{buildroot}%{_datadir}/doc
# Install the manual page for xslt-config
install -D -m0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/xslt-config.1
#kill all "la" files
find %{buildroot} -type f -name "*.la" -delete -print

# Hardlink same-content files
%fdupes %{buildroot}%{_datadir}

%ldconfig_scriptlets -n libxslt%{libver}
%ldconfig_scriptlets -n libexslt%{libexver}

%files -n libxslt%{libver}
%license COPYING* Copyright
%{_libdir}/libxslt.so.%{libver}*

%files -n libexslt%{libexver}
%license COPYING* Copyright
%{_libdir}/libexslt.so.%{libexver}*

%files tools
%license COPYING* Copyright
%doc AUTHORS NEWS TODO FEATURES
%{_bindir}/xsltproc
%{_mandir}/man1/xsltproc.1%{?ext_man}

%files devel
%license COPYING* Copyright
%{_libdir}/libxslt.so
%{_libdir}/libexslt.so
%{_libdir}/*.sh
%{_libdir}/pkgconfig/libxslt.pc
%{_libdir}/pkgconfig/libexslt.pc
%dir %{_libdir}/cmake/libxslt/
%{_libdir}/cmake/libxslt/FindGcrypt.cmake
%{_libdir}/cmake/libxslt/libxslt-config.cmake
%{_includedir}/*
%{_bindir}/xslt-config
%{_mandir}/man1/xslt-config.1%{?ext_man}
%{_mandir}/man3/*
%dir %{_datadir}/gtk-doc/
%dir %{_datadir}/gtk-doc/html/
%{_datadir}/gtk-doc/html/libexslt/
%{_datadir}/gtk-doc/html/libxslt/
%doc doc/*.html doc/tutorial doc/tutorial2

%changelog
