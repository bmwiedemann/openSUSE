#
# spec file for package libgit2
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2011, Sascha Peilicke <saschpe@gmx.de>
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


%global flavor @BUILD_FLAVOR@%{nil}
%define pname libgit2
%if "%{flavor}" == "experimental"
%define psuffix -%{flavor}
%define sosuffix 1_9
%bcond_without expt_sha256
%else
%define sosuffix -1_9
%bcond_with expt_sha256
%endif
Name:           %{pname}%{?psuffix}
Version:        1.9.2
Release:        0
Summary:        C git library
License:        GPL-2.0-only WITH GCC-exception-2.0
Group:          Development/Libraries/C and C++
URL:            https://libgit2.github.com/
Source0:        https://github.com/libgit2/libgit2/archive/v%{version}.tar.gz#/%{pname}-%{version}.tar.gz
Source1:        libgit2-rpmlintrc
BuildRequires:  cmake >= 3.5.1
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpcre2-posix)
BuildRequires:  pkgconfig(libssh2)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing
you to write native speed custom Git applications in any language
with bindings.

%package -n %{name}%{sosuffix}
Summary:        C git library
Group:          System/Libraries

%description -n %{name}%{sosuffix}
libgit2 is a portable, pure C implementation of the Git core methods
provided as a re-entrant linkable library with a solid API, allowing
you to write native speed custom Git applications in any language
with bindings.

%package devel
Summary:        C git library
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sosuffix} = %{version}
Conflicts:      cmake(libgit2)

%description devel
This package contains all necessary include files and libraries needed
to compile and develop applications that use libgit2.

%package tools
Summary:        A Git command-line interface based on libgit2
Group:          Development/Tools/Version Control

%description tools
This package contains a git cli based on libgit2.

%prep
%autosetup -p1 -n %{pname}-%{version}

%build
%cmake \
	-DUSE_SSH:BOOL=ON \
	-DREGEX_BACKEND=pcre2 \
	-DENABLE_REPRODUCIBLE_BUILDS:BOOL=ON \
	-DEXPERIMENTAL_SHA256:BOOL=%{?with_expt_sha256:ON}%{!?with_expt_sha256:OFF} \
	-DBUILD_TESTS:BOOL=OFF \
	%{nil}
%cmake_build

%install
%cmake_install

%ldconfig_scriptlets -n %{name}%{sosuffix}

%files -n %{name}%{sosuffix}
%license COPYING
%doc AUTHORS README.md
%{_libdir}/%{name}.so.*

%files devel
%license COPYING
%doc examples
%{_libdir}/%{name}.so
%{_includedir}/git2*
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/libgit2

%files tools
%license COPYING
%{_bindir}/git2%{?with_expt_sha256:-experimental}

%changelog
