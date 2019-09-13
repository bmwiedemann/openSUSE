#
# spec file for package PythonQt
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define sover   3
%define mypyver 3
Name:           PythonQt
Version:        3.2
Release:        0
Summary:        Dynamic Python binding for the Qt framework
Group:          Development/Libraries/C and C++
License:        LGPL-2.1+
URL:            http://pythonqt.sourceforge.net
Source0:        https://downloads.sourceforge.net/pythonqt/%{name}%{version}.zip
# PATCH-FIX-OPENSUSE PythonQt-add-install-target.patch
Patch0:         %{name}-add-install-target.patch
# PATCH-FIX-UPSTREAM PythonQt-create-pkg-config.patch
Patch1:         PythonQt-create-pkg-config.patch
BuildRequires:  libqt5-qtbase-private-headers-devel
BuildRequires:  libqt5-qtdeclarative-devel
BuildRequires:  libqt5-qttools-devel
BuildRequires:  pkgconfig
BuildRequires:  unzip
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5WebKit)
BuildRequires:  pkgconfig(Qt5WebKitWidgets)
BuildRequires:  pkgconfig(Qt5XmlPatterns)
BuildRequires:  pkgconfig(python3)

%description
PythonQt offers an easy way to embed the Python scripting language into a
C++ Qt applications. It makes heavy use of the QMetaObject system and
requires Qt 5.x.
The focus of PythonQt is on embedding Python into an existing C++ application,
not on writing the whole application completely in Python. If you want to write
your whole application in Python, you should use PyQt or PySide instead.
If you are looking for a simple way to embed Python objects into your C++/Qt
Application and to script parts of your application via Python, PythonQt is the
way to go!

%package        devel
Summary:        Header files and development libraries for the pythonqt package
Group:          Development/Libraries/C and C++
Requires:       lib%{name}-Qt5-Python%{mypyver}-%{sover} = %{version}
Requires:       lib%{name}_QtAll-Qt5-Python%{mypyver}-%{sover} = %{version}
Requires:       pkgconfig(Qt5Concurrent)
Requires:       pkgconfig(Qt5Multimedia)
Requires:       pkgconfig(Qt5Svg)
Requires:       pkgconfig(Qt5WebKit)
Requires:       pkgconfig(Qt5WebKitWidgets)
Requires:       pkgconfig(Qt5XmlPatterns)
Requires:       pkgconfig(python3)

%description    devel
Header files and development libraries for the PythonQt package.

PythonQt offers an easy way to embed the Python scripting language into a
C++ Qt applications. It makes heavy use of the QMetaObject system and
requires Qt 5.x.
The focus of PythonQt is on embedding Python into an existing C++ application,
not on writing the whole application completely in Python. If you want to write
your whole application in Python, you should use PyQt or PySide instead.
If you are looking for a simple way to embed Python objects into your C++/Qt
Application and to script parts of your application via Python, PythonQt is the
way to go!

%package     -n lib%{name}-Qt5-Python%{mypyver}-%{sover}
Summary:        Dynamic Python binding for the Qt framework
Group:          System/Libraries

%description -n lib%{name}-Qt5-Python%{mypyver}-%{sover}
PythonQt offers an easy way to embed the Python scripting language into a
C++ Qt applications. It makes heavy use of the QMetaObject system and
requires Qt 5.x.
The focus of PythonQt is on embedding Python into an existing C++ application,
not on writing the whole application completely in Python. If you want to write
your whole application in Python, you should use PyQt or PySide instead.
If you are looking for a simple way to embed Python objects into your C++/Qt
Application and to script parts of your application via Python, PythonQt is the
way to go!

%package     -n lib%{name}_QtAll-Qt5-Python%{mypyver}-%{sover}
Summary:        Dynamic Python binding for the Qt framework
Group:          System/Libraries

%description -n lib%{name}_QtAll-Qt5-Python%{mypyver}-%{sover}
PythonQt offers an easy way to embed the Python scripting language into a
C++ Qt applications. It makes heavy use of the QMetaObject system and
requires Qt 5.x.
The focus of PythonQt is on embedding Python into an existing C++ application,
not on writing the whole application completely in Python. If you want to write
your whole application in Python, you should use PyQt or PySide instead.
If you are looking for a simple way to embed Python objects into your C++/Qt
Application and to script parts of your application via Python, PythonQt is the
way to go!

%prep
%setup -q -n %{name}%{version}
%patch0 -p1
%patch1 -p1
sed -r -i -e "s/(unix:PYTHON_VERSION=).*/\1%{mypyver}/g" build/python.prf
# Fix README end-of-line encoding
sed -i 's/\r//' README

%build
%qmake5 \
  "LIB_INSTALL=%{_libdir}" \
  "HEADER_INSTALL=%{_includedir}/PythonQt"
make %{?_smp_mflags}

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
