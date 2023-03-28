#
# spec file for package flatbuffers
#
# Copyright (c) 2023 SUSE LLC
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


%define   sonum 23_3_3
Name:           flatbuffers
Version:        23.3.3
Release:        0
Summary:        Memory Efficient Serialization Library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://google.github.io/flatbuffers/
Source0:        https://github.com/google/flatbuffers/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.8
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig

%description
FlatBuffers is a serialization library for games and other memory constrained programs.
FlatBuffers allows to directly access serialized data without unpacking/parsing
it first, while still having great forwards/backwards compatibility.

%package        -n libflatbuffers%{sonum}
Summary:        Memory Efficient Serialization Library
Group:          System/Libraries
Provides:       libflatbuffers = %{version}

%description    -n libflatbuffers%{sonum}
FlatBuffers is a serialization library for games and other memory constrained programs.
FlatBuffers allows to directly access serialized data without unpacking/parsing
it first, while still having great forwards/backwards compatibility.

This package provides the libflatbuffers shared library.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       libflatbuffers%{sonum} = %{version}
Provides:       %{name}-devel-static = %{version}

%description    devel
FlatBuffers is a serialization library for games and other memory constrained programs.
FlatBuffers allows to directly access serialized data without unpacking/parsing
it first, while still having great forwards/backwards compatibility.

This package provides the libflatbuffers headers, development libraries,
and tools.

%prep
%autosetup -p1

%build
chmod -x readme.md docs/source/*.md docs/footer.html docs/source/doxyfile
%cmake -DCMAKE_BUILD_TYPE=Release \
       -DFLATBUFFERS_BUILD_SHAREDLIB=ON \
       -DFLATBUFFERS_BUILD_FLATLIB=OFF \
       -DFLATBUFFERS_BUILD_FLATC=ON
%cmake_build

%install
%cmake_install
mkdir -p %{buildroot}/%{_datadir}/cmake/Modules
install -Dm0644 CMake/*FlatBuffers.cmake %{buildroot}%{_datadir}/cmake/Modules/

%check
# does not support out-of-tree builds, see https://github.com/google/flatbuffers/issues/7009
#%%ctest
%{__builddir}/flattests

%post   -n libflatbuffers%{sonum} -p /sbin/ldconfig
%postun -n libflatbuffers%{sonum} -p /sbin/ldconfig

%files -n libflatbuffers%{sonum}
%license LICENSE
%{_libdir}/libflatbuffers.so.*

%files devel
%doc readme.md docs/
%{_bindir}/flatc
%{_libdir}/libflatbuffers.so
%{_includedir}/flatbuffers/
%{_libdir}/pkgconfig/flatbuffers.pc
%{_libdir}/cmake/flatbuffers/
%{_datadir}/cmake/Modules/*FlatBuffers.cmake

%changelog
