#
# spec file for package libisoburn
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


%define so_ver 1
Name:           libisoburn
Version:        1.5.0
Release:        0
Summary:        Frontend for libburn and libisofs
License:        GPL-2.0-or-later
Group:          Productivity/Multimedia/CD/Record
URL:            http://libburnia-project.org/
Source0:        http://files.libburnia-project.org/releases/%{name}-%{version}.tar.gz
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  libacl-devel
BuildRequires:  libburn-devel
BuildRequires:  libisofs-devel
BuildRequires:  pkgconfig
BuildRequires:  readline-devel
BuildRequires:  zlib-devel
%if 0%{?suse_version} > 1320 || (0%{?is_opensuse} && 0%{?sle_version} >= 120300)
BuildRequires:  libjte-devel
%endif

%description
Libisoburn is a frontend for libraries libburn and libisofs which enables
creation and expansion of ISO-9660 filesystems on all CD/DVD/BD media supported
by libburn. This includes media like DVD+RW, which do not support multi-session
management on media level and even plain disk files or block devices. Since it
specializes on data files in ISO-9660 filesystem images it is not suitable for
audio (CD-DA) or any other CD layout which does not entirely consist of
ISO-9660 sessions.

%package devel
Summary:        Development Files for libburn
Group:          Development/Libraries/C and C++
Requires:       libburn-devel
Requires:       libisoburn%{so_ver} = %{version}
Requires:       libisofs-devel
# libburnia-devel was last used in version 1.4.0
Provides:       libburnia-devel = %{version}
Obsoletes:      libburnia-devel < %{version}

%description devel
Development files for developing applications using libisoburn.

%package -n libisoburn%{so_ver}
Summary:        Frontend for libburn and libisofs
Group:          System/Libraries

%description -n libisoburn%{so_ver}
Libisoburn is a frontend for libraries libburn and libisofs which enables
creation and expansion of ISO-9660 filesystems on all CD/DVD/BD media supported
by libburn. This includes media like DVD+RW, which do not support multi-session
management on media level and even plain disk files or block devices. Since it
specializes on data files in ISO-9660 filesystem images it is not suitable for
audio (CD-DA) or any other CD layout which does not entirely consist of
ISO-9660 sessions.

%package -n xorriso
Summary:        ISO 9660 Rock Ridge Filesystem Manipulator
Group:          Productivity/Multimedia/CD/Record
Requires(post): info
Requires(preun): info
# libburnia-tools was last used in version 1.4.0
Provides:       libburnia-tools = %{version}
Obsoletes:      libburnia-tools < %{version}
# libburnia-tools-x11 was last used in version 1.4.0
Provides:       libburnia-tools-x11 = %{version}
Obsoletes:      libburnia-tools-x11 < %{version}

%description -n xorriso
xorriso is a program which maps file objects from POSIX compliant filesystems
into Rock Ridge enhanced ISO 9660 filesystems and allows session-wise
manipulation of such filesystems. It can load the management information of
existing ISO images and it writes the session results to optical media or to
filesystem objects.
Vice versa xorriso is able to restore file objects from ISO 9660 filesystems.

%package -n xorriso-tcltk
Summary:        Graphical frontend for xorriso
Group:          Productivity/Multimedia/CD/Record
Requires:       tcl
Requires:       tk
Requires:       xorriso = %{version}

%description -n xorriso-tcltk
xorriso is a program which maps file objects from POSIX compliant filesystems
into Rock Ridge enhanced ISO 9660 filesystems and allows session-wise
manipulation of such filesystems. It can load the management information of
existing ISO images and it writes the session results to optical media or to
filesystem objects.

This package provides a graphical frontend to xorriso.

%prep
%setup -q

# Remove build time references so build-compare can do its work
echo "HTML_TIMESTAMP = NO" >> doc/doxygen.conf.in

%build
%configure --disable-static
make %{?_smp_mflags}
doxygen doc/doxygen.conf

%install
%make_install

# Remove libtool config files
find %{buildroot} -type f -name "*.la" -delete -print

# Install devel docs
mkdir -p %{buildroot}%{_docdir}/%{name}-devel
cp -a doc/html/ %{buildroot}%{_docdir}/%{name}-devel/

%fdupes -s %{buildroot}%{_docdir}/%{name}-devel/

%post -n libisoburn%{so_ver} -p /sbin/ldconfig
%postun -n libisoburn%{so_ver} -p /sbin/ldconfig
%post -n xorriso
%install_info --info-dir="%{_infodir}" "%{_infodir}/xorriso.info%{ext_info}"
%install_info --info-dir="%{_infodir}" "%{_infodir}/xorrisofs.info%{ext_info}"
%install_info --info-dir="%{_infodir}" "%{_infodir}/xorrecord.info%{ext_info}"
%post -n xorriso-tcltk
%install_info --info-dir="%{_infodir}" "%{_infodir}/xorriso-tcltk.info%{?ext_info}"

%preun -n xorriso
%install_info_delete --info-dir="%{_infodir}" "%{_infodir}/xorriso.info%{ext_info}"
%install_info_delete --info-dir="%{_infodir}" "%{_infodir}/xorrisofs.info%{ext_info}"
%install_info_delete --info-dir="%{_infodir}" "%{_infodir}/xorrecord.info%{ext_info}"
%preun -n xorriso-tcltk
%install_info_delete --info-dir="%{_infodir}" "%{_infodir}/xorriso-tcltk.info%{?ext_info}"

%files devel
%license COPYING
%doc AUTHORS COPYRIGHT ChangeLog README TODO
%doc doc/partition_offset.wiki
%doc %{_docdir}/%{name}-devel/html/
%{_includedir}/libisoburn/
%{_libdir}/pkgconfig/libisoburn-1.pc
%{_libdir}/libisoburn.so

%files -n libisoburn%{so_ver}
%{_libdir}/libisoburn.so.%{so_ver}*

%files -n xorriso
%license COPYING
%doc COPYRIGHT
%doc doc/{qemu_xorriso.wiki,startup_file.txt}
%doc xorriso/README_gnu_xorriso
%{_bindir}/osirrox
%{_bindir}/xorrecord
%{_bindir}/xorriso
%{_bindir}/xorrisofs
%{_mandir}/man1/xorriso.1%{?ext_man}
%{_mandir}/man1/xorrisofs.1%{?ext_man}
%{_mandir}/man1/xorrecord.1%{?ext_man}
%{_infodir}/xorriso.info%{?ext_info}
%{_infodir}/xorrisofs.info%{?ext_info}
%{_infodir}/xorrecord.info%{?ext_info}

%files -n xorriso-tcltk
%doc frontend/README-tcltk
%{_bindir}/xorriso-tcltk
%{_mandir}/man1/xorriso-tcltk.1%{?ext_man}
%{_infodir}/xorriso-tcltk.info%{?ext_info}

%changelog
