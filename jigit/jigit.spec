#
# spec file for package jigit
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


%define so_ver 1

Name:           jigit
Version:        1.20
Release:        0
Summary:        Tools for Working With jigdo Files
License:        GPL-2.0
Group:          Productivity/File utilities
Url:            http://www.einval.com/~steve/software/JTE/
Source0:        http://www.einval.com/~steve/software/JTE/download/%{name}_%{version}.orig.tar.gz
BuildRequires:  libbz2-devel
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Jigit is an interactive wrapper around mkimage to ease the download or upgrade
of existing CDs and CD images.

%package -n libjte%{so_ver}
Summary:        Jigdo Template Export Library
License:        LGPL-2.1+
Group:          System/Libraries

%description -n libjte%{so_ver}
libjte is a library providing support for creating jigdo files, to be used by
ISO image creation tools.

%package -n libjte-devel
Summary:        Development Files for libjte
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Requires:       libjte%{so_ver} = %{version}

%description -n libjte-devel
This package includes development files for libjte.

%prep
%setup -q

%build
export CFLAGS="%{optflags}"
make %{?_smp_mflags} jigit-mkimage extract-data jigsum rsyncsum jigdump
cd libjte
%configure \
 --disable-static
make %{?_smp_mflags}
cd ..

%install
install -dm 0755 %{buildroot}%{_bindir}
install -pm 0755 jigit-mkimage jigsum jigdump %{buildroot}%{_bindir}
install -pm 0755 extract-data %{buildroot}%{_bindir}/jigit-extract-data
install -pm 0755 rsyncsum %{buildroot}%{_bindir}/jigit-rsyncsum
install -pm 0755 jigit mkjigsnap %{buildroot}%{_bindir}
install -dm 0755 %{buildroot}%{_mandir}/man1
install -pm 0644 jigdump.1 jigit-mkimage.1 jigit.1 jigsum.1 %{buildroot}%{_mandir}/man1/
install -dm 0755 %{buildroot}%{_mandir}/man8
install -pm 0644 mkjigsnap.8 %{buildroot}%{_mandir}/man8/
cd libjte
%make_install
install -pm 0755 bin/jigdo-gen-md5-list %{buildroot}%{_bindir}
install -pm 0644 doc/jigdo-gen-md5-list.1 %{buildroot}%{_mandir}/man1/
cd ..

# Remove libtool config files
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libjte%{so_ver} -p /sbin/ldconfig

%postun -n libjte%{so_ver} -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog README iso-image.pl
%{_bindir}/jigit-mkimage
%{_bindir}/jigsum
%{_bindir}/jigdump
%{_bindir}/jigit-extract-data
%{_bindir}/jigit-rsyncsum
%{_bindir}/jigit
%{_bindir}/mkjigsnap
%{_bindir}/jigdo-gen-md5-list
%{_mandir}/man1/*.1%{ext_man}
%{_mandir}/man8/*.8%{ext_man}

%files -n libjte%{so_ver}
%defattr(-,root,root,-)
%{_libdir}/libjte.so.%{so_ver}*

%files -n libjte-devel
%defattr(-,root,root,-)
%doc libjte/{COPYING,COPYRIGHT,ChangeLog}
%doc libjte/doc/{API,NOTES,TODO}
%{_includedir}/libjte/
%{_libdir}/pkgconfig/*
%{_libdir}/libjte.so

%changelog
