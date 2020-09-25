#
# spec file for package libssh
#
# Copyright (c) 2020 SUSE LLC
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
%if "%{flavor}" == "test"
%define pkg_suffix -test
%ifarch s390 s390x ppc64le
  %define slow_test_system "ON"
%else
  %define slow_test_system "OFF"
%endif
%bcond_without test
%else
%define pkg_suffix %{nil}
%bcond_with test
%endif
Name:           libssh%{pkg_suffix}
Version:        0.9.5
Release:        0
Summary:        The SSH library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.libssh.org
Source0:        https://www.libssh.org/files/0.9/libssh-%{version}.tar.xz
Source1:        https://www.libssh.org/files/0.9/libssh-%{version}.tar.xz.asc
Source2:        https://cryptomilk.org/gpgkey-8DFF53E18F2ABC8D8F3C92237EE0FC4DCC014E3D.gpg#/libssh.keyring
Source3:        libssh_client.config
Source4:        libssh_server.config
Source99:       baselibs.conf
Patch0:         0001-disable-timeout-test-on-slow-buildsystems.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  krb5-devel
BuildRequires:  openssl-devel
BuildRequires:  pkgconfig
BuildRequires:  xz
BuildRequires:  zlib-devel
# doxygen generated documentation used to be in subpkg
Obsoletes:      %{name}-devel-doc <= 0.8.6
%if %{with test}
BuildRequires:  libcmocka-devel
BuildRequires:  openssh
%endif

%description
An SSH implementation in the form of a library. With libssh, you can remotely
execute programs, transfer files, use a secure and transparent tunnel for your
remote programs. It supports SFTP as well.

This package provides libssh from https://www.libssh.org that should not be
confused with libssh2 available from https://www.libssh2.org (libssh2 package)

%package -n libssh4
Summary:        SSH library
Group:          System/Libraries
Requires:       %{name}-config >= %{version}

%description -n libssh4
An SSH implementation in the form of a library. With libssh, you can remotely
execute programs, transfer files, use a secure and transparent tunnel for your
remote programs. It supports SFTP as well.

This package provides libssh from https://www.libssh.org that should not be
confused with libssh2 available from https://www.libssh2.org (libssh2 package)

%package config
Summary:        SSH library configuration files
Group:          Productivity/Networking/SSH

%description config
Configuration files for the SSH library.

%package devel
Summary:        SSH library development headers
Group:          Development/Libraries/C and C++
Requires:       cmake
Requires:       libssh4 = %{version}

%description devel
Development headers for the SSH library.

%prep
%autosetup -p1 -n libssh-%{version}

%build
%cmake \
    -DCMAKE_C_FLAGS:STRING="%{optflags} -DOPENSSL_LOAD_CONF" \
%if %{with test}
    -DUNIT_TESTING="ON" \
    -DSLOW_TEST_SYSTEM=%{slow_test_system} \
%endif
    -DWITH_GSSAPI=ON \
    -DWITH_EXAMPLES="OFF" \
    -DGLOBAL_CLIENT_CONFIG="%{_sysconfdir}/libssh/libssh_client.config" \
    -DGLOBAL_BIND_CONFIG="%{_sysconfdir}/libssh/libssh_server.config"

make %{?_smp_mflags}

%install
%if !%{with test}
%cmake_install

install -d -m755 %{buildroot}%{_sysconfdir}/libssh
install -m644 %{SOURCE3} %{buildroot}%{_sysconfdir}/libssh/libssh_client.config
install -m644 %{SOURCE4} %{buildroot}%{_sysconfdir}/libssh/libssh_server.config
%endif

%check
%if %{with test}
%ctest
%endif

%if !%{with test}
%post -n libssh4 -p /sbin/ldconfig
%postun -n libssh4 -p /sbin/ldconfig

%files -n libssh4
%doc AUTHORS README ChangeLog
%{_libdir}/libssh.so.*

%files config
%dir %{_sysconfdir}/libssh
%config(noreplace) %{_sysconfdir}/libssh/libssh_client.config
%config(noreplace) %{_sysconfdir}/libssh/libssh_server.config

%files devel
%{_includedir}/libssh
%{_libdir}/libssh.so
%{_libdir}/pkgconfig/libssh.pc
%dir %{_libdir}/cmake/libssh
%{_libdir}/cmake/libssh/libssh-config.cmake
%{_libdir}/cmake/libssh/libssh-config-relwithdebinfo.cmake
%{_libdir}/cmake/libssh/libssh-config-version.cmake
%endif

%changelog
