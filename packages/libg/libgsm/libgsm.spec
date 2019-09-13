#
# spec file for package libgsm
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


%define _name gsm
%define _version 1.0-pl18
Name:           libgsm
Version:        1.0.18
Release:        0
Summary:        GSM 06.10 Lossy Speech Compressor Library and Utilities
License:        ISC
Group:          Productivity/Multimedia/Sound/Editors and Convertors
URL:            http://www.quut.com/gsm/
Source:         http://www.quut.com/gsm/%{_name}-%{version}.tar.gz
Source2:        baselibs.conf
# This is a Debian patch file with debian chunks removed.
Patch0:         %{name}-1.0.13.patch
Patch1:         libgsm-paths.patch
Patch2:         libgsm-include.patch

%description
libgsm implements the European GSM 06.10 provisional standard for
full-rate speech transcoding, prI-ETS 300 036, which uses RPE/LTP
coding at 13 kbit/s. GSM 06.10 compresses frames of 160 13-bit
samples (8 kHz sampling rate) into 260 bits.

%package -n libgsm1
Summary:        GSM 06.10 Lossy Speech Compressor Library and Utilities
Group:          Productivity/Multimedia/Sound/Editors and Convertors

%description -n libgsm1
Contains the library for a GSM speech compressor.

libgsm implements the European GSM 06.10 provisional standard for
full-rate speech transcoding, prI-ETS 300 036, which uses RPE/LTP
(residual pulse excitation/long term prediction) coding at 13 kbit/s.
GSM 06.10 compresses frames of 160 13-bit samples (8 kHz sampling
rate) into 260 bits.

%package utils
Summary:        GSM 06.10 Lossy Speech Compressor Library and Utilities
Group:          Productivity/Multimedia/Sound/Editors and Convertors

%description utils
Contains binaries for a GSM speech compressor, verified against the
ETSI standard test patterns.

libgsm implements the European GSM 06.10 provisional standard for
full-rate speech transcoding, prI-ETS 300 036, which uses RPE/LTP
(residual pulse excitation/long term prediction) coding at 13 kbit/s.
GSM 06.10 compresses frames of 160 13-bit samples (8 kHz sampling
rate) into 260 bits.

The front-end is modeled after the historic compress(1) utility.

%package devel
Summary:        GSM 06.10 Lossy Speech Compressor Library and Utilities
Group:          Development/Libraries/C and C++
Requires:       libgsm1 = %{version}

%description devel
Contains the development kit for the libgsm speech compressor.

libgsm implements the European GSM 06.10 provisional standard for
full-rate speech transcoding, prI-ETS 300 036, which uses RPE/LTP
coding at 13 kbit/s. GSM 06.10 compresses frames of 160 13-bit
samples (8 kHz sampling rate) into 260 bits.

This implementation turns frames of 160 16-bit linear samples into
33-byte frames (1650 bytes/s) and has been verified against the ETSI
standard test patterns.

%prep
%setup -q -n %{_name}-%{_version}
%patch0 -p1
%patch1
%patch2

%build
make -j1 CCFLAGS="-c %{optflags} -D_POSIX_SOURCE -D_BSD_SOURCE -DNeedFunctionPrototypes=1" lib/libgsm.a
cp lib/libgsm.a lib/libgsm.a.save
make -j1 clean
make -j1 CCFLAGS="-c %{optflags} -D_POSIX_SOURCE -D_BSD_SOURCE -DNeedFunctionPrototypes=1 -fPIC"
cp lib/libgsm.a.save lib/libgsm.a
touch lib/libgsm.a

%install
mkdir -p %{buildroot}%{_prefix}/{include/gsm,%{_lib},bin,share/man/man{1,3}}
make INSTALL_ROOT=%{buildroot}%{_prefix} GSM_INSTALL_LIB=%{buildroot}%{_libdir} install
cp -d lib/libgsm.so* %{buildroot}%{_libdir}
( cd %{buildroot}%{_libdir} ; ln -sf libgsm.so.1 libgsm.so )
cp inc/{private.h,proto.h,unproto.h} %{buildroot}%{_includedir}/gsm/
rm -f %{buildroot}%{_libdir}/*.a

%post -n libgsm1 -p /sbin/ldconfig
%postun -n libgsm1 -p /sbin/ldconfig

%files utils
%{_bindir}/*
%{_mandir}/man1/*.*

%files -n libgsm1
%license COPYRIGHT
%doc ChangeLog MACHINES README
%{_libdir}/*.so.*

%files devel
%{_libdir}/*.so
%{_mandir}/man3/*.*
%{_includedir}/gsm

%changelog
