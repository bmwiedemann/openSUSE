#
# spec file for package deltarpm
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%bcond_without python2
%bcond_without python3
# we need to build against recent rpm, so avoid the new payload
%define _binary_payload w9.bzdio
Name:           deltarpm
Version:        3.6.2
Release:        0
Summary:        Tools to Create and Apply deltarpms
License:        BSD-3-Clause
Group:          System/Packages
Url:            https://github.com/rpm-software-management/deltarpm/
Source:         deltarpm-3.6.2.tar.bz2
BuildRequires:  libbz2-devel
%if %{with python2}
BuildRequires:  python2-devel
%endif
%if %{with python3}
BuildRequires:  python3-devel
%endif
BuildRequires:  rpm-devel
BuildRequires:  xz-devel
BuildRequires:  pkgconfig(libzstd)

%description
This package contains tools to create and apply deltarpms. A deltarpm
contains the difference between an old and a new version of an RPM,
which makes it possible to recreate the new RPM from the deltarpm and
the old one. You do not need to have a copy of the old RPM, because
deltarpms can also work with installed RPMs.


%package -n python2-deltarpm
Summary:        Tools to Create and Apply deltarpms
Group:          Development/Languages/Python
Provides:       python-deltarpm = %{version}-%{release}
Obsoletes:      python-deltarpm < %{version}-%{release}
Requires:       %{name} = %{version}

%description -n python2-deltarpm
Python 2 bindings for deltarpm

%package -n python3-deltarpm
Summary:        Tools to Create and Apply deltarpms
Group:          Development/Languages/Python
Requires:       %{name} = %{version}

%description -n python3-deltarpm
Python 3 bindings for deltarpm

%prep
%setup -q

%build
make CC="gcc" CFLAGS="%{optflags} -DWITH_ZSTD=1" rpmdumpheader="%{_prefix}/lib/rpm/rpmdumpheader" %{?_smp_mflags} all python

%install
PYS=""
%if %{with python2}
PYS="$PYS python"
%endif
%if %{with python3}
PYS="$PYS python3"
%endif

mkdir -p %{buildroot}%{_prefix}/lib/rpm
make install DESTDIR=%{buildroot} \
    prefix="%{_prefix}" libdir="%{_libdir}" mandir="%{_mandir}" \
    rpmdumpheader="%{_prefix}/lib/rpm/rpmdumpheader" PYTHONS="$PYS"
%if %{with python2}
rm -rf %{buildroot}%{_libdir}/python/site-packages/{_deltarpmmodule.so,deltarpm.py} # Remove wrongly installed Python 2 module
mv %{buildroot}%{python_sitearch}/_deltarpm{module,}.so # Fix binary Python 2 module name
%endif
%if %{with python3}
mv %{buildroot}%{python3_sitearch}/_deltarpm{module,}.so # Fix binary Python 3 module name
%endif

%files
%doc README LICENSE.BSD
%{_bindir}/*
%{_mandir}/man8/*
%{_prefix}/lib/rpm/rpmdumpheader

%if %{with python2}
%files -n python2-deltarpm
%{python_sitearch}/deltarpm.py
%{python_sitearch}/_deltarpm.so
%endif

%if %{with python3}
%files -n python3-deltarpm
%{python3_sitearch}/deltarpm.py
%{python3_sitearch}/_deltarpm.so
%endif

%changelog
