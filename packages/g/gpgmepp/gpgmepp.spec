#
# spec file for package gpgmepp
#
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


%define sover 7
Name:           gpgmepp
Version:        2.0.0
Release:        0
Summary:        C++ bindings/wrapper for GPGME
License:        LGPL-2.0-or-later AND LGPL-2.1-or-later
URL:            https://gnupg.org/software/gpgme/index.html
Source:         https://gnupg.org/ftp/gcrypt/gpgmepp/%{name}-%{version}.tar.xz
Source1:        https://gnupg.org/ftp/gcrypt/gpgmepp/%{name}-%{version}.tar.xz.sig
Source2:        baselibs.conf
# https://www.gnupg.org/signature_key.html
Source3:        %{name}.keyring
BuildRequires:  c++_compiler
BuildRequires:  cmake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gpg-error) >= 1.47
BuildRequires:  pkgconfig(gpgme) >= 2.0.0
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12-c++
%endif

%description
GPGME++ is a C++ wrapper (or C++ bindings) for the GnuPG project's GPGME
(GnuPG Made Easy) library, version 0.4.4 and later.

%package -n libgpgmepp%{sover}
Summary:        C++ bindings/wrapper for GPGME

%description -n libgpgmepp%{sover}
GPGME++ is a C++ wrapper (or C++ bindings) for the GnuPG project's GPGME
(GnuPG Made Easy) library, version 0.4.4 and later.

This package contains the shared library.

%package devel
Summary:        Development files for %{name}
Requires:       libgpgmepp%{sover} = %{version}
Provides:       libgpgmepp-devel = %{version}
Obsoletes:      libgpgmepp-devel < %{version}

%description devel
GPGME++ is a C++ wrapper (or C++ bindings) for the GnuPG project's GPGME
(GnuPG Made Easy) library, version 0.4.4 and later.

This package contains the files neede for building with %{name}.

%prep
%autosetup -p1

%build
%if 0%{?suse_version} < 1600
export CXX=g++-12
%endif
%cmake
%cmake_build

%install
%cmake_install

%check
%ctest

%ldconfig_scriptlets -n libgpgmepp%{sover}

%files -n libgpgmepp%{sover}
%license COPYING.LIB COPYING.LESSER
%{_libdir}/libgpgmepp.so.%{sover}{,.*}

%files devel
%license COPYING.LIB COPYING.LESSER
%doc NEWS README ChangeLog AUTHORS
%{_includedir}/gpgme++
%{_libdir}/libgpgmepp.so
%{_libdir}/pkgconfig/gpgmepp.pc
%{_libdir}/cmake/Gpgmepp

%changelog
