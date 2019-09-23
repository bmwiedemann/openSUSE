#
# spec file for package antlr4
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

%bcond_with complete
%bcond_without runtime_cpp
# TODO: using of conditions
%bcond_with runtime_cs
%bcond_with runtime_go
%bcond_with runtime_java
%bcond_with runtime_js
%bcond_with runtime_python2
%bcond_with runtime_python3
%bcond_with runtime_swift

%define libver 4_7_2
%define runtime_cpp_lib libantlr4-runtime
%define runtime_cpp_libver %{runtime_cpp_lib}%{libver}

Name:           antlr4
Version:        4.7.2
Release:        0
Summary:        A parser generator
License:        BSD-3-Clause
Group:          Development/Tools/Other
Url:            http://www.antlr.org/
Source:         %{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Change installation paths for docs&libs to openSUSE default
Patch0:         antlr4-install-path.patch
%if %{with complete}
BuildRequires:  java-devel >= 1.7
BuildRequires:  maven
%endif
#BuildArch:      noarch

%description
ANTLR (ANother Tool for Language Recognition) is a parser generator
for reading, processing, executing, or translating structured text or
binary files. It can be used to build languages, tools, and
frameworks. From a grammar, ANTLR generates a parser that can build
and walk parse trees.

%if %{with runtime_cpp}

%package -n %{runtime_cpp_libver}
Summary:        Runtime C++ ANTRL libraries
Group:          System/Libraries
BuildRequires:  cmake >= 3.3.0
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  libstdc++-devel
BuildRequires:  pkgconfig(uuid)

%description -n %{runtime_cpp_libver}
ANTLR runtime libraries for C++.
ANTLR (ANother Tool for Language Recognition) is a parser generator
for reading, processing, executing, or translating structured text or
binary files.

%package -n %{runtime_cpp_lib}-devel
Summary:        Development files for the ANTRL libraries
Group:          Development/Libraries/C and C++
Requires:       %{runtime_cpp_libver} = %{version}

%description -n %{runtime_cpp_lib}-devel
ANTLR runtime libraries for C++.
ANTLR (ANother Tool for Language Recognition) is a parser generator
for reading, processing, executing, or translating structured text or
binary files.

%endif

%prep
%setup -q
%patch0 -p1

%build
%if %{with complete}
# it looks like we need antlr4-bootstrap for this
export MAVEN_OPTS="-Xmx1G"
mvn clean
mvn -DskipTests install
%endif

%if %{with runtime_cpp}
pushd runtime/Cpp
%cmake -DWITH_DEMO=False
%cmake_build
popd
%endif

%install
%if %{with complete}
#tree ~/.m2/repository/org/antlr
install -m 0644 -p ~/.m2/repository/org/antlr/antlr4-master/%{version}/%{name}-%{version}-complete.jar %{buildroot}/%{_datadir}/java/%{name}-%{version}-complete.jar
%endif

%if %{with runtime_cpp}
pushd runtime/Cpp
%cmake_install
popd
# drop static library as unused
rm %{buildroot}/%{_libdir}/lib%{name}-runtime.a
%endif

%if %{with runtime_cpp}

%post -n %{runtime_cpp_libver} -p /sbin/ldconfig

%postun -n %{runtime_cpp_libver} -p /sbin/ldconfig

%endif

%files
%license LICENSE.txt
%doc CHANGES.txt README.md

%files -n %{runtime_cpp_libver}
%license LICENSE.txt
%doc runtime/Cpp/README.md runtime/Cpp/VERSION
%{_libdir}/lib%{name}-runtime.so.%{version}

%files -n %{runtime_cpp_lib}-devel
%{_libdir}/lib%{name}-runtime.so
%{_includedir}/%{name}-runtime/

%changelog
