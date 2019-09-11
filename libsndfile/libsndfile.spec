#
# spec file for package libsndfile
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


%define lname	%{name}1
Name:           libsndfile
Version:        1.0.28
Release:        0
Summary:        Development/Libraries/C and C++
License:        LGPL-2.1-or-later
Group:          System/Libraries
Url:            http://www.mega-nerd.com/libsndfile
Source0:        http://www.mega-nerd.com/%{name}/files/%{name}-%{version}.tar.gz
Source1:        http://www.mega-nerd.com/%{name}/files/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
Source3:        baselibs.conf
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
# not yet upstreamed, CVE-2018-19758, bsc#1117954
Patch40:        libsndfile-wav-loop-count-fix.patch
# PATCH-FIX-OPENSUSE
Patch100:       sndfile-ocloexec.patch
BuildRequires:  alsa-devel
BuildRequires:  flac-devel
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  libvorbis-devel
BuildRequires:  pkg-config
BuildRequires:  speex-devel
BuildRequires:  sqlite-devel
Obsoletes:      libsnd
Provides:       libsnd
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Libsndfile is a C library for reading and writing sound files, such as
AIFF, AU, and WAV files, through one standard interface.  It can
currently read and write 8, 16, 24, and 32-bit PCM files as well as
32-bit floating point WAV files and a number of compressed formats.

%package -n %{lname}
Summary:        A Library to Handle Various Audio File Formats
Group:          System/Libraries
Provides:       %{name} = %{version}
Obsoletes:      %{name} <= 1.0.25

%description -n %{lname}
Libsndfile is a C library for reading and writing sound files, such
as AIFF, AU, and WAV files, through one standard interface. It can
currently read and write 8, 16, 24, and 32-bit PCM files as well as
32-bit floating point WAV files and a number of compressed formats.

%package devel
Summary:        Development package for the libsndfile library
Group:          Development/Libraries/C and C++
Requires:       %{lname} = %{version}
Requires:       glibc-devel
Requires:       libstdc++-devel
Obsoletes:      libsndd
Provides:       libsndd

%description devel
This package contains the files needed to compile programs that use the
libsndfile library.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch10 -p1
%patch20 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch40 -p1
%patch100 -p1

%build
%define warn_flags -W -Wall -Wstrict-prototypes -Wpointer-arith -Wno-unused-parameter
%if 0%{?suse_version} < 1200
sed -i -e'/^AM_SILENT_RULES/d' configure.ac
%endif
autoreconf --force --install
CFLAGS="%{optflags} %{warn_flags}"
export CFLAGS
%configure \
	--disable-silent-rules \
	--disable-static \
	--enable-sqlite \
	--with-pic \
	--enable-experimental
make %{?_smp_mflags}

%install
%make_install
# remove unnecessary files
find %{buildroot} -type f -name "*.la" -delete -print
# remove programs; built in another spec file
rm -rf %{buildroot}%{_bindir}
rm -rf %{buildroot}%{_mandir}/man1
# remove binaries from examples directory
make -C examples distclean
rm -rf %{buildroot}%{_datadir}/doc/libsndfile

%post -n %{lname} -p /sbin/ldconfig

%postun -n %{lname} -p /sbin/ldconfig

%check
pushd src
make %{?_smp_mflags} check
popd

%files -n %{lname}
%defattr(-, root, root)
%{_libdir}/libsndfile.so.1*

%files devel
%defattr(-, root, root)
%doc AUTHORS ChangeLog NEWS README
%doc doc/*.html doc/*.jpg doc/*.css doc/*.HOWTO
%license COPYING
%{_libdir}/libsndfile.so
%{_includedir}/sndfile.h
%{_includedir}/sndfile.hh
%{_libdir}/pkgconfig/*.pc
%doc examples

%changelog
