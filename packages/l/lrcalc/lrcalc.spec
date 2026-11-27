#
# spec file for package lrcalc
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           lrcalc
Version:        2.1
Release:        0
Summary:        Littlewood-Richardson Calculator
License:        GPL-3.0-or-later
URL:            https://sites.math.rutgers.edu/~asbuch/lrcalc/
Source0:        https://sites.math.rutgers.edu/~asbuch/lrcalc/lrcalc-%{version}.tar.gz
BuildRequires:  binutils
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires:  make
Requires:       liblrcalc2 = %{version}

%description
The Littlewood-Richardson Calculator (lrcalc) is a package of C and Maple
programs for computing Littlewood-Richardson coefficients and products of
Schubert polynomials.

%package -n liblrcalc-devel
Summary:        Development files for %{name}
Requires:       liblrcalc2 = %{version}
Provides:       %{name}-devel = %{version}

%description -n liblrcalc-devel
Development files and header files for the Littlewood-Richardson Calculator.

%package -n liblrcalc2
Summary:        Library files for %{name}

%description -n liblrcalc2
Shared library for the Littlewood-Richardson Calculator.

%prep
%autosetup

%build
%configure \
  --disable-static
%make_build

%check
%make_build check

%install
%make_install
find %{buildroot} -type f -name "*.la" -delete -print

%ldconfig_scriptlets -n liblrcalc2

%files
%license COPYING LICENSE
%doc AUTHORS ChangeLog README
%{_bindir}/lrcalc
%{_bindir}/schubmult
%{_datadir}/lrcalc

%files -n liblrcalc2
%{_libdir}/liblrcalc.so.2*

%files -n liblrcalc-devel
%{_includedir}/lrcalc
%{_libdir}/liblrcalc.so

%changelog
