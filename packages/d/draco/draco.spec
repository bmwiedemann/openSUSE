#
# spec file for package draco
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


%define build_gtest 1
%define commit  703bd9caab50b139428cea1aaff9974ebee5742e
%define lname libdraco8
Name:           draco
Version:        1.5.6
Release:        0
Summary:        Library for compressing and decompressing 3D geometric meshes and point clouds
License:        Apache-2.0
Group:          Productivity/Archiving/Compression
URL:            https://google.github.io/draco
Source0:        https://github.com/google/%{name}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        https://github.com/google/googletest/archive/%{commit}.zip#/googletest-%{commit}.zip
BuildRequires:  cmake >= 3.12
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  pkgconfig
%if %{build_gtest}
BuildRequires:  pkgconfig(gtest)
BuildRequires:  unzip
%endif

%description
Draco is a library for compressing and decompressing 3D geometric meshes
and point clouds. It is intended to improve the storage and transmission of
3D graphics.

%package -n %{lname}
Summary:        Library for compressing and decompressing 3D geometric meshes and point clouds
Group:          System/Libraries

%description -n %{lname}
Draco is a library for compressing and decompressing 3D geometric meshes
and point clouds. It is intended to improve the storage and transmission of
3D graphics.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}-%{release}
 
%description    devel
Draco is a library for compressing and decompressing 3D geometric meshes
and point clouds. It is intended to improve the storage and transmission of
3D graphics.
 
%prep
%autosetup -p1 -a1
%if %{build_gtest}
mv googletest-%{commit}/.[a-z]* third_party/googletest/
mv googletest-%{commit}/* third_party/googletest/
%endif

%build
%cmake \
%if %{build_gtest}
    -DDRACO_TESTS=ON
%endif

%cmake_build

%install
%cmake_install
rm -v %{buildroot}/%{_libdir}/*.a

# Create missing man files downstream
install -dm 0755 %{buildroot}%{_mandir}/man1
LD_LIBRARY_PATH=%{buildroot}%{_libdir} help2man -N --version-string=%{version} \
    -o %{buildroot}%{_mandir}/man1/%{name}_decoder-%{version}.1 \
    %{buildroot}%{_bindir}/%{name}_decoder
LD_LIBRARY_PATH=%{buildroot}%{_libdir} help2man -N --version-string=%{version} \
    -o %{buildroot}%{_mandir}/man1/%{name}_encoder-%{version}.1 \
    %{buildroot}%{_bindir}/%{name}_encoder

%if %{build_gtest}
%check
build/draco_tests
%endif

%post   -n %{lname} -p /sbin/ldconfig
%postun -n %{lname} -p /sbin/ldconfig

%files
%doc AUTHORS README.md
%{_bindir}/%{name}_decoder
%{_bindir}/%{name}_decoder-*
%{_bindir}/%{name}_encoder
%{_bindir}/%{name}_encoder-*
%{_mandir}/man?/%{name}_decoder-*.?%{?ext_man}
%{_mandir}/man?/%{name}_encoder-*.?%{?ext_man}
%license LICENSE

%files -n %{lname}
%{_libdir}/libdraco.so.*

%files devel
%{_includedir}/%{name}/
%{_datadir}/cmake/%{name}/
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
