#
# spec file for package libssh2_org
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define sover 1
%define pkg_name libssh2
Name:           libssh2_org
Version:        1.11.1
Release:        0
Summary:        A library implementing the SSH2 protocol
License:        BSD-3-Clause
Group:          Development/Libraries/C and C++
URL:            https://www.libssh2.org/
Source0:        https://www.libssh2.org/download/%{pkg_name}-%{version}.tar.xz
Source1:        https://www.libssh2.org/download/%{pkg_name}-%{version}.tar.xz.asc
Source2:        baselibs.conf
Source3:        libssh2_org.keyring
Patch0:         libssh2-ocloexec.patch
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcrypto)
BuildRequires:  pkgconfig(zlib)
# drops build cycle in Factory
#!BuildIgnore:  groff-full

%description
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS, SECSH-USERAUTH, SECSH-CONNECTION,
SECSH-ARCH, SECSH-FILEXFER, SECSH-DHGEX, SECSH-NUMBERS, and
SECSH-PUBLICKEY.

%package -n libssh2-%{sover}
Summary:        A library implementing the SSH2 protocol
Group:          Development/Libraries/C and C++

%description -n libssh2-%{sover}
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS, SECSH-USERAUTH, SECSH-CONNECTION,
SECSH-ARCH, SECSH-FILEXFER, SECSH-DHGEX, SECSH-NUMBERS, and
SECSH-PUBLICKEY.

%package -n libssh2-devel
Summary:        A library implementing the SSH2 protocol
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libssh2-%{sover} = %{version}

%description -n libssh2-devel
libssh2 is a library implementing the SSH2 protocol as defined by
Internet Drafts: SECSH-TRANS, SECSH-USERAUTH, SECSH-CONNECTION,
SECSH-ARCH, SECSH-FILEXFER, SECSH-DHGEX, SECSH-NUMBERS, and
SECSH-PUBLICKEY.

%prep
%autosetup -p1 -n %{pkg_name}-%{version}

%build
%cmake \
	-DCRYPTO_BACKEND=OpenSSL \
	-DBUILD_EXAMPLES:BOOL=OFF \
	-DBUILD_TESTING:BOOL=OFF \
	%{nil}
%cmake_build

%install
%cmake_install
# installed via %%license
rm %{buildroot}%{_docdir}/%{name}/COPYING

%check
%ctest

%ldconfig_scriptlets -n libssh2-%{sover}

%files -n libssh2-%{sover}
%license COPYING
%{_libdir}/libssh2.so.%{sover}{,.*}

%files -n libssh2-devel
%license COPYING
%{_docdir}/libssh2_org
%{_libdir}/libssh2.so
%{_includedir}/*.h
%{_mandir}/man3/*.3%{?ext_man}
%{_libdir}/pkgconfig/libssh2.pc
%{_libdir}/cmake/libssh2

%changelog
