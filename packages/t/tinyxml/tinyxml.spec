#
# spec file for package tinyxml
#
# Copyright (c) 2012 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define so_version 0

Name:           tinyxml
Version:        2.6.2
Release:        0
%define file_version 2_6_2
%define lib_package lib%{name}%{so_version}
Summary:        A simple, small, C++ XML parser
License:        Zlib
Group:          System/Libraries
Source:         http://downloads.sourceforge.net/tinyxml/%{name}_%{file_version}.tar.gz
Source1:        configure.ac
Source2:        Makefile.am
Source3:        tinyxml.h.in
Source4:        use_stl_def
Source5:        Makefile.am.docs
Patch0:         tinyxml-c_headers.patch
Patch1:         tinyxml-entity.patch
Url:            http://sourceforge.net/projects/tinyxml
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  gcc-c++
BuildRequires:  libtool

%description
TinyXML is a simple, small, C++ XML parser that can be easily integrating
into other programs. Have you ever found yourself writing a text file parser
every time you needed to save human readable data or serialize objects?
TinyXML solves the text I/O file once and for all.
(Or, as a friend said, ends the Just Another Text File Parser problem.)

%package -n     %{lib_package}
Summary:        A simple, small, C++ XML parser
License:        Zlib
Group:          System/Libraries

%description -n %{lib_package}
TinyXML is a simple, small, C++ XML parser that can be easily integrating
into other programs. Have you ever found yourself writing a text file parser
every time you needed to save human readable data or serialize objects?
TinyXML solves the text I/O file once and for all.
(Or, as a friend said, ends the Just Another Text File Parser problem.)

%package        devel
Summary:        Development files for libtinyxml
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Requires:       %{lib_package} = %{version}
Provides:       libtinyxml-devel = %{version}
Obsoletes:      libtinyxml-devel < %{version}
Suggests:       %{name}-%{docs}

%description    devel
The libtinyxml-devel package contains libraries and header files for
developing applications that use libtinyxml.

%package        docs
Summary:        Documentaqtion for libtinyxml
License:        GPL-2.0+
Group:          Development/Libraries/C and C++
Requires:       %{lib_package} = %{version}

%description    docs
This packages contains the HTML documentation and a tutorial for
libtinyxml

%prep
%setup -q -n tinyxml
%patch0
%patch1
mkdir -p m4
cp %{S:1} %{S:2} %{S:3} %{S:4} .
cp %{S:5} docs/Makefile.am
rm -f tinyxml.h

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%makeinstall
rm -f %{buildroot}%{_libdir}/*.la

%post -n %{lib_package} -p /sbin/ldconfig

%postun -n %{lib_package} -p /sbin/ldconfig

%files -n %{lib_package}
%defattr(-,root,root,-)
%doc changes.txt readme.txt
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/*.so

%files docs
%defattr(-,root,root,-)
%doc docs/*.html docs/*.gif docs/*.png docs/*.css

%changelog
