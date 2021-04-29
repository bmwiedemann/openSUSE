#
# spec file for package olm
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%global origname olm
%global origlibname lib%{origname}
%global libname %{origlibname}3
%global descriptor An implementation of the Double Ratchet cryptographic ratchet \
in C and C++, including an implementation of the Megolm cryptographic ratchet

Name:           %{origname}
Version:        3.2.2
Release:        0
Summary:        Double Ratchet cryptographic library
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://git.matrix.org/git/%{origname}/about/
Source0:        https://gitlab.matrix.org/matrix-org/%{origname}/-/archive/%{version}/%{origname}-%{version}.tar.gz
BuildRequires:  %{python_module cffi >= 1.0.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  pkg-config
BuildRequires:  python-rpm-macros
Requires:       %{libname} = %{version}
Requires:       python-cffi >= 1.0.0
Requires:       python-future
%ifpython2
Requires:       python-typing
%endif
%python_subpackages

%description
%{descriptor} .
This package contains %{python_flavor} bindings for %{origname}.

%package -n %{origname}-doc
Summary:        Documentation files for %{origname}
Group:          Documentation/Other
Suggests:       %{libname} = %{version}
BuildArch:      noarch

%description -n %{origname}-doc
%{descriptor}.
%{summary}

%package -n %{libname}
Summary:        Double Ratchet cryptographic library as a C API
Group:          System/Libraries
Recommends:     %{origname}-doc = %{version}

%description -n %{libname}
%{descriptor}.
%{summary}

%package -n %{origname}-devel
Summary:        Development files for %{origname}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description -n %{origname}-devel
%{descriptor}.
%{summary}


%prep
%autosetup -n %{origname}-%{version}
sed -i 's@$(PREFIX)/lib@%{_libdir}@g' Makefile

%build
workdir=$(pwd)
export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"

#Leap 42.3 and SLE_12_SP3 with rpm < 4.12
%if 0%{?sle_version} == 120300
  make %{?_smp_mflags}
%else
  %cmake
  %cmake_build
%endif

cd $workdir/python
%python_build

%install
workdir=$(pwd)
mkdir -p %{buildroot}%{_includedir}/%{origname}
%cmake_install DESTDIR=%{buildroot} PREFIX=%{_prefix}

cd $workdir/python
%python_install

%fdupes %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files -n %{origname}-doc
%defattr(0644, root, root, 0755)
%doc *.md *.rst docs/*.md docs/*.svg

%files -n %{libname}
%license LICENSE
%{_libdir}/%{origlibname}.so.*

%files -n %{origname}-devel
%defattr(0644, root, root, 0755)
%{_includedir}/%{origname}
%{_libdir}/%{origlibname}.so
%{_libdir}/cmake/Olm
%{_libdir}/pkgconfig/%{origname}.pc

%files %{python_files}
%license LICENSE
%doc python/README.md
%{python_sitearch}/%{origname}
%{python_sitearch}/python_%{origname}-*.egg-info

%ifpython2
%{python_sitearch}/_%{origlibname}.so
%else
%{python_sitearch}/_%{origlibname}.abi3.so
%endif

%changelog
