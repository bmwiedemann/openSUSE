#
# spec file for package libspf2
#
# Copyright (c) 2022 SUSE LLC
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


Name:           libspf2
%define lname	libspf2-2
Version:        1.2.11
Release:        0
%global fname   %{name}-%{version}-4915c308
Summary:        Implementation of the Sender Policy Framework
License:        BSD-2-Clause OR LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.libspf2.org/
Source0:        %{fname}.tar.xz
# SPF_debugf macro should always have at least two parameters
Patch0:         libspf2-1.2.10-format.patch
# PATCH-FIX-OPENSUSE Drop usage of libreplace
Patch1:         libspf2-1.2.10-libreplace.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
# For API docs
BuildRequires:  automake
BuildRequires:  autoconf
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  ghostscript-fonts-std
BuildRequires:  graphviz-gd
BuildRequires:  libtool
# For perl bindings (Makefile.PL claims Mail::SPF is needed, but it isn't)
BuildRequires:  perl
BuildRequires:  perl(DynaLoader)
BuildRequires:  perl(Exporter)
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(strict)
BuildRequires:  perl(vars)
BuildRequires:  perl(warnings)
# For perl test suite
BuildRequires:  perl(String::Escape)
BuildRequires:  perl(Test::Pod)
# POD Coverage is non-existent, causes test suite to fail
BuildConflicts: perl(Test::Pod::Coverage)
# Perl module fails the standard test suite
BuildConflicts: perl(Mail::SPF::Test)

%description
Implementation of the Sender Policy Framework, a part of the SPF/SRS protocol
pair.

%package -n %{lname}
Summary:        An implementation of the SPF specification
License:        BSD-2-Clause OR LGPL-2.1-or-later
Group:          System/Libraries

%description -n %{lname}
libspf2 is an implementation of the SPF (Sender Policy Framework)
specification as found at:
http://www.ietf.org/internet-drafts/draft-mengwong-spf-00.txt
SPF allows email systems to check SPF DNS records and make sure that
an email is authorized by the administrator of the domain name that
it is coming from. This prevents email forgery, commonly used by
spammers, scammers, and email viruses/worms.

A lot of effort has been put into making it secure by design, and a
great deal of effort has been put into the regression tests.

%package devel
Summary:        Development files for libspf
License:        BSD-2-Clause OR LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}

%description devel
The libspf2-devel package contains the header files and static
libraries necessary for developing programs using the libspf2 (Sender
Policy Framework) library.

If you want to develop programs that will look up and process SPF records,
you should install libspf2-devel.

API documentation is in the separate libspf2-apidocs package.

%package apidocs
Summary:        API documentation for the libspf2 library
License:        BSD-2-Clause OR LGPL-2.1-or-later
Group:          Documentation
BuildArch:      noarch

%description apidocs
The libspf2-apidocs package contains the API documentation for creating
applications that use the libspf2 (Sender Policy Framework) library.

%package tools
Summary:        Programs for making SPF queries using libspf2
License:        BSD-2-Clause OR LGPL-2.1-or-later
Group:          Applications/System
Obsoletes:      spf2 < %{version}-%{release}
Provides:       spf2 = %{version}-%{release}

%description tools
Programs for making SPF queries and checking their results using libspf2.

%package -n perl-Mail-SPF_XS
Summary:        An XS implementation of Mail::SPF
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries
Version:        0.01
Release:        0
Requires:       perl(:MODULE_COMPAT_%(eval "`perl -V:version`"; echo $version))

%description -n perl-Mail-SPF_XS
This is an interface to the C library libspf2 for the purpose of
testing. While it can be used as an SPF implementation, you can also
use Mail::SPF, which is a little more perlish.

%prep
%autosetup -p0 -n %{fname}
# libreplace is not needed on modern Linux
rm -rf src/libreplace
find . "(" -name Makefile.am -o -name Makefile.in ")" -exec touch {} +

%build
autoreconf -vif
%configure --enable-perl --disable-dependency-tracking
# using --disable-static does not build

# Kill bogus RPATHs
sed -i 's|^sys_lib_dlsearch_path_spec="/lib /usr/lib|sys_lib_dlsearch_path_spec="/%{_lib} %{_libdir}|' libtool

make %{?_smp_mflags} CFLAGS="%{optflags} -fno-strict-aliasing"

# Generate API docs
sed -i -e 's/\(SHORT_NAMES[[:space:]]*=[[:space:]]*\)NO/\1YES/' Doxyfile
doxygen
rm -f doxygen/html/*.map
rm -f doxygen/html/*.md5

%install
%make_install \
	PERL_INSTALL_ROOT=$(grep DESTDIR perl/Makefile &> /dev/null && echo "" || echo %{buildroot}) \
	INSTALLDIRS=vendor \
	INSTALL="install -p"

# Clean up after impure perl installation
find %{buildroot} \( -name perllocal.pod -o -name .packlist \) -delete
find %{buildroot} -type f -name '*.bs' -size 0 -delete
%{_fixperms} %{buildroot}

# Don't want statically-linked binaries
rm -f %{buildroot}%{_bindir}/spf*_static

mv %{buildroot}%{_bindir}/spfquery %{buildroot}%{_bindir}/spf_query

mkdir -p %{buildroot}%{_docdir}/spf2-apidocs/
cp -r doxygen/html %{buildroot}%{_docdir}/spf2-apidocs/html
%fdupes %{buildroot}%{_docdir}/spf2-apidocs/

%check
LD_PRELOAD=$(pwd)/src/libspf2/.libs/libspf2.so make -C perl test

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%files -n %{lname}
%doc README TODO
%license LICENSES
%{_libdir}/libspf2.so.*

%files devel
%dir %{_includedir}/spf2
%{_includedir}/spf2/spf*.h
%{_libdir}/libspf2.so
%exclude %{_libdir}/libspf2.a
%exclude %{_libdir}/libspf2.la

%files apidocs
%doc %{_docdir}/spf2-apidocs

%files tools
%{_bindir}/spfd
%{_bindir}/spf_query
%{_bindir}/spftest
%{_bindir}/spf_example

%files -n perl-Mail-SPF_XS
%{perl_vendorarch}/Mail/
%{perl_vendorarch}/auto/Mail/
%{_mandir}/man3/Mail::SPF_XS.3*

%changelog
