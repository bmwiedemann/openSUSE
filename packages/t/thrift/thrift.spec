#
# spec file for package thrift
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


%global libversion 0_17_0
%global libgversion 0
%bcond_without perl
%bcond_without c
%bcond_without python2
%bcond_without python3
%bcond_with java
%bcond_with ruby
%bcond_with qt5
%define skip_python2 1
%if %{without python3}
%define skip_python3 1
%endif
Name:           thrift
Version:        0.17.0
Release:        0
Summary:        Framework for scalable cross-language services development
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://thrift.apache.org
Source0:        https://www.apache.org/dist/thrift/%{version}/%{name}-%{version}.tar.gz
Source1:        https://www.apache.org/dist/thrift/%{version}/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  automake
BuildRequires:  bison
BuildRequires:  fdupes
BuildRequires:  flex
BuildRequires:  gcc-c++
BuildRequires:  libboost_headers-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libevent)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)
%if %{with qt5}
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Network)
%endif
%if %{with c}
BuildRequires:  pkgconfig(glib-2.0)
%endif
%if %{with java}
BuildRequires:  ant
BuildRequires:  java-devel
%endif
%if %{with ruby}
BuildRequires:  ruby-devel
BuildRequires:  rubygem(bundler)
%endif
%if %{with perl}
BuildRequires:  perl
BuildRequires:  perl(Bit::Vector)
BuildRequires:  perl(Class::Accessor)
%endif
%if %{with python3}
BuildRequires:  %{python_module devel}
BuildRequires:  python-rpm-macros
%if 0%{?suse_version} >= 1550
# if python multiflavor is available, use it to generate subpackages
%define python_subpackage_only 1
%python_subpackages
%else
%define python_sitearch %python3_sitearch
%define python_files() -n python3-%{**}
%endif
%endif

%description
Thrift is a software framework for scalable cross-language services
development. It combines a software stack with a code generation
engine to build services that work between C++, Java, C#, Python,
Ruby, Perl, PHP, Objective C/Cocoa, Smalltalk, Erlang, Objective
Caml, and Haskell.

%package -n libthrift-%{libversion}
Summary:        C++ API for the Thrift software framework
Group:          System/Libraries

%description -n libthrift-%{libversion}
Shared library providing the C++ API for the Thrift software framework.

Thrift is a software framework for scalable cross-language services
development. It combines a software stack with a code generation
engine to build services that work between C++, Java, C#, Python,
Ruby, Perl, PHP, Objective C/Cocoa, Smalltalk, Erlang, Objective
Caml, and Haskell.

%package -n libthriftnb-%{libversion}
Summary:        Thrift non-blocking server library
Group:          System/Libraries

%description -n libthriftnb-%{libversion}
Shared library providing the non-blocking server component of the
Thrift software framework.

%package -n libthriftz-%{libversion}
Summary:        Thrift Zlib API
Group:          System/Libraries

%description -n libthriftz-%{libversion}
A shared library from the Thrift software framework.

%package -n libthrift_c_glib%{libgversion}
Summary:        C API for the Thrift software framework
Group:          System/Libraries
Conflicts:      libthrift-0_11_0

%description -n libthrift_c_glib%{libgversion}
Shared library providing the C API for the Thrift software framework.

%package -n libthrift-devel
Summary:        Thrift C++ library development files
Group:          Development/Libraries/C and C++
Requires:       libthrift-%{libversion} = %{version}
Requires:       libthrift_c_glib%{libgversion} = %{version}
Requires:       libthriftnb-%{libversion} = %{version}
Requires:       libthriftz-%{libversion} = %{version}

%description -n libthrift-devel
Thrift C++ library development files

Thrift is a software framework for scalable cross-language services
development. It combines a software stack with a code generation
engine to build services that work between C++, Java, C#, Python,
Ruby, Perl, PHP, Objective C/Cocoa, Smalltalk, Erlang, Objective
Caml, and Haskell.

%package -n perl-thrift
Summary:        Perl bindings to the Thrift software framework
Group:          Development/Libraries/Perl
%{perl_requires}

%description -n perl-thrift
Thrift Perl library

Thrift is a software framework for scalable cross-language services
development. It combines a software stack with a code generation
engine to build services that work between C++, Java, C#, Python,
Ruby, Perl, PHP, Objective C/Cocoa, Smalltalk, Erlang, Objective
Caml, and Haskell.

%define oldpython python

%if 0%{?python_subpackage_only}
%package -n python-thrift
Summary:        Python %{python_version} bindings for the Thrift software framework
Group:          Development/Libraries/Python
Requires:       python-six >= 1.7.2
Suggests:       python-Twisted
Suggests:       python-tornado >= 4.0
%if %{python_version_nodots} <= 34 && %{python_version_nodots} > 30
Recommends:     python-backports.ssl_match_hostname >= 3.5
%endif

%description -n python-thrift
Thrift Python %{python_version} library

Thrift is a software framework for scalable cross-language services
development. It combines a software stack with a code generation
engine to build services that work between C++, Java, C#, Python,
Ruby, Perl, PHP, Objective C/Cocoa, Smalltalk, Erlang, Objective
Caml, and Haskell.

%else

%package -n python3-thrift
Summary:        Python3 bindings for the Thrift software framework
Group:          Development/Libraries/Python
Requires:       python3-six >= 1.7.2
Suggests:       python3-Twisted
Suggests:       python3-tornado >= 4.0
%if %{python3_version_nodots} <= 34
Recommends:     python3-backports.ssl_match_hostname >= 3.5
%endif

%description -n python3-thrift
Thrift Python3 library

Thrift is a software framework for scalable cross-language services
development. It combines a software stack with a code generation
engine to build services that work between C++, Java, C#, Python,
Ruby, Perl, PHP, Objective C/Cocoa, Smalltalk, Erlang, Objective
Caml, and Haskell.
%endif

%prep
%autosetup -p1

%build
# https://issues.apache.org/jira/browse/THRIFT-5498
%global _lto_cflags %{nil}
export CXXFLAGS="%{optflags} -fPIC"

# tests require static boost library
%configure \
	--disable-tests \
	--enable-static=no
make %{?_smp_mflags}

%if %{with python3}
pushd lib/py
%python_build
popd
%endif

%install
%make_install
pushd compiler/cpp
%make_install
popd
pushd lib/cpp
%make_install
popd

%if %{with python3}
pushd lib/py
%python_install
popd
%python_expand %fdupes %{buildroot}%{$python_sitearch}
%endif

%if %{with perl}
pushd lib/perl
perl Makefile.PL
%perl_make_install
%perl_process_packlist
mv %{buildroot}%{_prefix}/local/lib/perl5 \
  %{buildroot}%{_perl_vendorlib}
popd
%endif

find %{buildroot} -type f -name "*.la" -delete -print

%post -n libthrift-%{libversion} -p /sbin/ldconfig
%post -n libthriftnb-%{libversion} -p /sbin/ldconfig
%post -n libthriftz-%{libversion} -p /sbin/ldconfig
%post -n libthrift_c_glib%{libgversion} -p /sbin/ldconfig
%postun -n libthrift-%{libversion} -p /sbin/ldconfig
%postun -n libthriftnb-%{libversion} -p /sbin/ldconfig
%postun -n libthriftz-%{libversion} -p /sbin/ldconfig
%postun -n libthrift_c_glib%{libgversion} -p /sbin/ldconfig

%files
%doc CHANGES.md
%license LICENSE NOTICE
%{_bindir}/thrift

%files -n libthrift-%{libversion}
%{_libdir}/libthrift-*.so

%files -n libthriftnb-%{libversion}
%{_libdir}/libthriftnb-*.so

%files -n libthriftz-%{libversion}
%{_libdir}/libthriftz-*.so

%files -n libthrift_c_glib%{libgversion}
%{_libdir}/libthrift_c_glib.so.*

%files -n libthrift-devel
%{_includedir}/thrift
%{_libdir}/libthrift.so
%{_libdir}/libthriftnb.so
%{_libdir}/libthriftz.so
%{_libdir}/libthrift_c_glib.so
%{_libdir}/pkgconfig/*.pc

%if %{with perl}
%files -n perl-thrift
%license LICENSE NOTICE
%doc lib/perl/README.md
%{perl_vendorlib}/Thrift.pm
%{perl_vendorlib}/Thrift
%endif

%if %{with python3}
%files %{python_files thrift}
%license LICENSE NOTICE
%doc lib/py/README.md
%{python_sitearch}/thrift
%{python_sitearch}/thrift-%{version}*-info
%endif

%changelog
