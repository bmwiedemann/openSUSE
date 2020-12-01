#
# spec file for package python-pkgutil-resolve-name
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-pkgutil-resolve-name
Version:        1.0.0
Release:        0
Summary:        Backport of Python 3.9's pkgutil.resolve_name
License:        Python-2.0 AND MIT
Group:          Development/Languages/Python
URL:            https://github.com/graingert/pkgutil-resolve-name
Source:         https://files.pythonhosted.org/packages/source/p/pkgutil_resolve_name/pkgutil_resolve_name-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# No tests provided in repo of backport

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
