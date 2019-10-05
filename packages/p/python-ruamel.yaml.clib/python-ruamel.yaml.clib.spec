#
# spec file for package python-ruamel.yaml.clib
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
Name:           python-ruamel.yaml.clib
Version:        0.2.0
Release:        0
Summary:        Python YAML parser c-library
License:        MIT
Group:          Development/Languages/Python
URL:            https://bitbucket.org/ruamel/yaml.clib
Source:         https://files.pythonhosted.org/packages/source/r/ruamel.yaml.clib/ruamel.yaml.clib-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools >= 28.7.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
ruamel.yaml.clib is a YAML parser/emitter that supports roundtrip preservation
of comments, seq/map flow style, and map key order.
This package contains the C library counterpart of it.

%prep
%setup -q -n ruamel.yaml.clib-%{version}
rm -rf *egg-info

%build
%python_build

%install
%python_install --single-version-externally-managed
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitearch}/_ruamel_yaml*.so
%{python_sitearch}/ruamel
%{python_sitearch}/ruamel.yaml.clib-%{version}-py%{python_version}.egg-info

%changelog
