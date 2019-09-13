#
# spec file for package python-sarge
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-sarge
Version:        0.1.5.post0
Release:        0
License:        BSD-3-Clause
Summary:        Command pipelines for python
Url:            https://sarge.readthedocs.org/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/s/sarge/sarge-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch

%python_subpackages

%description
A wrapper for subprocess which provides command pipeline functionality.

%prep
%setup -q -n sarge-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
