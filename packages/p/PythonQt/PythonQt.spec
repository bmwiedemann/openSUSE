#
# spec file for package PythonQt
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


%define sover   3
%define mypyver 3
Name:           PythonQt
Version:        3.2
Release:        0
Summary:        Dynamic Python binding for the Qt framework
License:        LGPL-2.1-or-later
Group:          Development/Libraries/C and C++
URL:            http://pythonqt.sourceforge.net
Source0:        https://downloads.sourceforge.net/pythonqt/%{name}%{version}.zip
# PATCH-FIX-OPENSUSE PythonQt-add-install-target.patch
Patch0:         %{name}-add-install-target.patch
# PATCH-FIX-UPSTREAM PythonQt-create-pkg-config.patch
Patch1:         PythonQt-create-pkg-config.patch
# PATCH-FIX-UPSTREAM
Patch2:         0001-Fix-build-with-python-3.8.patch
BuildRequires:  dos2unix
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(python3)

%description
PythonQt offers embedding of the Python scripting language into a
C++ Qt applications. It makes heavy use of the QMetaObject system and
requires Qt 5.x.
It is focused on embedding, not writing entire applications in Python -
that should use PyQt or PySide instead.

%package        devel
Summary:        Header files and development libraries for the pythonqt package
Group:          Development/Libraries/C and C++
Requires:       lib%{name}-Qt5-Python%{mypyver}-%{sover} = %{version}
Requires:       lib%{name}_QtAll-Qt5-Python%{mypyver}-%{sover} = %{version}
Requires:       pkgconfig(Qt5Concurrent)
Requires:       pkgconfig(Qt5Multimedia)
Requires:       pkgconfig(Qt5Svg)
Requires:       pkgconfig(Qt5XmlPatterns)
Requires:       pkgconfig(python3)

%description    devel
Header files and development libraries for the PythonQt package.

PythonQt offers embedding of the Python scripting language into a
C++ Qt applications. It makes heavy use of the QMetaObject system and
requires Qt 5.x.
It is focused on embedding, not writing entire applications in Python -
that should use PyQt or PySide instead.

%package     -n lib%{name}-Qt5-Python%{mypyver}-%{sover}
Summary:        Dynamic Python binding for the Qt framework
Group:          System/Libraries

%description -n lib%{name}-Qt5-Python%{mypyver}-%{sover}
PythonQt offers embedding of the Python scripting language into a
C++ Qt applications. It makes heavy use of the QMetaObject system and
requires Qt 5.x.

%package     -n lib%{name}_QtAll-Qt5-Python%{mypyver}-%{sover}
Summary:        Dynamic Python binding for the Qt framework
Group:          System/Libraries

%description -n lib%{name}_QtAll-Qt5-Python%{mypyver}-%{sover}
PythonQt offers embedding of the Python scripting language into a
C++ Qt applications. It makes heavy use of the QMetaObject system and
requires Qt 5.x.

%prep
%setup -q -n %{name}%{version}

find . -type f -exec dos2unix {} \;

%autopatch -p1

sed -r -i -e "s/(unix:PYTHON_VERSION=).*/\1%{mypyver}/g" build/python.prf

%build
%qmake5 \
  "LIB_INSTALL=%{_libdir}" \
  "HEADER_INSTALL=%{_includedir}/PythonQt"
%make_build

%install
%qmake5_install

%post -n lib%{name}-Qt5-Python%{mypyver}-%{sover} -p /sbin/ldconfig
%postun -n lib%{name}-Qt5-Python%{mypyver}-%{sover} -p /sbin/ldconfig
%post -n lib%{name}_QtAll-Qt5-Python%{mypyver}-%{sover} -p /sbin/ldconfig
%postun -n lib%{name}_QtAll-Qt5-Python%{mypyver}-%{sover} -p /sbin/ldconfig

%files -n lib%{name}-Qt5-Python%{mypyver}-%{sover}
%{_libdir}/lib%{name}-Qt5-Python%{mypyver}.so.%{sover}*

%files -n lib%{name}_QtAll-Qt5-Python%{mypyver}-%{sover}
%{_libdir}/lib%{name}_QtAll-Qt5-Python%{mypyver}.so.%{sover}*

%files devel
%doc README
%license COPYING
%{_includedir}/PythonQt
%{_libdir}/lib%{name}-Qt5-Python%{mypyver}.so
%{_libdir}/lib%{name}_QtAll-Qt5-Python%{mypyver}.so
%{_libdir}/pkgconfig/%{name}-Qt5-Python%{mypyver}.pc
%{_libdir}/pkgconfig/%{name}_QtAll-Qt5-Python%{mypyver}.pc

%changelog
