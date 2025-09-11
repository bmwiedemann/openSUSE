#
# spec file for package nativefiledialog-extended
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2022 Jonathan Wright <jonathan@almalinux.org>
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


%define sover   1
Name:           nativefiledialog-extended
Version:        1.2.1
Release:        0
Summary:        Native file dialog library with C and C++ bindings
License:        Zlib
URL:            https://github.com/btzy/nativefiledialog-extended
Source0:        https://github.com/btzy/nativefiledialog-extended/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE nfd-use_correct_cmake_folder.patch
Patch0:         nfd-use_correct_cmake_folder.patch
BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0)

%description
A small C library with that portably invokes native file open, folder
select and file save dialogs. Write dialog code once and have it pop up
native dialogs on all supported platforms. Avoid linking large
dependencies like wxWidgets and Qt.
This library is based on Michael Labbe's Native File Dialog
(mlabbe/nativefiledialog).

%package -n libnfd%{sover}
Summary:        Native file dialog library with C and C++ bindings

%description -n libnfd%{sover}
A small C library with that portably invokes native file open, folder
select and file save dialogs. Write dialog code once and have it pop up
native dialogs on all supported platforms. Avoid linking large
dependencies like wxWidgets and Qt.
This library is based on Michael Labbe's Native File Dialog
(mlabbe/nativefiledialog).

%package devel
Summary:        Development files for %{name}
Requires:       libnfd%{sover} = %{version}

%description devel
A small C library with that portably invokes native file open, folder
select and file save dialogs. Write dialog code once and have it pop up
native dialogs on all supported platforms. Avoid linking large
dependencies like wxWidgets and Qt.
This library is based on Michael Labbe's Native File Dialog
(mlabbe/nativefiledialog).

%prep
%autosetup -p1

%build
%cmake \
  -D NFD_BUILD_TESTS=OFF \
  -D BUILD_SHARED_LIBRARY=ON
%cmake_build

%install
%cmake_install

# creates support file for pkg-config
mkdir -p %{buildroot}/%{_libdir}/pkgconfig
tee %{buildroot}/%{_libdir}/pkgconfig/nfd.pc << "EOF"
prefix=%{_prefix}
exec_prefix=${prefix}
libdir=${exec_prefix}/%{_lib}
includedir=${prefix}/include

Name: nativefiledialog-extended
Description: Native file dialog library with C and C++ bindings
Version: %{version}
Libs: -lnfd
Cflags: -I${includedir}
EOF

%check
# all tests will fail because they require a display

%ldconfig_scriptlets -n libnfd%{sover}

%files -n libnfd%{sover}
%license LICENSE
%doc README.md
%{_libdir}/libnfd.so.%{sover}*

%files devel
%license LICENSE
%{_includedir}/nfd.h
%{_includedir}/nfd.hpp
%{_includedir}/nfd_glfw3.h
%{_includedir}/nfd_sdl2.h
%{_libdir}/libnfd.so
%dir %{_libdir}/cmake/nfd
%{_libdir}/cmake/nfd/nfd-config-relwithdebinfo.cmake
%{_libdir}/cmake/nfd/nfd-config.cmake
%{_libdir}/pkgconfig/nfd.pc

%changelog
