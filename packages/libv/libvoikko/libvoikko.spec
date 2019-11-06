#
# spec file for package libvoikko
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


Name:           libvoikko
Version:        4.3
Release:        0
Summary:        Library of free natural language processing tools
License:        GPL-2.0-or-later
Group:          Productivity/Text/Spell
URL:            http://voikko.puimula.org
Source0:        http://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz
Source1:        http://www.puimula.org/voikko-sources/%{name}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source99:       baselibs.conf
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(hfstospell)

%description
Libvoikko is a library of free natural language processing tools. It
aims to provide support for languages that are not well served by
other existing free linguistic tools. 

The library supports multiple backends, of which VFST and HFST are
enabled in the default build:

 - VFST: Finite state transducer format used for Finnish morphology
   and as an experimental language independent backend.
 - HFST (Helsinki Finite-State Transducer Technology): Supports ZHFST
   speller archives for various languages.
 - Experimental backends: Weighted VFST and Lttoolbox.

Libvoikko provides spell checking, hyphenation, grammar checking and
morphological analysis for Finnish language. Spell checking is
supported for other languages through the HFST backend.

%package -n libvoikko1
Summary:        Library of free natural language processing tools
Group:          System/Libraries
Requires:       malaga-suomi

%description -n libvoikko1
Libvoikko is a library of free natural language processing tools. It
aims to provide support for languages that are not well served by
other existing free linguistic tools. 

The library supports multiple backends, of which VFST and HFST are
enabled in the default build:

 - VFST: Finite state transducer format used for Finnish morphology
   and as an experimental language independent backend.
 - HFST (Helsinki Finite-State Transducer Technology): Supports ZHFST
   speller archives for various languages.
 - Experimental backends: Weighted VFST and Lttoolbox.

Libvoikko provides spell checking, hyphenation, grammar checking and
morphological analysis for Finnish language. Spell checking is
supported for other languages through the HFST backend.

%package devel
Summary:        Library of free natural language processing tools
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libvoikko1 = %{version}

%description devel
Libvoikko is a library of free natural language processing tools. It
aims to provide support for languages that are not well served by
other existing free linguistic tools. 

This package contains the files needed to build or develop applications
that use Voikko.

%package -n voikkospell
Summary:        Test program for Voikko spell checker
Group:          Productivity/Text/Spell
Requires:       libvoikko1 = %{version}

%description -n voikkospell
Libvoikko is a library of free natural language processing tools. It
aims to provide support for languages that are not well served by
other existing free linguistic tools. 

This package contains a test program for using Voikko spell checker.

%package -n     python3-libvoikko
Summary:        Python interface to %{name}
Group:          Development/Libraries/Python
Requires:       libvoikko1 = %{version}-%{release}
BuildArch:      noarch

%description -n python3-libvoikko
Libvoikko is a library of free natural language processing tools. It
aims to provide support for languages that are not well served by
other existing free linguistic tools. 

This package contains a Python interface to libvoikko. This module 
can be used to perform various natural language analysis tasks on text.

%prep
%setup -q

%build
%configure \
	--disable-silent_rules \
	--disable-static \
	--with-dictionary-path=%{_libexecdir}/voikko:%{_datadir}/voikko
make %{?_smp_mflags}

%check
make %{?_smp_mflags} check || :

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

install -d %{buildroot}/%{python3_sitelib}
install -pm 0644 python/libvoikko.py %{buildroot}/%{python3_sitelib}/

%post -n libvoikko1 -p /sbin/ldconfig
%postun -n libvoikko1 -p /sbin/ldconfig

%files -n libvoikko1
%license COPYING
%doc ChangeLog README
%{_libdir}/*.so.*

%files -n voikkospell
%{_bindir}/*
%{_mandir}/man?/*%{ext_man}

%files devel
%{_includedir}/libvoikko
%{_libdir}/*.so
%{_libdir}/pkgconfig/libvoikko.pc

%files -n python3-libvoikko
%{python3_sitelib}/*

%changelog
