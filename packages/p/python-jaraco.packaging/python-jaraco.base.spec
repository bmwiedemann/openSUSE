#
# spec file for package python-jaraco.base
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
Name:           python-jaraco.base
Version:        6.1
Release:        0
Summary:        Base namespace for jaraco packages
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/jaraco/jaraco.packaging
Source:         https://files.pythonhosted.org/packages/source/j/jaraco.packaging/jaraco.packaging-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This package provides a base namespace to guarantee
that other jaraco packages can be imported.

This should not be installed directly, all packages
using the  "jaraco" namespace should depend on it.

%prep
%setup -q -n jaraco.packaging-%{version}
rm -rf jaraco.packaging.egg-info

%build
# Not needed

%install
%{python_expand install -D -m 644 jaraco/__init__.py  %{buildroot}%{$python_sitelib}/jaraco/__init__.py
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/jaraco/
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}/jaraco/
%fdupes %{buildroot}%{$python_sitelib}
}

%files %{python_files}
%license LICENSE
%dir %{python_sitelib}/jaraco/
%{python_sitelib}/jaraco/__init__.py*
%pycache_only %dir %{python_sitelib}/jaraco/__pycache__/
%pycache_only %{python_sitelib}/jaraco/__pycache__/__init__*.py*

%changelog
