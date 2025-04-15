#
# spec file for package python-yamlloader
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
Name:           python-yamlloader
Version:        1.4.1
Release:        0
Summary:        Ordered YAML loader and dumper for PyYAML
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/Phynix/yamlloader
Source:         https://files.pythonhosted.org/packages/source/y/yamlloader/yamlloader-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This module provides loaders and dumpers for PyYAML. Currently, an
OrderedDict loader/dumper is implemented, allowing to keep items order
when loading resp. dumping a file from/to an OrderedDict (Python 3.7:
Also regular dicts are supported and are the default items to be loaded
to. As of Python 3.7 preservation of insertion order is a language
feature of regular dicts.)

[API Documentation](https://phynix.github.io/yamlloader/index.html).

%prep
%setup -q -n yamlloader-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# there are no tests at all. Sorry.

%files %{python_files}
%{python_sitelib}/yamlloader
%{python_sitelib}/yamlloader-%{version}*-info

%changelog
