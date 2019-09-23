#
# spec file for package angelscript
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover 2_33_0
Name:           angelscript
Version:        2.33.0
Release:        0
Summary:        Scripting library
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            http://www.angelcode.com/angelscript/
Source:         http://www.angelcode.com/angelscript/sdk/files/%{name}_%{version}.zip
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  unzip

%description
The AngelCode Scripting Library, or AngelScript as it is also known,
is a scripting library designed to allow applications to extend their
functionality through external scripts.

It supports Unix sockets and TCP/IP sockets with optional
SSL/TLS support.

%package -n lib%{name}%{sover}
Summary:        Scripting library
Group:          System/Libraries

%description -n lib%{name}%{sover}
The AngelCode Scripting Library, or AngelScript as it is also known,
is a scripting library designed to allow applications to extend their
functionality through external scripts.

It supports Unix sockets and TCP/IP sockets with optional
SSL/TLS support.

%package devel
Summary:        Development files for AngelScript
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}

%description devel
The AngelCode Scripting Library, or AngelScript as it is also known,
is a scripting library designed to allow applications to extend their
functionality through external scripts.

This subpackage contains libraries and header files for developing
applications that want to make use of the AngelScript library.

%prep
%setup -q -n sdk/%{name}/projects/gnuc

%build
export CXXFLAGS="%{optflags}"
make %{?_smp_mflags} shared

%install
make install_shared install_header install_docs PREFIX=%{_prefix} DESTDIR=%{buildroot} LIBDIR_DEST=%{_libdir} DOCDIR_BASEDIR=%{_defaultdocdir}/%{name}
%fdupes %{buildroot} %{_defaultdocdir}/%{name}

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig

%files
# manual also contains the license
%{_defaultdocdir}/%{name}

%files -n lib%{name}%{sover}
%{_libdir}/libangelscript.so.*

%files devel
%attr(0644,root,root) %{_includedir}/*.h
%{_libdir}/libangelscript.so

%changelog
