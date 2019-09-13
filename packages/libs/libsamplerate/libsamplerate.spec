#
# spec file for package libsamplerate
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           libsamplerate
Version:        0.1.9
Release:        0
Summary:        A Sample Rate Converter Library
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
Url:            http://www.mega-nerd.com/SRC/
Source0:        http://www.mega-nerd.com/SRC/libsamplerate-%{version}.tar.gz
Source1:        baselibs.conf
# PATCH-FEATURE-OPENSUSE -- Make build reproducible
Patch0:         libsamplerate-0.1.9-reproducible.patch
BuildRequires:  fftw3-devel
BuildRequires:  libsndfile-devel
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

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

%package progs
Summary:        Example Programs for libsamplerate
Group:          Productivity/Multimedia/Sound/Utilities

%description progs
This package includes the example programs for libsamplerate.

%prep
%setup -q
%patch0 -p1

%build
%ifnarch %arm aarch64
# ARM has no working profile support in gcc atm
profiledir=`mktemp -d`
%configure --disable-silent-rules --disable-static
make %{?_smp_mflags} CFLAGS="%optflags %cflags_profile_generate=$profiledir"
pushd tests
make check
popd
make clean
make %{?_smp_mflags} CFLAGS="%optflags %cflags_profile_feedback=$profiledir"
%else
%configure --disable-silent-rules --disable-static
make %{?_smp_mflags} CFLAGS="%optflags"
%endif

%check
pushd tests
make check
popd

%install
# Since configure doesn't honor --docdir set htmldocdir here
make install DESTDIR=%{?buildroot} \
             htmldocdir=%{_defaultdocdir}/libsamplerate-devel
# remove unneeded files
rm -f %{buildroot}%{_libdir}/*.la

%post -n libsamplerate0 -p /sbin/ldconfig
%postun -n libsamplerate0 -p /sbin/ldconfig

%files -n libsamplerate0
%defattr(-,root,root)
%doc AUTHORS COPYING
%{_libdir}/libsamplerate.so.0*

%files devel
%defattr(-,root,root)
%doc ChangeLog
%{_defaultdocdir}/libsamplerate-devel
%{_libdir}/libsamplerate.so
%{_includedir}/samplerate.h
%{_libdir}/pkgconfig/samplerate.pc

%files progs
%defattr(-,root,root)
%{_bindir}/sndfile-resample

%changelog
