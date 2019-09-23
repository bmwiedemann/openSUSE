#
# spec file for package libsndfile-progs
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


Name:           libsndfile-progs
Version:        1.0.28
Release:        0
Summary:        Example Programs for libsndfile
License:        LGPL-2.1-or-later
Group:          System/Libraries
Url:            http://www.mega-nerd.com/libsndfile/
Source0:        http://www.mega-nerd.com/libsndfile/files/libsndfile-%{version}.tar.gz
Source1:        http://www.mega-nerd.com/libsndfile/files/libsndfile-%{version}.tar.gz.asc
Source2:        libsndfile.keyring
# PATCH-FIX-UPSTREAM
Patch1:         0001-FLAC-Fix-a-buffer-read-overrun.patch
Patch2:         0002-src-flac.c-Fix-a-buffer-read-overflow.patch
Patch10:        0010-src-aiff.c-Fix-a-buffer-read-overflow.patch
Patch20:        0020-src-common.c-Fix-heap-buffer-overflows-when-writing-.patch
Patch30:        0030-double64_init-Check-psf-sf.channels-against-upper-bo.patch
# not yet upstreamed, https://github.com/erikd/libsndfile/issues/317
Patch31:        0031-sfe_copy_data_fp-check-value-of-max-variable.patch
# not yet upstreamed
Patch32:        libsndfile-CVE-2017-17456-alaw-range-check.patch
Patch33:        libsndfile-CVE-2017-17457-ulaw-range-check.patch
Patch34:        sndfile-deinterlace-channels-check.patch
# PATCH-FIX-OPENSUSE
Patch100:       sndfile-ocloexec.patch
BuildRequires:  alsa-devel
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  libjack-devel
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  pkgconfig
BuildRequires:  sqlite-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This package includes the example programs for libsndfile.

%prep
%setup -q -n libsndfile-%{version}
%patch1 -p1
%patch2 -p1
%patch10 -p1
%patch20 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch100 -p1

%build
%define warn_flags -W -Wall -Wstrict-prototypes -Wpointer-arith -Wno-unused-parameter
# autoreconf --force --install
CFLAGS="%{optflags} %{warn_flags}"
export CFLAGS
%configure --disable-silent-rules \
	--disable-static \
        --enable-sqlite \
	--with-pic
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

# remove unnecessary files
rm -rf %{buildroot}%{_datadir}/doc/libsndfile
rm -rf %{buildroot}%{_libdir}
rm -rf %{buildroot}%{_includedir}
rm -rf %{buildroot}%{_datadir}/doc/libsndfile1-dev

%files
%defattr(-, root, root)
%{_bindir}/*
%doc %{_mandir}/man?/*

%changelog
