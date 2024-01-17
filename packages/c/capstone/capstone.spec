#
# spec file for package capstone
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


%define sover   4
Name:           capstone
Version:        4.0.2
Release:        0
Summary:        A multi-platform, multi-architecture disassembly framework
License:        BSD-3-Clause
Group:          Development/Tools/Building
URL:            https://www.capstone-engine.org
Source:         https://github.com/aquynh/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description
Capstone is a disassembly framework.
disasm engine for binary analysis and reversing in the security community.

%package -n libcapstone%{sover}
Summary:        A multi-platform, multi-architecture disassembly framework
Group:          System/Libraries

%description -n libcapstone%{sover}
Capstone is a disassembly framework.

%package -n libcapstone-devel
Summary:        Development files to build upon libcapstone
Group:          Development/Libraries/C and C++
Requires:       libcapstone%{sover} = %{version}

%description -n libcapstone-devel
Development files to build upon libcapstone, C language only.

%package -n libcapstone-devel-static
Summary:        Static library for capstone
Group:          Development/Libraries/C and C++
Requires:       libcapstone-devel = %{version}

%description -n libcapstone-devel-static
Statically linked libcapstone.

%package doc
Summary:        Documentation for capstone, a disassembly framework
Group:          Documentation/Other
BuildArch:      noarch

%description doc
Capstone is a multi-architecture disassembly framework.

%package -n python3-capstone
Summary:        Python bindings for the Capstone disassembly framework
Group:          Development/Languages/Python
BuildArch:      noarch

%description -n python3-capstone
Capstone is a multi-architecture disassembly framework.

This package contains the Capstone bindings for Python.

%prep
%autosetup

%build
CAPSTONE_ARCHS="arm aarch64 mips powerpc sparc systemz x86" CAPSTONE_STATIC="yes" \
  CFLAGS="%{optflags}" ./make.sh

pushd bindings/python/
%python3_build
popd

%install
CAPSTONE_ARCHS="arm aarch64 mips powerpc sparc systemz x86" \
  LIBDIRARCH="%{_lib}" INCDIR="%{_includedir}" \
  DESTDIR=%{buildroot} V=1 CAPSTONE_STATIC="yes" ./make.sh install

install -m 755 -d %{buildroot}%{_docdir}/%{name}-doc/docs
install -m 644 -t %{buildroot}%{_docdir}/%{name}-doc/docs docs/README docs/*.pdf

# Available bindings: Java, OCaml, Python2 and Python3 (pure/C)
# Python3 bindings only for now
pushd bindings/python/
%python3_install
rm -rf %{buildroot}%{python3_sitelib}/%{name}/include
rm -rf %{buildroot}%{python3_sitelib}/%{name}/lib
popd

# fix pkgconfig file
sed -e '/^archive/d' -e 's|^libdir=.*|libdir=%{_libdir}|' \
    -i %{buildroot}%{_libdir}/pkgconfig/%{name}.pc

%fdupes %{buildroot}

%post -n libcapstone%{sover} -p /sbin/ldconfig
%postun -n libcapstone%{sover} -p /sbin/ldconfig

%files
%license LICENSE*.TXT
%{_bindir}/cstool

%files -n libcapstone%{sover}
%{_libdir}/lib%{name}.so.%{sover}*

%files -n libcapstone-devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files -n libcapstone-devel-static
%{_libdir}/lib%{name}.a

%files -n python3-capstone
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}*.egg-info

%files doc
%license LICENSE*.TXT
%doc ChangeLog README.md
%{_docdir}/%{name}-doc/docs/

%changelog
