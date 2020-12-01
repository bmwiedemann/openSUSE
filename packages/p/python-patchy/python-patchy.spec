#
# spec file for package python-patchy
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-patchy
Version:        2.1.0
Release:        0
License:        BSD-3-Clause
Summary:        Patch the inner source of python functions at runtime
Url:            https://github.com/adamchainz/patchy
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/p/patchy/patchy-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pkgutil-resolve-name}
BuildRequires:  fdupes
Requires:       python-pkgutil-resolve-name
BuildArch:      noarch

%python_subpackages

%description
Patch the inner source of python functions at runtime.

%prep
%setup -q -n patchy-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc AUTHORS.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
