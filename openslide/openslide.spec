#
# spec file for package openslide
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


%define soversion 0
%define libname lib%{name}

Name:           openslide
Version:        3.4.1
Release:        0
Summary:        C library for reading virtual slides
License:        LGPL-2.1-only
Group:          System/Libraries
Url:            http://openslide.org/
Source0:        https://github.com/openslide/openslide/releases/download/v%{version}/openslide-%{version}.tar.xz
BuildRequires:  cairo-devel
BuildRequires:  fdupes
BuildRequires:  gdk-pixbuf-devel
BuildRequires:  glib2-devel
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  libtiff-devel
BuildRequires:  libxml2-devel
BuildRequires:  openjpeg2-devel
BuildRequires:  pkg-config
BuildRequires:  sqlite3-devel
BuildRequires:  xz
BuildRequires:  zlib-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.

%package -n %{libname}%{soversion}
Summary:        C library for reading virtual slides
Group:          System/Libraries

%description -n %{libname}%{soversion}
The OpenSlide library allows programs to access virtual slide files
regardless of the underlying image format.

%package -n %{libname}-devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname}%{soversion} = %{version}
Recommends:     %{libname}-doc = %{version}

%description -n %{libname}-devel
This package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary:        Documentation for %{name}
Group:          Documentation/Other
BuildArch:      noarch

%description doc
This package contains documentation for developing with openslide library.

%package tools
Summary:        Command line tools for %{name}
Group:          Productivity/Graphics/Other
Requires:       %{libname}%{soversion} = %{version}

%description tools
This package contains command line tools for working with virtual slides.

%prep
%setup -q

%build
%configure --disable-static
make %{?_smp_mflags}

%install
%make_install
find %{buildroot}%{_libdir} -name '*.la' -type f -delete -print
%fdupes -s doc/html/

%clean
rm -rf %{buildroot}

%post -n %{libname}%{soversion} -p /sbin/ldconfig

%postun -n %{libname}%{soversion} -p /sbin/ldconfig

%files -n %{libname}%{soversion}
%defattr(-,root,root)
%{_libdir}/*.so.%{soversion}*

%files -n %{libname}-devel
%defattr(-,root,root)
%{_includedir}/%{name}/
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

%files doc
%defattr(-,root,root)
%doc README.txt lgpl-2.1.txt LICENSE.txt CHANGELOG.txt doc/html/

%files tools
%defattr(-,root,root)
%{_bindir}/*
%{_mandir}/man1/openslide*.1.gz

%changelog
