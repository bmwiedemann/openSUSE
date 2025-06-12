#
# spec file for package python-sarge
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


Name:           python-sarge
Version:        0.1.7.post1
Release:        0
Summary:        Command pipelines for python
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://sarge.readthedocs.org/
Source:         https://files.pythonhosted.org/packages/source/s/sarge/sarge-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A wrapper for subprocess which provides command pipeline functionality.

%prep
%setup -q -n sarge-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/sarge
%{python_sitelib}/sarge-%{version}*-info

%changelog
