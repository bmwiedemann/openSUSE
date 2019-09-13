#
# spec file for package dapl
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


%define git_version %nil
Name:           dapl
Summary:        A Library for userspace access to RDMA devices using OS Agnostic DAT APIs
License:        BSD-3-Clause OR GPL-2.0-or-later OR CPL-1.0
Group:          Productivity/Networking/System
Version:        2.1.10
Release:        0
Source0:        https://www.openfabrics.org/downloads/dapl/dapl-%version.tar.gz
Source1:        dapl-rpmlintrc
Source2:        baselibs.conf
Patch1:         dapl-2.0.30-dat-ia-open-hang.patch
Patch5:         dapl-define_NULL.patch
Patch6:         dapl-man_page_fixes.patch
Patch7:         dapl-fsf_address.patch
Patch12:        dapl-s390.patch
Patch13:        dapl-add-arm-platform-support.patch
Patch14:        ucm-mcm-fix-backlog-parameter-for-socket.patch
# PATCH-FIX-UPSTREAM http://git.openfabrics.org/?p=~ardavis/dapl.git;a=commitdiff;h=f1e05b7adcee629ee7c1d4d86ea55344d9309232
Patch15:        reproducible.patch
Url:            http://www.openfabrics.org
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libibverbs-devel
BuildRequires:  librdmacm-devel
BuildRequires:  libtool

%if "%name" == "dapl"
Conflicts:      dapl-debug
%else
Conflicts:      dapl
%endif

# bug437293
%ifarch ppc64
Obsoletes:      dapl-64bit
%endif
#
Requires(post):   /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires(post):   sed
Requires(post):   coreutils

# libdapl*.so work like plugins, hence they do not get a separate subpackage.

%if "%{name}" == "dapl-debug"
%define lname       dapl-debug-libs
%define other_lname libdat2-2
%else
%define lname       libdat2-2
%define other_lname dapl-debug-libs
%endif

%description
Along with the OpenFabrics kernel drivers, libdat and libdapl provide
a userspace RDMA API that supports DAT 2.0 specification and IB
transport extensions for atomic operations and rdma write with
immediate data.

%package     -n %lname
Summary:        DAPL runtime libraries
Group:          System/Libraries
Conflicts:      %other_lname
Obsoletes:      dapl2 < %version
Provides:       dapl2 = %version
# Need dat.conf
Requires:       %name

%description -n %lname
libdat and libdapl provide a userspace RDMA API that supports DAT 2.0
specification and IB transport extensions for atomic operations and
rdma write with immediate data.

This package contains the runtime libraries.
%if "%{name}" == "dapl-debug"
The libraries have tracing enabled.
%endif

%package        devel
Summary:        Development files for the libdat and libdapl libraries
Group:          Development/Libraries/Other
Requires:       %{name} = %{version}
Requires:       glibc-devel
%if "%name" == "dapl"
Conflicts:      dapl-debug-devel
%else
Conflicts:      dapl-devel
%endif

%description    devel
Library links and header files for the libdat and libdapl libraries.
%if "%{name}" == "dapl-debug"
The libraries have tracing enabled.
%endif

%package        utils
Summary:        Test suite for the uDAPL library
Group:          Productivity/Networking/System
Requires:       %{name} = %{version}-%{release}
Recommends:     dapl-doc = %{version}
%if "%name" == "dapl"
Conflicts:      dapl-debug-utils
%else
Conflicts:      dapl-utils
%endif

%description utils
Test suite to validate the uDAPL library APIs.

%prep
%setup -q -n dapl-%{version}
%patch1
%patch5
%patch6
%patch7
%patch12
%patch13
%patch14
%patch15 -p1

%build
%if %suse_version == 1110
export ac_cv_suse11=yes
%endif
autoreconf -fi
%if "%name" == "dapl"
%configure --disable-static --with-pic
%else
%configure --disable-static --with-pic --enable-debug 
%endif

make %{?_smp_mflags} V=1

%check
export MALLOC_CHECK_=2
make check
unset MALLOC_CHECK_

%install
make DESTDIR=%{buildroot} install

rm -f %{buildroot}%_libdir/*.la
%if "%{name}" == "dapl-debug"
rm -rf %{buildroot}%{_mandir}/man{1,5}/* 
%endif
mkdir -p %{buildroot}%_sysconfdir
touch %{buildroot}%_sysconfdir/dat.conf

#Rename tests to avoid conflicts.
# dtest clashes with dateutils package
mv %{buildroot}%{_bindir}/dapltest %{buildroot}%{_bindir}/dapl-test
mv %{buildroot}%{_bindir}/dtest %{buildroot}%{_bindir}/dapl-utest
mv %{buildroot}%{_bindir}/dtestcm %{buildroot}%{_bindir}/dapl-testcm
mv %{buildroot}%{_bindir}/dtestsrq %{buildroot}%{_bindir}/dapl-testsrx
mv %{buildroot}%{_bindir}/dtestx %{buildroot}%{_bindir}/dapl-testx

%define man_regexp -e s/dapltest/dapl-test/g -e s/dtestcm/dapl-testcm/g -e s/dtestsrq/dapl-testsrq/g -e s/dtestx/dapl-testx/g -e s/dtest/dapl-utest/g

%if "%{name}" != "dapl-debug"
# Fix man pages accordingly
for manpage in dapltest dtest dtestcm dtestsrq dtestx; do
	new_name=$(echo $manpage | sed %man_regexp)
	sed %man_regexp %{buildroot}%{_mandir}/man1/$manpage.1 > %{buildroot}%{_mandir}/man1/$new_name.1
	rm %{buildroot}%{_mandir}/man1/$manpage.1
done
%endif

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%post
/sbin/ldconfig
if test -e %_sysconfdir/dat.conf; then
	sed -i -e '/ofa-v2-.* u2/d' %_sysconfdir/dat.conf
else
    touch %_sysconfdir/dat.conf
fi
cat <<EOF >>%_sysconfdir/dat.conf
ofa-v2-mlx4_0-1 u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "mlx4_0 1" ""
ofa-v2-mlx4_0-2 u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "mlx4_0 2" ""
ofa-v2-ib0 u2.0 nonthreadsafe default libdaplofa.so.2 dapl.2.0 "ib0 0" ""
ofa-v2-ib1 u2.0 nonthreadsafe default libdaplofa.so.2 dapl.2.0 "ib1 0" ""
ofa-v2-mthca0-1 u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "mthca0 1" ""
ofa-v2-mthca0-2 u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "mthca0 2" ""
ofa-v2-ipath0-1 u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "ipath0 1" ""
ofa-v2-ipath0-2 u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "ipath0 2" ""
ofa-v2-ehca0-2 u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "ehca0 1" ""
ofa-v2-iwarp u2.0 nonthreadsafe default libdaplofa.so.2 dapl.2.0 "eth2 0" ""
ofa-v2-mlx4_0-1u u2.0 nonthreadsafe default libdaploucm.so.2 dapl.2.0 "mlx4_0 1" ""
ofa-v2-mlx4_0-2u u2.0 nonthreadsafe default libdaploucm.so.2 dapl.2.0 "mlx4_0 2" ""
ofa-v2-mthca0-1u u2.0 nonthreadsafe default libdaploucm.so.2 dapl.2.0 "mthca0 1" ""
ofa-v2-mthca0-2u u2.0 nonthreadsafe default libdaploucm.so.2 dapl.2.0 "mthca0 2" ""
ofa-v2-cma-roe-eth2 u2.0 nonthreadsafe default libdaplofa.so.2 dapl.2.0 "eth2 0" ""
ofa-v2-cma-roe-eth3 u2.0 nonthreadsafe default libdaplofa.so.2 dapl.2.0 "eth3 0" ""
ofa-v2-scm-roe-mlx4_0-1 u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "mlx4_0 1" ""
ofa-v2-scm-roe-mlx4_0-2 u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "mlx4_0 2" ""
ofa-v2-mcm-1 u2.0 nonthreadsafe default libdaplomcm.so.2 dapl.2.0 "mlx4_0 1" ""
ofa-v2-mcm-2 u2.0 nonthreadsafe default libdaplomcm.so.2 dapl.2.0 "mlx4_0 2" ""
ofa-v2-scif0 u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "scif0 1" ""
ofa-v2-scif0-u u2.0 nonthreadsafe default libdaploucm.so.2 dapl.2.0 "scif0 1" ""
ofa-v2-mic0 u2.0 nonthreadsafe default libdaplofa.so.2 dapl.2.0 "mic0:ib 1" ""
ofa-v2-mlx4_0-1s u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "mlx4_0 1" ""
ofa-v2-mlx4_0-2s u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "mlx4_0 2" ""
ofa-v2-mlx4_1-1s u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "mlx4_1 1" ""
ofa-v2-mlx4_1-2s u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "mlx4_1 2" ""
ofa-v2-mlx4_1-1u u2.0 nonthreadsafe default libdaploucm.so.2 dapl.2.0 "mlx4_1 1" ""
ofa-v2-mlx4_1-2u u2.0 nonthreadsafe default libdaploucm.so.2 dapl.2.0 "mlx4_1 2" ""
ofa-v2-mlx4_0-1m u2.0 nonthreadsafe default libdaplomcm.so.2 dapl.2.0 "mlx4_0 1" ""
ofa-v2-mlx4_0-2m u2.0 nonthreadsafe default libdaplomcm.so.2 dapl.2.0 "mlx4_0 2" ""
ofa-v2-mlx4_1-1m u2.0 nonthreadsafe default libdaplomcm.so.2 dapl.2.0 "mlx4_1 1" ""
ofa-v2-mlx4_1-2m u2.0 nonthreadsafe default libdaplomcm.so.2 dapl.2.0 "mlx4_1 2" ""
ofa-v2-mlx5_0-1s u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "mlx5_0 1" ""
ofa-v2-mlx5_0-2s u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "mlx5_0 2" ""
ofa-v2-mlx5_1-1s u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "mlx5_1 1" ""
ofa-v2-mlx5_1-2s u2.0 nonthreadsafe default libdaploscm.so.2 dapl.2.0 "mlx5_1 2" ""
ofa-v2-mlx5_0-1u u2.0 nonthreadsafe default libdaploucm.so.2 dapl.2.0 "mlx5_0 1" ""
ofa-v2-mlx5_0-2u u2.0 nonthreadsafe default libdaploucm.so.2 dapl.2.0 "mlx5_0 2" ""
ofa-v2-mlx5_1-1u u2.0 nonthreadsafe default libdaploucm.so.2 dapl.2.0 "mlx5_1 1" ""
ofa-v2-mlx5_1-2u u2.0 nonthreadsafe default libdaploucm.so.2 dapl.2.0 "mlx5_1 2" ""
ofa-v2-mlx5_0-1m u2.0 nonthreadsafe default libdaplomcm.so.2 dapl.2.0 "mlx5_0 1" ""
ofa-v2-mlx5_0-2m u2.0 nonthreadsafe default libdaplomcm.so.2 dapl.2.0 "mlx5_0 2" ""
ofa-v2-mlx5_1-1m u2.0 nonthreadsafe default libdaplomcm.so.2 dapl.2.0 "mlx5_1 1" ""
ofa-v2-mlx5_1-2m u2.0 nonthreadsafe default libdaplomcm.so.2 dapl.2.0 "mlx5_1 2" ""
EOF
#On update save configuration before uninstall of old package runs
if [ $1 -gt 0 ]; then
	cp -p %_sysconfdir/dat.conf %_sysconfdir/dat.conf.rpmtmp
fi

%posttrans
if [ -e "%_sysconfdir/dat.conf.rpmtmp" ]; then
  mv %_sysconfdir/dat.conf.rpmtmp %_sysconfdir/dat.conf
fi

%postun
/sbin/ldconfig
#remove if this isn't an update
if [ $1 -eq 0 ]; then
	if test -e %_sysconfdir/dat.conf; then
		sed -i -e '/OpenIB-.* u1/d' %_sysconfdir/dat.conf
	fi
fi

%files
%defattr(-, root, root)
%doc AUTHORS README COPYING ChangeLog LICENSE.txt LICENSE2.txt LICENSE3.txt
%_libdir/libdapl*.so.*
%config %ghost %_sysconfdir/dat.conf
%if "%{name}" != "dapl-debug"
%_mandir/man5/dat.conf.5*
%endif
%doc 

%files -n %lname
%defattr(-,root,root)
%_libdir/libdat2.so.*

%files devel
%defattr(-, root, root)
%_includedir/dat2/
%_libdir/*.so

%files utils
%defattr(-,root,root,-)
%{_bindir}/*
%if "%{name}" != "dapl-debug"
%_mandir/man1/dapl-test.1*
%_mandir/man1/dapl-utest.1*
%_mandir/man1/dapl-testcm.1*
%_mandir/man1/dapl-testsrq.1*
%_mandir/man1/dapl-testx.1*
%endif

%changelog
