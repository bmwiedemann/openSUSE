#
# spec file for package python-cypari2
#
# Copyright (c) 2026 SUSE LLC
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

Name:           python-cypari2
Version:        2.2.9
Release:        0
Summary:        A Python interface to the number theory library PARI/GP
License:        GPL-2.0-or-later
URL:            https://github.com/sagemath/cypari2
Source:         https://files.pythonhosted.org/packages/source/c/cypari2/cypari2-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module cysignals >= 1.13.0}
BuildRequires:  %{python_module cysignals-devel >= 1.13.0}
BuildRequires:  %{python_module Cython >= 3.0}
BuildRequires:  %{python_module meson-python >= 0.18.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  pari-devel
BuildRequires:  pari-gp
BuildRequires:  fdupes
Requires:       python-cysignals >= 1.13.0
%python_subpackages

%description
A Python interface to the number theory library PARI/GP.

The complete documentation of cypari2 is available at https://cypari2.readthedocs.io and
the PARI/GP documentation at https://pari.math.u-bordeaux.fr/doc.html

CyPari 2 is maintained by the SageMath community.

Open issues or submit pull requests at https://github.com/sagemath/cypari2
and join https://groups.google.com/group/sage-devel to discuss.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}

%description devel
A Python interface to the number theory library PARI/GP.
This package contains header files.

%prep
%autosetup -p1 -n cypari2-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%{python_expand %fdupes %{buildroot}%{$python_sitearch}}

%check
%pytest_arch

%files %{python_files}
%doc NEWS README.rst
%license LICENSE
%{python_sitearch}/cypari2
%{python_sitearch}/cypari2-%{version}.dist-info
%exclude %{python_sitearch}/cypari2/*.pc
%exclude %{python_sitearch}/cypari2/*.h

%files %{python_files devel}
%{python_sitearch}/cypari2/*.pc
%{python_sitearch}/cypari2/*.h


%changelog
