#
# spec file for package python-typepy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-typepy
Version:        0.6.4
Release:        0
License:        MIT
Summary:        Python library for run time variable type checker 
Url:            https://github.com/thombashi/typepy
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/t/typepy/typepy-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools >= 38.3.0}
# SECTION test requirements
BuildRequires:  %{python_module mbstrdecoder >= 0.8.3}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module python-dateutil >= 2.8.0}
BuildRequires:  %{python_module pytz >= 2018.9}
BuildRequires:  %{python_module six >= 1.10.0}
BuildRequires:  %{python_module termcolor}
BuildRequires:  python-enum34
BuildRequires:  python-ipaddress
# /SECTION
BuildRequires:  fdupes
Requires:       python-mbstrdecoder >= 0.8.3
Requires:       python-setuptools >= 38.3.0
Requires:       python-six >= 1.10.0
Suggests:       python-python-dateutil >= 2.8.0
Suggests:       python-pytz >= 2018.9
Suggests:       python-path.py
Suggests:       python-termcolor
%ifpython2
Requires:       python-ipaddress
Requires:       python-enum34
%endif
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
%doc README.rst
%license LICENSE
%{python_sitelib}/typepy*

%changelog
