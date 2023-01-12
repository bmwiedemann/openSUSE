#
# spec file for package leptonica
#
# Copyright (c) 2023 SUSE LLC
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


%define major   6
Name:           leptonica
Version:        1.83.0
Release:        0
Summary:        Library for image processing and image analysis applications
License:        BSD-2-Clause
Group:          Development/Libraries/C and C++
URL:            http://leptonica.org/
Source0:        http://leptonica.org/source/%{name}-%{version}.tar.gz
Source1:        baselibs.conf
BuildRequires:  giflib-devel
BuildRequires:  gnuplot
BuildRequires:  libjpeg-devel
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libopenjp2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libwebp) >= 0.2.0

%description
Library for efficient image processing and image analysis operations.

%package -n libleptonica%{major}
Summary:        Library for image processing and image analysis applications
Group:          System/Libraries
Obsoletes:      liblept < %{version}
Provides:       liblept = %{version}

%description -n libleptonica%{major}
Library for efficient image processing and image analysis operations.

%package devel
Summary:        Leptonica Development Files
Group:          Development/Libraries/C and C++
Requires:       libleptonica%{major} = %{version}
Provides:       libleptonica-devel = %{version}
Obsoletes:      liblept-devel < %{version}
Provides:       liblept-devel = %{version}

%description devel
Development files for the Leptonica library.

%package tools
Summary:        Leptonica tools
Group:          Productivity/Graphics/Other

%description tools
Programs for manipulating images.

%prep
%autosetup -p1

%build
%configure \
    --disable-static \
    --program-prefix=lept-
%make_build

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print
rm -f %{buildroot}%{_bindir}/{*gen,*reg,*test*}

# Something related to cmake build. Not use at the moment.
rm -fr %{buildroot}%{_libdir}/cmake/

%check
# Don't run multiple jobs: some tests failed somehow.
%make_build -j1 check

%post -n libleptonica%{major} -p /sbin/ldconfig
%postun -n libleptonica%{major} -p /sbin/ldconfig

%files -n libleptonica%{major}
%license leptonica-license.txt
%doc version-notes.html moller52.jpg
%{_libdir}/libleptonica.so.*

%files devel
%license leptonica-license.txt
%doc README.html version-notes.html moller52.jpg
%{_includedir}/leptonica/
%{_libdir}/libleptonica.so
%{_libdir}/pkgconfig/*

%files -n leptonica-tools
%license leptonica-license.txt
%{_bindir}/lept-*

%changelog
