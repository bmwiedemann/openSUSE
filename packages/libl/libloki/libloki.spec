#
# spec file for package libloki
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

%define _S0_name loki
%define _SO_nr 0_1_7

Name:           lib%{_S0_name}
Version:        0.1.7
Release:        0
Summary:        Loki C++ Library of common design patterns and idioms
License:        MIT
Group:          Development/Libraries/C and C++
Url:            http://loki-lib.sourceforge.net
Source:         %{_S0_name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  doxygen
BuildRequires:  fdupes
BuildRequires:  gcc-c++

%description
Loki is a C++ library of designs, containing flexible implementations of
common design patterns and idioms. The library makes extensive use of
C++ template metaprogramming and implements several commonly used
tools: typelist, functor, singleton, smart pointer, object factory,
visitor and multimethods.


%package -n %{name}%{_SO_nr}
Summary:        Loki C++ Library of common design patterns and idioms
Group:          Development/Libraries/C and C++

%description -n %{name}%{_SO_nr}
Loki is a C++ library of designs, containing flexible implementations of
common design patterns and idioms. The library makes extensive use of
C++ template metaprogramming and implements several commonly used
tools: typelist, functor, singleton, smart pointer, object factory,
visitor and multimethods.


%package devel
Summary:        The Loki C++ headers and development libraries
Group:          Development/Libraries/C and C++
Requires:       glibc-devel
Requires:       %{name}%{_SO_nr} = %{version}

%description devel
Headers, static libraries, and shared object symlinks for the Loki C++ Library.


%package doc
Summary:        The Loki C++ html docs
Group:          Development/Libraries/C and C++

%description doc
HTML documentation files for the Loki C++ Library.


%prep
%setup  -n %{_S0_name}-%{version} -q

%build
make build-static build-shared
grep '^PREDEFINED.*= _WINDOWS_H' doc/Doxyfile && (
    sed -i 's/= _WINDOWS_H/= LOKI_WINDOWS_H/' doc/Doxyfile
    cd doc
    rm -rf html
    doxygen
)

%install
mkdir -p %{buildroot}%{_includedir}
cp -a include/%{_S0_name} %{buildroot}%{_includedir}

mkdir -p %{buildroot}%{_libdir}
cp -a lib/lib%{_S0_name}.* %{buildroot}%{_libdir}
ln -s lib%{_S0_name}.so.%{version} %{buildroot}%{_libdir}/lib%{_S0_name}.so

mkdir -p %{buildroot}%{_docdir}/%{name}
cp CHANGES README %{buildroot}%{_docdir}/%{name}
cp -a doc/{flex,html,yasli} %{buildroot}%{_docdir}/%{name}

%fdupes %buildroot

%post -n %{name}%{_SO_nr} -p /sbin/ldconfig

%postun -n %{name}%{_SO_nr} -p /sbin/ldconfig

%files -n %{name}%{_SO_nr}
%defattr(0755,root,root)
%{_libdir}/%{name}.so.*

%files devel
%defattr(0644,root,root,0755)
%{_includedir}/%{_S0_name}
%{_libdir}/%{name}.a
%{_libdir}/%{name}.so

%files doc
%defattr(0644,root,root,0755)
%doc %{_docdir}/%{name}

%changelog
