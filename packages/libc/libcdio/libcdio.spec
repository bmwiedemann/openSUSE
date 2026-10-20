#
# spec file for package libcdio
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%define cdio_name libcdio21
%define cdiopp_name libcdio++2
%define iso9660_name libiso9660-13
%define iso9660pp_name libiso9660++1
%define udf_name libudf0
Name:           libcdio
Version:        2.4.0
Release:        0
Summary:        CD-ROM Access Library
License:        GPL-3.0-or-later
URL:            https://savannah.gnu.org/projects/libcdio
Source0:        https://github.com/libcdio/libcdio/releases/download/%{version}/libcdio-%{version}.tar.bz2
Source3:        baselibs.conf
Patch1:         c99.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  help2man
BuildRequires:  libtool
BuildRequires:  makeinfo
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(form)
BuildRequires:  pkgconfig(formw)
BuildRequires:  pkgconfig(libcddb) >= 1.0.1
BuildRequires:  pkgconfig(menu)
BuildRequires:  pkgconfig(menuw)
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(ncurses++)
BuildRequires:  pkgconfig(ncurses++w)
BuildRequires:  pkgconfig(ncursesw)
BuildRequires:  pkgconfig(panel)
BuildRequires:  pkgconfig(panelw)
BuildRequires:  pkgconfig(popt)
BuildRequires:  pkgconfig(tic)
BuildRequires:  pkgconfig(ticw)
BuildRequires:  pkgconfig(tinfo)
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
The libcdio package contains libraries for CD-ROM and CD image
access. Applications can use them as an abstraction to OS- and
device-dependent properties of a CD-ROM or of the specific details of
various CD image formats.

%package -n %{cdio_name}
Summary:        CD-ROM Access Library

%description -n %{cdio_name}
The libcdio package contains libraries for CD-ROM and CD image
access. Applications can use them as an abstraction to OS- and
device-dependent properties of a CD-ROM or of the specific details of
various CD image formats.

This subpackage contains the C API library from cdio.

%package -n %{cdiopp_name}
Summary:        C++ API for the libcdio CD-ROM access library

%description -n %{cdiopp_name}
The libcdio package contains libraries for CD-ROM and CD image
access.

This subpackage contains the C++ API library for cdio.

%package -n %{iso9660_name}
Summary:        Library for working with ISO 9660 filesystems

%description -n %{iso9660_name}
A library for working with ISO 9660 filesystems, which are mainly used on CDs.

%package -n %{iso9660pp_name}
Summary:        Library for working with ISO 9660 filesystems

%description -n %{iso9660pp_name}
A library for working with ISO 9660 filesystems, which are mainly used on CDs.
This subpackage contains the C++ API library for cdio.

%package -n %{udf_name}
Summary:        Library for working with Universal Disk Format filesystems

%description -n %{udf_name}
This library is made to read and write UDF filesystems, which are mainly
used on DVDs.

%package devel
Summary:        CD-ROM access library
Requires:       %{cdio_name} = %{version}
Requires:       %{cdiopp_name} = %{version}
Requires:       %{iso9660_name} = %{version}
Requires:       %{iso9660pp_name} = %{version}
Requires:       %{udf_name} = %{version}
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description devel
The libcdio package contains libraries for CD-ROM and CD image
access. Applications can use them as an abstraction to OS- and
device-dependent properties of a CD-ROM or of the specific details of
various CD image formats.

This subpackage contains libraries and header files for developing
applications that want to make use of the cdio libraries.

%prep
%autosetup -p1

%build
%configure \
	--disable-silent-rules \
	--disable-rpath \
	--disable-static \
	--enable-rock \
	--without-cd-drive \
	--without-cd-info \
	--without-cdda-player \
	--without-cd-read
%make_build

%install
%make_install
#empty depdendency libs
rm -rf %{buildroot}%{_bindir} %{buildroot}%{_mandir}
find %{buildroot} -type f -name "*.la" -delete -print

%check
%make_build check

%post -n %{cdio_name} -p /sbin/ldconfig
%post -n %{cdiopp_name} -p /sbin/ldconfig
%post -n %{iso9660_name} -p /sbin/ldconfig
%post -n %{iso9660pp_name} -p /sbin/ldconfig
%post -n %{udf_name} -p /sbin/ldconfig
%postun -n %{cdio_name} -p /sbin/ldconfig
%postun -n %{cdiopp_name} -p /sbin/ldconfig
%postun -n %{iso9660_name} -p /sbin/ldconfig
%postun -n %{iso9660pp_name} -p /sbin/ldconfig
%postun -n %{udf_name} -p /sbin/ldconfig

%post devel
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{?ext_info}

%preun devel
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{?ext_info}

%files -n %{cdio_name}
%{_libdir}/libcdio.so.*

%files -n %{cdiopp_name}
%{_libdir}/libcdio++.so.*

%files -n %{iso9660pp_name}
%{_libdir}/libiso9660++.so.*

%files -n %{iso9660_name}
%{_libdir}/libiso9660.so.*

%files -n %{udf_name}
%{_libdir}/libudf.so.*

%files devel
%{_infodir}/*.info%{?ext_info}
%{_includedir}/cdio
%{_includedir}/cdio++
%{_libdir}/libcdio*.so
%{_libdir}/libiso9660*.so
%{_libdir}/libudf*.so
%{_libdir}/pkgconfig/*.pc

%changelog
