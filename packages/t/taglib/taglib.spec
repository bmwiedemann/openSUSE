#
# spec file for package taglib
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Version:        2.1.1
Release:        0
Summary:        Audio Meta-Data Library
License:        LGPL-2.1-or-later AND MPL-1.1
Group:          Productivity/Multimedia/Other
URL:            https://taglib.github.io/
Source0:        https://taglib.github.io/releases/taglib-%{version}.tar.gz
Source100:      baselibs.conf
Patch1:         taglib-utf8cpp-include.patch
Patch2:         0001-Do-not-warn-when-seeing-FLAC-picture-block-in-Ogg-fi.patch
Patch3:         0002-Set-last-header-flag-in-FLAC-Metadata-block-type-fie.patch
Patch4:         0003-Avoid-corrupting-an-invalid-FLAC-Ogg-file-without-Vo.patch
Patch5:         0004-Fix-reading-of-last-page-in-ogg-stream.patch
BuildRequires:  cmake >= 3.5
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  cmake(utf8cpp)
BuildRequires:  pkgconfig(zlib)
%if %{with tests}
BuildRequires:  doxygen
BuildRequires:  ghostscript-fonts-std
BuildRequires:  graphviz-gd
BuildRequires:  libcppunit-devel
%endif

%description
TagLib is a library for reading and editing the meta-data of several popular
audio formats. Currently it supports both ID3v1 and ID3v2 for MP3 files, Ogg
Vorbis comments and ID3 tags and Vorbis comments in FLAC, MPC, Speex, WavPack
TrueAudio, WAV, AIFF, MP4 and ASF files.

This package contains built examples to read and write tags from the
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
Requires:       libtag2 = %{version}-%{release}
Requires:       libtag_c2 = %{version}-%{release}
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
%ldconfig_scriptlets -n libtag2
%ldconfig_scriptlets -n libtag_c2

%files
%license COPYING.LGPL COPYING.MPL
%{_bindir}/framelist
%{_bindir}/strip-id3v1
%{_bindir}/tagreader
%{_bindir}/tagreader_c
%{_bindir}/tagwriter
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
%endif

%changelog
