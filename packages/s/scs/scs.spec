#
# spec file for package scs
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


Name:           scs
Version:        2.1.2
Release:        0
Summary:        Numerical package for solving large-scale convex cone problems
License:        MIT
URL:            https://github.com/cvxgrp/scs
Source:         https://github.com/cvxgrp/scs/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  lapack-devel
BuildRequires:  make

%description
SCS (splitting conic solver) is a numerical optimization package for
solving large-scale convex cone problems.

%package  devel
Summary:        Development files for %{name}

%description devel
SCS (splitting conic solver) is a numerical optimization package for
solving large-scale convex cone problems.
This package provides development libraries and headers for %{name}.

%prep
%setup -q

%build
%make_build

%install
%make_install INSTALL_LIB_DIR=%{buildroot}%{_libdir} INSTALL_INC_DIR=%{buildroot}%{_includedir}/%{name}

%files devel
%doc README.md
%license LICENSE.txt
%{_includedir}/%{name}
%{_libdir}/*.so
%exclude %{_libdir}/*.a

%changelog
