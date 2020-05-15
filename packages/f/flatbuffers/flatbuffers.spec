#
# spec file for package flatbuffers
#
# Copyright (c) 2020 SUSE LLC
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


%define   sonum 1
Name:           flatbuffers
Version:        1.12.0
Release:        0
Summary:        Memory Efficient Serialization Library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://google.github.io/flatbuffers/
Source0:        https://github.com/google/flatbuffers/archive/v%{version}.tar.gz
BuildRequires:  cmake >= 2.8.11.2
BuildRequires:  gcc-c++

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
# Fixup CMake/FlatbuffersConfigVersion.cmake.in - Upstream releases tarballs
# that make no sense. They exect git describe to find correct information about
# the version in use - and replace that into the cmake file in the end. Obviously
# the tarball has no .git directory and thus does not carry that inormation
# We just inject %%version there. Easiest fix.
sed -i 's/@VERSION_MAJOR@.@VERSION_MINOR@.@VERSION_PATCH@/%{version}/' CMake/FlatbuffersConfigVersion.cmake.in
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
%ctest

%post   -n libflatbuffers%{sonum} -p /sbin/ldconfig
%postun -n libflatbuffers%{sonum} -p /sbin/ldconfig

%files -n libflatbuffers%{sonum}
%license LICENSE.txt
%{_libdir}/libflatbuffers.so.*

%files devel
%doc readme.md docs/
%{_bindir}/flatc
%{_libdir}/libflatbuffers.so
%{_includedir}/flatbuffers/
%{_libdir}/cmake/flatbuffers/
%{_datadir}/cmake/Modules/*FlatBuffers.cmake

%changelog
