#
# spec file for package rtags
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


Name:           rtags
Version:        2.38
Release:        0
Summary:        Clang based source code indexer
License:        GPL-3.0-or-later
URL:            https://github.com/Andersbakken/rtags
Source0:        https://github.com/Andersbakken/rtags/releases/download/v%{version}/rtags-%{version}.tar.bz2
# PATCH-FIX-UPSTREAM rtags-2.38-emacs-28.patch -- Fix build with Emacs 28
Patch0:         rtags-2.38-emacs-28.patch
BuildRequires:  clang-devel
BuildRequires:  cmake >= 3.5
BuildRequires:  emacs-nox
BuildRequires:  gcc-c++
BuildRequires:  llvm-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
Rtags is Clang based source file indexer supporting C/C++/Objective-C(++) code.

%define _sitedir %{_datadir}/emacs/site-lisp
%define _scriptdir %{_datadir}/rtags/

%prep
%autosetup -p1

%build
%cmake \
  -DCURSES_CURSES_LIBRARY:FILEPATH="%{_libdir}/libncurses.so" \
  -DCMAKE_POLICY_VERSION_MINIMUM=3.5
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}%{_sitedir} %{buildroot}%{_scriptdir}
install -m 0755 -t %{buildroot}%{_scriptdir} bin/*.sh
chmod 0755 %{buildroot}%{_bindir}/gcc-rtags-wrapper.sh

%check
%ctest

%files
%doc README.org CHANGELOG
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
