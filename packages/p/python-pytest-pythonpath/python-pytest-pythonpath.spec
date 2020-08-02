#
# spec file for package python-pytest-pythonpath
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
Name:           python-pytest-pythonpath
Version:        0.7.3
Release:        0
Summary:        Pytest plugin for adding to the PYTHONPATH from command line or configs
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/bigsassy/pytest-pythonpath
Source:         https://files.pythonhosted.org/packages/source/p/pytest-pythonpath/pytest-pythonpath-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest
BuildArch:      noarch
%python_subpackages

%description
This is a py.test plugin for adding to the PYTHONPATH from the pytests.ini file before tests run.

%prep
%setup -q -n pytest-pythonpath-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/*

%changelog
