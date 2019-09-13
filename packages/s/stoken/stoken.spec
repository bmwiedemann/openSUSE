#
# spec file for package stoken
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


%define         soname libstoken1
Name:           stoken
Version:        0.92
Release:        0
Summary:        Token code generator compatible with RSA SecurID 128-bit (AES) token
License:        LGPL-2.0-or-later AND BSD-3-Clause
Group:          Productivity/Security
Url:            http://stoken.sf.net
Source0:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz
Source1:        http://downloads.sourceforge.net/%{name}/%{name}-%{version}.tar.gz.asc
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  libtomcrypt-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(nettle)

%description
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

This package contains the command line tool for %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{soname} = %{version}-%{release}

%description devel
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

This package provides the development files for %{name}.

%package -n %{soname}
Summary:        Libraries for %{name}
Group:          System/Libraries

%description -n %{soname}
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

This package contains %{name} libraries.

%package gui
Summary:        Graphical interface program for %{name}
Group:          Productivity/Security
Requires:       %{soname} = %{version}-%{release}

%description gui
Software Token for Linux/UNIX. It's a token code generator compatible with RSA
SecurID 128-bit (AES) tokens. It is a hobbyist project, not affiliated with or
endorsed by RSA Security.

This package contains the graphical interface program for %{name}.

%prep
%setup -q

%build
autoreconf -fvi
%configure \
    --with-gtk \
    --disable-static
make %{?_smp_mflags}

%install
%make_install
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}-gui.desktop

# Remove stuff we don't need
find %{buildroot} -type f -name "*.la" -delete -print
rm -fr %{buildroot}%{_datarootdir}/doc/%{name}

%post -n %{soname} -p /sbin/ldconfig
%postun -n %{soname} -p /sbin/ldconfig

%files -n %{soname}
%license COPYING.LIB
%doc CHANGES README.md TODO
%{_libdir}/*.so.*

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%files gui
%dir %{_datadir}/%{name}
%{_bindir}/%{name}-gui
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/applications/%{name}-gui-small.desktop
%{_datadir}/%{name}/*.ui
%{_datadir}/pixmaps/%{name}-gui.png
%{_mandir}/man1/%{name}-gui.1%{?ext_man}

%files devel
%{_includedir}/%{name}.h
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
