#
# spec file for package python-pkgutil-resolve-name
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


%{?sle15_python_module_pythons}
Name:           python-pkgutil-resolve-name
Version:        1.3.10
Release:        0
Summary:        Backport of Python 3.9's pkgutil.resolve_name
License:        MIT AND Python-2.0
Group:          Development/Languages/Python
URL:            https://github.com/graingert/pkgutil-resolve-name
Source:         https://files.pythonhosted.org/packages/source/p/pkgutil_resolve_name/pkgutil_resolve_name-%{version}.tar.gz
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Backport of Python 3.9's pkgutil.resolve_name which
resolves a name to an object.

%prep
%setup -q -n pkgutil_resolve_name-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# No tests provided in repo of backport

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pkgutil_resolve_name.py*
%pycache_only %{python_sitelib}/__pycache__/pkgutil_resolve_name*.pyc
%{python_sitelib}/pkgutil_resolve_name-%{version}*-info

%changelog
