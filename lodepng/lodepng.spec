#
# spec file for package lodepng
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define _libver r84
Name:           lodepng
Version:        0~git84
Release:        0
Summary:        PNG encoder and decoder
License:        Zlib
Group:          Development/Libraries/C and C++
Url:            http://lodev.org/lodepng/
# from https://github.com/lvandeve/lodepng.git
Source0:        %{name}-%{version}.tar.xz
Source99:       %{name}-rpmlintrc
BuildRequires:  dos2unix
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A PNG encoder and decoder library.

%package        devel
Summary:        Development files for lib%{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}-%{_libver} = %{version}

%description    devel
Development files for lib%{name}, a PNG encoder and decoder library.

%package     -n lib%{name}-%{_libver}
Summary:        PNG encoder and decoder
Group:          Development/Libraries/C and C++

%description -n lib%{name}-%{_libver}
A PNG encoder and decoder library.

%prep
%setup -q
dos2unix examples/*

%build
g++ -fPIC %{optflags} -shared -Wl,-soname,lib%{name}-%{_libver}.so -o lib%{name}-%{_libver}.so lodepng.cpp
g++ %{optflags} pngdetail.cpp lodepng_util.cpp -L. -l%{name}-%{_libver} -o pngdetail

%install
mkdir -pv %{buildroot}%{_libdir}/pkgconfig
mkdir -pv %{buildroot}%{_includedir}
mkdir -pv %{buildroot}%{_bindir}
install -m 0644 lib%{name}-%{_libver}.so -t %{buildroot}%{_libdir}
install -m 0644 lodepng.h -t %{buildroot}%{_includedir}
install -m 0755 pngdetail -t %{buildroot}%{_bindir}
pushd %{buildroot}%{_libdir}
ln -s lib%{name}-%{_libver}.so lib%{name}.so
popd

# creates support file for pkg-config
tee %{buildroot}/%{_libdir}/pkgconfig/lodepng.pc << "EOF"
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}/%{_lib}
includedir=${prefix}/include

Name: lodepng
Description: PNG encoder and decoder library
Version: %{version}
Libs: -L${libdir} -llodepng
Cflags: -I${includedir}
EOF

%check
g++ %{optflags} lodepng_unittest.cpp lodepng_util.cpp -L. -l%{name}-%{_libver} -o lodepng_unittest
LD_LIBRARY_PATH=. ./lodepng_unittest

%files devel
%defattr(-,root,root)
%doc README.md examples
%{_bindir}/pngdetail
%{_includedir}/%{name}.h
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n lib%{name}-%{_libver}
%defattr(-,root,root)
%doc README.md
%{_libdir}/lib%{name}-%{_libver}.so

%changelog
