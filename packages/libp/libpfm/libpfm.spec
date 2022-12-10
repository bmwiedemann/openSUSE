#
# spec file for package libpfm
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


%global python_config CONFIG_PFMLIB_NOPYTHON=y
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define vname   libpfm4
%bcond_without python2
Name:           libpfm
Version:        4.12.0
Release:        0
Summary:        Library to encode performance events
License:        MIT
Group:          Development/Libraries/C and C++
URL:            https://perfmon2.sourceforge.net/
Source:         https://downloads.sourceforge.net/project/perfmon2/libpfm4/%{name}-%{version}.tar.gz
Source1:        baselibs.conf

BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
BuildRequires:  swig >= 2.0.5

%if 0%{?suse_version} >= 1550
# TW: generate subpackages for every python3 flavor
%define python_subpackage_only 1
%python_subpackages
%else
%define python_sitearch %python3_sitearch
%define python_files() -n python3-%{**}
%endif

%description
This package provides a library that can be used to encode events into the
format required by the operating systems performance monitoring subsystem.

%package -n %{vname}
Summary:        Runtime library to encode performance events for use by perf tool
Group:          System/Libraries

%description -n %{vname}
This package provides a library that can be used to encode events into the
format required by the operating systems performance monitoring subsystem.
The library does not make any performance monitoring system calls, it simply
provides a method to convert an event name, expressed as a string, to an event
encoding. The user of the library may use this event encoding in a subsequent
system call.

The current libpfm4 provides support for the perf_events interface which was
introduced in Linux v2.6.31.

%package        devel
Summary:        Development library to encode performance events for perf_events interface
Group:          Development/Libraries/C and C++
Requires:       %{vname} = %{version}

%description devel
This package provides development libraries and header files used to encode performance events for perf_events interface.

%package        devel-static
Summary:        Static library version of libpfm
Group:          Development/Libraries/C and C++
Requires:       %{name}-devel = %{version}

%description devel-static
This package contains the static variant of libpfm.

%if 0%{?python_subpackage_only}
%package -n     python-%{name}
Summary:        Python bindings for libpfm and perf_event_open system call
Group:          Development/Libraries/Python
Requires:       %{vname} = %{version}

%description -n python-%{name}
This package provides python bindings for the libpfm4 package and the perf_event_open system call.

%else

%package -n     python2-%{name}
Summary:        Python bindings for libpfm and perf_event_open system call
Group:          Development/Libraries/Python
Provides:       python-%{name}
Obsoletes:      python-%{name}
Requires:       %{vname} = %{version}

%description -n python2-%{name}
This package provides python bindings for the libpfm4 package and the perf_event_open system call.

%package -n     python3-%{name}
Summary:        Python3 bindings for libpfm and perf_event_open system call
Group:          Development/Libraries/Python
Requires:       %{vname} = %{version}

%description -n python3-%{name}
This package provides python3 bindings for the libpfm4 package and the perf_event_open system call.
%endif

%prep
%setup -q
# disable werror
sed -i \
    -e 's:-Werror::g' \
    config.mk
%autopatch -p1

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CFLAGS="%{optflags}"
make %{?_smp_mflags} %{python_config}

pushd python
%python_build
popd

%install
%global python_config %{python_config}
make \
    PREFIX="%{buildroot}/%{_prefix}" \
    LIBDIR="%{buildroot}/%{_libdir}" \
    %{python_config} \
    LDCONFIG=/bin/true \
    install
install -D -p -m 0755 examples/check_events \
  %{buildroot}/%{_bindir}/check_events
install -D -p -m 0755 examples/showevtinfo \
  %{buildroot}/%{_bindir}/showevtinfo
install -D -p -m 0755 perf_examples/evt2raw \
  %{buildroot}/%{_bindir}/evt2raw

pushd python
%python_install
popd

%post -n %{vname} -p /sbin/ldconfig

%postun	-n %{vname} -p /sbin/ldconfig

%files -n %{vname}
%doc README
%{_libdir}/libpfm.so.*

%files devel
%{_includedir}/*
%{_mandir}/man3/*
%{_libdir}/lib*.so
%{_bindir}/check_events
%{_bindir}/showevtinfo
%{_bindir}/evt2raw

%files devel-static
%{_libdir}/lib*.a

%files %{python_files %{name}}
%{python_sitearch}/perfmon
%{python_sitearch}/perfmon-*-info

%if %{with python2} && ! 0%{?python_subpackage_only}
%files -n python2-%{name}
%{python2_sitearch}/*
%endif

%changelog
