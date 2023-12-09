#
# spec file for package podofo
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


%define libver 2
%bcond_with tools
Name:           podofo
Version:        0.10.2
Release:        0
Summary:        Tools to work with PDF files
License:        GPL-2.0-or-later
Group:          Productivity/Publishing/PDF
URL:            http://podofo.sourceforge.net/
Source0:        https://github.com/podofo/podofo/archive/%{version}/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE: manuals does not build
Patch0:         podofo-tools_man.patch
BuildRequires:  cmake >= 2.6
BuildRequires:  doxygen
BuildRequires:  fdupes
%if 0%{?suse_version} <= 1500
BuildRequires:  gcc12
BuildRequires:  gcc12-c++
%else
BuildRequires:  gcc
BuildRequires:  gcc-c++
%endif
BuildRequires:  libboost_headers-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(cppunit)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(libjpeg)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  pkgconfig(libtiff-4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(lua)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(zlib)

%description
Command line tools for working with PDF files.

%package -n libpodofo%{libver}
Summary:        PDF parsing and creation library
License:        LGPL-2.1-or-later
Group:          System/Libraries

%description -n libpodofo%{libver}
A cross platform PDF parsing and creation library.

%package -n libpodofo-devel
Summary:        Development files for podofo
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Other
Requires:       libboost_headers-devel
Requires:       libpodofo%{libver} = %{version}

%description -n libpodofo-devel
This package contains development files for podofo library.

%prep
%autosetup -p1

# Remove build time references so build-compare can do its work
echo "HTML_TIMESTAMP = NO" >> Doxyfile

%build
%if 0%{?suse_version} <= 1500
export CC=gcc-12
export CXX=g++-12
%endif
%cmake \
  -DWANT_FONTCONFIG=ON \
  -DWANT_BOOST=ON \
   %if %{with tools}
  -DPODOFO_BUILD_TOOLS=TRUE \
  %endif
  -DPODOFO_BUILD_STATIC=OFF \
  -DPODOFO_USE_VISIBILITY=ON
%cmake_build

# Build devel doc
cd ..
doxygen

%install
%cmake_install

# Install devel docs (do it manually to fix also rpmlint warning "files-duplicate" with %%fdupes)
mkdir -p %{buildroot}%{_docdir}/libpodofo-devel
install -pm 0644 AUTHORS.md CHANGELOG.md README.md TODO.md %{buildroot}%{_docdir}/libpodofo-devel/
cp -a doc/html/ %{buildroot}%{_docdir}/libpodofo-devel/

%fdupes -s %{buildroot}

%post -n libpodofo%{libver} -p /sbin/ldconfig
%postun -n libpodofo%{libver} -p /sbin/ldconfig

%files
%license COPYING
%doc AUTHORS.md README.md
%if %{with tools}
%{_bindir}/*
%{_mandir}/man1/podofo*.1%{?ext_man}
%endif

%files -n libpodofo%{libver}
%license COPYING
%{_libdir}/libpodofo.so.%{libver}
%{_libdir}/libpodofo.so.%{version}

%files -n libpodofo-devel
%license COPYING
%doc %{_docdir}/libpodofo-devel/
%{_includedir}/podofo/
%{_libdir}/libpodofo.so
%{_libdir}/pkgconfig/libpodofo.pc
%dir %{_datadir}/podofo
%{_datadir}/podofo/podofo-*.cmake

%changelog
