#
# spec file for package modglue
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


%define soname lib%{name}1

Name:           modglue
Version:        1.19
Release:        0
Summary:        A C++ library for handling co-processes
License:        GPL-2.0
Group:          Development/Libraries/C and C++ 
Url:            http://cadabra.phi-sci.com/index.html 
Source:         http://cadabra.phi-sci.com/%{name}-%{version}.tar.gz  
# PATCH-FIX-OPENSUSE -- dont add build date (boo#1047218)
Patch0:         modglue-1.19-reproducible.patch
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  pkg-config
BuildRequires:  pkgconfig(sigc++-2.0)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Modglue is a C++ library with classes for forking external
processes and asynchronous reading from streams. It takes away the
burden of all subtleties involving the Unix fork call. The
asynchronous read facility enables one to read on multiple input
streams at the same time, without losing any of the standard C++
stream facilities.

There are also several small additional programs bundled with modglue,
such as a program to add readline capability to any command line
program. Moreover, the modglue library extends the idea of standard
Unix pipes by providing a general framework for the creation of new
processes with more than just the standard stdin/stdout/stderr pipes.

%package -n %{soname}
Summary:        A C++ library for handling co-processes
Group:          Development/Libraries/C and C++ 

%description -n %{soname}
Modglue is a C++ library with classes for forking external
processes and asynchronous reading from streams. It takes away the
burden of all subtleties involving the Unix fork call. The
asynchronous read facility enables one to read on multiple input
streams at the same time, without losing any of the standard C++
stream facilities.

There are also several small additional programs bundled with modglue,
such as a program to add readline capability to any command line
program. Moreover, the modglue library extends the idea of standard
Unix pipes by providing a general framework for the creation of new
processes with more than just the standard stdin/stdout/stderr pipes.

This package provides the shared libraries for %{name}.

%package devel
Summary:        A C++ library for handling co-processes
Group:          Development/Libraries/C and C++ 
Requires:       %{soname} = %{version}

%description devel
Modglue is a C++ library with classes for forking external
processes and asynchronous reading from streams. It takes away the
burden of all subtleties involving the Unix fork call. The
asynchronous read facility enables one to read on multiple input
streams at the same time, without losing any of the standard C++
stream facilities.

There are also several small additional programs bundled with modglue,
such as a program to add readline capability to any command line
program. Moreover, the modglue library extends the idea of standard
Unix pipes by providing a general framework for the creation of new
processes with more than just the standard stdin/stdout/stderr pipes.

This package provides the header and source files for development with
%{name}.

%prep
%setup -q 
%patch0 -p1

%build
./configure --prefix=%{_prefix} --libdir=/%{_lib}
# PARALLEL MAKE DOES NOT WORK
make

%install
%make_install

rm %{buildroot}%{_libdir}/*.la
rm %{buildroot}%{_libdir}/*.a

# REMOVE SPURIOUS EXEC PERMISSIONS
chmod -x %{buildroot}%{_mandir}/man1/prompt.*
chmod -x %{buildroot}%{_mandir}/man1/ptywrap.*

%post -n %{soname}
/sbin/ldconfig

%postun -n %{soname}
/sbin/ldconfig

%files -n %{soname}
%defattr(-,root,root)
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_bindir}/prompt
%{_bindir}/ptywrap
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/%{name}/
%{_mandir}/man1/prompt.*
%{_mandir}/man1/ptywrap.*

%changelog
