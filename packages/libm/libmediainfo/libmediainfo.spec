#
# spec file for package libmediainfo
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2016 Packman Team <packman@links2linux.de>
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


%define sover	0
Name:           libmediainfo
Version:        24.06
Release:        0
Summary:        Library for supplying technical and tag information about a video or audio file
License:        BSD-2-Clause
Group:          System/Libraries
URL:            https://mediaarea.net
Source:         https://mediaarea.net/download/source/%{name}/%{version}/%{name}_%{version}.tar.xz
Source1:        baselibs.conf
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmms)
BuildRequires:  pkgconfig(libzen) >= 0.4.40
BuildRequires:  pkgconfig(zlib)

%description
MediaInfo is a library that supplies technical and tag information about a
video or audio file.

%package -n %{name}%{sover}
Summary:        Library for supplying technical and tag information about a video or audio file
Group:          System/Libraries

%description -n %{name}%{sover}
MediaInfo supplies technical and tag information about a video or
audio file.

Information that can be retrieved:
* General: title, author, director, album, track number, date, duration...
* Video: codec, aspect, fps, bitrate...
* Audio: codec, sample rate, channels, language, bitrate...
* Text: language of subtitle
* Chapters: number of chapters, list of chapters

DivX, XviD, H263, H.263, H264, x264, ASP, AVC, iTunes, MPEG-1,
MPEG1, MPEG-2, MPEG2, MPEG-4, MPEG4, MP4, M4A, M4V, QuickTime,
RealVideo, RealAudio, RA, RM, MSMPEG4v1, MSMPEG4v2, MSMPEG4v3,
VOB, DVD, WMA, VMW, ASF, 3GP, 3GPP, 3GP2

Container formats that are supported:
* Video: MKV, OGM, AVI, DivX, WMV, QuickTime, Real, MPEG-1,
  MPEG-2, MPEG-4, DVD (VOB) (Codecs: DivX, XviD, MSMPEG4, ASP,
  H.264, AVC...)
* Audio: OGG, MP3, WAV, RA, AC3, DTS, AAC, M4A, AU, AIFF
* Subtitles: SRT, SSA, ASS, SAMI

This package contains the shared library for MediaInfo(-gui).

%package -n libmediainfo-devel
Summary:        Header files for libmediainfo
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sover} = %{version}
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libmms)
BuildRequires:  pkgconfig(zlib)

%description -n libmediainfo-devel
MediaInfo supplies technical and tag information about a video or
audio file.

This subpackage contains the C API header definitions.

%prep
%setup -q -n MediaInfoLib
cp Release/ReadMe_DLL_Linux.txt \
    ReadMe.txt
mv History_DLL.txt \
    History.txt

sed -i 's/\r$//' *.txt *.html Source/Doc/Documentation.html
chmod 644 *.txt *.html Source/Doc/Documentation.html

%build
# generate docs
pushd Source/Doc
    doxygen -u 2> /dev/null
    doxygen Doxyfile
popd

export CFLAGS="%{optflags} -I%{_includedir}/libmms"
export CPPFLAGS="%{optflags} -I%{_includedir}/libmms"
export CXXFLAGS="%{optflags} -I%{_includedir}/libmms"

pushd Project/GNU/Library
    autoreconf -fiv
    %configure \
    	--enable-shared \
    	--disable-static \
    	--with-libcurl \
    	--with-libmms=%{_libdir}
    make %{?_smp_mflags}
popd

%install
pushd Project/GNU/Library/
%make_install
popd

# MediaInfoDLL headers and MediaInfo-config
for i in MediaInfo MediaInfoDLL; do
    install -dm 755 %{buildroot}%{_includedir}/$i
    install -m 644 Source/$i/*.h \
    	%{buildroot}%{_includedir}/$i
done

install -m 644 Source/MediaInfoDLL/MediaInfoDLL.cs \
    %{buildroot}%{_includedir}/MediaInfoDLL
install -m 644 Source/MediaInfoDLL/MediaInfoDLL.JNA.java \
    %{buildroot}%{_includedir}/MediaInfoDLL
install -m 644 Source/MediaInfoDLL/MediaInfoDLL.JNative.java \
    %{buildroot}%{_includedir}/MediaInfoDLL
install -m 644 Source/MediaInfoDLL/MediaInfoDLL.py \
    %{buildroot}%{_includedir}/MediaInfoDLL
install -m 644 Source/MediaInfoDLL/MediaInfoDLL3.py \
    %{buildroot}%{_includedir}/MediaInfoDLL

sed -i -e '/^Libs_Static/d' \
    %{buildroot}%{_libdir}/pkgconfig/%{name}.pc
rm Doc/installdox || true
rm %{buildroot}%{_libdir}/libmediainfo.la
%fdupes -s %{buildroot}/%{_datadir}

%post   -n libmediainfo%{sover} -p /sbin/ldconfig
%postun -n libmediainfo%{sover} -p /sbin/ldconfig

%files -n %{name}%{sover}
%license License.html
%doc History.txt ReadMe.txt
%{_libdir}/libmediainfo.so.%{sover}
%{_libdir}/libmediainfo.so.%{sover}.*

%files -n libmediainfo-devel
%doc Changes.txt Source/Doc/Documentation.html
%doc Doc/*
%{_includedir}/MediaInfo/
%{_includedir}/MediaInfoDLL/
%{_libdir}/libmediainfo.so
%{_libdir}/pkgconfig/*.pc

%changelog
