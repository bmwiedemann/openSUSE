#
# spec file for package aubio
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


%define libpkgname libaubio5
%define debug_package_requires %{libpkgname} = %{version}-%{release}
Name:           aubio
Version:        0.4.9
Release:        0
Summary:        Library for real-time audio labelling
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://aubio.org
Source:         http://aubio.org/pub/%{name}-%{version}.tar.bz2
Source1:        http://aubio.org/pub/%{name}-%{version}.tar.bz2.asc
# PATCH-FIX-UPSTREAM https://github.com/aubio/aubio/commit/cdfe9ce.patch -- [source_avcodec] avoid deprecation warning with latest avcodec api (58.134.100)
Patch0:         cdfe9ce.patch
# PATCH-FIX-UPSTREAM https://github.com/aubio/aubio/commit/8a05420.patch -- [source_avcodec] define FF_API_LAVF_AVCTX for libavcodec > 59, thx @berolinux (closes gh-353)
Patch1:         8a05420.patch

Source99:       baselibs.conf
BuildRequires:  alsa-devel
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  fftw3-devel
BuildRequires:  libjack-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  txt2man
%if 1 == 0
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
%else
BuildRequires:  ffmpeg-4-libavcodec-devel
BuildRequires:  ffmpeg-4-libavdevice-devel
BuildRequires:  ffmpeg-4-libavformat-devel
BuildRequires:  ffmpeg-4-libavutil-devel
BuildRequires:  ffmpeg-4-libswresample-devel
%endif

#ExcludeArch:    i586

%description
Aubio is a library for real time audio labelling. Its features include
segmenting a sound file before each of its attacks, performing pitch
detection, tapping the beat and producing midi streams from live audio.
The name aubio comes from 'audio' with a typo: several transcription
errors are likely to be found in the results too.

%package -n %{libpkgname}
Summary:        Library for real-time audio labelling
Group:          System/Libraries

%description -n %{libpkgname}
Aubio is a library for real time audio labelling. Its features include
segmenting a sound file before each of its attacks, performing pitch
detection, tapping the beat and producing midi streams from live audio.
The name aubio comes from 'audio' with a typo: several transcription
errors are likely to be found in the results too.

%package -n libaubio-devel
Summary:        Development package for aubio library
Group:          Development/Libraries/C and C++
Requires:       %{libpkgname} = %{version}
Requires:       glibc-devel

%description -n libaubio-devel
This package contains the files needed to compile programs that use
aubio library.

%package tools
Summary:        Example programs for aubio library
Group:          Productivity/Multimedia/Sound/Editors and Convertors

%description tools
This package includes the example programs for aubio library.

%package docs
Summary:        Documentation for aubio library
Group:          Documentation/HTML
BuildArch:      noarch

%description docs
This package includes the documentation for aubio library.

%prep
%autosetup -p1
# set proper library dir
sed -i -e "s#/lib#/%{_lib}#" src/wscript_build
# set python3 as testrunner
sed -i -e 's#python\ ${SRC}#python3 ${SRC}#g' tests/wscript_build

%build
python3 ./waf configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-fftw3
python3 ./waf build -v %{?_smp_mflags}

%install
python3 ./waf install --destdir=%{buildroot}
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -pR %{buildroot}%{_datadir}/doc/libaubio-doc/api %{buildroot}%{_docdir}/%{name}
rm -rf %{buildroot}%{_datadir}/doc/libaubio-doc
rm -f %{buildroot}%{_libdir}/libaubio.a
%fdupes -s %{buildroot}%{_docdir}

%post -n %{libpkgname} -p /sbin/ldconfig
%postun -n %{libpkgname} -p /sbin/ldconfig

%files -n %{libpkgname}
%{_libdir}/lib*.so.*

%files -n libaubio-devel
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/aubio

%files docs
%doc %{_docdir}/%{name}

%files tools
%{_mandir}/man1/*
%{_bindir}/*

%changelog
