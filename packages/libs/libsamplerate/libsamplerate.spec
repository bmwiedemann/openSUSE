#
# spec file for package libsamplerate
#
# Copyright (c) 2021 SUSE LLC
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


Name:           libsamplerate
Version:        0.2.2
Release:        0
Summary:        A Sample Rate Converter Library
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            https://libsndfile.github.io/libsamplerate/
Source0:        https://github.com/libsndfile/libsamplerate/releases/download/%{version}/libsamplerate-%{version}.tar.xz
Source1:        baselibs.conf
# PATCH-FEATURE-OPENSUSE -- Make build reproducible
Patch0:         libsamplerate-0.2.1-reproducible.patch
BuildRequires:  automake
BuildRequires:  fftw3-devel
BuildRequires:  libsndfile-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig

%description
Secret Rabbit Code (aka libsamplerate) is a Sample Rate Converter for
audio. One example of where such a thing would be useful is in
converting audio from the CD sample rate of 44.1kHz to the 48kHz sample
rate used by DAT players.

SRC is capable of arbitrary and time varying conversions; from
downsampling by a factor of 12 to upsampling by the same factor.  The
conversion ratio can also vary with time for speeding up and slowing
down effects.

%package -n libsamplerate0
Summary:        A Sample Rate Converter Library
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} < %{version}
Obsoletes:      libsamplerate-progs < %{version}

%description -n libsamplerate0
Secret Rabbit Code (aka libsamplerate) is a Sample Rate Converter for
audio. One example of where such a thing would be useful is in
converting audio from the CD sample rate of 44.1kHz to the 48kHz sample
rate used by DAT players.

SRC is capable of arbitrary and time varying conversions; from
downsampling by a factor of 12 to upsampling by the same factor.  The
conversion ratio can also vary with time for speeding up and slowing
down effects.

%package devel
Summary:        Include Files and Libraries mandatory for Development
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       libsamplerate0 = %{version}

%description devel
This package contains all necessary include files and libraries needed
to develop applications that require these.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fvi
%configure
profiledir=`mktemp -d`

%make_build CFLAGS="%{optflags} %{cflags_profile_generate}=$profiledir"
%make_build check
%make_build clean
%make_build CFLAGS="%{optflags} %{cflags_profile_feedback}=$profiledir"

%check
%make_build check

%install
%make_install
install -d %{buildroot}%{_defaultdocdir}/
mv %{buildroot}/usr/share/doc/libsamplerate %{buildroot}%{_defaultdocdir}/libsamplerate
# remove unneeded files
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libsamplerate0 -p /sbin/ldconfig
%postun -n libsamplerate0 -p /sbin/ldconfig

%files -n libsamplerate0
%license COPYING
%doc AUTHORS
%{_libdir}/libsamplerate.so.0*

%files devel
%doc ChangeLog
%{_defaultdocdir}/libsamplerate
%{_libdir}/libsamplerate.so
%{_includedir}/samplerate.h
%{_libdir}/pkgconfig/samplerate.pc

%changelog
