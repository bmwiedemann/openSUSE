#
# spec file for package libart_lgpl
#
# Copyright (c) 2022 SUSE LLC
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


Name:           libart_lgpl
Version:        2.3.21
Release:        0
# NOTE: on upgrade to a new upstream version, change the Obsoletes from <= to <
Summary:        Libart Components Licensed under the LGPL
License:        LGPL-2.1-or-later
Group:          System/GUI/GNOME
Source:         https://download.gnome.org/sources/%{name}/2.3/%{name}-%{version}.tar.bz2
BuildRequires:  pkgconfig

%description
Libart is a library for high-performance 2D graphics. It is currently
being used as the antialiased rendering engine for GNOME Canvas. It is
also the rendering engine for Gill, the GNOME Illustration application.

%package -n libart_lgpl_2-2
Summary:        Libart Components Licensed under the LGPL
Group:          System/Libraries
Provides:       %{name} = %{version}
# Note: we keep <= (and a rpmlint warning...) until we get a version higher than 2.3.21 (when this provides/obsoletes was introduced)
Obsoletes:      %{name} <= %{version}
#

%description -n libart_lgpl_2-2
Libart is a library for high-performance 2D graphics. It is currently
being used as the antialiased rendering engine for GNOME Canvas. It is
also the rendering engine for Gill, the GNOME Illustration application.

%package devel
Summary:        Header files for the libart 2D graphics library
Group:          System/GUI/GNOME
Requires:       libart_lgpl_2-2 = %{version}

%description devel
This package contains the header files for developing
applications that want to make use of libart_lgpl.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libart_lgpl_2-2 -p /sbin/ldconfig
%postun -n libart_lgpl_2-2 -p /sbin/ldconfig

%files -n libart_lgpl_2-2
%license COPYING
%doc AUTHORS README NEWS ChangeLog
%{_libdir}/*.so.*

%files devel
%{_bindir}/*-config
%{_includedir}/libart-2.0/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%changelog
