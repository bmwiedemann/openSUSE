#
# spec file for package python-sphinx-version-warning
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
Name:           python-sphinx-version-warning
Version:        1.1.2
Release:        0
Summary:        Sphinx extension to add a warning banner
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/humitos/sphinx-version-warning
Source:         https://files.pythonhosted.org/packages/source/s/sphinx-version-warning/sphinx-version-warning-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Sphinx
BuildArch:      noarch
%python_subpackages

%description
Sphinx extension to add a warning banner

%prep
%setup -q -n sphinx-version-warning-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no tests provided

%files %{python_files}
%doc CHANGELOG.rst README.rst
%license LICENSE
%{python_sitelib}/versionwarning
%{python_sitelib}/sphinx[-_]version[-_]warning-%{version}*-info

%changelog
