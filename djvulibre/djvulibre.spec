#
# spec file for package djvulibre
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define	libname	lib%{name}21
Name:           djvulibre
Version:        3.5.27
Release:        0
Summary:        An Open Source Implementation of DjVu
License:        GPL-2.0+
Group:          Productivity/Graphics/Other
Url:            http://djvu.sourceforge.net
Source:         http://downloads.sourceforge.net/djvu/%{name}-%{version}.tar.gz
# PATCH-FIX-UPSTREAM -- https://sourceforge.net/p/djvu/djvulibre-git/ci/ff8e5b68f856a7fe17c9aa33d0f2220f4ba6b40c/
Patch0:         reproducible.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  hicolor-icon-theme
BuildRequires:  libjpeg-devel
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(libtiff-4)
Requires(post):    shared-mime-info
Requires(postun):  shared-mime-info
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
DjVu is a Web-centric format and software platform for distributing
documents and images. DjVuLibre is an open source (GPL) implementation
of DjVu, including viewers, browser plug-ins, decoders, simple
encoders, and utilities. DjVu can advantageously replace PDF, PS, TIFF,
JPEG, and GIF for distributing scanned documents, digital documents, or
high-resolution pictures. DjVu content downloads faster, displays and
renders faster, looks nicer on a screen, and consumes less client
resources than competing formats. DjVu images display instantly and can
be smoothly zoomed and panned with no lengthy rerendering. DjVu is used
by hundreds of academic, commercial, governmental, and noncommercial
Web sites around the world.

%package -n %{libname}
Summary:        Libraries of Open Source Implementation of DjVu - djvulibre
Group:          Productivity/Graphics/Other

%description -n  %{libname}
DjVu is a Web-centric format and software platform for distributing
documents and images. DjVuLibre is an open source (GPL) implementation
of DjVu, including viewers, browser plug-ins, decoders, simple
encoders, and utilities. DjVu can advantageously replace PDF, PS, TIFF,
JPEG, and GIF for distributing scanned documents, digital documents, or
high-resolution pictures. DjVu content downloads faster, displays and
renders faster, looks nicer on a screen, and consumes less client
resources than competing formats. DjVu images display instantly and can
be smoothly zoomed and panned with no lengthy rerendering. DjVu is used
by hundreds of academic, commercial, governmental, and noncommercial
Web sites around the world.

This package contains shared libraries

%package -n libdjvulibre-devel
Summary:        Libraries of Open Source Implementation of DjVu - djvulibre
Group:          Development/Libraries/Other
Requires:       %{libname} = %{version}

%description -n libdjvulibre-devel
DjVu is a Web-centric format and software platform for distributing
documents and images. DjVuLibre is an open source (GPL) implementation
of DjVu, including viewers, browser plug-ins, decoders, simple
encoders, and utilities. DjVu can advantageously replace PDF, PS, TIFF,
JPEG, and GIF for distributing scanned documents, digital documents, or
high-resolution pictures. DjVu content downloads faster, displays and
renders faster, looks nicer on a screen, and consumes less client
resources than competing formats. DjVu images display instantly and can
be smoothly zoomed and panned with no lengthy rerendering. DjVu is used
by hundreds of academic, commercial, governmental, and noncommercial
Web sites around the world.

This package contains development files

%package doc
Summary:        Documentation for the the DjVu - djvulibre
Group:          Productivity/Graphics/Other

%description doc
DjVu is a Web-centric format and software platform for distributing
documents and images. DjVuLibre is an open source (GPL) implementation
of DjVu, including viewers, browser plug-ins, decoders, simple
encoders, and utilities. DjVu can advantageously replace PDF, PS, TIFF,
JPEG, and GIF for distributing scanned documents, digital documents, or
high-resolution pictures. DjVu content downloads faster, displays and
renders faster, looks nicer on a screen, and consumes less client
resources than competing formats. DjVu images display instantly and can
be smoothly zoomed and panned with no lengthy rerendering. DjVu is used
by hundreds of academic, commercial, governmental, and noncommercial
Web sites around the world.

This package contains documentation

%prep
%setup -q
%patch0 -p1

%build
%configure

make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

# do not ship these
rm %{buildroot}%{_libdir}/libdjvulibre.la

%fdupes %{buildroot}

%post
%mime_database_post
%icon_theme_cache_post

%post  -n  %{libname} -p /sbin/ldconfig

%postun
%mime_database_postun
%icon_theme_cache_postun

%postun -n  %{libname} -p /sbin/ldconfig

%files
%license COPYING COPYRIGHT
%doc NEWS README
%doc %{_mandir}/man1/*
%{_datadir}/djvu
%{_bindir}/*
%{_datadir}/icons/hicolor/*
%{_datadir}/mime/packages/djvulibre-mime.xml

%files -n %{libname}
%{_libdir}/libdjvulibre.so.*

%files -n libdjvulibre-devel
%{_libdir}/libdjvulibre.so
%dir %{_includedir}/libdjvu
%{_includedir}/libdjvu/*.h
%{_libdir}/pkgconfig/ddjvuapi.pc

%files doc
%doc doc/*

%changelog
