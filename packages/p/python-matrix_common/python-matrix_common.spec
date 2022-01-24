#
# spec file for package python-matrix_common
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python39 1
Name:           python-matrix_common
Version:        1.0.0
Release:        0
Summary:        Common utilities for Synapse, Sydent and Sygnal
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/matrix-org/matrix-python-common
Source:         https://files.pythonhosted.org/packages/source/m/matrix_common/matrix_common-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module flit-core}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
Common utilities for Synapse, Sydent and Sygnal.

%prep
%setup -q -n matrix_common-%{version}

%build
export PYTHONPATH=$PWD
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# no upstream tests

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/matrix_common-%{version}*info/
%{python_sitelib}/matrix_common

%changelog
