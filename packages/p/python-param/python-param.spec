#
# spec file for package python-param
#
# Copyright (c) 2022 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define modname param
Name:           python-param
Version:        1.12.3
Release:        0
Summary:        Declarative Python programming using Parameters
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://param.pyviz.org/
Source0:        https://github.com/holoviz/param/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz
Source100:      python-param-rpmlintrc
BuildRequires:  %{python_module jsonschema}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module numpy if (%python-base without python36-base)}
BuildRequires:  %{python_module pandas if (%python-base without python36-base)}
Recommends:     python-jsonschema
Recommends:     python-numpy
Recommends:     python-pandas
BuildArch:      noarch
%python_subpackages

%description
Param is a library providing Parameters: Python attributes extended to
have features such as type and range checking, dynamically generated
values, documentation strings, default values, etc., each of which is
inherited from parent classes if not specified in a subclass.

Param contains only two required Python files, with no external
dependencies, and is provided freely for both non-commercial and
commercial use under a BSD license, so that it can easily be included
as part of other projects.

%prep
%autosetup -p1 -n param-%{version}

sed -i -e 's:version=get_setup_version("param"):version="%{version}":g' setup.py
sed -i -e 's:__version__ = "0.0.0+unknown":__version__ = "%{version}":' param/__init__.py
echo '{"git_describe": "v%{version}", "version_string": "%{version}"}' > param/.version

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Exclusion documented in gh#holoviz/param#423
%pytest -k 'not test_abstract_class' tests/*/*.py -ra
%{python_expand # make sure the correct version is reported. Other packages depend on it.
PYTHONPATH=%{buildroot}%{$python_sitelib}
$python -c '
import param
v = param.__version__
assert v == "%{version}", "wrong version reported: {}".format(v)
'
}

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/param/
%{python_sitelib}/numbergen/
%{python_sitelib}/param-%{version}-py%{python_version}.egg-info/

%changelog
