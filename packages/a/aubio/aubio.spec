#
# spec file for package aubio
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


%define libpkgname libaubio5
%define debug_package_requires %{libpkgname} = %{version}-%{release}
Name:           aubio
Version:        0.4.9+git376
%define rev     ad5cf975aed08cc4562dd008cf9f83b12b82ffb8
Release:        0
Summary:        Library for real-time audio labelling
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            http://aubio.org
Source:         https://github.com/aubio/aubio/archive/%{rev}.tar.gz
#Source:         http://aubio.org/pub/%{name}-%{version}.tar.bz2
#Source1:        http://aubio.org/pub/%{name}-%{version}.tar.bz2.asc
Source99:       baselibs.conf
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  pkg-config
BuildRequires:  python3-base
BuildRequires:  sox
BuildRequires:  txt2man
BuildRequires:  waf
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavfilter)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswresample)
BuildRequires:  pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)
# Need full ffmpeg for tests
BuildConflicts: ffmpeg-4-mini-libs
BuildConflicts: ffmpeg-4-mini-devel
BuildConflicts: ffmpeg-5-mini-libs
BuildConflicts: ffmpeg-5-mini-devel
BuildConflicts: ffmpeg-6-mini-libs
BuildConflicts: ffmpeg-6-mini-devel
BuildConflicts: ffmpeg-7-mini-libs
BuildConflicts: ffmpeg-7-mini-devel
BuildConflicts: ffmpeg-8-mini-libs
BuildConflicts: ffmpeg-8-mini-devel
BuildConflicts: ffmpeg-9-mini-libs
BuildConflicts: ffmpeg-9-mini-devel

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

%package devel
Summary:        Development package for aubio library
Group:          Development/Libraries/C and C++
Requires:       %{libpkgname} = %{version}
Requires:       glibc-devel
Obsoletes:      libaubio-devel < %{version}-%{release}
Provides:       libaubio-devel = %{version}-%{release}

%description devel
This package contains the files needed to compile programs that use
aubio library.

%package tools
Summary:        Example programs for aubio library
Group:          Productivity/Multimedia/Sound/Editors and Convertors

%description tools
This package includes the example programs for aubio library.

%package doc
Summary:        Documentation for aubio library
Group:          Documentation/HTML
BuildArch:      noarch
Obsoletes:      %{name}-docs < %{version}-%{release}
Provides:       %{name}-docs = %{version}-%{release}

%description doc
This package includes the documentation for aubio library.

%prep
%autosetup -p1 -n aubio-%{rev}
# set proper library dir
sed -i -e "s#/lib#/%{_lib}#" src/wscript_build
# set python3 as testrunner
sed -i -e 's#python\ ${SRC}#python3 ${SRC}#g' tests/wscript_build

%build
waf configure --prefix=%{_prefix} --libdir=%{_libdir} --enable-fftw3
%make_build create_test_sounds
waf build -v %{?_smp_mflags}

%install
waf install --destdir=%{buildroot}
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -pR %{buildroot}%{_datadir}/doc/libaubio-doc/api %{buildroot}%{_docdir}/%{name}
rm -rf %{buildroot}%{_datadir}/doc/libaubio-doc
rm -f %{buildroot}%{_libdir}/libaubio.a
%fdupes -s %{buildroot}%{_docdir}

%ldconfig_scriptlets -n %{libpkgname}

%files -n %{libpkgname}
%{_libdir}/lib*.so.*

%files devel
%doc AUTHORS ChangeLog README.md
%license COPYING
%{_libdir}/lib*.so
%{_libdir}/pkgconfig/*.pc
%{_includedir}/aubio

%files doc
%doc %{_docdir}/%{name}

%files tools
%{_mandir}/man1/*
%{_bindir}/*

%changelog
