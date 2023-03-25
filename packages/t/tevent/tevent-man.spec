#
# spec file for package tevent-man
#
# Copyright (c) 2023 SUSE LLC
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


%{!?py3_soflags:  %global py3_soflags cpython-%{python3_version_nodots}m}

%define talloc_version 2.4.0
%define build_man 1

%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150300
%define bundle_cmocka 0
%else
%define bundle_cmocka 1
%endif

%if %{build_man}
Name:           tevent-man
BuildRequires:  doxygen
%else
Name:           tevent
BuildRequires:  libtalloc-devel >= %{talloc_version}
%if 0%{?suse_version} >= 1330
BuildRequires:  libtirpc-devel
%endif
%if 0%{?suse_version} > 1020
BuildRequires:  pkg-config
%else
BuildRequires:  pkgconfig
%endif
BuildRequires:  pkg-config
BuildRequires:  python3-devel
BuildRequires:  python3-talloc >= %{talloc_version}
BuildRequires:  python3-talloc-devel >= %{talloc_version}
%if ! %{bundle_cmocka}
BuildRequires:  pkgconfig(cmocka) >= 1.1.3
%endif
%endif # build_man
%if 0%{?suse_version} == 0 || 0%{?suse_version} > 1140
%define	build_make_smp_mflags %{?_smp_mflags}
%else
%define	build_make_smp_mflags %{?jobs:-j%jobs}
%endif
URL:            https://tevent.samba.org/
Version:        0.14.1
Release:        0
Summary:        An event system based on the talloc memory management library
License:        LGPL-3.0-or-later
Group:          Development/Libraries/C and C++
Source:         https://download.samba.org/pub/tevent/tevent-%{version}.tar.gz
Source1:        https://download.samba.org/pub/tevent/tevent-%{version}.tar.asc
Source2:        tevent.keyring
Source4:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Tevent is an event system based on the talloc memory management library. It
is the core event system used in Samba.

The low level tevent has support for many event types, including timers,
signals, and the classic file descriptor events.

Tevent also provide helpers to deal with asynchronous code providing the
tevent_req (tevent request) functions.

%if ! %{build_man}

%package -n libtevent0
PreReq:         /sbin/ldconfig
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
# Man pages are built in a 2nd spec file in order to break a build cycle with doxygen->cmake->krb5->libtevent
Group:          Development/Libraries/C and C++
%if 0%{?suse_version} > 1030
Recommends:     %{name}-man
%endif
Requires:       libtalloc-devel >= %{talloc_version}
Requires:       libtevent0 = %{version}
%if 0%{?suse_version} > 1020
Requires:       pkg-config
%else
Requires:       pkgconfig
%endif

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
PreReq:         /sbin/ldconfig
Obsoletes:      python-tevent

%description -n python3-tevent
This package contains the python bindings for the Tevent library.

%endif # ! build_man

%prep
%setup -n tevent-%{version} -q

%build
%if ! %{build_man}
%if 0%{?suse_version} && 0%{?suse_version} < 911
	OPTIMIZATION="-O"
%else
	# use the default optimization
	unset OPTIMIZATION
%endif
%if %{bundle_cmocka}
	BUNDLED_LIBS="cmocka"
%endif
export CFLAGS="${RPM_OPT_FLAGS} -D_GNU_SOURCE ${OPTIMIZATION} -D_LARGEFILE64_SOURCE -DIDMAP_RID_SUPPORT_TRUSTED_DOMAINS"
CONFIGURE_OPTIONS="\
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--disable-rpath \
	--disable-rpath-install \
	--disable-silent-rules \
	--bundled-libraries=NONE,${BUNDLED_LIBS} \
	--builtin-libraries=replace \
"
./configure ${CONFIGURE_OPTIONS}
%{__make} %{build_make_smp_mflags} \
	all
%else

doxygen doxy.config

%endif # ! build_man

%if ! %{build_man}
%check
LD_LIBRARY_PATH=bin/shared %{__make} test
%endif # ! build_man

%install
%if ! %{build_man}
DESTDIR=${RPM_BUILD_ROOT} make install

# Shared libraries need to be marked executable for rpmbuild to strip them and
# include them in debuginfo
find ${RPM_BUILD_ROOT} -name "*.so*" -exec chmod -c +x {} \;

%else

# install API docs
mkdir -p $RPM_BUILD_ROOT/%{_mandir}
cp -a doc/man/* $RPM_BUILD_ROOT/%{_mandir}
rm $RPM_BUILD_ROOT/%{_mandir}/man3/todo.3

%endif # ! build_man

%if ! %{build_man}
%post -n libtevent0 -p /sbin/ldconfig

%postun -n libtevent0 -p /sbin/ldconfig

%post -n python3-tevent -p /sbin/ldconfig

%postun -n python3-tevent -p /sbin/ldconfig

%files -n libtevent0
%defattr(-,root,root)
%{_libdir}/libtevent.so.*
%if %{bundle_cmocka}
%dir %{_libdir}/tevent
%{_libdir}/tevent/libcmocka-tevent.so
%endif

%files -n libtevent-devel
%defattr(-,root,root)
%{_includedir}/tevent.h
%{_libdir}/libtevent.so
%{_libdir}/pkgconfig/tevent.pc

%files -n python3-tevent
%defattr(-,root,root)
%{python3_sitearch}/_tevent.%{py3_soflags}.so
%{python3_sitearch}/tevent.py
%if 0%{?centos_version} > 599 || 0%{?fedora_version} > 11 || 0%{?rhel_version} > 599
%{python3_sitearch}/__pycache__/tevent.cpython-*.py[co]
%endif

%else

%files
%defattr(-,root,root)
%{_mandir}/man3/tevent*.*

%endif # ! build_man

%changelog
