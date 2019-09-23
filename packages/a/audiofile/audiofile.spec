#
# spec file for package audiofile
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define so_num 1

Name:           audiofile
Version:        0.3.6
Release:        0
Summary:        An Audio File Library
License:        GPL-2.0-or-later AND LGPL-2.1-or-later
Group:          System/Libraries
%define lname	libaudiofile%{so_num}
Url:            http://www.68k.org/~michael/audiofile/
Source:         http://download.gnome.org/sources/audiofile/0.3/%{name}-%{version}.tar.xz
Source2:        baselibs.conf
# PATCH-FIX-SECURITY audiofile-CVE-2015-7747.patch bsc949399 CVE-2015-7747 sbrabec@suse.com -- Fix overflow when changing both number of channels and sample format https://github.com/mpruett/audiofile/pull/25/files https://github.com/mpruett/audiofile/pull/25.patch
Patch:          audiofile-CVE-2015-7747.patch
Patch2:         audiofile-gcc6.patch
# PATCH-FIX-UPSTREAM 0001-Always-check-the-number-of-coefficients.patch boo#1026978 alarrosa@suse.com -- Check number of coefficients https://github.com/mpruett/audiofile/pull/42
Patch3:         0001-Always-check-the-number-of-coefficients.patch
# PATCH-FIX-UPSTREAM 0002-Check-for-multiplication-overflow-in-MSADPCM-decodeS.patch boo#1026978 alarrosa@suse.com -- Check for multiplication overflow in MSADPCM.cpp https://github.com/mpruett/audiofile/pull/42
Patch4:         0002-Check-for-multiplication-overflow-in-MSADPCM-decodeS.patch
# PATCH-FIX-UPSTREAM 0003-Check-for-multiplication-overflow-in-sfconvert.patch boo#1026978 alarrosa@suse.com -- Check for multiplication overflow in sfconvert https://github.com/mpruett/audiofile/pull/42
Patch5:         0003-Check-for-multiplication-overflow-in-sfconvert.patch
# PATCH-FIX-UPSTREAM 0004-clamp-index-values-to-fix-index-overflow-in-IMA.cpp.patch boo#1026981 alarrosa@suse.com -- Clamp index values to fix index overflow https://github.com/mpruett/audiofile/pull/43
Patch6:         0004-clamp-index-values-to-fix-index-overflow-in-IMA.cpp.patch
# PATCH-FIX-UPSTREAM 0005-Actually-fail-when-error-occurs-in-parseFormat.patch boo#1026983 alarrosa@suse.com -- Actually fail when error occurs in parseFormat https://github.com/mpruett/audiofile/pull/44
Patch7:         0005-Actually-fail-when-error-occurs-in-parseFormat.patch
# PATCH-FIX-UPSTREAM 0006-Check-for-division-by-zero-in-BlockCodec-runPull.patch boo#1026983 alarrosa@suse.com -- Check for division by zero in BlockCodec::runPull https://github.com/mpruett/audiofile/pull/44
Patch8:         0006-Check-for-division-by-zero-in-BlockCodec-runPull.patch
# PATCH-FIX-UPSTREAM 0007-set-the-output-chunk-to-the-amount-of-frames.patch boo#11115865 qzheng@suse.com -- Set output chunk framecount after pull https://github.com/mpruett/audiofile/pull/52
Patch9:         0007-set-the-output-chunk-to-the-amount-of-frames.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  xz
%if 0%{?sles_version}
BuildRequires:  flac-devel >= 1.2.1
%else
BuildRequires:  pkgconfig(flac) >= 1.2.1
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This audio file library is an implementation of the SGI audio file
library. At present, not all features of the SGI audio file library are
implemented.

This library allows the processing of audio data to and from audio
files of many common formats (currently AIFF, AIFC, WAVE, and
NeXT/Sun).

%package -n %lname
Summary:        An Audio File Library
Group:          System/Libraries

%description -n %lname
This audio file library is an implementation of the SGI audio file
library. At present, not all features of the SGI audio file library are
implemented.

This library allows the processing of audio data to and from audio
files of many common formats (currently AIFF, AIFC, WAVE, and
NeXT/Sun).

%package devel
Summary:        An audio file library
Group:          Development/Libraries/C and C++
Requires:       %lname = %{version}

%description devel
This Audio File Library is an implementation of the SGI Audio File
library. At present, not all features of the SGI Audio File library are
implemented.

This library allows the processing of audio data to and from audio
files of many common formats (currently AIFF, AIFC, WAVE, and
NeXT/Sun).

%package doc
Summary:        An audio file library
Group:          Documentation/Man
Requires:       %{name} = %{version}

%description doc
This Audio File Library is an implementation of the SGI Audio File
library. At present, not all features of the SGI Audio File library are
implemented.

This library allows the processing of audio data to and from audio
files of many common formats (currently AIFF, AIFC, WAVE, and
NeXT/Sun).

%prep
%setup -q
%patch -p1
%patch2
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1

%build
autoreconf -fi
%configure --disable-examples
make %{?_smp_mflags}
cp -a docs install_docs
rm install_docs/Makefile*

%install
make DESTDIR=$RPM_BUILD_ROOT install
rm %{buildroot}/%{_libdir}/*.la
# The static library is needed for "UnitTests" (from make check) to build
rm %{buildroot}/%{_libdir}/*.a

%check
make check %{?_smp_mflags}

%post -n %lname -p /sbin/ldconfig

%postun -n %lname -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc README TODO COPYING* ACKNOWLEDGEMENTS AUTHORS NEWS NOTES
%{_bindir}/sfconvert
%{_bindir}/sfinfo
%{_mandir}/man1/sfconvert.1*
%{_mandir}/man1/sfinfo.1*

%files -n %lname
%defattr(-,root,root)
%{_libdir}/libaudiofile.so.%{so_num}*

%files devel
%defattr(-, root, root)
%{_includedir}/*
%{_libdir}/libaudiofile.so
%{_libdir}/pkgconfig/audiofile.pc

%files doc
%defattr(-, root, root)
%{_mandir}/man3/af*.3*

%changelog
