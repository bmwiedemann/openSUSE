#
# spec file for package libsidplayfp
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


%define soname 4
%define stilview_soname 0

Name:           libsidplayfp
Version:        1.8.7
Release:        0
Summary:        A library to play Commodore 64 music
License:        GPL-2.0+
Group:          System/Libraries
Url:            http://sourceforge.net/projects/sidplay-residfp/
Source0:        http://downloads.sourceforge.net/project/sidplay-residfp/libsidplayfp/1.8/libsidplayfp-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  pkg-config

%description
A library to play Commodore 64 music based on libsidplay2.

%package -n libsidplayfp%{soname}
Summary:        A library to play Commodore 64 music
Group:          System/Libraries

%description -n libsidplayfp%{soname}
A library to play Commodore 64 music based on libsidplay2.

%package devel
Summary:        Development files for libsidplayfp
Group:          Development/Libraries/C and C++
Requires:       libsidplayfp%{soname} = %{version}

%description devel
This package contains headers and libraries required to build applications that
use libsidplayfp.

%package -n libstilview%{stilview_soname}
Summary:        A library to play Commodore 64 music
Group:          System/Libraries

%description -n libstilview%{stilview_soname}
A library to play Commodore 64 music based on libsidplay2.

%package -n libstilview-devel
Summary:        Development files for libstilview
Group:          Development/Libraries/C and C++
Requires:       libstilview%{stilview_soname} = %{version}

%description -n libstilview-devel
This package contains headers and libraries required to build applications that
use libstilview.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}
# fool the following "make install", we have no xa(1)
touch sidplayfp/psiddrv.o65
touch sidplayfp/psiddrv.bin

%install
%make_install
rm %{buildroot}%{_libdir}/*.la

%post -n libsidplayfp%{soname} -p /sbin/ldconfig

%postun -n libsidplayfp%{soname} -p /sbin/ldconfig

%post -n libstilview%{stilview_soname} -p /sbin/ldconfig

%postun -n libstilview%{stilview_soname} -p /sbin/ldconfig

%files -n libsidplayfp%{soname}
%defattr(0644, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO
%{_libdir}/libsidplayfp.so.%{soname}*

%files -n libstilview%{stilview_soname}
%defattr(0644, root, root, 0755)
%doc AUTHORS COPYING NEWS README TODO
%{_libdir}/libstilview.so.%{stilview_soname}*

%files devel
%defattr(0644, root, root, 0755)
%{_libdir}/libsidplayfp.so
%{_includedir}/sidplayfp/
%{_libdir}/pkgconfig/libsidplayfp.pc

%files -n libstilview-devel
%defattr(0644, root, root, 0755)
%{_libdir}/libstilview.so
%{_includedir}/stilview/
%{_libdir}/pkgconfig/libstilview.pc

%changelog
