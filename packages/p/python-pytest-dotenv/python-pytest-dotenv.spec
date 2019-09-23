#
# spec file for package python-pytest-dotenv
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
Name:           python-pytest-dotenv
Version:        0.4.0
Release:        0
Summary:        A pytest plugin that parses environment files
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/quiqua/pytest-dotenv
Source:         https://files.pythonhosted.org/packages/source/p/pytest-dotenv/pytest-dotenv-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 2.6.0
Requires:       python-python-dotenv >= 0.9.1
BuildArch:      noarch
%python_subpackages

%description
A py.test plugin that parses environment files before running tests.

%prep
%setup -q -n pytest-dotenv-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
