#
# spec file for package libXcm
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libXcm
Version:        0.5.4
Release:        0
Summary:        X Color Management Library
License:        MIT
Group:          Productivity/Graphics/Other
Url:            http://www.oyranos.org
#Git-Clone:	git://github.com/oyranos-cms/libxcm
Source:         %{name}-%version.tar.gz
Source1:        libxcm_0.5.4.orig.tar.bz2
Source2:        libxcm_0.5.4-1.debian.tar.gz
Source3:        libxcm.dsc
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} != 0 && 0%{?suse_version} < 1130
BuildRequires:  Mesa-devel
BuildRequires:  xorg-x11-devel
%else
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xfixes)
BuildRequires:  pkgconfig(xmu)
%endif

%package -n %{name}0
Summary:        X Color Management Library
Group:          System/Libraries

%package -n %{name}EDID0
Summary:        EDID Color Management Parsing
Group:          System/Libraries

%package -n %{name}DDC0
Summary:        EDID over DDC Detection
Group:          System/Libraries

%package -n %{name}X11-0
Summary:        X Color Management Implementation
Group:          System/Libraries

%package devel
Summary:        Headers, Configuration and static Libs + Documentation
Group:          Development/Libraries/C and C++
Requires:       %{name}0 = %{version}
Requires:       %{name}DDC0 = %{version}
Requires:       %{name}EDID0 = %{version}
Requires:       %{name}X11-0 = %{version}

%description
The libXcm library is a color management helper for Xorg. It contains a
reference implementation of the X Color Management specification.
It allows to attach color regions to X windows to communicate with colour
servers. A EDID parser and a observer tool are included.

%description -n %{name}0
The libXcm library is a reference implementation of the X Color Management specification.
It allows to attach color regions to X windows to communicate with color
servers. A EDID parser and a color management event observer are included.

%description -n %{name}EDID0
EDID parser implementing the key/value pairs needed for the ICC meta Tag for Monitor Profiles spec.
http://www.freedesktop.org/wiki/Specifications/icc_meta_tag_for_monitor_profiles

%description -n %{name}DDC0
Provide EDID detection through display data channel (DDC) communication.

%description -n %{name}X11-0
The libXcmX11 library is a reference implementation of the X Color Management specification.
It allows to attach color regions to X windows to communicate with color
+servers.

%description devel
The libXcm library is a reference implementation of the X Color Management specification.
It allows to attach color regions to X windows to communicate with color
servers. A EDID parser and a color management event observer are included.
The package contains headers and other development files.

%prep
%setup -q

%build
%ifarch %{arm}
export CFLAGS="%{optflags} -fPIC"
export CXXFLAGS="%{optflags} -fPIC"
%endif
%configure --disable-static
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

#Remove installed doc
rm -fr %{buildroot}/%{_datadir}/doc/%{name}

#Fix timestamp to prevent multilibs conflict
touch -r docs/ChangeLog.md doc/man/*

# Remove libtool files
find %{buildroot} -type f -name "*.la" -delete -print

%post -n %{name}0 -p /sbin/ldconfig

%post -n %{name}EDID0 -p /sbin/ldconfig

%post -n %{name}DDC0 -p /sbin/ldconfig

%post -n %{name}X11-0 -p /sbin/ldconfig

%postun -n %{name}0 -p /sbin/ldconfig

%postun -n %{name}EDID0 -p /sbin/ldconfig

%postun -n %{name}DDC0 -p /sbin/ldconfig

%postun -n %{name}X11-0 -p /sbin/ldconfig

%files -n %{name}0
%defattr(-, root, root)
%{_libdir}/%{name}.so.*

%files -n %{name}EDID0
%defattr(-, root, root)
%{_libdir}/%{name}EDID.so.*

%files -n %{name}DDC0
%defattr(-, root, root)
%{_libdir}/%{name}DDC.so.*

%files -n %{name}X11-0
%defattr(-, root, root)
%{_libdir}/%{name}X11.so.*

%files devel
%defattr(-, root, root)
%doc docs/AUTHORS.md docs/COPYING.md docs/ChangeLog.md README.md
%doc docs/X_Color_Management.md
%{_libdir}/%{name}*.so
%{_libdir}/cmake/
%{_includedir}/X11/Xcm/
%{_libdir}/pkgconfig/xcm*.pc
%{_mandir}/man3/*.3*

%changelog
