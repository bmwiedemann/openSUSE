#
# spec file for package lapack-man
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


Name:           lapack-man
%define _name   lapack
Version:        3.8.0
Release:        0
Summary:        Manpages for LAPACK and BLAS
License:        BSD-3-Clause
Group:          Documentation/Other
URL:            http://www.netlib.org/lapack/
Source0:        http://www.netlib.org/lapack/%{_name}-%{version}.tar.gz
BuildRequires:  doxygen >= 1.7
BuildRequires:  fdupes
# Merged blas-man into lapack-man with 3.8.0 update
Provides:       blas-man = %{version}
Obsoletes:      blas-man < %{version}
BuildArch:      noarch

%description
The lapack-man package contains documentation for LAPACK 
(Linear Algebra PACKage) and BLAS (Basic Linear Algebra
Subprograms) routines, in the form of man pages.

%prep
%setup -q -n %{_name}-%{version}

%build
cp make.inc.example make.inc
make man %{?_smp_mflags}

# Remove some intermediate files
rm -f DOCS/man/man3/_*_.3
rm -f DOCS/man/man3/{BLAS_,}SRC_xerbla{_array,}.f.3

%install
install -d %{buildroot}%{_mandir}/man3
install -m 0644 DOCS/man/man3/*.3 %{buildroot}%{_mandir}/man3/

%fdupes %{buildroot}/%{_mandir}/man3/

%files
%doc %{_mandir}/man3/

%changelog
