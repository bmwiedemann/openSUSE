#
# spec file for package exiv2
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


# the tests don't work on Leap 42.x & SLE <= 12 because gmock & gtest are
# missing
%if 0%{?suse_version} <= 1315
%{bcond_with tests}
%else
# there is a test failure on ARM & PPC
# upstream issue: https://github.com/Exiv2/exiv2/issues/933
%ifarch x86_64
%{bcond_without tests}
%else
%{bcond_with tests}
%endif
%endif

Name:           exiv2
Version:        0.27.2
Release:        0
Summary:        Tool to access image Exif metadata
License:        GPL-2.0-or-later AND BSD-3-Clause
Group:          Productivity/Graphics/Other
URL:            http://www.exiv2.org/
Source0:        https://github.com/Exiv2/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
Patch0:         exiv2-build-date.patch
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
# doxygen likes to have this
BuildRequires:  graphviz
BuildRequires:  libcurl-devel
BuildRequires:  libexpat-devel
BuildRequires:  libxslt
BuildRequires:  python3-base
BuildRequires:  zlib-devel
%if %{with tests}
# testsuite:
BuildRequires:  dos2unix
BuildRequires:  gmock
BuildRequires:  gtest
BuildRequires:  libxml2-tools
BuildRequires:  which
%endif
Recommends:     %{name}-lang = %{version}

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
        -DEXIV2_BUILD_DOC=ON \
        -DEXIV2_ENABLE_CURL=ON \
        -DEXIV2_ENABLE_WEBREADY=ON \
        -DEXIV2_ENABLE_NLS=ON \
        -DCMAKE_SKIP_RPATH=OFF
make %{?_smp_mflags}
make %{?_smp_mflags} doc

%install
%cmake_install

%if %{with tests}
%check
pushd build
make tests
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
    rm -f %{buildroot}/usr/lib/debug%{_bindir}/${t}*
done
%endif

%find_lang exiv2
%fdupes -s %{buildroot}%{_docdir}/libexiv2

%post -n libexiv2-27 -p /sbin/ldconfig
%postun -n libexiv2-27 -p /sbin/ldconfig

%files lang -f exiv2.lang

%files
%doc doc/ChangeLog doc/cmd.txt
%license COPYING COPYING-CMAKE-SCRIPTS
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

%files -n libexiv2-doc
%{_docdir}/libexiv2

%changelog
