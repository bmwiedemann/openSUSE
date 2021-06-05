#
# spec file for package libclaw
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


Name:           libclaw
Version:        1.7.4
Release:        0
Summary:        C++ library of various utility functions
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://libclaw.sourceforge.net/
Source:         http://downloads.sf.net/%{name}/%{name}-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE not to strip libs.
Patch0:         libclaw-1.6.1-nostrip.patch
# PATCH-FEATURE-UPSTREAM libclaw-1.7.0-libdir.patch -- https://github.com/j-jorge/libclaw/pull/4
Patch1:         libclaw-1.7.0-libdir.patch
# PATCH-FIX-OPENSUSE libclaw-doxy-w-date-time.patch -- https://github.com/j-jorge/libclaw/pull/5
Patch2:         libclaw-doxy-w-date-time.patch
# PATCH-FIX-UPSTREAM fix-cmake.patch -- https://github.com/j-jorge/libclaw/commit/ff4d26816ded3da87c393b1accd07a63ee8a91cb
Patch3:         fix-cmake.patch
# PATCH-FIX-UPSTREAM libclaw-1.7.4-gcc7.patch -- modified https://github.com/j-jorge/libclaw/commit/6033275773313fe052f6e222321a8ec87587fbe6
Patch4:         libclaw-1.7.4-gcc7.patch
# PATCH-FIX-UPSTREAM no-boost-math.patch -- https://github.com/j-jorge/libclaw/pull/3
Patch5:         no-boost-math.patch
BuildRequires:  boost-devel >= 1.42
BuildRequires:  cmake >= 2.8.8
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
find examples -type f |
while read F
do
        iconv -f iso8859-1 -t utf-8 $F |sed 's/\r//' >.utf8
        touch -r $F .utf8
        mv .utf8 $F
done

%build
%cmake
%make_build

%install
%cmake_install
cp -R examples %{buildroot}%{_datadir}/doc/%{name}1/examples
rm %{buildroot}%{_libdir}/*.a
%fdupes -s %{buildroot}%{_datadir}/doc/%{name}1
%find_lang %{name}

%post -n %{name}1 -p /sbin/ldconfig
%postun -n %{name}1 -p /sbin/ldconfig

%files -n %{name}1 -f %{name}.lang
%license COPYING
%{_libdir}/%{name}*.so.*

%files devel
%{_bindir}/claw-config
%{_datadir}/cmake/libclaw/
%{_includedir}/claw/
%{_libdir}/%{name}*.so

%files doc
%doc %{_datadir}/doc/%{name}1

%changelog
