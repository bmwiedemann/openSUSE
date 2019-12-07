#
# spec file for package python-yamlordereddictloader
#
# Copyright (c) 2019 SUSE LLC
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
%define modname yamlordereddictloader
Name:           python-yamlordereddictloader
Version:        0.4.0
Release:        0
Summary:        YAML loader and dump for PyYAML allowing to keep keys order
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/fmenabe/python-yamlordereddictloader
Source:         https://files.pythonhosted.org/packages/source/y/yamlordereddictloader/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This module provide a loader and a dumper for PyYAML allowing to
keep items order when loading a file (by putting them in
``OrderedDict`` objects) and to manage ``OrderedDict`` objects
when dumping to a file.

The loader is based on stackoverflow topic (thanks to Eric
Naeseth):
http://stackoverflow.com/questions/5121931/in-python-how-can-you-load-yaml-mappings-as-ordereddicts#answer-5121963

DEPRECATED: the
[Phynix/yamlloader](https://github.com/Phynix/yamlloader) project
provide an improved
version of this library with unit tests, performance improvements
(by providing access to the C implementation of PyYAML) and is
more actively developed. You should use it!

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# There are just no tests at all. Period.
/bin/true

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/%{modname}*
%pycache_only %{python_sitelib}/__pycache__

%changelog
