#
# spec file for package lucene++
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


Name:           lucene++
Version:        3.0.7
Release:        0
Summary:        A high-performance, full-featured text search engine written in C++
License:        Apache-2.0 or LGPL-3.0+
Group:          Development/Libraries/C and C++
Url:            https://github.com/luceneplusplus/LucenePlusPlus
Source:         https://github.com/luceneplusplus/LucenePlusPlus/archive/rel_%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch1:         0001-Fix-compilation-with-Boost-1.58.patch
%if 0%{?suse_version} > 1325
BuildRequires:  libboost_filesystem-devel
BuildRequires:  libboost_iostreams-devel
BuildRequires:  libboost_regex-devel
BuildRequires:  libboost_system-devel
BuildRequires:  libboost_thread-devel
%else
BuildRequires:  boost-devel
%endif
BuildRequires:  cmake >= 2.8.6
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  subversion
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
An up to date C++ port of the popular Java Lucene library, a high-performance, full-featured text search engine.

%package -n liblucene++0
Summary:        A high-performance, full-featured text search engine written in C++
Group:          Development/Libraries/C and C++

%description -n liblucene++0
An up to date C++ port of the popular Java Lucene library, a high-performance, full-featured text search engine.

%package devel
Summary:        Development files for lucene++
Group:          Development/Libraries/C and C++
Requires:       liblucene++0 = %{version}

%description devel
Development files for lucene++, a high-performance, full-featured text search engine written in C++

%prep
%setup -q -n LucenePlusPlus-rel_%{version}
%patch1 -p1

%build
%if 0%{?suse_version} >= 1310
%cmake
%else # openSUSE 12.3
mkdir build
cd build
cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	-DCMAKE_INSTALL_LIBDIR:PATH=%{_libdir} \
	-DINCLUDE_INSTALL_DIR:PATH=%{_includedir} \
	-DLIB_INSTALL_DIR:PATH=%{_libdir} \
	-DCMAKE_BUILD_TYPE=release \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DCMAKE_C_FLAGS:STRING="%{optflags}" \
	-DCMAKE_CXX_FLAGS:STRING="%{optflags}"
%endif # openSUSE 12.3
make %{?_smp_mflags} lucene++
make %{?_smp_mflags} lucene++-contrib

%install
%if 0%{?suse_version} >= 1310
%cmake_install
%else # openSUSE 12.3
cd build
make DESTDIR=%{buildroot} install/fast
%endif # openSUSE 12.3

%post -n liblucene++0 -p /sbin/ldconfig

%postun -n liblucene++0 -p /sbin/ldconfig

%files -n liblucene++0
%defattr(-,root,root,-)
%{_libdir}/liblucene++.so.*
%{_libdir}/liblucene++-contrib.so.*
%doc COPYING APACHE.license GPL.license LGPL.license
%doc AUTHORS README* REQUESTS

%files devel
%defattr(-,root,root,-)
%doc COPYING APACHE.license GPL.license LGPL.license
%{_includedir}/lucene++/
%{_libdir}/liblucene++.so
%{_libdir}/liblucene++-contrib.so
%{_libdir}/pkgconfig/liblucene++.pc
%{_libdir}/pkgconfig/liblucene++-contrib.pc

%changelog
