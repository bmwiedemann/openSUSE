#
# spec file for package gretl
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2012, Efstathios Agrapidis (stathisagrapidis@gmail.com)
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


%define libname libgretl-1_0-48
Name:           gretl
Version:        2024b
Release:        0
Summary:        GNU regression, econometrics and time-series library
License:        GPL-3.0-only
Group:          Productivity/Office/Finance
URL:            https://gretl.sourceforge.net/
Source0:        https://downloads.sourceforge.net/gretl/%{name}-%{version}.tar.xz
Source1:        https://downloads.sourceforge.net/gretl/gretl-guide.pdf
Source2:        https://downloads.sourceforge.net/gretl/gretl-ref.pdf
BuildRequires:  R-base-devel
BuildRequires:  fdupes
# Documented build requirements
BuildRequires:  gcc-c++
BuildRequires:  gcc-fortran
BuildRequires:  gnuplot
# Extra build requirements for openSUSE
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gmp)
BuildRequires:  pkgconfig(gtksourceview-4)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(lapack)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libgsf-1)
BuildRequires:  pkgconfig(libxml-2.0)
# Documented optional build requirements
BuildRequires:  pkgconfig(mpfr)
BuildRequires:  pkgconfig(readline)
# Documented runtime requirements
Requires:       gnuplot
%lang_package

%description
Gretl (GNU regression, econometrics and time-series library) comprises
libgretl, a shared library which provides various functions relating to
econometric estimation, a command-line client program and a gui client,
using GTK+.

%package -n %{libname}
Summary:        Shared library for %{name}
Group:          System/Libraries

%description -n %{libname}
This package contains the shared libraries for %{name}.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries/Other
Requires:       %{libname} = %{version}

%description devel
This package contains the development files for %{name}.

%package doc
Summary:        Documentation for gretl
BuildArch:      noarch

%description doc
This package provides the guide and command reference documentation (as PDF)
for gretl.

%prep
%autosetup
cp %{S:1} %{S:2} ./

%build
%configure \
  --disable-static \
  --disable-avx \
  --enable-build-editor \
  %{nil}
%make_build

%install
%make_install
%find_lang %{name}
find %{buildroot} -type f -name "*.la" -delete -print

%fdupes %{buildroot}%{_datadir}

%check
pushd tests
%make_build check
popd

%ldconfig_scriptlets -n %{libname}

%files
%doc ChangeLog CompatLog README
%{_bindir}/gretl*
%{_libdir}/%{name}-gtk3
%{_datadir}/%{name}/
%{_datadir}/metainfo/%{name}.appdata.xml
%{_datadir}/applications/%{name}*.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/mimetypes/*.png
%{_datadir}/mime/packages/%{name}.xml
%{_mandir}/man1/*%{?_ext_man}

%files -n %{libname}
%license COPYING
%{_libdir}/libgretl*.so.*

%files lang -f %{name}.lang

%files devel
%license COPYING
%{_libdir}/pkgconfig/gretl.pc
%{_libdir}/libgretl*.so
%{_includedir}/%{name}/

%files doc
%doc gretl-*.pdf

%changelog
