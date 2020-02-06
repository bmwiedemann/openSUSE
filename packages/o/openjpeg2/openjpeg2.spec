#
# spec file for package openjpeg2
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


%define library_name  libopenjp2-7
%define base_version 2.3

Name:           openjpeg2
Version:        2.3.1
Release:        0
Summary:        Opensource JPEG 2000 Codec Implementation
License:        BSD-2-Clause
Group:          Productivity/Graphics/Other
URL:            http://www.openjpeg.org/
Source0:        https://github.com/uclouvain/openjpeg/archive/v%{version}.tar.gz#/openjpeg-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FIX-UPSTREAM -- like CVE-2018-6616, but rle4 instead of rle8, bsc#1079845, https://github.com/uclouvain/openjpeg/commit/21399f6b7d318fcd.patch
Patch0:         21399f6b7d318fcd.patch
# PATCH-FIX-UPSTREAM -- CVE-2019-12973, bsc#1140359, https://github.com/uclouvain/openjpeg/commit/3aef207f90e937d4.patch
Patch1:         3aef207f90e937d4.patch
# PATCH-FIX-UPSTREAM -- OSS-fuzz, https://github.com/uclouvain/openjpeg/commit/4cb1f663049aab96.patch
Patch2:         4cb1f663049aab96.patch
# PATCH-FIX-UPSTREAM -- CVE-2020-6851, bsc#1160782, https://github.com/uclouvain/openjpeg/commit/024b8407392cb0b8.patch
Patch3:         024b8407392cb0b8.patch
# PATCH-FIX-UPSTREAM -- CVE-2020-8112, bsc#1162090, https://github.com/uclouvain/openjpeg/commit/05f9b91e60debda0.patch
Patch4:         05f9b91e60debda0.patch
BuildRequires:  cmake > 2.8.2
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The OpenJPEG library is an open-source JPEG 2000 codec written in C language.
It has been developed in order to promote the use of JPEG 2000, the new
still-image compression standard from the Joint Photographic Experts Group
(JPEG).

This package provides the codec executables.

%package -n %{library_name}
Summary:        Opensource JPEG 2000 Codec Implementation
Group:          System/Libraries

%description -n %{library_name}
The OpenJPEG library is an open-source JPEG 2000 codec written in C language.
It has been developed in order to promote the use of JPEG 2000, the new
still-image compression standard from the Joint Photographic Experts Group
(JPEG).

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{library_name} = %{version}
Requires:       %{name} = %{version}
Recommends:     %{name}-devel-doc

%description    devel
The OpenJPEG library is an open-source JPEG 2000 codec written in C language.
It has been developed in order to promote the use of JPEG 2000, the new
still-image compression standard from the Joint Photographic Experts Group
(JPEG).

This package provides the development files for %{name}.

%package        devel-doc
Summary:        API documentation for %{name}
Group:          Documentation/HTML
Recommends:     %{library_name} = %{version}
Recommends:     %{name} = %{version}

%description    devel-doc
The OpenJPEG library is an open-source JPEG 2000 codec written in C language.

This package provides the API documentation for %{name}.

%prep
%setup -q -n openjpeg-%{version}
%autopatch -p1

# do not embed timestamps into html documentation
sed -i 's|^HTML_TIMESTAMP[ =].*$|HTML_TIMESTAMP = NO|' doc/Doxyfile.dox.cmake.in

# ensure no bundled libraries are used, but keep thirdparty/CMakeLists.txt
for d in thirdparty/*; do
    [ -d "$d" ] && rm -rf "$d"
done

%build
%cmake \
  -DBUILD_SHARED_LIBS=ON \
  -DBUILD_CODEC=ON \
  -DBUILD_JPIP=OFF \
  -DBUILD_JPWL=OFF \
  -DBUILD_MJ2=OFF \
  -DBUILD_TESTING=OFF \
  -DBUILD_DOC=ON \
  -DBUILD_THIRDPARTY=OFF \
  -DOPENJPEG_INSTALL_LIB_DIR=%{_lib} \
  -DOPENJPEG_INSTALL_DOC_DIR=share/doc/packages/%{name}-devel-doc

make %{?_smp_mflags} VERBOSE=1 all doc

%install
%cmake_install
rm %{buildroot}%{_defaultdocdir}/%{name}-devel-doc/LICENSE
mv %{buildroot}%{_prefix}/share/doc/html %{buildroot}%{_defaultdocdir}/%{name}-devel-doc
%fdupes %{buildroot}%{_defaultdocdir}

%post -n %{library_name} -p /sbin/ldconfig

%postun -n %{library_name} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license LICENSE
%{_bindir}/opj_*
%{_mandir}/man1/opj_*.1%{ext_man}

%files -n %{library_name}
%defattr(-,root,root,-)
%{_libdir}/libopenjp2.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/openjpeg-%{base_version}/
%{_libdir}/libopenjp2.so
%{_libdir}/pkgconfig/libopenjp2.pc
%{_libdir}/openjpeg-%{base_version}/
%{_mandir}/man3/libopenjp2.3%{ext_man}

%files devel-doc
%defattr(-,root,root,-)
%license LICENSE
%doc AUTHORS.md CHANGELOG.md NEWS.md README.md THANKS.md
%doc %{_defaultdocdir}/%{name}-devel-doc/html

%changelog
