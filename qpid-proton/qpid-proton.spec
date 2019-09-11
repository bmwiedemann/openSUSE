#
# spec file for package qpid-proton
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

# libqpid-proton dependency leaves detritus in __pycache__ on Red Hat which should be excluded from RPM
%if 0%{?fedora} || 0%{?rhel}
%define _unpackaged_files_terminate_build 0
%endif

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global         qpid_proton_soversion 10
Name:           qpid-proton
Version:        0.17.0
Release:        0
Summary:        A high performance, lightweight messaging library
License:        Apache-2.0
Group:          Productivity/Networking/Other
Url:            http://qpid.apache.org/proton/
Source0:        http://www.apache.org/dist/qpid/proton/%{version}/%{name}-%{version}.tar.gz
Patch101:       qpid-proton-cmake-fixes.patch
Patch102:       qpid-proton-0.9-pthread.patch
Patch103:       qpid-proton-0.16.0-gcc7.patch
# PATCH-FIX-UPSTREAM - qpid-proton-fix-dh-openssl-1.1.0.patch - Modify openssl DH code to work with openssl 1.1
Patch104:       qpid-proton-fix-dh-openssl-1.1.0.patch
# PATCH-FIX-UPSTREAM - qpid-proton-fix-session-resume-openssl-1.1.0.patch - Rework Openssl session resume code to work with openssl 1.1
Patch105:       qpid-proton-fix-session-resume-openssl-1.1.0.patch
Patch106:       catch-by-const-reference.patch
Patch107:       reproducible.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module xml}
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libuuid-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  swig >= 2.0.9
BuildRequires:  perl(ExtUtils::MakeMaker)
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl(Test::More)

%description
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.

%package -n libqpid-proton%{qpid_proton_soversion}
Summary:        C library for Qpid Proton
Group:          Development/Libraries/C and C++

%description -n libqpid-proton%{qpid_proton_soversion}
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.

%package -n libqpid-proton-cpp%{qpid_proton_soversion}
Summary:        C++ library for Qpid Proton
Group:          Development/Libraries/C and C++

%description -n libqpid-proton-cpp%{qpid_proton_soversion}
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.

%package devel
Summary:        Development libraries for writing messaging apps with Qpid Proton
Group:          Development/Libraries/C and C++
Requires:       libqpid-proton%{qpid_proton_soversion} = %{version}-%{release}
Requires:       libqpid-proton-cpp%{qpid_proton_soversion} = %{version}-%{release}

%description devel
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.

%package devel-doc
Summary:        Documentation for the C development libraries for Qpid Proton
Group:          Documentation/Other
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
%if 0%{?suse_version} >= 1120
BuildArch:      noarch
%endif

%description devel-doc
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.

%if 0%{?have_python2}
%package -n python2-python-qpid-proton
Summary:        Python language bindings for the Qpid Proton messaging framework
Group:          Development/Libraries/Python
Requires:       libqpid-proton%{qpid_proton_soversion} = %{version}-%{release}
Requires:       python = %{python2_version}
# NOTE: the name on pypi for the package is python-qpid-proton so the name
# for the RPM package should be python-python-qpid-proton (python-$pypi_name)
Provides:       python-qpid-proton = %{version}
Obsoletes:      python-qpid-proton < %{version}
# as long as python2 is the default, provide also the non-versioned python pkg
Provides:       python-python-qpid-proton = %{version}

%description -n python2-python-qpid-proton
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.
%endif

%package -n python3-python-qpid-proton
Summary:        Python language bindings for the Qpid Proton messaging framework
Group:          Development/Libraries/Python
Requires:       libqpid-proton%{qpid_proton_soversion} = %{version}-%{release}
Requires:       python = %{python3_version}
# NOTE: the name on pypi for the package is python-qpid-proton so the name
# for the RPM package should be python-python-qpid-proton (python-$pypi_name)
Provides:       python3-qpid-proton = %{version}
Obsoletes:      python3-qpid-proton < %{version}

%description -n python3-python-qpid-proton
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.

%package -n perl-qpid-proton
Summary:        Perl language bindings for Qpid Proton messaging framework
Group:          Development/Libraries/Perl
Requires:       libqpid-proton%{qpid_proton_soversion} = %{version}-%{release}
Requires:       perl = %{perl_version}

%description -n perl-qpid-proton
Proton is a high performance, lightweight messaging library. It can be used in
the widest range of messaging applications including brokers, client libraries,
routers, bridges, proxies, and more. Proton is based on the AMQP 1.0 messaging
standard. Using Proton it is trivial to integrate with the AMQP 1.0 ecosystem
from any platform, environment, or language.

%prep
%setup -q
%autopatch -p1

%build
%cmake \
    -DPROTON_DISABLE_RPATH=true \
    -DNOBUILD_RUBY=1 \
    -DNOBUILD_PHP=1 \
    -DSYSINSTALL_PERL=1 \
    -DSYSINSTALL_PYTHON=1 \
    -DCHECK_SYSINSTALL_PYTHON=0

make all docs %{?_smp_mflags}
# build for python2 and python3
(cd proton-c/bindings/python/dist; %python_build)

%install
%cmake_install

(cd build/proton-c/bindings/python/dist; %python_install)
rm -rf %{buildroot}%{python3_sitearch}/__pycache__

chmod +x %{buildroot}%{python_sitearch}/*_cproton.so
find %{buildroot}%{_datadir}/proton-%{version}/examples/ -type f | xargs chmod -x

mkdir -p %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_datadir}/proton-%{version}/docs/* %{buildroot}%{_docdir}/%{name}/

%fdupes -s %{buildroot}

%post -n libqpid-proton%{qpid_proton_soversion} -p /sbin/ldconfig
%postun -n libqpid-proton%{qpid_proton_soversion} -p /sbin/ldconfig
%post -n libqpid-proton-cpp%{qpid_proton_soversion} -p /sbin/ldconfig
%postun -n libqpid-proton-cpp%{qpid_proton_soversion} -p /sbin/ldconfig

%files -n libqpid-proton%{qpid_proton_soversion}
%{_libdir}/libqpid-proton.so.*
%{_libdir}/libqpid-proton-core.so.*

%files -n libqpid-proton-cpp%{qpid_proton_soversion}
%{_libdir}/libqpid-proton-cpp.so.*

%files devel
%{_includedir}/proton
%{_libdir}/libqpid-proton.so
%{_libdir}/libqpid-proton-core.so
%{_libdir}/libqpid-proton-cpp.so
%{_libdir}/pkgconfig/libqpid-proton.pc
%{_libdir}/pkgconfig/libqpid-proton-core.pc
%{_libdir}/pkgconfig/libqpid-proton-cpp.pc
%dir %{_libdir}/cmake/Proton
%dir %{_libdir}/cmake/ProtonCpp
%{_libdir}/cmake/Proton/*.cmake
%{_libdir}/cmake/ProtonCpp/*.cmake

%files devel-doc
%dir %{_datadir}/proton-%{version}
%doc %{_datadir}/proton-%{version}/LICENSE
%doc %{_datadir}/proton-%{version}/README.md
%{_datadir}/proton-%{version}/examples
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/api-c
%{_docdir}/%{name}/api-cpp

%if 0%{?have_python2}
%files -n python2-python-qpid-proton
%{python2_sitearch}/*_cproton.so
%{python2_sitearch}/cproton.*
%{python2_sitearch}/proton
%{python2_sitearch}/python_qpid_proton-%{version}-py*.egg-info
%endif

%files -n python3-python-qpid-proton
%{python3_sitearch}/*_cproton*.so
%{python3_sitearch}/cproton.*
%{python3_sitearch}/proton
%{python3_sitearch}/python_qpid_proton-%{version}-py*.egg-info

%files -n perl-qpid-proton
%{perl_vendorarch}/*

%changelog
