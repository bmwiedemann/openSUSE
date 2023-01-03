#
# spec file for package python-node-semver
#
# Copyright (c) 2023 SUSE LLC
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-node-semver
Version:        0.8.1
Release:        0
Summary:        Port of node-semver
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/podhmo/python-node-semver
Source:         https://github.com/podhmo/python-node-semver/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module base}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# See https://github.com/k-bx/python-semver/issues/67 for why conflicts is needed
Conflicts:      python-semver
BuildArch:      noarch
%python_subpackages

%description
python version of node-semver (https://github.com/isaacs/node-semver)

%prep
%setup -q -n python-node-semver-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/*

%changelog
