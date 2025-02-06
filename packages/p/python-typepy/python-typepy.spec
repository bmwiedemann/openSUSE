#
# spec file for package python-typepy
#
# Copyright (c) 2025 SUSE LLC
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
Name:           python-typepy
Version:        1.3.4
Release:        0
Summary:        Python library for run time variable type checker
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/thombashi/typepy
Source:         https://files.pythonhosted.org/packages/source/t/typepy/typepy-%{version}.tar.gz
BuildRequires:  %{python_module setuptools >= 38.3.0}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module mbstrdecoder >= 1.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.8.0}
BuildRequires:  %{python_module pytz >= 2018.9}
BuildRequires:  %{python_module tcolorpy}
# /SECTION
BuildRequires:  fdupes
Requires:       python-mbstrdecoder >= 1.0.0
Suggests:       python-python-dateutil >= 2.8.0
Suggests:       python-pytz >= 2018.9
Suggests:       python-path.py
Suggests:       python-tcolorpy
BuildArch:      noarch

%python_subpackages

%description
typepy is a Python library for variable type checker/validator/converter at run time.

%prep
%setup -q -n typepy-%{version}
echo > requirements/test_requirements.txt

# Remove build alias
sed -i '/build =/d' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/typepy*

%changelog
