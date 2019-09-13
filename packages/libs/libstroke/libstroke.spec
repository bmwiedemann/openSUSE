#
# spec file for package libstroke
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libstroke
BuildRequires:  libtool
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(x11)
Version:        0.5.1
Release:        0
Url:            http://www.etla.net/libstroke/
Source0:        http://www.etla.net/libstroke/libstroke-%{version}.tar.bz2
Patch:          libstroke-0.4.dif
Patch1:         no-gtk1.patch
Patch2:         fix-implicit-declarations.patch
# PATCH-FIX-UPSTREAM Fix quoting of AC_DEFUN args (bnc#794807) (2013-01-07)
Patch3:         libstroke-quote_m4_definitions.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Summary:        A Stroke Translation Library
License:        GPL-2.0+
Group:          System/Libraries

%description
LibStroke is a stroke interface library.  Strokes are motions of the
mouse that can be interpreted by a program as a command.  Strokes are
used extensively in CAD programs.

%package     -n libstroke-devel
Summary:        Development package for libstroke
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       pkgconfig(x11)

%description  -n libstroke-devel
This package is needed if you want to program or compile applications
that use libstroke.

%prep
%setup0 -q
%patch
%patch1 -p1
%patch2 -p1
%patch3

%build
rm -f config.cache
# update config.{guess,sub}
autoreconf --force --install
%configure --disable-static --with-pic
%{__make} %{?jobs:-j%jobs}

%install
%make_install
rm -f %{buildroot}%{_libdir}/*.la

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc AUTHORS COPY* CREDITS ChangeLog INSTALL NEWS README* TODO
%{_libdir}/libstroke.so.*

%files -n libstroke-devel
%defattr(-, root, root)
%{_libdir}/libstroke.so
/usr/include/*.h
/usr/share/aclocal/*.m4

%changelog
