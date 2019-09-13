#
# spec file for package libqb
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


%bcond_without check
%bcond_without testsrpm

Name:           libqb
Version:        1.0.3+20190326.a521604
Release:        0
Summary:        An IPC library for high performance servers
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Url:            https://github.com/ClusterLabs/libqb
Source0:        %{name}-%{version}.tar.xz
Source1:        baselibs.conf
Patch1:         libqb-configure-package-version.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  check-devel
BuildRequires:  doxygen
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  procps
# Need git so build-aux/git-version-gen can extract the version number and
# commit hash during autogen run (not used currently)
#BuildRequires:  git

%description
libqb is a library providing high performance client server reusable
features. It provides logging, tracing, IPC, and polling.

%package -n libqb20
Summary:        An IPC library for high performance servers
Group:          System/Libraries

%description -n libqb20
libqb is a library providing high performance client server reusable
features. It provides logging, tracing, IPC, and polling.

%package	devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libqb20 = %{version}-%{release}

%description devel
libqb is a library providing high performance client server reusable
features. It provides logging, tracing, IPC, and polling.

%package tools
Summary:        Utilities from libqb, an IPC library
Group:          Development/Tools/Other
Provides:       libqb0:/usr/sbin/qb-blackbox
Conflicts:      libqb0 <= 1.0.3

%description tools
libqb is a library providing high performance client server reusable
features. It provides logging, tracing, IPC, and polling.

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1

%build
./autogen.sh
%configure \
%if %{with testsrpm}
 --enable-install-tests \
%endif
 --disable-static
make %{?_smp_mflags}

%if 0%{?with_check}
%check
# Tests require writable /dev/shm and /var/run
# TODO: This test might not be quite right -- it seems to fail on OBS,
# but OBS is capable of doing "make check" successfully, whereas
# "osc build" in a chroot fails.
if [ -w /dev/shm -a -w /var/run ] ; then

	make V=1 check
fi
%endif

%install
%make_install
find %{buildroot} -name '*.la' -delete
rm -rf %{buildroot}%{_datadir}/doc

%post -n libqb20 -p /sbin/ldconfig

%postun -n libqb20 -p /sbin/ldconfig

%files -n libqb20
%doc COPYING
%{_libdir}/libqb.so.*

%files devel
%defattr(-,root,root,-)
%doc COPYING README.markdown
%{_includedir}/qb/
%{_libdir}/libqb.so
%{_libdir}/pkgconfig/libqb.pc
%{_mandir}/man3/qb*3*

%files tools
%defattr(-,root,root,-)
%doc COPYING
%{_sbindir}/qb-blackbox
%{_mandir}/man8/qb-blackbox.8.gz

%package	tests
Summary:        Test suite for %{name}
Group:          Development/Tools/Other

%files		tests
%doc COPYING
%dir %{_libdir}/libqb
%dir %{_libdir}/libqb/tests
%{_libdir}/libqb/tests/*

%description	tests
The %{name}-tests package contains the %{name} test suite.

%changelog
