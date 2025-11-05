#
# spec file for package python-pyregion
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           python-pyregion
Version:        2.3.0
Release:        0
License:        MIT
Summary:        Python parser for ds9 region files
Url:            https://github.com/astropy/pyregion
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/pyregion/pyregion-%{version}.tar.gz
Patch0:         add_pkg_packages_and_fix_deprecation_warning.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module astropy >= 5.0}
BuildRequires:  %{python_module Cython}
BuildRequires:  %{python_module extension-helpers}
BuildRequires:  %{python_module numpy-devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyparsing >= 2.0}
BuildRequires:  %{python_module pytest-astropy}
BuildRequires:  fdupes
Requires:       python-astropy >= 5.0
Requires:       python-numpy
Requires:       python-pyparsing >= 2.0

%python_subpackages

%description
pyregion is a python module to parse ds9 region files. It also supports ciao region files.

%prep
%autosetup -n pyregion-%{version} -p0

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%{python_expand rm %{buildroot}%{$python_sitearch}/pyregion/*.{c,h}
%fdupes %{buildroot}%{$python_sitearch}
}

%check
%pytest_arch -k 'not test_region'

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitearch}/pyregion
%{python_sitearch}/pyregion-%{version}.dist-info

%changelog
