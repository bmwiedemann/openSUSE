#
# spec file for package olm
#
# Copyright (c) 2020 SUSE LLC
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


%global libname libolm3
%global descriptor An implementation of the Double Ratchet cryptographic ratchet \
in C and C++, including an implementation of the Megolm cryptographic ratchet
Name:           olm
Version:        3.2.1
Release:        0
Summary:        Double Ratchet cryptographic library
License:        Apache-2.0
Group:          Development/Libraries/C and C++
URL:            https://git.matrix.org/git/%{name}/about/
Source0:        https://gitlab.matrix.org/matrix-org/olm/-/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  cmake
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++

%description
%{descriptor}

%package doc
Summary:        Documentation files for %{name}
Group:          Documentation/Other
Suggests:       %{libname} = %{version}
BuildArch:      noarch

%description doc
%{descriptor}.
%{summary}

%package -n %{libname}
Summary:        Double Ratchet cryptographic library as a C API
Group:          System/Libraries
Recommends:     %{name}-doc = %{version}

%description -n %{libname}
%{descriptor}.
%{summary}

%package    devel
Summary:        Development files for %{name}
Group:          Development/Libraries/C and C++
Requires:       %{libname} = %{version}

%description devel
%{descriptor}.
%{summary}

%prep
%autosetup -n %{name}-%{version}
sed -i 's@$(PREFIX)/lib@%{_libdir}@g' Makefile

%build
export CFLAGS="%{optflags}"
export CXXFLAGS="$CFLAGS"

#Leap 42.3 and SLE_12_SP3 with rpm < 4.12
%if 0%{?sle_version} == 120300
  make %{?_smp_mflags}
%else
  %cmake
  %cmake_build
%endif

%install
mkdir -p %{buildroot}%{_includedir}/%{name}
%cmake_install DESTDIR=%{buildroot} PREFIX=%{_prefix}

%fdupes %{buildroot}

%post -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%files doc
%defattr(0644, root, root, 0755)
%doc *.md *.rst docs/*.md

%files -n %{libname}
%license LICENSE
%{_libdir}/libolm.so.*

%files devel
%defattr(0644, root, root, 0755)
%{_includedir}/%{name}
%{_libdir}/libolm.so
%{_libdir}/cmake/Olm

%changelog
