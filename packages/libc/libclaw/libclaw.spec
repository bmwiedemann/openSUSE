#
# spec file for package libclaw
#
# Copyright (c) 2024 SUSE LLC
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


Name:           libclaw
Version:        1.8.2
Release:        0
Summary:        C++ library of various utility functions
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            https://github.com/j-jorge/libclaw
Source:         https://github.com/j-jorge/libclaw/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE lib64-installation-path.diff -- ..
Patch0:         lib64-installation-path.diff
BuildRequires:  boost-devel >= 1.42
BuildRequires:  cmake >= 3.14
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  gettext-devel
BuildRequires:  graphviz
BuildRequires:  libjpeg-devel
BuildRequires:  libpng-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(zlib)

%description
Claw is a generalist library written in C++ and providing various
structures (multitype map, AVL binary tree) and algorithms.

%package        -n %{name}1
Summary:        C++ library of various utility functions
Group:          System/Libraries

%description    -n %{name}1
Claw is a generalist library written in C++ and providing various
structures (multitype map, AVL binary tree) and algorithms.

%package devel
Summary:        Development files for the Claw library
Group:          Development/Libraries/C and C++
Requires:       %{name}1 = %{version}
Requires:       cmake

%description devel
This subpackage contains libraries and header files for developing
applications that want to make use of libclaw.

%package doc
Summary:        Documentation for Claw library
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
This subpackage contains the documentation and examples for using
libclaw.

%prep
%autosetup -p1
# Fix encoding of examples
find example -type f |
while read F
do
        iconv -f iso8859-1 -t utf-8 $F |sed 's/\r//' >.utf8
        touch -r $F .utf8
        mv .utf8 $F
done

%build
pushd cmake
%cmake
%make_build
popd

%install
pushd cmake
%cmake_install
popd
cp -R example %{buildroot}%{_datadir}/doc/%{name}1/examples
%fdupes -s %{buildroot}%{_datadir}/doc/%{name}1
%find_lang %{name}

%post -n %{name}1 -p /sbin/ldconfig
%postun -n %{name}1 -p /sbin/ldconfig

%files -n %{name}1 -f %{name}.lang
%license COPYING
%{_libdir}/%{name}*.so.*

%files devel
%{_libdir}/cmake/claw/
%{_includedir}/claw/
%{_libdir}/%{name}*.so

%files doc
%doc %{_datadir}/doc/%{name}1

%changelog
