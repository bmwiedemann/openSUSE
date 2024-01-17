#
# spec file for package libpgf
#
# Copyright (c) 2021 SUSE LLC
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


%define so_ver 7
Name:           libpgf
Version:        7.21.7
Release:        0
Summary:        Progressive Graphics File Library
License:        LGPL-2.1-or-later
Group:          Productivity/Graphics/Other
URL:            https://www.libpgf.org/
Source0:        https://sourceforge.net/projects/%{name}/files/%{name}/%{version}/libpgf.zip
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  graphviz
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  unzip

%description
libpgf is a library for working with PGF (Progresive Graphics File) images.

%package devel
Summary:        Development files for the libpgf library
Group:          Development/Libraries/C and C++
Requires:       libpgf%{so_ver} = %{version}

%description devel
This package contains header files and libraries needed for developing programs
using the libpgf library.

%package -n libpgf%{so_ver}
Summary:        Progressive Graphics File Library
Group:          System/Libraries

%description -n libpgf%{so_ver}
libpgf is a library for working with PGF (Progresive Graphics File) images.

%prep
%setup -q -n %{name}

# Fix autogen.sh failure "wrong-file-end-of-line-encoding"
find . -name Makefile.am | xargs sed -i 's/\r$//'
sed -i 's/\r$//' config.h.in
sed -i 's/\r$//' configure.ac
sed -i 's/\r$//' autogen.sh

# Fix autogen.sh failure
touch README

# Add "libpgf-" prefix to all man pages to prevent conflicts with other packages
sed -i 's/\$(mandir)\/man3\/\$\$f/\$(mandir)\/man3\/libpgf-\$\$f/' doc/Makefile.am

# Fix rpmlint warning "wrong-file-end-of-line-encoding"
sed -i 's/\r$//' README.txt

# Remove build time references so build-compare can do its work
echo "HTML_TIMESTAMP = NO" >> doc/Doxyfile.in

%build
sh autogen.sh
%configure --disable-static
%make_build

%install
%make_install DOC_DIR=%{buildroot}%{_docdir}/%{name}-devel/

# Remove libtool config files
find %{buildroot} -type f -name "*.la" -delete -print

%post -n libpgf%{so_ver} -p /sbin/ldconfig
%postun -n libpgf%{so_ver} -p /sbin/ldconfig

%files devel
%license COPYING
%doc README.txt
%doc %{_docdir}/%{name}-devel/
%{_includedir}/libpgf/
%{_libdir}/pkgconfig/libpgf.pc
%{_libdir}/libpgf.so
%{_mandir}/man3/libpgf-*.3%{?ext_man}

%files -n libpgf%{so_ver}
%{_libdir}/libpgf.so.%{so_ver}*

%changelog
