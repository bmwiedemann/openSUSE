#
# spec file for package libqb
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


%bcond_without check
%bcond_without testsrpm
%bcond_without doxygen2man

Name:           libqb
Version:        2.0.6+20220323.758044b
Release:        0
Summary:        An IPC library for high performance servers
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/ClusterLabs/libqb
Source0:        %{name}-%{version}.tar.xz
Source1:        baselibs.conf

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

%package -n libqb100
Summary:        An IPC library for high performance servers
Group:          System/Libraries

%description -n libqb100
libqb is a library providing high performance client server reusable
features. It provides logging, tracing, IPC, and polling.

%package	devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libqb100 = %{version}-%{release}

%description devel
libqb is a library providing high performance client server reusable
features. It provides logging, tracing, IPC, and polling.

%package tools
Summary:        Utilities from libqb, an IPC library
Group:          Development/Tools/Other
Conflicts:      libqb0 <= 1.0.3
Provides:       libqb0:%{_sbindir}/qb-blackbox

%description tools
libqb is a library providing high performance client server reusable
features. It provides logging, tracing, IPC, and polling.

%prep
%setup -q -n %{name}-%{version}

%build
if [ ! -f .tarball-version ]; then
  echo %{VERSION} > .tarball-version
fi
./autogen.sh
%configure \
%if %{with testsrpm}
 --enable-install-tests \
%endif
 --disable-static
%make_build

%if 0%{?with_check}
%check
# Tests require writable /dev/shm and /var/run
# TODO: This test might not be quite right -- it seems to fail on OBS,
# but OBS is capable of doing "make check" successfully, whereas
# "osc build" in a chroot fails.
if [ -w /dev/shm -a -w %{_localstatedir}/run ] ; then

	%make_build check
fi
%endif

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -rf %{buildroot}%{_datadir}/doc

%post -n libqb100 -p /sbin/ldconfig

%postun -n libqb100 -p /sbin/ldconfig

%files -n libqb100
%license COPYING
%{_libdir}/libqb.so.*

%files devel
%license COPYING
%doc README.markdown
%{_includedir}/qb/
%{_libdir}/libqb.so
%{_libdir}/pkgconfig/libqb.pc
%{_mandir}/man3/qb*3%{?ext_man}

%files tools
%license COPYING
%{_sbindir}/qb-blackbox
%{_mandir}/man8/qb-blackbox.8%{?ext_man}

%package	tests
Summary:        Test suite for %{name}
Group:          Development/Tools/Other

%files tests
%license COPYING
%dir %{_libdir}/libqb
%dir %{_libdir}/libqb/tests
%{_libdir}/libqb/tests/*

%description	tests
The %{name}-tests package contains the %{name} test suite.

%if %{with doxygen2man}
%package	-n doxygen2man
Summary:        tool to generate man pages from Doxygen XML files
Group:          Development/Tools/Doc Generators
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libxml-2.0)
Requires:       libqb100 = %{version}-%{release}

%files -n doxygen2man
%{_bindir}/doxygen2man
%{_mandir}/man1/doxygen2man.1%{?ext_man}
%license COPYING

%description	-n doxygen2man
The doxygen2man package contains the doxygen2man utility.
%endif

%changelog
