#
# spec file for package libclc
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


Name:           libclc
Version:        0.2.0+git.20190805
Release:        0
Summary:        OpenCL C programming language library
License:        (BSD-3-Clause OR MIT) AND Apache-2.0 WITH LLVM-exception
Group:          Development/Libraries/C and C++
URL:            https://libclc.llvm.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        %{name}-rpmlintrc
BuildRequires:  gcc
BuildRequires:  libstdc++-devel >= 3.9
BuildRequires:  llvm >= 4.0
BuildRequires:  llvm-clang-devel >= 4.0
BuildRequires:  pkgconfig
BuildRequires:  python3-base
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(zlib)

%description
Library requirements of the OpenCL C programming language.

%prep
%autosetup

%build
sed -i "s|python|python3|g" configure.py
export \
  CFLAGS="%{optflags}" \
  CXXFLAGS="%{optflags}" \
  CC=clang \
  CXX=clang++
python3 ./configure.py \
  --prefix=%{_prefix} \
  --with-llvm-config=%{_bindir}/llvm-config \
  --with-cxx-compiler=${CXX} \
  --enable-runtime-subnormal \
  --pkgconfigdir=%{_libdir}/pkgconfig/ \
  --libexecdir=%{_libdir}/clc/
%make_build

%install
%make_install

%files
%license LICENSE.TXT
%{_includedir}/clc
%{_libdir}/clc
%{_libdir}/pkgconfig/libclc.pc

%changelog
