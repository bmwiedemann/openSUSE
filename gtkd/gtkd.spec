#
# spec file for package gtkd
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


%define gtkd_major  3
%define gtkd_minor  8
%define gtkd_bugfix 5
%define sover  0
# DMD is available only on x86*. Use LDC otherwise.
%ifarch %{ix86} x86_64
%bcond_without dcompiler_dmd
%else
%bcond_with dcompiler_dmd
%endif
Name:           gtkd
Version:        3.8.5
Release:        0
Summary:        D binding and OO wrapper for GTK+
License:        LGPL-3.0-or-later
Group:          Development/Libraries/Other
URL:            http://gtkd.org/
Source:         https://github.com/gtkd-developers/GtkD/archive/v%{version}/gtkd-%{version}.tar.gz
BuildRequires:  pkgconfig
Requires:       Mesa-libGL1
Requires:       atk
Requires:       cairo
Requires:       gstreamer
Requires:       gstreamer-plugins-base
Requires:       gtk3
Requires:       gtksourceview
Requires:       libGLU1
Requires:       libcurl
Requires:       libgstreamerd-%{gtkd_major}-%{sover} = %{version}
Requires:       libgtkd-%{gtkd_major}-%{sover} = %{version}
Requires:       libgtkdgl-%{gtkd_major}-%{sover} = %{version}
Requires:       libgtkdsv-%{gtkd_major}-%{sover} = %{version}
Requires:       libpeas
Requires:       libpeas-gtk
Requires:       libpeasd-%{gtkd_major}-%{sover} = %{version}
Requires:       libvted-%{gtkd_major}-%{sover} = %{version}
Requires:       pango
Requires:       vte
%if %{with dcompiler_dmd}
BuildRequires:  dmd
BuildRequires:  phobos-devel
%else
BuildRequires:  ldc
BuildRequires:  ldc-phobos-devel
%endif

%description
GTK+ is a highly usable, feature rich toolkit for creating graphical user
interfaces which boasts cross platform compatibility and an easy to use API.

%package     -n libgstreamerd-%{gtkd_major}-%{sover}
Summary:        GtkD gstreamerd library
Group:          System/Libraries

%description -n libgstreamerd-%{gtkd_major}-%{sover}
This package contains the GtkD gstreamerd library.

%package     -n libgtkd-%{gtkd_major}-%{sover}
Summary:        GtkD base library
Group:          System/Libraries

%description -n libgtkd-%{gtkd_major}-%{sover}
This package contains the GtkD base library.

%package     -n libgtkdgl-%{gtkd_major}-%{sover}
Summary:        GtkD gtkdgl library
Group:          System/Libraries

%description -n libgtkdgl-%{gtkd_major}-%{sover}
This package contains the GtkDGL library.

%package     -n libgtkdsv-%{gtkd_major}-%{sover}
Summary:        GtkD sourceview library
Group:          System/Libraries

%description -n libgtkdsv-%{gtkd_major}-%{sover}
This package contains the GtkD sourceview library.

%package     -n libpeasd-%{gtkd_major}-%{sover}
Summary:        GtkD peasd library
Group:          System/Libraries

%description -n libpeasd-%{gtkd_major}-%{sover}
This package contains the GtkD peasd library.

%package     -n libvted-%{gtkd_major}-%{sover}
Summary:        GtkD vted library
Group:          System/Libraries

%description -n libvted-%{gtkd_major}-%{sover}
This package contains the GtkD vted library.

%package     -n gtkd-devel
Summary:        GtkD devel and header files
Group:          Development/Languages/Other
Requires:       libgstreamerd-%{gtkd_major}-%{sover} = %{version}
Requires:       libgtkd-%{gtkd_major}-%{sover} = %{version}
Requires:       libgtkdgl-%{gtkd_major}-%{sover} = %{version}
Requires:       libgtkdsv-%{gtkd_major}-%{sover} = %{version}
Requires:       libpeasd-%{gtkd_major}-%{sover} = %{version}
Requires:       libvted-%{gtkd_major}-%{sover} = %{version}

%description -n gtkd-devel
This package contains the header files for GtkD a D binding and OO wrapper of GTK+

%prep
%setup -q -n GtkD-%{version}
sed -i 's|ldconfig|/sbin/ldconfig|g' GNUmakefile
sed -i 's|/lib/|/$(libdir)/|g' GNUmakefile

%build
make %{?_smp_mflags} \
%if %{with dcompiler_dmd}
    DC=dmd \
%else
    DC=ldmd2 \
%endif
    CC=gcc libdir=%{?_lib} DCFLAGS='-O -release -inline -boundscheck=off -w -g' \
    shared-gstreamer \
    shared-gtkd \
    shared-gtkdgl \
    shared-peas \
    shared-sv \
    shared-vte

%install
make %{?_smp_mflags} DESTDIR=%{buildroot} prefix=%{_prefix} libdir=%{?_lib} datadir=%{_datadir} \
    install-shared-gstreamer install-headers-gstreamer \
    install-shared-gtkd install-headers-gtkd \
    install-shared-gtkdgl install-headers-gtkdgl \
    install-shared-gtkdsv install-headers-gtkdsv \
    install-shared-peas install-headers-peas \
    install-shared-vte install-headers-vte

%post -n libgstreamerd-%{gtkd_major}-%{sover} -p /sbin/ldconfig
%postun -n libgstreamerd-%{gtkd_major}-%{sover} -p /sbin/ldconfig
%post -n libgtkd-%{gtkd_major}-%{sover} -p /sbin/ldconfig
%postun -n libgtkd-%{gtkd_major}-%{sover} -p /sbin/ldconfig
%post -n libgtkdgl-%{gtkd_major}-%{sover} -p /sbin/ldconfig
%postun -n libgtkdgl-%{gtkd_major}-%{sover} -p /sbin/ldconfig
%post -n libgtkdsv-%{gtkd_major}-%{sover} -p /sbin/ldconfig
%postun -n libgtkdsv-%{gtkd_major}-%{sover} -p /sbin/ldconfig
%post -n libpeasd-%{gtkd_major}-%{sover} -p /sbin/ldconfig
%postun -n libpeasd-%{gtkd_major}-%{sover} -p /sbin/ldconfig
%post -n libvted-%{gtkd_major}-%{sover} -p /sbin/ldconfig
%postun -n libvted-%{gtkd_major}-%{sover} -p /sbin/ldconfig

%files -n libgstreamerd-%{gtkd_major}-%{sover}
%{_libdir}/libgstreamerd-%{gtkd_major}.so.%{sover}
%{_libdir}/libgstreamerd-%{gtkd_major}.so.%{sover}.%{gtkd_minor}.%{gtkd_bugfix}

%files -n libgtkd-%{gtkd_major}-%{sover}
%{_libdir}/libgtkd-%{gtkd_major}.so.%{sover}
%{_libdir}/libgtkd-%{gtkd_major}.so.%{sover}.%{gtkd_minor}.%{gtkd_bugfix}

%files -n libgtkdgl-%{gtkd_major}-%{sover}
%{_libdir}/libgtkdgl-%{gtkd_major}.so.%{sover}
%{_libdir}/libgtkdgl-%{gtkd_major}.so.%{sover}.%{gtkd_minor}.%{gtkd_bugfix}

%files -n libgtkdsv-%{gtkd_major}-%{sover}
%{_libdir}/libgtkdsv-%{gtkd_major}.so.%{sover}
%{_libdir}/libgtkdsv-%{gtkd_major}.so.%{sover}.%{gtkd_minor}.%{gtkd_bugfix}

%files -n libpeasd-%{gtkd_major}-%{sover}
%{_libdir}/libpeasd-%{gtkd_major}.so.%{sover}
%{_libdir}/libpeasd-%{gtkd_major}.so.%{sover}.%{gtkd_minor}.%{gtkd_bugfix}

%files -n libvted-%{gtkd_major}-%{sover}
%{_libdir}/libvted-%{gtkd_major}.so.%{sover}
%{_libdir}/libvted-%{gtkd_major}.so.%{sover}.%{gtkd_minor}.%{gtkd_bugfix}

%files devel
%doc AUTHORS CHANGELOG README.md
%license COPYING
%dir %{_includedir}/d
%dir %{_includedir}/d/gtkd-%{gtkd_major}
%{_includedir}/d/gtkd-%{gtkd_major}/*
%{_libdir}/libgstreamerd-%{gtkd_major}.so
%{_libdir}/libgtkd-%{gtkd_major}.so
%{_libdir}/libgtkdgl-%{gtkd_major}.so
%{_libdir}/libgtkdsv-%{gtkd_major}.so
%{_libdir}/libpeasd-%{gtkd_major}.so
%{_libdir}/libvted-%{gtkd_major}.so
%{_datadir}/pkgconfig/*

%changelog
