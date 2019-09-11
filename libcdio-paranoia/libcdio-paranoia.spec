#
# spec file for package libcdio-paranoia
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


%define sonum 2

Name:           libcdio-paranoia
Version:        10.2+2.0.0
Release:        0
Summary:        CDDA reader
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Other
Url:            http://savannah.gnu.org/projects/libcdio
Source0:        http://ftp.gnu.org/gnu/libcdio/libcdio-paranoia-%{version}.tar.bz2
Source1:        http://ftp.gnu.org/gnu/libcdio/libcdio-paranoia-%{version}.tar.bz2.sig
Source2:        https://savannah.nongnu.org/project/memberlist-gpgkeys.php?group=libcdio&download=1#/%{name}.keyring
Source3:        baselibs.conf
Patch1:         libcdio-paranoia.libcdio_cddda-libs.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libcdio)

%description
This CDDA reader distribution ('libcdio-cdparanoia') reads audio from
he CDROM directly as data, with no analog step between, and writes
the data to a file or pipe as .wav, .aifc or as raw 16 bit linear PCM.

%package -n cd-paranoia
Summary:        CDDA reader
Group:          Productivity/Multimedia/Other

%description -n cd-paranoia
This CDDA reader distribution ('libcdio-cdparanoia') reads audio from
he CDROM directly as data, with no analog step between, and writes
the data to a file or pipe as .wav, .aifc or as raw 16 bit linear PCM.

%package -n libcdio_cdda%{sonum}
Summary:        CDDA reader
Group:          System/Libraries

%description -n libcdio_cdda%{sonum}
This CDDA reader distribution ('libcdio-cdparanoia') reads audio from
he CDROM directly as data, with no analog step between, and writes
the data to a file or pipe as .wav, .aifc or as raw 16 bit linear PCM.

%package -n libcdio_paranoia%{sonum}
Summary:        CDDA reader
Group:          System/Libraries

%description -n libcdio_paranoia%{sonum}
This CDDA reader distribution ('libcdio-cdparanoia') reads audio from
he CDROM directly as data, with no analog step between, and writes
the data to a file or pipe as .wav, .aifc or as raw 16 bit linear PCM.

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
%setup -q
%patch1 -p1
%define buildir ${PWD}

%build
%configure --disable-static --with-pic
make -e %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
find %{buildroot} -name '*.la' -exec rm -f {} ';'
mv %{buildroot}%{_mandir}/jp %{buildroot}%{_mandir}/ja
# I have no idea WTF upstream is trying to do. But most software currently
# expects the headers to be in %%{_includedir}/cdio/, not in %%{_includedir}/cdio/paranoia/
ln -s paranoia/cdda.h %{buildroot}%{_includedir}/cdio/cdda.h
ln -s paranoia/paranoia.h %{buildroot}%{_includedir}/cdio/paranoia.h

%post -n libcdio_cdda%{sonum} -p /sbin/ldconfig

%postun -n libcdio_cdda%{sonum} -p /sbin/ldconfig

%postun -n libcdio_paranoia%{sonum} -p /sbin/ldconfig

%post -n libcdio_paranoia%{sonum} -p /sbin/ldconfig

%files -n cd-paranoia
%defattr (-, root, root)
%doc README* NEWS NEWS AUTHORS
%license COPYING
%{_bindir}/cd-paranoia
%doc %{_mandir}/ja/man1/cd-paranoia.1.gz
%doc %{_mandir}/man1/cd-paranoia.1.gz

%files -n libcdio_cdda%{sonum}
%defattr (-, root, root)
%{_libdir}/libcdio_cdda.so.*

%files -n libcdio_paranoia%{sonum}
%defattr (-, root, root)
%{_libdir}/libcdio_paranoia.so.*

%files devel
%defattr (-, root, root)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
