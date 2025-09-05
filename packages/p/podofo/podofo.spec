#
# spec file for package podofo
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define libver 3
Name:           podofo
Version:        1.0.2
Release:        0
Summary:        PDF parsing and creation library
License:        GPL-2.0-or-later
URL:            https://podofo.sourceforge.net/
Source0:        https://github.com/podofo/podofo/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.23
BuildRequires:  dos2unix
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  graphviz
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
%if 0%{?suse_version} > 1600
BuildRequires:  gcc-c++
%else
BuildRequires:  gcc13-c++
%endif

%description
A cross platform PDF parsing and creation library.

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
dos2unix API-MIGRATION.md

# Remove build time references so build-compare can do its work
echo "HTML_TIMESTAMP = NO" >> Doxyfile

%build
export CXX=g++
test -x "$(type -p g++-13)" && export CXX=g++-13
%cmake \
  -DPODOFO_BUILD_STATIC=OFF \
  -DPODOFO_BUILD_TEST=OFF \
  -DPODOFO_BUILD_UNSUPPORTED_TOOLS=OFF
%cmake_build

# Build devel doc
cd ..
doxygen

%install
%cmake_install

# Install devel docs (do it manually to fix also rpmlint warning "files-duplicate" with %%fdupes)
mkdir -p %{buildroot}%{_docdir}/libpodofo-devel/doc
install -pm 0644 API-MIGRATION.md AUTHORS.md CHANGELOG.md README.md TODO.md %{buildroot}%{_docdir}/libpodofo-devel/
cp -a html %{buildroot}%{_docdir}/libpodofo-devel/doc/

%fdupes -s %{buildroot}

%ldconfig_scriptlets -n libpodofo%{libver}

%files -n libpodofo%{libver}
%license COPYING
%{_libdir}/libpodofo.so.%{libver}
%{_libdir}/libpodofo.so.%{version}

%files -n libpodofo-devel
%license COPYING
%doc %{_docdir}/libpodofo-devel/
%{_includedir}/podofo/
%{_libdir}/libpodofo.so
%{_libdir}/cmake/podofo
%{_libdir}/pkgconfig/libpodofo.pc

%changelog
