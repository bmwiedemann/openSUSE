#
# spec file for package rtags
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


%define rct_commit f9b32c837c4c6a58d8f071ffd4f87078ab6f2cdf
Name:           rtags
Version:        2.46
Release:        0
Summary:        Clang based source code indexer
License:        GPL-3.0-or-later
URL:            https://github.com/Andersbakken/rtags
# Upstream published no release tarball for 2.45/2.46, so the sources are taken
# from the git tag. src/rct is a git submodule and therefore has to be fetched
# separately; rct_commit is the submodule revision recorded for tag v%%{version}.
Source0:        %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/Andersbakken/rct/archive/%{rct_commit}.tar.gz#/rct-%{rct_commit}.tar.gz
BuildRequires:  clang-devel
BuildRequires:  cmake >= 3.8.2
BuildRequires:  emacs-nox
BuildRequires:  gcc-c++
BuildRequires:  llvm-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
Rtags is Clang based source file indexer supporting C/C++/Objective-C(++) code.

%define _sitedir %{_datadir}/emacs/site-lisp
%define _scriptdir %{_datadir}/rtags/

%prep
%autosetup -p1
mkdir -p src/rct
tar -xf %{SOURCE1} --strip-components=1 -C src/rct

%build
%cmake
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_sitedir} %{buildroot}%{_scriptdir}
install -m 0755 -t %{buildroot}%{_scriptdir} bin/*.sh
chmod 0755 %{buildroot}%{_bindir}/gcc-rtags-wrapper.sh

%check
# Upstream's test suite (-DWITH_TESTS=1) is not enabled: the pytest
# "automated_tests" are clang-version-sensitive and fail against the
# rolling Clang, and the rct cppunit tests hang in the build environment.
# Without WITH_TESTS there are no ctest tests, so %%ctest would be a no-op.
#%%ctest

%files
%doc README.org CHANGELOG.md
%license LICENSE.txt
%{_bindir}/rdm
%{_bindir}/rc
%{_bindir}/rp
%{_bindir}/gcc-rtags-wrapper.sh
%{_mandir}/man7/rc.7%{?ext_man}
%{_mandir}/man7/rdm.7%{?ext_man}
%{_sitedir}/rtags
%{_scriptdir}

%changelog
