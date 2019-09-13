#
# spec file for package rawstudio
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


%define sover 2_1
Name:           rawstudio
Version:        2.0+git20170413.003dd4f3
Release:        0
Summary:        Converter for RAW image files
License:        GPL-2.0-only
Group:          Productivity/Graphics/Other
URL:            http://rawstudio.org/
Source0:        %{name}-%{version}.tar.xz
# PATCH-FIX-UPSTREAM
Patch0:         exiv2-0.27-buildfix.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRequires:  git
BuildRequires:  intltool
BuildRequires:  libjpeg-devel
BuildRequires:  libtiff-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(fftw3f)
BuildRequires:  pkgconfig(flickcurl)
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(lensfun)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgphoto2)
BuildRequires:  pkgconfig(libssl)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
Requires(post): update-desktop-files
Requires(postun): update-desktop-files

%description
RawStudio is a digital camera RAW files processing software.

%package -n 	lib%{name}-%{sover}
Summary:        RawStudio library
Group:          System/Libraries

%description -n lib%{name}-%{sover}
This package contain the library needed to run a programs compiled
using lib%{name}.

%package -n 	lib%{name}-devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       lib%{name}-%{sover} = %{version}

%description -n lib%{name}-devel
This package contains, header files, and libraries needed to develop
application that use lib%{name}.

%lang_package

%prep
%setup -q
%patch0 -p1

%build
./autogen.sh --no-configure
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
install -Dm0644 {pixmaps/,%{buildroot}%{_datadir}/pixmaps/}%{name}.png
find %{buildroot}{%{_libdir},%{_datadir}/icons} \
-maxdepth 1 -type f \( -name \*.la -o -name \*.png \) -delete -print
%find_lang %{name}

%post
%desktop_database_post

%postun
%desktop_database_postun

%post -n lib%{name}-%{sover} -p /sbin/ldconfig
%postun -n lib%{name}-%{sover} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS NEWS README.md
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%dir %{_datadir}/appdata
%{_datadir}/appdata/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}/
%{_datadir}/pixmaps/%{name}.png
%{_libdir}/%{name}/
%{_datadir}/%{name}/
%{_datadir}/rawspeed/

%files -n lib%{name}-%{sover}
%{_libdir}/lib%{name}-*.so

%files -n lib%{name}-devel
%{_includedir}/%{name}*/
%{_libdir}/pkgconfig/%{name}*.pc
%{_libdir}/lib%{name}.so

%files lang -f %{name}.lang

%changelog
