#
# spec file for package libreplaygain
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


%define so_ver 1

Name:           libreplaygain
Summary:        Library for analyzing sound and recommending volume change
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Version:        r475
Release:        0
URL:            https://www.musepack.net/
Source0:        https://files.musepack.net/source/%{name}_%{version}.tar.gz
Patch0:         libreplaygain-math.patch
BuildRequires:  cmake

%description
libreplaygain is a library that analyzes input samples and gives the
recommended volume change.

%package devel
Summary:        Development files for libreplaygain
Group:          Development/Libraries/C and C++
Requires:       libreplaygain%{so_ver} = %{version}

%description devel
This package includes development files for libreplaygain.

%package -n libreplaygain%{so_ver}
Summary:        Library for analyzing sound and recommending volume change
Group:          System/Libraries

%description -n libreplaygain%{so_ver}
libreplaygain is a library that analyzes input samples and gives the
recommended volume change.

%prep
%setup -q -n %{name}_%{version}
%patch0 -p1

%build
# Fix rpmlint error "spurious-executable-perm"
chmod 644 include/replaygain/*.h

# Make the package use rpm optflags
sed -i "s/set(CMAKE_C_FLAGS.*$//" CMakeLists.txt

%cmake
%cmake_build

%install
%cmake_install

mkdir -p %{buildroot}%{_includedir}
cp -a include/replaygain/ %{buildroot}%{_includedir}

rm -f %{buildroot}%{_libdir}/*.a

%post -n libreplaygain%{so_ver} -p /sbin/ldconfig

%postun -n libreplaygain%{so_ver} -p /sbin/ldconfig

%files devel
%{_includedir}/replaygain/
%{_libdir}/libreplaygain.so

%files -n libreplaygain%{so_ver}
%{_libdir}/libreplaygain.so.%{so_ver}*

%changelog
