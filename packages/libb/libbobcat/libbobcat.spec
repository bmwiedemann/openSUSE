#
# spec file
#
# Copyright (c) 2023 SUSE LLC
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


%global _name bobcat
%global _lib_name lib%{_name}
%global _lib_version 6

%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "light"
%global psuffix -light
%else
%global psuffix %{nil}
%endif

Name:           %{_lib_name}%{?psuffix}
Version:        6.02.02
Release:        0
Summary:        Shared library implementing C++ classes that are frequently used
License:        GPL-3.0-only
Group:          Development/Tools/Building
URL:            https://gitlab.com/fbb-git/bobcat
Source0:        https://gitlab.com/fbb-git/bobcat/-/archive/%{version}/bobcat-%{version}.tar.gz
Source1:        initialbobcatlib
%if "%{name}" == "%{_lib_name}-light"
BuildRequires:  the_silver_searcher
%endif
#BuildRequires:  libX11-devel
#BuildRequires:  libopenssl-1_1-devel
#BuildRequires:  readline-devel
#BuildRequires:  sendmail-devel
%if "%{name}" == "%{_lib_name}"
BuildRequires:  icmake
# BuildRequires for man:
BuildRequires:  yodl
%endif
BuildRequires:  gcc-c++

%package devel-static
Summary:        Bobcat static library
Group:          Development/Libraries/C and C++
%if "%{name}" == "%{_lib_name}-light"
Conflicts:      %{_lib_name}-devel
Conflicts:      %{_lib_name}-devel-static
%endif

%if "%{name}" == "%{_lib_name}"
Requires:       %{_lib_name}-devel = %{version}

%description
Bobcat is an acronym of `Brokken's Own Base Classes And Templates'. It is a
shared library implementing C++ classes that are frequently used in software
developed by Frank Brokken. All of Frank's C++ programs hosted at GitLab
depend on `bobcat'.

%package -n %{_lib_name}%{_lib_version}
Summary:        Shared library implementing C++ classes that are frequently used
Group:          Development/Tools/Building
Provides:       %{_lib_name} = %{version}
Obsoletes:      %{_lib_name} < %{version}

%description -n %{_lib_name}%{_lib_version}
Bobcat is an acronym of `Brokken's Own Base Classes And Templates'. It is a
shared library implementing C++ classes that are frequently used in software
developed by Frank Brokken. All of Frank's C++ programs hosted at GitLab
depend on `bobcat'.

%package devel
Summary:        Headers and documentation for the Bobcat library
Group:          Development/Libraries/C and C++
Requires:       %{_lib_name}%{_lib_version} = %{version}

%description devel
Headers and documentation of classes defined in the Bobcat library.

%endif

%description devel-static
Bobcat static library

%prep
%setup -q -n %{_name}-%{version}

%if "%{name}" == "%{_lib_name}"

%build
# Incase we have to use specific version of gcc:
export CXXFLAGS="%{optflags} --std=c++2a -Werror -fdiagnostics-color=never -ffat-lto-objects"
export CXX="g++"
sed -i 's/^#define CXX/\/\/ #define CXX/g' %{_name}/INSTALL.im
sed -i 's/^#define CXXFLAGS/\/\/ #define CXXFLAGS/g' %{_name}/INSTALL.im
sed -i 's/^#define DOC/\/\/ #define DOC/g' %{_name}/INSTALL.im
sed -i 's/^#define HDR/\/\/ #define HDR/g' %{_name}/INSTALL.im
sed -i 's/^#define LIB/\/\/ #define LIB/g' %{_name}/INSTALL.im
sed -i 's/^#define MAN/\/\/ #define MAN/g' %{_name}/INSTALL.im
echo "/* created during rpmbuild */"                            >> %{_name}/INSTALL.im
echo "#define CXX         \"${CXX}\""                           >> %{_name}/INSTALL.im
echo "#define CXXFLAGS    \"${CXXFLAGS}\""                      >> %{_name}/INSTALL.im
echo "#define DOC         \"%{_docdir}/%{_lib_name}%{_lib_version}-devel\""   >> %{_name}/INSTALL.im
echo "#define HDR         \"%{_includedir}/%{_name}\""          >> %{_name}/INSTALL.im
echo "#define LIB         \"%{_libdir}\""                       >> %{_name}/INSTALL.im
echo "#define MAN         \"%{_mandir}\""                       >> %{_name}/INSTALL.im
pushd %{_name}
./build dep
./build light
#echo -e "y\nn\ny\ny\n" | ./build libraries
./build man
popd

%install
pushd %{_name}
./build install x %{buildroot}
popd

%post -n %{_lib_name}%{_lib_version} -p /sbin/ldconfig
%postun -n%{_lib_name}%{_lib_version} -p /sbin/ldconfig

%files -n %{_lib_name}%{_lib_version}
%doc README
%{_libdir}/%{_lib_name}.so.%{_lib_version}
%attr(755, -, -) %{_libdir}/%{_lib_name}.so.%{version}

%files devel
%{_libdir}/%{_lib_name}.so
%doc %{_docdir}/%{_lib_name}%{_lib_version}-devel/
%{_includedir}/%{_name}/
%{_mandir}/man3/*.3%{_name}.gz
%{_mandir}/man7/*.7%{_name}.gz
%{_mandir}/man7/%{_name}.7.gz

%files devel-static

%else
cp -a %{SOURCE1} ./bobcat/

%description
Bobcat is an acronym of `Brokken's Own Base Classes And Templates'. This is the light library
would be use to build icmake without required it.

%build
export CXXFLAGS="%{optflags} --std=c++2a -Werror -fdiagnostics-color=never -ffat-lto-objects"
export CXX="g++"

pushd %{_name}
bash ./$(basename %{SOURCE1})
popd

%install
pushd %{_name}
mkdir -p %{buildroot}%{_libdir}
install -m 644 tmp/%{_lib_name}.a %{buildroot}%{_libdir}/
mkdir -p %{buildroot}%{_includedir}/%{_name}
install -m 644 tmp/%{_name}/* %{buildroot}%{_includedir}/%{_name}/
popd

%files devel-static
%{_includedir}/%{_name}/
%endif

%{_libdir}/%{_lib_name}.a

%changelog
