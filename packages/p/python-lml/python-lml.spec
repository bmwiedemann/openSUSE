#
# spec file for package python-lml
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
Name:           python-lml
Version:        0.2.0
Release:        0
Summary:        A lazy plugin management system for Python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/chfw/lml
Source:         https://files.pythonhosted.org/packages/source/l/lml/lml-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module isort}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
LML is "Load me later". lml seamlessly finds the lml-based
plugins from the current Python environment but loads plugins on
demand. It supports plugins that have external dependencies,
especially bulky and/or memory hungry ones. lml provides the plugin
management system only and the plugin interface is for the developer
to do.

Plugins loaded by lml may be installed packages or standalone
Python modules in a supplied directory.

%prep
%autosetup -p1 -n lml-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_plugin_loader': no pyexcel_test module
%pytest tests -k 'not test_plugin_loader'

%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst docs/source
%{python_sitelib}/lml
%{python_sitelib}/lml-%{version}.dist-info

%changelog
