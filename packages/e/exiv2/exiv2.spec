#
# spec file for package exiv2
#
# Copyright (c) 2022 SUSE LLC
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


%bcond_with docs
Name:           exiv2
Version:        0.27.5
Release:        0
Summary:        Tool to access image Exif metadata
License:        BSD-3-Clause AND GPL-2.0-or-later
Group:          Productivity/Graphics/Other
URL:            https://exiv2.org/
Source0:        https://github.com/Exiv2/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         exiv2-build-date.patch
Patch1:         CVE-2022-3953.patch
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  libcurl-devel
BuildRequires:  libexpat-devel
BuildRequires:  libxslt
BuildRequires:  python3-base
BuildRequires:  pkgconfig(zlib)
Recommends:     %{name}-lang = %{version}
%if %{with docs}
BuildRequires:  doxygen
# doxygen likes to have this
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
# Todo: graph generation fails with missing fonts
%else
Obsoletes:      libexiv2-doc < %{version}-%{release}
%endif
# there is a test failure on ARM & PPC
# upstream issue: https://github.com/Exiv2/exiv2/issues/933
%ifarch x86_64
%{bcond_without tests}
%else
%{bcond_with tests}
%endif
%if %{with tests}
# testsuite:
BuildRequires:  dos2unix
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  libxml2-tools
BuildRequires:  which
%endif

%description
Exiv2 is a command line utility to access image metadata from tags like
Exif.

%package -n libexiv2-27
Summary:        Library to access image metadata
Group:          System/Libraries

%description -n libexiv2-27
libexiv2 is a C++ library with a C compatibility interface to access
image metadata, esp from Exif tags.

%package -n libexiv2-xmp-static
Summary:        Library required too link libexiv2
Group:          System/Libraries

%description -n libexiv2-xmp-static
libexiv2-xmp is a static library required to link with libexiv2.

%package -n libexiv2-devel
Summary:        Development Headers for Exiv2
Group:          Development/Libraries/C and C++
Requires:       libexiv2-27 = %{version}
# needed by exiv2Config.cmake
Requires:       libexiv2-xmp-static
Requires:       libexpat-devel
Requires:       libstdc++-devel

%description -n libexiv2-devel
Exiv2 is a C++ library and a command line utility to access image
metadata.

%package -n libexiv2-doc
Summary:        Library to access image metadata - Documentation
Group:          System/Libraries

%description -n libexiv2-doc
libexiv2 is a C++ library with a C compatibility interface to access
image metadata, esp from Exif tags. This package contains the developer
documentation in HTML format.

%lang_package

%prep
%autosetup -p1
# Upstream will switch to C++11 with 0.28.0, but googletest requires C++11
# See https://github.com/Exiv2/exiv2/issues/1163
sed -i -e 's/CXX_STANDARD 98/CXX_STANDARD 11/' cmake/mainSetup.cmake

%build
%global _lto_cflags %{_lto_cflags} -ffat-lto-objects
export CXXFLAGS="%{optflags} $(getconf LFS_CFLAGS)"
export CFLAGS="%{optflags} $(getconf LFS_CFLAGS)"
%cmake \
        -DCMAKE_INSTALL_DOCDIR="%{_docdir}/libexiv2" \
%if %{with tests}
        -DEXIV2_BUILD_SAMPLES=ON \
        -DEXIV2_BUILD_UNIT_TESTS=ON \
%else
        -DEXIV2_BUILD_SAMPLES=OFF \
        -DEXIV2_BUILD_UNIT_TESTS=OFF \
%endif
        -DEXIV2_BUILD_PO=ON \
%if %{with docs}
        -DEXIV2_BUILD_DOC=ON \
%else
        -DEXIV2_BUILD_DOC=OFF \
%endif
        -DEXIV2_ENABLE_CURL=ON \
        -DEXIV2_ENABLE_WEBREADY=ON \
        -DEXIV2_ENABLE_NLS=ON \
        -DEXIV2_ENABLE_BMFF=ON \
        -DCMAKE_SKIP_RPATH=OFF

%cmake_build
# make %{?_smp_mflags} doc

%install
%cmake_install

%if %{with tests}
%check
pushd build
%make_build tests
popd

for t in \
    addmoddel \
    convert-test \
    easyaccess-test \
    exifcomment \
    exifdata \
    exifdata-test \
    exifprint \
    exifvalue \
    exiv2json \
    geotag \
    ini-test \
    iotest \
    iptceasy \
    iptcprint \
    iptctest \
    key-test \
    largeiptc-test \
    metacopy \
    mmap-test \
    mrwthumb \
    path-test \
    prevtest \
    stringto-test \
    taglist \
    tiff-test \
    werror-test \
    write-test \
    write2-test \
    xmpdump \
    xmpparse \
    xmpparser-test \
    xmpprint \
    xmpsample \
    ; do
    rm -f %{buildroot}%{_bindir}/${t}
    rm -f %{buildroot}%{_prefix}/lib/debug%{_bindir}/${t}*
done
%endif

%find_lang exiv2
%fdupes -s %{buildroot}%{_docdir}/libexiv2

%post -n libexiv2-27 -p /sbin/ldconfig
%postun -n libexiv2-27 -p /sbin/ldconfig

%files lang -f exiv2.lang

%files
%doc doc/ChangeLog doc/cmd.txt
%license COPYING
%{_bindir}/exiv2
%{_mandir}/man1/*

%files -n libexiv2-27
%{_libdir}/libexiv2.so.*

%files -n libexiv2-xmp-static
%{_libdir}/libexiv2-xmp.a

%files -n libexiv2-devel
%{_includedir}/exiv2
%{_libdir}/libexiv2.so
# needed by exiv2Config.cmake
%{_libdir}/pkgconfig/exiv2.pc
%dir %{_libdir}/cmake
%dir %{_libdir}/cmake/exiv2
%{_libdir}/cmake/exiv2/exiv2Config-relwithdebinfo.cmake
%{_libdir}/cmake/exiv2/exiv2Config.cmake
%{_libdir}/cmake/exiv2/exiv2ConfigVersion.cmake

%if %{with docs}
%files -n libexiv2-doc
%{_docdir}/libexiv2
%endif

%changelog
