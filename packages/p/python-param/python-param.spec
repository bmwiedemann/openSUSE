#
# spec file for package python-param
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-param
Version:        1.9.1
Release:        0
Summary:        Declarative Python programming using Parameters
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            http://param.pyviz.org/
Source0:        https://github.com/ioam/param/archive/v%{version}.tar.gz
Source100:      python-param-rpmlintrc
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-numpy
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
%setup -q -n param-%{version}
sed -i -e 's:version=get_setup_version("param"):version="%{version}":g' setup.py
echo '{"git_describe": "v%{version}", "version_string": "%{version}"}' > param/.version

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand nosetests-%{$python_bin_suffix}

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/param/
%{python_sitelib}/numbergen/
%{python_sitelib}/param-%{version}-py*.egg-info

%changelog
