#
# spec file for package libcdio-paranoia
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


%define sonum 2
Name:           libcdio-paranoia
Version:        10.2+2.0.1
Release:        0
Summary:        CD-DA reader
License:        GPL-3.0-or-later
Group:          Productivity/Multimedia/Other
URL:            http://savannah.gnu.org/projects/libcdio
Source0:        http://ftp.gnu.org/gnu/libcdio/libcdio-paranoia-%{version}.tar.bz2
Source1:        http://ftp.gnu.org/gnu/libcdio/libcdio-paranoia-%{version}.tar.bz2.sig
Source2:        https://savannah.nongnu.org/project/memberlist-gpgkeys.php?group=libcdio&download=1#/%{name}.keyring
Source3:        baselibs.conf
Patch0:         libcdio-paranoia.libcdio_cddda-libs.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcdio)

%description
This CD-DA reader distribution ("libcdio-cdparanoia") reads audio from
CD-ROMs directly as data, with no analog step between, and writes
the data to a file or pipe as .wav, .aifc or as raw 16-bit linear PCM.

%package -n cd-paranoia
Summary:        CDDA reader
Group:          Productivity/Multimedia/Other

%description -n cd-paranoia
This CD-DA reader distribution ("libcdio-cdparanoia") reads audio from
CD-ROMs directly as data, with no analog step between, and writes
the data to a file or pipe as .wav, .aifc or as raw 16-bit linear PCM.

%package -n libcdio_cdda%{sonum}
Summary:        CD-DA reading library
Group:          System/Libraries

%description -n libcdio_cdda%{sonum}
This CD-DA reader distribution ("libcdio-cdparanoia") reads audio from
CD-ROMs directly as data, with no analog step between, and writes
the data to a file or pipe as .wav, .aifc or as raw 16-bit linear PCM.

%package -n libcdio_paranoia%{sonum}
Summary:        Error correction library for CD-DA data blocks
Group:          System/Libraries

%description -n libcdio_paranoia%{sonum}
This CD-DA reader distribution ("libcdio-cdparanoia") reads audio from
CD-ROMs directly as data, with no analog step between, and writes
the data to a file or pipe as .wav, .aifc or as raw 16-bit linear PCM.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/C and C++
Requires:       libcdio_cdda%{sonum} = %{version}-%{release}
Requires:       libcdio_paranoia%{sonum} = %{version}-%{release}
Requires:       pkgconfig(libcdio)

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup -p1

%build
%configure --disable-static
%make_build -e

%install
%make_install
find %{buildroot} -name '*.la' -delete
mv %{buildroot}%{_mandir}/jp %{buildroot}%{_mandir}/ja
# I have no idea WTF upstream is trying to do. But most software currently
# expects the headers to be in %%{_includedir}/cdio/, not in %%{_includedir}/cdio/paranoia/
ln -s paranoia/cdda.h %{buildroot}%{_includedir}/cdio/cdda.h
ln -s paranoia/paranoia.h %{buildroot}%{_includedir}/cdio/paranoia.h
ln -s paranoia/toc.h %{buildroot}%{_includedir}/cdio/toc.h
%find_lang cd-paranoia --with-man

%post -n libcdio_cdda%{sonum} -p /sbin/ldconfig

%postun -n libcdio_cdda%{sonum} -p /sbin/ldconfig

%postun -n libcdio_paranoia%{sonum} -p /sbin/ldconfig

%post -n libcdio_paranoia%{sonum} -p /sbin/ldconfig

%files -n cd-paranoia -f cd-paranoia.lang
%doc README.md NEWS.md AUTHORS
%license COPYING
%{_bindir}/cd-paranoia
%doc %{_mandir}/man1/cd-paranoia.1%{?ext_man}

%files -n libcdio_cdda%{sonum}
%{_libdir}/libcdio_cdda.so.*

%files -n libcdio_paranoia%{sonum}
%{_libdir}/libcdio_paranoia.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
