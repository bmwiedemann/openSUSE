#
# spec file for package asco
#
# Copyright (c) 2024 SUSE LLC
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


Name:           asco
Version:        0.4.11
Release:        0
Summary:        A SPICE Circuit Optimizer
License:        GPL-2.0-only
Group:          Productivity/Scientific/Electronics
URL:            http://asco.sourceforge.net/
Source0:        http://downloads.sourceforge.net/asco/ASCO-%{version}.tar.gz
# PATCH-FIX-OPENSUSE asco_unbuffered.patch -- patch from QUCS team
Patch0:         asco_unbuffered.patch
# PATCH-FIX-OPENSUSE asco-add-missing-header.patch -- fix build for Tumbleweed
Patch1:         asco-add-missing-headers.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++

%description
ASCO brings circuit optimization capabilities to existing SPICE
simulators using a parallel differential evolution (DE) optimization
algorithm. Currently, out-of-the-box support for Eldo, HSPICE, LTspice,
Spectre, Qucs and ngspice exist.

%package        doc
Summary:        Documentation for ASCO
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
ASCO brings circuit optimization capabilities to existing SPICE
simulators using a parallel differential evolution (DE) optimization
algorithm. Currently, out-of-the-box support for Eldo, HSPICE, LTspice,
Spectre, Qucs and ngspice exist.

This package provides documentation for ASCO in PDF format.

%prep
%autosetup -n ASCO-%{version} -p1
tar -zxf Autotools.tar.gz

%build
# workaround for GCC10 build failure
export CFLAGS="%{optflags} -fcommon"
export CXXFLAGS="$CFLAGS"
autoreconf -fi
%configure
%make_build

%install
%make_install
install -Dm 644 doc/ASCO.pdf %{buildroot}/%{_docdir}/%{name}/ASCO.pdf

%check

%files
%license LICENSE
%doc ChangeLog README
%exclude %{_docdir}/%{name}/ASCO.pdf
%{_bindir}/alter
%{_bindir}/asco
%{_bindir}/asco-test
%{_bindir}/log
%{_bindir}/monte
%{_bindir}/postp
%{_bindir}/rosen

%files doc
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/ASCO.pdf

%changelog
