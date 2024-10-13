#
# spec file for package python-yamlcore
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-yamlcore
Version:        0.0.4
Release:        0
Summary:        YAML 1.2 Support for PyYAML
License:        MIT
URL:            https://github.com/perlpunk/pyyaml-core
Source:         https://files.pythonhosted.org/packages/source/y/yamlcore/yamlcore-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest >= 2.3.5}
# /SECTION
BuildRequires:  fdupes
Requires:       python-PyYAML
BuildArch:      noarch
%python_subpackages

%description
YAML 1.2 Support for PyYAML

This module can be used on top of PyYAML to load YAML 1.2 files. It depends on
PyYAML and inherits from it, it's not a fork.

Currently it supports enabling all YAML 1.2 Core Schema tags on top of the
PyYAML BaseLoader. It does not (yet) support other tags like the << merge key.
You can add custom constructors, though.

%prep
%autosetup -p1 -n yamlcore-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest tests/*.py

%files %{python_files}
%doc Changelog.md Readme.md
%license LICENSE
%{python_sitelib}/yamlcore
%{python_sitelib}/yamlcore-%{version}.dist-info

%changelog
