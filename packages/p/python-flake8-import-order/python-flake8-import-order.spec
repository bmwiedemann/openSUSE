#
# spec file for package python-flake8-import-order
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


Name:           python-flake8-import-order
Version:        0.19.2
Release:        0
Summary:        Flake8 plugin that checks the ordering of import statements
License:        LGPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/PyCQA/flake8-import-order
Source:         https://files.pythonhosted.org/packages/source/f/flake8_import_order/flake8_import_order-%{version}.tar.gz
BuildRequires:  %{python_module flake8}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pycodestyle}
BuildRequires:  %{python_module pylama}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-flake8
Requires:       python-pycodestyle
BuildArch:      noarch
%python_subpackages

%description
Flake8 and pylama plugin that checks the ordering of import statements.

%prep
%setup -q -n flake8_import_order-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license COPYING
%doc README.rst CHANGELOG.rst
%{python_sitelib}/flake8_import_order/
%{python_sitelib}/flake8_import_order-%{version}*-info

%changelog
