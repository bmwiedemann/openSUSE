#
# spec file for package cdparanoia
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


%define filever III-10.2
Name:           cdparanoia
Version:        3.10.2
Release:        0
Summary:        A Program for Extracting, Verifying, and Fixing Audio Tracks from CDs
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/CD/Grabbers
URL:            http://www.xiph.org/paranoia/index.html
Source:         http://downloads.xiph.org/releases/%{name}/%{name}-%{filever}.src.tgz
Source2:        baselibs.conf
Patch1:         010_build_system.patch
Patch2:         cdparanoia-III-ide_majors.patch
Patch3:         cdparanoia-III-c++.patch
Patch4:         050_all_build_only_shared_libraries.patch
Patch10:        cdparanoia-III-01-typos-and-spelling.dpatch
Patch11:        cdparanoia-III-05-gcc4.3.dpatch
Patch12:        cdparanoia-III-06-endian.dpatch
Patch14:        config-guess-sub-update.diff
BuildRequires:  autoconf
BuildRequires:  automake
Provides:       cdparano = %{version}
Obsoletes:      cdparano < %{version}

%package -n libcdda_interface0
Summary:        Library for Extracting, Verifying, and Fixing Audio Tracks from CDs
License:        LGPL-2.1-or-later
Group:          System/Libraries
Suggests:       ImageMagick-extra = %{version}

%package -n libcdda_paranoia0
Summary:        Library for Extracting, Verifying, and Fixing Audio Tracks from CDs
License:        LGPL-2.1-or-later
Group:          System/Libraries

%package devel
Summary:        Development files for cdparanoia, a library for extractnig audio tracks from CDs
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libcdda_interface0 = %{version}
Requires:       libcdda_paranoia0 = %{version}

%description
This CDDA reader distribution ('cdparanoia') reads audio from the
CD-ROM directly as data and writes the data to a file or pipe as .wav,
.aifc, or raw 16-bit linear PCM.

%description devel
This CDDA reader distribution ('cdparanoia') reads audio from the
CD-ROM directly as data and writes the data to a file or pipe as .wav,
.aifc, or raw 16-bit linear PCM.

%description -n libcdda_interface0
This CDDA reader distribution ('cdparanoia') reads audio from the
CD-ROM directly as data and writes the data to a file or pipe as .wav,
.aifc, or raw 16-bit linear PCM.

%description -n libcdda_paranoia0
This CDDA reader distribution ('cdparanoia') reads audio from the
CD-ROM directly as data and writes the data to a file or pipe as .wav,
.aifc, or raw 16-bit linear PCM.

%prep
%setup -q -n cdparanoia-%{filever}
%patch -P 1 -p1
%patch -P 2
%patch -P 3
%patch -P 4
%patch -P 10 -p1
%patch -P 11 -p1
%patch -P 12 -p1
%patch -P 14

%build
autoreconf -vfi
%configure
%make_build OPT="%{optflags}"

%install
make prefix=%{buildroot}%{_prefix} \
     LIBDIR=%{buildroot}%{_libdir} \
     MANDIR=%{buildroot}%{_mandir} \
     BINDIR=%{buildroot}%{_bindir} \
     INCLUDEDIR=%{buildroot}%{_includedir} \
       install
JAPN_MANDIR=%{buildroot}%{_mandir}/ja/man1
mkdir -p $JAPN_MANDIR
install -m644 cdparanoia.1.jp $JAPN_MANDIR/cdparanoia.1

%post -n libcdda_interface0 -p /sbin/ldconfig
%postun -n libcdda_interface0 -p /sbin/ldconfig
%post -n libcdda_paranoia0 -p /sbin/ldconfig
%postun -n libcdda_paranoia0 -p /sbin/ldconfig

%files
%doc README
%license COPYING-GPL
%{_mandir}/man1/*
%{_mandir}/ja
%{_bindir}/*

%files -n libcdda_interface0
%license COPYING-LGPL
%{_libdir}/libcdda_interface.so.0
%{_libdir}/libcdda_interface.so.0.*

%files -n libcdda_paranoia0
%license COPYING-LGPL
%{_libdir}/libcdda_paranoia.so.0
%{_libdir}/libcdda_paranoia.so.0.*

%files devel
%{_includedir}/*
%{_libdir}/libcdda_paranoia.so
%{_libdir}/libcdda_interface.so

%changelog
