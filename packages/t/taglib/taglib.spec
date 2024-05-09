#
# spec file for package taglib
#
# Copyright (c) 2024 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%global sname taglib
%if "%{flavor}" != ""
%global psuffix -%{flavor}
# build also examples with tests
%bcond_without tests
%else
%global psuffix %{nil}
%bcond_with tests
%endif
Name:           taglib%{psuffix}
Version:        2.0
Release:        0
Summary:        Audio Meta-Data Library
License:        LGPL-2.1-or-later AND MPL-1.1
Group:          Productivity/Multimedia/Other
URL:            https://taglib.github.io/
Source0:        https://taglib.github.io/releases/taglib-%{version}.tar.gz
Source1:        %{sname}.desktop
Source100:      baselibs.conf
Patch1:         taglib-utf8cpp-include.patch
BuildRequires:  cmake >= 2.8
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  cmake(utf8cpp)
BuildRequires:  pkgconfig(zlib)
# NOTE: The tagreader and writer executables give different results when built with
# an earlier taglib-1.8-ds-rusxmms patch. See bnc#814814
Requires:       libtag2 >= %{version}-%{release}
Requires:       libtag_c2 >= %{version}-%{release}
%if %{with tests}
BuildRequires:  doxygen
BuildRequires:  ghostscript-fonts-std
BuildRequires:  graphviz-gd
BuildRequires:  libcppunit-devel
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
%endif

%description
TagLib is a library for reading and editing the meta-data of several popular
audio formats. Currently it supports both ID3v1 and ID3v2 for MP3 files, Ogg
Vorbis comments and ID3 tags and Vorbis comments in FLAC, MPC, Speex, WavPack
TrueAudio, WAV, AIFF, MP4 and ASF files.
This package contains built examples which manipulate tags from the
command line.

%package -n libtag2
Summary:        Audio Meta-Data Library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Conflicts:      taglib <= 1.6.3

%description -n libtag2
TagLib is a library for reading and editing the meta-data of several popular
audio formats. Currently it supports both ID3v1 and ID3v2 for MP3 files, Ogg
Vorbis comments and ID3 tags and Vorbis comments in FLAC, MPC, Speex, WavPack
TrueAudio, WAV, AIFF, MP4 and ASF files.

%package -n libtag_c2
Summary:        Audio Meta-Data Library
License:        LGPL-2.1-or-later
Group:          System/Libraries
Conflicts:      taglib <= 1.6.3

%description -n libtag_c2
TagLib is a library for reading and editing the meta-data of several popular
audio formats. Currently it supports both ID3v1 and ID3v2 for MP3 files, Ogg
Vorbis comments and ID3 tags and Vorbis comments in FLAC, MPC, Speex, WavPack
TrueAudio, WAV, AIFF, MP4 and ASF files.

%package -n libtag-devel
Summary:        Development files for taglib
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libstdc++-devel
Requires:       libtag2 >= %{version}-%{release}
Requires:       libtag_c2 >= %{version}-%{release}
Requires:       zlib-devel
# taglib-devel was last used in openSUSE 11.4 (taglib-devel-1.6.2)
# The last taglib-devel used was version 1.6.3 from multimedia:libs.
Provides:       taglib-devel = %{version}
Obsoletes:      taglib-devel <= 1.6.3

%description -n libtag-devel
This package contains development files for taglib.

%package -n libtag-doc
Summary:        API documentation for taglib
License:        LGPL-2.1-or-later
Group:          Documentation/HTML
BuildArch:      noarch

%description -n libtag-doc
This package contains the taglib API Documentation in HTML format.

%prep
%autosetup -p1 -n %{sname}-%{version}

%build
# The testing needs static libs too
%cmake \
  -DCMAKE_SKIP_BUILD_RPATH=ON \
%if %{with tests}
  -DBUILD_TESTS:BOOL=ON \
  -DBUILD_EXAMPLES:BOOL=OFF \
  -DBUILD_STATIC_LIBS:BOOL=ON \
  -DBUILD_SHARED_LIBS:BOOL=OFF
%else
  -DBUILD_TESTS:BOOL=OFF \
  -DBUILD_EXAMPLES:BOOL=ON
%endif
%cmake_build

%if %{with tests}
%cmake_build docs
%endif

%install
%if %{with tests}
# install susehelp file
mkdir -p %{buildroot}%{_datadir}/susehelp/meta/Development/Libraries/
install -pm 0644 %{SOURCE1} %{buildroot}%{_datadir}/susehelp/meta/Development/Libraries/

%suse_update_desktop_file %{buildroot}%{_datadir}/susehelp/meta/Development/Libraries/%{sname}.desktop

# Documentation
mkdir -p %{buildroot}%{_defaultdocdir}/libtag-doc
# Copy manually, otherwise fdupes does not work
cp -a build/doc/html/ %{buildroot}%{_defaultdocdir}/libtag-doc/

%else
%cmake_install
# install the examples
install -m755 build/examples/{framelist,strip-id3v1,tagreader,tagreader_c,tagwriter} %{buildroot}%{_bindir}
%endif
%fdupes %{buildroot}

%check
%if %{with tests}
%ctest
%endif

%if !%{with tests}
%post -n libtag2 -p /sbin/ldconfig
%postun -n libtag2 -p /sbin/ldconfig
%post -n libtag_c2 -p /sbin/ldconfig
%postun -n libtag_c2 -p /sbin/ldconfig

%files
%license COPYING.LGPL COPYING.MPL
%{_bindir}/*
%exclude %{_bindir}/taglib-config

%files -n libtag2
%license COPYING.LGPL COPYING.MPL
%{_libdir}/libtag.so.2
%{_libdir}/libtag.so.2.*

%files -n libtag_c2
%license COPYING.LGPL COPYING.MPL
%{_libdir}/libtag_c.so.2
%{_libdir}/libtag_c.so.2.*

%files -n libtag-devel
%{_bindir}/taglib-config
%{_includedir}/taglib/
%{_libdir}/libtag*.so
%{_libdir}/pkgconfig/*.pc
%dir %{_libdir}/cmake/taglib
%{_libdir}/cmake/taglib/*.cmake
%else

%files -n libtag-doc
%doc AUTHORS CHANGELOG.md examples
%{_docdir}/libtag-doc/html
%{_datadir}/susehelp/
%endif

%changelog
