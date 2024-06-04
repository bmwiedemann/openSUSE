#
# spec file for package FastCGI
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


Name:           FastCGI
%define lname	libfcgi0
Version:        2.4.0
Release:        0
Summary:        A Scalable, Open Extension to CGI
License:        OML
Group:          Development/Languages/C and C++
URL:            https://fastcgi-archives.github.io/
Source:         https://github.com/FastCGI-Archives/fcgi2/archive/%{version}.tar.gz
Source1:        README.supervise
Patch0:         FastCGI-makefile.am_cppflags.patch
Patch1:         FastCGI-clientdata_pointer.patch
Patch2:         FastCGI-supervise_cgi-fcgi.patch
Patch3:         fastcgi-2.4.0_missing_call_to_fclose.patch
Patch4:         FastCGI-gcc44.patch
Patch5:         FastCGI-perl514.patch
Patch6:         FastCGI-fix_deprecated_api.patch
Patch7:         FastCGI-perl526.patch
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  perl
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
FastCGI is a language-independent, scalable, open extension to CGI that
provides high performance without the limitations of server-specific
APIs.

%package devel
Summary:        A scalable, open extension to CGI
Group:          Development/Languages/C and C++
Requires:       %lname = %version
Requires:       glibc-devel

%description devel
FastCGI is a language independent, scalable, open extension to CGI that
provides high performance without the limitations of server specific
APIs.

%package -n %lname
Summary:        A scalable, open extension to CGI - System library
Group:          System/Libraries
Obsoletes:      libfcgi++-0 < %version-%release
Provides:       libfcgi++-0 = %version-%release

%description -n %lname
FastCGI is a language independent, scalable, open extension to CGI that
provides high performance without the limitations of server specific
APIs.

%package -n perl-FastCGI
Summary:        A scalable, open extension to CGI
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
%if 0%{?suse_version} < 1120
Requires:       perl >= 5.8.0
%else
%{perl_requires}
%endif

%description -n perl-FastCGI
FastCGI is a language independent, scalable, open extension to CGI that
provides high performance without the limitations of server specific
APIs.

%prep
%autosetup -n fcgi2-%{version} -p0
touch NEWS AUTHORS ChangeLog COPYING
find doc/{fastcgi-prog-guide,fastcgi-whitepaper} -type f -print0 | xargs -r0 chmod 0644
cp include/fcgi_config.h.in .
cp include/fcgi_config.h.in perl

%build
libtoolize --force
aclocal
automake --add-missing
autoconf
%configure --disable-static --includedir=%{_includedir}/fastcgi
make all
pushd perl
    libtoolize --force
    aclocal -I..
    autoconf
    %configure --disable-static --includedir=%{_includedir}/fastcgi
    %{__perl} Makefile.PL
    make %{?_smp_mflags} all
popd

%install
%make_install
pushd perl
    %perl_make_install
    %perl_process_packlist
popd
pushd examples
    %{__make} clean
popd
%{__install} -Dd -m 0755                     \
    %{buildroot}%{_mandir}/man{1,3}/         \
    %{buildroot}%{_docdir}/%{name}/examples/
%{__install} -m 0644 examples/* %{buildroot}%{_docdir}/%{name}/examples/
%{__install} -m 0644 doc/*.1    %{buildroot}%{_mandir}/man1/
%{__install} -m 0644 doc/*.3    %{buildroot}%{_mandir}/man3/
%{__install} -m 0644 doc/*.htm* doc/*.gif LICENSE.TERMS README \
    %{buildroot}%{_docdir}/%{name}/
%{__install} -m 0644 perl/README    %{buildroot}%{_docdir}/%{name}/README.perl
%{__install} -m 0644 perl/ChangeLog %{buildroot}%{_docdir}/%{name}/ChangeLog.perl
%{__cp} -vr doc/{fastcgi-prog-guide,fastcgi-whitepaper} java %{S:1} \
    %{buildroot}%{_docdir}/%{name}/
rm -f %{buildroot}%{_libdir}/libfcgi*.la

%post   -n %lname -p /sbin/ldconfig
%postun -n %lname -p /sbin/ldconfig

%files
%defattr(-,root,root)
%{_bindir}/cgi-fcgi
%{_mandir}/man1/*.1.gz
%doc %{_docdir}/%{name}

%files devel
%defattr(-,root,root)
%dir %{_includedir}/fastcgi/
%{_includedir}/fastcgi/*
%{_libdir}/libfcgi*.so
%{_mandir}/man3/*.3.gz

%files -n %lname
%defattr(-,root,root)
%{_libdir}/libfcgi*.so.*

%files -n perl-FastCGI
%defattr(-,root,root)
%{_mandir}/man3/*.3pm.gz
%{perl_vendorarch}/FCGI.pm
%dir %{perl_vendorarch}/auto/FCGI
%{perl_vendorarch}/auto/FCGI/*.*
%if %suse_version < 1140
%{perl_vendorarch}/auto/FCGI/.packlist
%{_var}/adm/perl-modules/%{name}
%endif

%changelog
