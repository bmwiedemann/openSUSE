#
# spec file for package asco
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


Name:           asco
Version:        0.4.10
Release:        0
Summary:        A SPICE Circuit Optimizer
License:        GPL-2.0-only
Group:          Productivity/Scientific/Electronics
Url:            http://asco.sourceforge.net/
Source0:        http://downloads.sourceforge.net/asco/ASCO-%{version}.tar.gz
# PATCH-FIX-UPSTREAM asco-0.4.10-fix-implicit-declaration.patch
Patch0:         asco-0.4.10-fix-implicit-declaration.patch
# PATCH-FIX-OPENSUSE asco_unbuffered.patch -- patch from QUCS team
Patch1:         asco_unbuffered.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gcc-c++
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
ASCO project aims to bring circuit optimization capabilities to existing SPICE
simulators using a high-performance parallel differential evolution (DE) optimization
algorithm. Currently out-of-the-box support for Eldo (TM), HSPICE (R), LTspice (TM),
Spectre (R), Qucs and ngspice exist.

%package        doc
Summary:        Documentation for ASCO
Group:          Documentation/Other
BuildArch:      noarch

%description    doc
ASCO project aims to bring circuit optimization capabilities to existing SPICE
simulators using a high-performance parallel differential evolution (DE) optimization
algorithm.

This package provides documentation for ASCO in PDF format.

%prep
%setup -qn ASCO-%{version}
%patch0 -p1
%patch1 -p1
tar -zxf Autotools.tar.gz
touch NEWS

%build
autoreconf -fi
%configure
make %{?_smp_mflags}

%install
%make_install
install -Dm 644 doc/ASCO.pdf %{buildroot}/%{_docdir}/%{name}/ASCO.pdf

%files
%defattr(-,root,root)
%doc ChangeLog README
%license LICENSE
%exclude %{_docdir}/%{name}/ASCO.pdf
%{_bindir}/alter
%{_bindir}/asco
%{_bindir}/asco-test
%{_bindir}/log
%{_bindir}/monte
%{_bindir}/postp
%{_bindir}/rosen

%files doc
%defattr(-,root,root)
%dir %{_docdir}/%{name}
%doc %{_docdir}/%{name}/ASCO.pdf

%changelog
