#
# spec file for package angelscript
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


%define sover 2_37_0
Name:           angelscript
Version:        2.37.0
Release:        0
Summary:        Scripting library
License:        Zlib
Group:          Development/Libraries/C and C++
URL:            https://www.angelcode.com/angelscript/
Source:         https://www.angelcode.com/angelscript/sdk/files/%{name}_%{version}.zip
# PATCH-FEATURE-OPENSUSE angelscript-addons_lib.patch aloisio@gmx.com -- build and install addons library
Patch0:         angelscript-addons_lib.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  meson >= 0.49.0
BuildRequires:  pkgconfig
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

%package -n lib%{name}_addons%{sover}
Summary:        Scripting library
Group:          System/Libraries

%description -n lib%{name}_addons%{sover}
The AngelCode Scripting Library, or AngelScript as it is also known,
is a scripting library designed to allow applications to extend their
functionality through external scripts.

It supports Unix sockets and TCP/IP sockets with optional
SSL/TLS support.

%package devel
Summary:        Development files for AngelScript
Group:          Development/Libraries/C and C++
Requires:       lib%{name}%{sover} = %{version}
Requires:       lib%{name}_addons%{sover} = %{version}

%description devel
The AngelCode Scripting Library, or AngelScript as it is also known,
is a scripting library designed to allow applications to extend their
functionality through external scripts.

This subpackage contains libraries and header files for developing
applications that want to make use of the AngelScript library.

%prep
%autosetup -p1 -n sdk

%build
pushd %{name}/projects/meson
%meson
%meson_build
popd

%install
pushd %{name}/projects/meson
%meson_install
popd

mv docs html

%post -n lib%{name}%{sover} -p /sbin/ldconfig
%postun -n lib%{name}%{sover} -p /sbin/ldconfig
%post -n lib%{name}_addons%{sover} -p /sbin/ldconfig
%postun -n lib%{name}_addons%{sover} -p /sbin/ldconfig

%files -n lib%{name}%{sover}
%{_libdir}/libangelscript.so.*

%files -n lib%{name}_addons%{sover}
%{_libdir}/libangelscript_addons.so.*

%files devel
# manual also contains the license
%doc html
%dir %{_includedir}/AngelScript
%dir %{_includedir}/AngelScript/autowrapper
%dir %{_includedir}/AngelScript/contextmgr
%dir %{_includedir}/AngelScript/datetime
%dir %{_includedir}/AngelScript/debugger
%dir %{_includedir}/AngelScript/scriptany
%dir %{_includedir}/AngelScript/scriptarray
%dir %{_includedir}/AngelScript/scriptbuilder
%dir %{_includedir}/AngelScript/scriptdictionary
%dir %{_includedir}/AngelScript/scriptfile
%dir %{_includedir}/AngelScript/scriptgrid
%dir %{_includedir}/AngelScript/scripthandle
%dir %{_includedir}/AngelScript/scripthelper
%dir %{_includedir}/AngelScript/scriptmath
%dir %{_includedir}/AngelScript/scriptstdstring
%dir %{_includedir}/AngelScript/serializer
%dir %{_includedir}/AngelScript/weakref
%{_includedir}/AngelScript/angelscript.h
%{_includedir}/AngelScript/autowrapper/aswrappedcall.h
%{_includedir}/AngelScript/contextmgr/contextmgr.h
%{_includedir}/AngelScript/datetime/datetime.h
%{_includedir}/AngelScript/debugger/debugger.h
%{_includedir}/AngelScript/scriptany/scriptany.h
%{_includedir}/AngelScript/scriptarray/scriptarray.h
%{_includedir}/AngelScript/scriptbuilder/scriptbuilder.h
%{_includedir}/AngelScript/scriptdictionary/scriptdictionary.h
%{_includedir}/AngelScript/scriptfile/scriptfile.h
%{_includedir}/AngelScript/scriptfile/scriptfilesystem.h
%{_includedir}/AngelScript/scriptgrid/scriptgrid.h
%{_includedir}/AngelScript/scripthandle/scripthandle.h
%{_includedir}/AngelScript/scripthelper/scripthelper.h
%{_includedir}/AngelScript/scriptmath/scriptmath.h
%{_includedir}/AngelScript/scriptmath/scriptmathcomplex.h
%{_includedir}/AngelScript/scriptstdstring/scriptstdstring.h
%{_includedir}/AngelScript/serializer/serializer.h
%{_includedir}/AngelScript/weakref/weakref.h
%{_libdir}/libangelscript.so
%{_libdir}/libangelscript_addons.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/pkgconfig/%{name}_addons.pc

%changelog
