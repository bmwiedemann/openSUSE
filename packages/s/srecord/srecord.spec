#
# spec file for package srecord
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


Name:           srecord
Version:        1.65.0
%define short_version 1.65
Release:        0
%define so_ver  0
Summary:        Hex/bin format conversion package
License:        GPL-3.0-or-later
Group:          Development/Tools/Other
URL:            https://srecord.sourceforge.net/
Source:         https://sourceforge.net/projects/srecord/files/srecord/%{short_version}/srecord-%{version}-Source.tar.gz
BuildRequires:  cmake >= 3.21
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
# groff-full for PDF output driver
BuildRequires:  groff-full
BuildRequires:  libgcrypt-devel

%description
The srecord package is a collection of powerful tools for manipulating EPROM
load files. It reads and writes numerous EPROM file formats, and can perform
many different manipulations.

%package     -n lib%{name}%{so_ver}
Summary:        Srecord libraries
Group:          System/Libraries

%description -n lib%{name}%{so_ver}
This package contains the shared libraries for programs that manipulate EPROM
load files.

%package        devel
Summary:        Srecord development files
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{so_ver} = %{version}

%description    devel
This package contains libraries and header files for compiling programs
that manipulate EPROM load files.

%package        doc
Summary:        Srecord PDF documentation
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
The srecord package is a collection of powerful tools for manipulating EPROM
load files. It reads and writes numerous EPROM file formats, and can perform
many different manipulations.

This package contains documentation in PDF format.

%prep
%setup -q -n %{name}-%{version}-Source
# Workaround git not working properly with tarball, fixed upstream
sed -ie '/GIT Hash Not Found/ d' etc/configure.cmake
# Fix library build
sed -ie '/add_library/ {
    s/STATIC// ;
    s/\${LIB_GCRYPT}//
    a target_link_libraries(lib_srecord \${LIB_GCRYPT})
    a set_target_properties(lib_srecord PROPERTIES OUTPUT_NAME srecord SOVERSION %{so_ver})
    } ' srecord/CMakeLists.txt
# Do not install system libraries
sed -ie '/install(RUNTIME_DEPENDENCY_SET/ a EXCLUDE_FROM_ALL' etc/packaging.cmake
# Prefer SVG icons, avoid dep on full graphviz
echo 'set(DOXYGEN_DOT_IMAGE_FORMAT svg)' >> etc/configure.cmake

%build
%cmake \
  -DCMAKE_INSTALL_DOCDIR=%{_docdir}/%{name} \
  %{nil}
%cmake_build

%install
%cmake_install
# Only keep the reference PDF, remove HTML versions of man pages
rm -rf %{buildroot}%{_docdir}/%{name}/htdocs

%check
%ctest

%post -n lib%{name}%{so_ver} -p /sbin/ldconfig
%postun -n lib%{name}%{so_ver} -p /sbin/ldconfig

%files
%license LICENSE
%doc AUTHORS README.md
%{_bindir}/srec_cat
%{_bindir}/srec_cmp
%{_bindir}/srec_info
%{_mandir}/man1/srec_*.1.gz
%{_mandir}/man5/srec_*.5.gz
%exclude %{_docdir}/%{name}/*.pdf

%files -n lib%{name}%{so_ver}
%{_libdir}/libsrecord.so.%{so_ver}*

%files devel
%{_libdir}/libsrecord.so
%{_includedir}/srecord
%{_mandir}/man3/srecord.3.gz
%{_mandir}/man3/srecord_license.3.gz

%files doc
%{_docdir}/%{name}/*.pdf

%changelog
