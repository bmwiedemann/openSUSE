#
# spec file for package aubio
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
Source99:       baselibs.conf
BuildRequires:  alsa-devel
BuildRequires:  doxygen
BuildRequires:  fftw3-devel
BuildRequires:  libjack-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  pkg-config
BuildRequires:  python-devel
%if 0%{?suse_version} > 1320 || (0%{?suse_version} == 1315 && 0%{?is_opensuse})
BuildRequires:  txt2man
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavresample)
BuildRequires:  pkgconfig(libavutil)
%endif

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

%prep
%setup -q
sed -e "s,/lib,/%{_lib}," src/wscript_build > src/wscript_build.new
diff -u src/wscript_build src/wscript_build.new || :
mv src/wscript_build.new src/wscript_build

%build
./waf configure --prefix=%{_prefix} --libdir=%{_libdir}
./waf build

%install
./waf install --destdir=%{buildroot}
mkdir -p %{buildroot}%{_docdir}/%{name}
cp -pR %{buildroot}%{_datadir}/doc/libaubio-doc/api %{buildroot}%{_docdir}/%{name}
rm -rf %{buildroot}%{_datadir}/doc/libaubio-doc
rm -f %{buildroot}%{_libdir}/libaubio.a

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

%files tools
%doc %{_docdir}/%{name}
%if 0%{?suse_version} > 1320 || (0%{?suse_version} == 1315 && 0%{?is_opensuse})
%{_mandir}/man1/*
%endif
%{_bindir}/*

%changelog
