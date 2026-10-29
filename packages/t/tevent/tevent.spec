#
# spec file for package tevent
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "man"
%define psuffix -man
%bcond_without man
%else
%define psuffix %{nil}
%bcond_with man
%endif # build_man
%define talloc_version 2.5.0

%if 0%{?suse_version} >= 1699
%define bundle_cmocka 0
%else
%define bundle_cmocka 1
%endif

Name:           tevent%{?psuffix}
Version:        0.17.2
Release:        0
%if %{with man}
Summary:        Man pages for the tevent library
%else
Summary:        An event system based on the talloc memory management library
%endif
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://tevent.samba.org/
Source:         https://download.samba.org/pub/tevent/tevent-%{version}.tar.gz
Source1:        https://download.samba.org/pub/tevent/tevent-%{version}.tar.asc
Source2:        tevent.keyring
%if %{without man}
Source4:        baselibs.conf
%endif
Patch0:         config-sitearch.patch
%if %{with man}
BuildRequires:  doxygen
%else
BuildRequires:  libtalloc-devel >= %{talloc_version}
BuildRequires:  libtirpc-devel
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base
BuildRequires:  python3-devel
BuildRequires:  python3-talloc >= %{talloc_version}
BuildRequires:  python3-talloc-devel >= %{talloc_version}
%if ! %{bundle_cmocka}
BuildRequires:  pkgconfig(cmocka) >= 1.1.8
%endif
%endif # with man

%description
Tevent is an event system based on the talloc memory management library. It
is the core event system used in Samba.

The low level tevent has support for many event types, including timers,
signals, and the classic file descriptor events.

Tevent also provide helpers to deal with asynchronous code providing the
tevent_req (tevent request) functions.

%if %{with man}
This package contains the manual pages for the tevent API.
%endif

%if %{without man}
%package -n libtevent0
Summary:        Samba tevent Library
Group:          System/Libraries

%description -n libtevent0
Tevent is an event system based on the talloc memory management library. It
is the core event system used in Samba.

The low level tevent has support for many event types, including timers,
signals, and the classic file descriptor events.

This package contains the tevent0 library.

%package -n libtevent-devel
Summary:        Libraries and Header Files to Develop Programs with tevent0 Support
# Build man pages in the separate "man" flavor to break the
# doxygen->cmake->krb5->libtevent build cycle.
Group:          Development/Libraries/C and C++
Requires:       libtalloc-devel >= %{talloc_version}
Requires:       libtevent0 = %{version}
Requires:       pkgconfig
Recommends:     tevent-man

%description -n libtevent-devel
Tevent is an event system based on the talloc memory management library. It
is the core event system used in Samba.

The low level tevent has support for many event types, including timers,
signals, and the classic file descriptor events.

Tevent also provide helpers to deal with asynchronous code providing the
tevent_req (tevent request) functions.

This package contains libraries and header files need for development.

%package -n python3-tevent
Summary:        Python3 bindings for the Tevent library
Group:          Development/Libraries/Python
Requires:       libtevent0 = %{version}
Obsoletes:      python-tevent

%description -n python3-tevent
This package contains the python bindings for the Tevent library.

%endif # without man

%prep
%autosetup -p1 -n tevent-%{version}

%build
%if %{with man}
doxygen doxy.config

%install
# Install API documentation
mkdir -p "%{buildroot}/%{_mandir}"
cp -a doc/man/* "%{buildroot}/%{_mandir}/"
rm "%{buildroot}/%{_mandir}/man3/todo.3"

%files
%{_mandir}/man3/tevent*.*

%else
%if %{bundle_cmocka}
BUNDLED_LIBS="cmocka"
%endif
export CFLAGS="%{optflags} -D_GNU_SOURCE -D_LARGEFILE64_SOURCE -DIDMAP_RID_SUPPORT_TRUSTED_DOMAINS"
CONFIGURE_OPTIONS="\
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--disable-rpath \
	--disable-rpath-install \
	--disable-silent-rules \
	--bundled-libraries=NONE,${BUNDLED_LIBS} \
	--builtin-libraries=replace \
	--pythonarchdir=%{python3_sitearch}
"
# The waf based build system does not understand the %%configure macro
./configure ${CONFIGURE_OPTIONS}
%make_build all

%check
LD_LIBRARY_PATH=bin/shared make test

%install
%make_install

%python_compileall

# Shared libraries need to be marked executable for rpmbuild to strip them and
# include them in debuginfo
find %{buildroot} -name "*.so*" -exec chmod -c +x {} \;

%post -n libtevent0 -p /sbin/ldconfig
%postun -n libtevent0 -p /sbin/ldconfig
%post -n python3-tevent -p /sbin/ldconfig
%postun -n python3-tevent -p /sbin/ldconfig

%files -n libtevent0
%{_libdir}/libtevent.so.*
%if %{bundle_cmocka}
%dir %{_libdir}/tevent
%{_libdir}/tevent/libcmocka-tevent.so
%endif

%files -n libtevent-devel
%{_includedir}/tevent.h
%{_libdir}/libtevent.so
%{_libdir}/pkgconfig/tevent.pc

%files -n python3-tevent
%{python3_sitearch}/_tevent.%{python3_sysconfig_var SOABI}.so
%{python3_sitearch}/tevent.py
%{python3_sitearch}/__pycache__/tevent.cpython-*.py[co]

%endif # with man

%changelog
