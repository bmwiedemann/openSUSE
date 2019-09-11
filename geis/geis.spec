#
# spec file for package geis
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


%define soname  libgeis
%define sover   1
Name:           geis
Version:        2.2.17
Release:        0
Summary:        Gesture engine interface and support
License:        LGPL-3.0 and GPL-3.0
Group:          System/GUI/Other
Url:            https://launchpad.net/geis
Source:         https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.xz
Source1:        https://launchpad.net/%{name}/trunk/%{version}/+download/%{name}-%{version}.tar.xz.asc
Source2:        %{name}.keyring
Source3:        baselibs.conf
# PATCH-FIX-OPENSUSE geis-disable-werror.patch boo#985131 sor.alexei@meowr.ru -- Disable -Werror.
Patch0:         %{name}-disable-werror.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  fdupes
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(dbus-1) >= 1.2.16
BuildRequires:  pkgconfig(frame) >= 2.2
BuildRequires:  pkgconfig(grail) >= 3.0.8
BuildRequires:  pkgconfig(python3) >= 3.2
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcb) >= 1.6
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xi) >= 1.3
BuildRequires:  pkgconfig(xorg-server)

%description
GEIS is a library for applications and toolkit programmers which
provides a consistent platform independent interface for any
system-wide input gesture recognition mechanism.

%package -n %{soname}%{sover}
Summary:        Gesture engine interface and support
Group:          System/Libraries

%description -n %{soname}%{sover}
GEIS is a library for applications and toolkit programmers which
provides a consistent platform independent interface for any
system-wide input gesture recognition mechanism.

%package tools
Summary:        Gesture engine interface and support
Group:          System/GUI/Other
Requires:       python3-geis = %{version}

%description tools
GEIS is a library for applications and toolkit programmers which
provides a consistent platform independent interface for any
system-wide input gesture recognition mechanism.

%package -n python3-geis
Summary:        Python3 bindings for GEIS
Group:          Development/Languages/Python

%description -n python3-geis
This package provides the python3 bindings for GEIS.

%package devel
Summary:        Development files for the GEIS interface implementation
Group:          Development/Libraries/C and C++
Requires:       %{soname}%{sover} = %{version}

%description devel
GEIS is a library for applications and toolkit programmers which
provides a consistent platform independent interface for any
system-wide input gesture recognition mechanism.

%prep
%setup -q
%patch0 -p1

%build
autoreconf -fi
%configure \
  --disable-static                   \
  --disable-silent-rules             \
  --docdir=%{_docdir}/%{name}-devel/
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%suse_update_desktop_file -G "Geis Viewer" geisview Utility DesktopSettings
chmod a+x %{buildroot}%{python3_sitelib}/geisview/__init__.py
%fdupes %{buildroot}%{python3_sitelib}

%post -n %{soname}%{sover} -p /sbin/ldconfig

%postun -n %{soname}%{sover} -p /sbin/ldconfig

%files tools
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.GPL README
%{_bindir}/geistest
%{_bindir}/geisview
%{_bindir}/pygeis
%{_datadir}/geisview/
%{_datadir}/applications/geisview.desktop
%{_datadir}/pixmaps/geisview*.xpm
%{_mandir}/man1/*geis*.1%{?ext_man}

%files -n %{soname}%{sover}
%defattr(-,root,root)
%doc AUTHORS COPYING COPYING.GPL README
%{_libdir}/libgeis.so.%{sover}*

%files -n python3-geis
%defattr(-,root,root)
%{python3_sitelib}/geis*/
%{python3_sitearch}/*.so

%files devel
%defattr(-,root,root)
%doc %{_docdir}/%{name}-devel/
%{_includedir}/geis/
%{_libdir}/libgeis.so
%{_libdir}/pkgconfig/libgeis.pc

%changelog
