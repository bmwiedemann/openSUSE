#
# spec file for package jigit
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


%define so_ver 2
Name:           jigit
Version:        1.22
Release:        0
Summary:        Tools for Working With jigdo Files
License:        GPL-2.0-only
Group:          Productivity/File utilities
URL:            https://www.einval.com/~steve/software/JTE/
Source0:        http://www.einval.com/~steve/software/JTE/download/%{name}-%{version}.tar.xz
BuildRequires:  libbz2-devel
BuildRequires:  zlib-devel

%description
Jigit is an interactive wrapper around mkimage to ease the download or upgrade
of existing CDs and CD images.

%package -n libjte%{so_ver}
Summary:        Jigdo Template Export Library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libjte%{so_ver}
libjte is a library providing support for creating jigdo files, to be used by
ISO image creation tools.

%package -n libjte-devel
Summary:        Development Files for libjte
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
Requires:       libjte%{so_ver} = %{version}

%description -n libjte-devel
This package includes development files for libjte.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
%make_build all
cd libjte
%configure \
 --disable-static
%make_build
cd ..

%install
install -dm 0755 %{buildroot}%{_bindir}
install -pm 0755 jigit-mkimage jigsum jigsum-sha256 jigdump %{buildroot}%{_bindir}
install -pm 0755 extract-data %{buildroot}%{_bindir}/jigit-extract-data
install -pm 0755 rsyncsum %{buildroot}%{_bindir}/jigit-rsyncsum
install -pm 0755 parallel-sums %{buildroot}%{_bindir}/jigit-parallel-sums
install -pm 0755 jigit mkjigsnap %{buildroot}%{_bindir}
install -dm 0755 %{buildroot}%{_mandir}/man1
install -pm 0644 jigdump.1 jigit-mkimage.1 jigit.1 jigsum.1 jigsum-sha256.1 parallel-sums.1 %{buildroot}%{_mandir}/man1/
install -dm 0755 %{buildroot}%{_mandir}/man8
install -pm 0644 mkjigsnap.8 %{buildroot}%{_mandir}/man8/
cd libjte
%make_install
install -pm 0755 bin/jigdo-gen-checksum-list %{buildroot}%{_bindir}
#install -pm 0644 doc/jigdo-gen-checksum-list.1 %%{buildroot}%%{_mandir}/man1/
cd ..

# Remove libtool config files
find %{buildroot} -type f -name "*.la" -delete -print

# Remove static libraries
find %{buildroot} -type f -name "*.a" -delete -print

%post -n libjte%{so_ver} -p /sbin/ldconfig
%postun -n libjte%{so_ver} -p /sbin/ldconfig

%files
%license COPYING
%doc ChangeLog README iso-image.pl
%{_bindir}/jigit-mkimage
%{_bindir}/jigsum
%{_bindir}/jigsum-sha256
%{_bindir}/jigdump
%{_bindir}/jigit-extract-data
%{_bindir}/jigit-rsyncsum
%{_bindir}/jigit-parallel-sums
%{_bindir}/jigit
%{_bindir}/mkjigsnap
%{_bindir}/jigdo-gen-checksum-list
%{_mandir}/man1/*.1%{?ext_man}
%{_mandir}/man8/*.8%{?ext_man}

%files -n libjte%{so_ver}
%{_libdir}/libjte.so.%{so_ver}*

%files -n libjte-devel
%license libjte/{COPYING,COPYRIGHT}
%doc libjte/ChangeLog
%doc libjte/doc/{API,NOTES,TODO}
%{_includedir}/libjte/
%{_libdir}/pkgconfig/*
%{_libdir}/libjte.so

%changelog
