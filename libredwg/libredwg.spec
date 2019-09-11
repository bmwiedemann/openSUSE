#
# spec file for package libredwg
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


Name:           libredwg
Version:        0.8
Release:        0
Summary:        A library to handle DWG files
License:        GPL-3.0-or-later
Group:          Development/Libraries/C and C++
URL:            https://www.gnu.org/software/libredwg/
Source:         https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.xz
Source2:        https://ftp.gnu.org/pub/gnu/%{name}/%{name}-%{version}.tar.xz.sig
Source3:        http://savannah.gnu.org/people/viewgpg.php?user_id=101103#/%{name}.keyring
Source4:        %{name}-rpmlintrc
BuildRequires:  pkgconfig

%description
GNU LibreDWG is a C library to handle DWG files. It can replace the
OpenDWG libraries. DWG is the native file format of AutoCAD.

%package tools
Summary:        Command line utilities for handling DWG file
Group:          Productivity/File utilities
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}
# Both packages ship a /usr/bin/dwg2dxf
Conflicts:      libdxfrw-tools

%description tools
GNU LibreDWG is a C library to handle DWG files. It can replace the
OpenDWG libraries. DWG is the native file format of AutoCAD.

This package contains some command line utilities using this library.

%package devel
Summary:        Development files for libredwg
Group:          Development/Libraries/C and C++
Requires:       %{name}0 = %{version}

%description devel
GNU LibreDWG is a C library to handle DWG files. It can replace the
OpenDWG libraries. DWG is the native file format of AutoCAD.

This package contains the files required for development with libredwg.

%package -n %{name}0
Summary:        A library to handle DWG files
Group:          System/Libraries

%description -n %{name}0
GNU LibreDWG is a C library to handle DWG files. It can replace the
OpenDWG libraries. DWG is the native file format of AutoCAD.

%prep
%setup -q

%build
%configure \
	--disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post tools
%install_info --info-dir=%{_infodir} %{_infodir}/LibreDWG.info.gz

%preun tools
%install_info_delete --info-dir=%{_infodir} %{_infodir}/LibreDWG.info.gz

%post -n %{name}0 -p /sbin/ldconfig
%postun -n %{name}0 -p /sbin/ldconfig

%files tools
%license COPYING
%{_bindir}/dwg*
%{_mandir}/man?/*.1%{?ext_man}
%{_infodir}/LibreDWG.info%{?ext_info}

%files devel
%license COPYING
%doc AUTHORS ChangeLog README README-alpha TODO
%{_includedir}/*.h
%{_libdir}/libredwg.so
%{_libdir}/pkgconfig/libredwg.pc

%files -n %{name}0
%license COPYING
%{_libdir}/*.so.*

%changelog
