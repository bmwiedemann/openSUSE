#
# spec file for package musepack
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 Asterios Dramis <asterios.dramis@gmail.com>.
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


%define so_ver 6
Name:           musepack
Version:        r475
Release:        0
Summary:        Audio Compression Format
# libmpcdec: BSD, libmpcenc/libmpcpsy: LGPL, tools: GPL, huffman coding: Zlib
License:        BSD-3-Clause AND LGPL-2.1-or-later AND GPL-2.0-or-later AND Zlib
Group:          Productivity/Multimedia/Other
URL:            https://www.musepack.net/
Source0:        https://files.musepack.net/source/%{name}_src_%{version}.tar.gz
Source99:       baselibs.conf
# PATCH-FIX-UPSTREAM libmpcdec.patch asterios.dramis@gmail.com -- Fix CMakeLists.txt to install a libmpcdec shared library, fix missing libmpcdec link to libm
Patch0:         libmpcdec.patch
BuildRequires:  cmake
BuildRequires:  libcuefile-devel
BuildRequires:  libreplaygain-devel

%description
Musepack is an audio compression format with a strong emphasis on high quality.
It's not lossless, but it is designed for transparency, so that you won't be
able to hear differences between the original wave file and the much smaller MPC
file.

It is based on the MPEG-1 Layer-2 / MP2 algorithms, but has rapidly developed and
vastly improved and is now at an advanced stage in which it contains heavily
optimized and patentless code.

%package devel
Summary:        Development Files for Musepack
License:        BSD-3-Clause AND LGPL-2.1-or-later AND GPL-2.0-or-later AND Zlib
Group:          Development/Libraries/C and C++
Requires:       libmpcdec%{so_ver} = %{version}
Conflicts:      libmpcdec-devel

%description devel
This package includes development files for musepack.

%package -n libmpcdec%{so_ver}
Summary:        Audio Compression Format
License:        BSD-3-Clause AND Zlib
Group:          System/Libraries

%description -n libmpcdec%{so_ver}
Musepack is an audio compression format with a strong emphasis on high quality.
It's not lossless, but it is designed for transparency, so that you won't be
able to hear differences between the original wave file and the much smaller MPC
file.

It is based on the MPEG-1 Layer-2 / MP2 algorithms, but has rapidly developed and
vastly improved and is now at an advanced stage in which it contains heavily
optimized and patentless code.

%prep
%setup -q -n %{name}_src_%{version}
%patch0

%build
# Fix rpmlint warning "version-control-internal-file"
rm -rf include/mpc/.svn/

# Fix rpmlint errors "spurious-executable-perm" and "executable-docs"
chmod 644 libmpcdec/AUTHORS libmpcdec/COPYING libmpcdec/ChangeLog

# Make the package use rpm optflags
sed -i "s/set(CMAKE_C_FLAGS.*$//" CMakeLists.txt

%cmake
%cmake_build

%install
%cmake_install

%post -n libmpcdec%{so_ver} -p /sbin/ldconfig
%postun -n libmpcdec%{so_ver} -p /sbin/ldconfig

%files
%{_bindir}/*

%files devel
%license libmpcdec/COPYING
%doc libmpcdec/AUTHORS libmpcdec/ChangeLog
%{_includedir}/mpc/
%{_libdir}/libmpcdec.so

%files -n libmpcdec%{so_ver}
%{_libdir}/libmpcdec.so.%{so_ver}*

%changelog
