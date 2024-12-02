#
# spec file for package Botan
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define version_suffix 3-6
%define short_version 3
Name:           Botan
Version:        3.6.1
Release:        0
Summary:        A C++ Crypto Library
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://botan.randombit.net
Source0:        https://botan.randombit.net/releases/Botan-%{version}.tar.xz
Source1:        https://botan.randombit.net/releases/Botan-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source3:        baselibs.conf
BuildRequires:  bzip2 >= 1.0.2
BuildRequires:  c++_compiler
BuildRequires:  libbz2-devel
BuildRequires:  pkgconfig
BuildRequires:  python3
BuildRequires:  trousers-devel
BuildRequires:  zlib-devel
BuildRequires:  pkgconfig(liblzma)
BuildRequires:  pkgconfig(sqlite3)
%if 0%{?suse_version} < 1600
BuildRequires:  gcc12-c++
%endif

%description
Botan is a C++ library that provides support for many common
cryptographic operations, including encryption, authentication, and
X.509v3 certificates and CRLs. A wide variety of algorithms is
supported, including RSA, DSA, DES, AES, MD5, and SHA-1.

%package     -n libbotan-%{version_suffix}
Summary:        A C++ Crypto Library
Group:          System/Libraries

%description -n libbotan-%{version_suffix}
Botan is a C++ library that provides support for many common
cryptographic operations, including encryption, authentication, and
X.509v3 certificates and CRLs. A wide variety of algorithms is
supported, including RSA, DSA, DES, AES, MD5, and SHA-1.

%package     -n libbotan-devel
Summary:        Development files for Botan
Group:          Development/Libraries/C and C++
Requires:       libbotan-%{version_suffix} = %{version}
Requires:       libbz2-devel
Requires:       trousers-devel
Requires:       pkgconfig(liblzma)
Requires:       pkgconfig(sqlite3)
Provides:       Botan-devel = %{version}
Obsoletes:      Botan-devel < %{version}

%description  -n libbotan-devel
This package contains the header files and libraries needed to develop
programs that use the Botan library.

%package     -n python3-botan
Summary:        Botan python bindings
Group:          Development/Languages/Python
Requires:       python3

%description -n python3-botan
This package contains the python bindings to libbotan's C98 interface.

%package doc
%define botan_docdir %{_docdir}/botan-%{version}
Summary:        Documentation of Botan
Group:          Development/Libraries/C and C++
BuildArch:      noarch

%description doc
Documentation of Botan package.

%prep
%autosetup -n Botan-%{version}

%build
%define _lto_cflags %{nil}
export RPM_OPT_FLAGS
%if 0%{?suse_version} < 1600
export CC=gcc-12
export CXX=g++-12
%endif
python3 ./configure.py \
  --prefix=%{_prefix} \
  --bindir=%{_bindir} \
  --libdir=%{_libdir} \
  --docdir=%{_defaultdocdir} \
  --includedir=%{_includedir} \
  --with-bzip2 \
  --with-zlib \
  --with-lzma \
  --with-sqlite \
  --with-tpm \
%ifarch %{ix86}
  --cpu=x86_32
%else
%ifarch %{arm}
  --cpu=arm
%else
  --cpu=%{_target_cpu}
%endif
%endif

%make_build WARN_FLAGS="%{optflags}"

%install
sed -i 's/env python/env python3/' src/scripts/install.py
%make_install
rm -f %{buildroot}/%{_libdir}/libbotan*.a
chmod +x %{buildroot}%{python3_sitearch}/botan3.py
sed -i '1s@^#!/.*@#!%{_bindir}/python3@' %{buildroot}%{python3_sitearch}/botan3.py

%check
%make_build check

%ldconfig_scriptlets -n libbotan-%{version_suffix}

%files
%license license.txt
%{_bindir}/botan

%files doc
%license license.txt
%docdir %{botan_docdir}
%{botan_docdir}

%files -n libbotan-%{version_suffix}
%license license.txt
%{_libdir}/libbotan-%{short_version}.so.*

%files -n libbotan-devel
%license license.txt
%{_libdir}/libbotan-%{short_version}.so
%{_libdir}/pkgconfig/botan-%{short_version}.pc
%{_includedir}/botan-%{short_version}
%{_libdir}/cmake

%files -n python3-botan
%license license.txt
%{python3_sitearch}/botan3.py

%changelog
