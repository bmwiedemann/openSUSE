#
# spec file for package libqjson
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           libqjson
Summary:        QJson is a qt-based library that maps JSON data to QVariant objects
License:        LGPL-2.1+
Group:          Development/Libraries/C and C++
Version:        0.8.1
Release:        0
Url:            http://qjson.sourceforge.net/
Source:         qjson-%{version}.tar.bz2
Source1:        baselibs.conf
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  cmake
BuildRequires:  libqt4-devel
%define soname %{name}0
%define debug_package_requires libqjson0 = %version-%release

%description
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It can represent integer, real number, string, an ordered sequence of value,
and a collection of name/value pairs. QJson is a qt-based library that maps
JSON data to QVariant objects. JSON arrays will be mapped to QVariantList
instances, while JSON's objects will be mapped to QVariantMap.

Authors:
--------
    Flavio Castelli <flavio@castelli.name>

%package -n libqjson0
Summary:        QJson is a qt-based library that maps JSON data to QVariant objects
Group:          Development/Libraries/C and C++

%description -n libqjson0
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It can represent integer, real number, string, an ordered sequence of value,
and a collection of name/value pairs. QJson is a qt-based library that maps
JSON data to QVariant objects. JSON arrays will be mapped to QVariantList
instances, while JSON's objects will be mapped to QVariantMap.

Authors:
--------
    Flavio Castelli <flavio@castelli.name>

%package devel
Summary:        Development files for QJson
Group:          Development/Libraries/C and C++
Requires:       %{soname} = %{version}

%description devel
JSON (JavaScript Object Notation) is a lightweight data-interchange format.
It can represent integer, real number, string, an ordered sequence of value,
and a collection of name/value pairs. QJson is a qt-based library that maps
JSON data to QVariant objects. JSON arrays will be mapped to QVariantList
instances, while JSON's objects will be mapped to QVariantMap.

This package contains files for developing applications using QJson.

Authors:
--------
    Flavio Castelli <flavio@castelli.name>

%prep
%setup -q -n qjson-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
%if "%_lib" == "lib64"
LIBSUFFIX="-DLIB_SUFFIX=64"
%else
LIBSUFFIX=""
%endif
cmake . -DCMAKE_SKIP_RPATH=TRUE \
        -DCMAKE_INSTALL_PREFIX=%{_prefix} \
        -DCMAKE_MODULES_INSTALL_DIR=%{_datadir}/cmake/Modules \
        $LIBSUFFIX
make %{?jobs:-j %jobs}

%install
%makeinstall

%post -n %{soname} -p /sbin/ldconfig

%postun -n %{soname} -p /sbin/ldconfig

%files -n %{soname}
%defattr(-,root,root)
%doc ChangeLog COPYING.lib README*
%{_libdir}/libqjson.so.*

%files devel
%defattr(-,root,root)
%dir %{_libdir}/cmake
%{_includedir}/qjson
%{_libdir}/libqjson.so
%{_libdir}/pkgconfig/QJson.pc
%{_libdir}/cmake/qjson

%changelog
