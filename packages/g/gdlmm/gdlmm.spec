#
# spec file for package gdlmm
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


Name:           gdlmm
Version:        3.7.3
Release:        0
Summary:        C++ interface for gdl
License:        LGPL-2.1-or-later
Group:          Development/Libraries/GNOME
Url:            http://git.gnome.org/gdlmm/
Source0:        http://download.gnome.org/sources/gdlmm/3.7/%{name}-%{version}.tar.xz
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  perl(XML::Parser)
BuildRequires:  pkgconfig(gdl-3.0) >= 3.7
BuildRequires:  pkgconfig(glibmm-2.4) >= 2.16
BuildRequires:  pkgconfig(gtkmm-3.0) >= 3.0

%description
gdlmm provides a C++ interface to the gdl library.

%package -n libgdlmm-3_0-2
Summary:        C++ interface for gdl
Group:          System/Libraries

%description -n libgdlmm-3_0-2
gdlmm provides a C++ interface to the gdl library.

%package devel
Summary:        Development files for the C++ interface of gdl
Group:          Development/Libraries/C and C++
Requires:       libgdlmm-3_0-2 = %{version}

%description devel
gdlmm provides a C++ interface to the gdl library.

%prep
%setup -q

%build
%configure \
        --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libgdlmm-3_0-2 -p /sbin/ldconfig
%postun -n libgdlmm-3_0-2 -p /sbin/ldconfig

%files -n libgdlmm-3_0-2
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/libgdlmm-3.0.so.*

%files devel
%{_includedir}/gdlmm-3.0/
%{_libdir}/gdlmm-3.0/
%{_libdir}/libgdlmm-3.0.so
%{_libdir}/pkgconfig/gdlmm-3.0.pc
%doc %{_datadir}/devhelp/books/gdlmm-3.0/
%doc %{_datadir}/doc/gdlmm-3.0/
# Avoid BuildRequires on devhelp
%dir %{_datadir}/devhelp
%dir %{_datadir}/devhelp/books

%changelog
