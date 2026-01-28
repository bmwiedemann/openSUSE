#
# spec file for package python-mpl-animators
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


%{?sle15_python_module_pythons}
Name:           python-mpl-animators
Version:        1.2.4
Release:        0
Summary:        An interative animation framework for matplotlib
License:        BSD-3-Clause
URL:            https://github.com/sunpy/mpl-animators
Source:         https://files.pythonhosted.org/packages/source/m/mpl_animators/mpl_animators-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 62}
BuildRequires:  %{python_module setuptools_scm >= 8}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-matplotlib >= 3.5.0
Requires:       python-numpy >= 1.23.0
Suggests:       python-astropy >= 5.3.0
Provides:       python-mpl_animators = %{version}-%{release}
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module astropy >= 5.3.0}
BuildRequires:  %{python_module matplotlib >= 3.5.0}
BuildRequires:  %{python_module numpy >= 1.23.0}
BuildRequires:  %{python_module pytest-doctestplus}
BuildRequires:  %{python_module pytest-mpl}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Aframework for creating interactive animations with matplotlib.
It is designed to handle N-dimensional data, and can be used to create animations.

%prep
%setup -q -n mpl_animators-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -p no:warnings -n auto

%files %{python_files}
%{python_sitelib}/mpl_animators
%{python_sitelib}/mpl_animators-%{version}.dist-info

%changelog
