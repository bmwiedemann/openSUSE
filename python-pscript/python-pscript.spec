#
# spec file for package python-pscript
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
Name:           python-pscript
Version:        0.7.1
Release:        0
Summary:        Python to JavaScript compiler
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            https://github.com/flexxui/pscript
Source:         https://files.pythonhosted.org/packages/source/p/pscript/pscript-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module invoke}
BuildRequires:  %{python_module pytest}
BuildRequires:  python-faulthandler
# /SECTION
BuildArch:      noarch

%python_subpackages

%description
PScript is a Python to JavaScript compiler, and is also the name of the subset
of Python that this compiler supports.

%prep
%setup -q -n pscript-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# the tests actually do not invoke themselves
#%%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} invoke-%%{$python_bin_suffix} test --unit

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
