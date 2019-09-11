#
# spec file for package libclaw
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           libclaw
Version:        1.7.4
Release:        0
Summary:        C++ library of various utility functions
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Url:            http://libclaw.sourceforge.net/
Source:         http://downloads.sf.net/%{name}/%{name}-%{version}.tar.gz
# FEATURE-OPENSUSE not to strip libs.
Patch0:         libclaw-1.6.1-nostrip.patch
# FIX-OPENSUSE to set libs dir.
Patch1:         libclaw-1.7.0-libdir.patch
# FEATURE-OPENSUSE to prevent doxygen "W: file-contains-date-and-time".
Patch2:         libclaw-doxy-w-date-time.patch
# PATCH-FIX-UPSTREAM fix-cmake.patch
Patch3:         fix-cmake.patch
# PATCH-FIX-UPSTREAM to be built via gcc7.
Patch4:         libclaw-1.7.4-gcc7.patch
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
%setup -q
%patch0 -p1 -b .nostrip
%patch1 -p1 -b .libdir
%patch2
%patch3 -p1
%patch4 -p1
# Fix encoding of examples
find examples -type f |
while read F
do
        iconv -f iso8859-1 -t utf-8 $F |sed 's/\r//' >.utf8
        touch -r $F .utf8
        mv .utf8 $F
done

%build
%cmake \
%if 0%{suse_version} > 1320
	-DCMAKE_CXX_FLAGS="%{optflags} -std=c++98" \
%endif
	-DCMAKE_BUILD_TYPE=RelWithDebInfo
make %{?_smp_mflags} VERBOSE=1

%install
%cmake_install
cp -R examples %{buildroot}%{_datadir}/doc/%{name}1/examples
rm %{buildroot}%{_libdir}/*.a
%fdupes -s %{buildroot}%{_datadir}/doc/%{name}1
%find_lang %{name}

%post -n %{name}1 -p /sbin/ldconfig

%postun -n %{name}1 -p /sbin/ldconfig

%files -n %{name}1 -f %{name}.lang
%defattr(-,root,root)
%{_libdir}/*.so.*
%doc COPYING

%files devel
%defattr(-,root,root)
%{_bindir}/claw-config
%dir %{_datadir}/cmake/%{name}
%{_datadir}/cmake/libclaw/%{name}*.cmake
%{_includedir}/claw
%{_libdir}/*.so

%files doc
%defattr(-,root,root)
%doc %{_datadir}/doc/%{name}1

%changelog
