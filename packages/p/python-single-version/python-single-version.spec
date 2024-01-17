#
# spec file for package python-single-version
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


%{?sle15_python_module_pythons}
Name:           python-single-version
Version:        1.6.0
Release:        0
Summary:        Have a single source of version in your code base
License:        MIT
URL:            https://github.com/hongquan/single-version
Source0:        https://pypi.io/packages/source/s/single-version/single_version-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires:       python-first >= 2.0
Requires:       python-importlib-metadata
BuildArch:      noarch
%python_subpackages

%description
Utility to let you have a single source of version in your code base.

%prep
%autosetup -n single_version-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/single_version
%{python_sitelib}/single_version-%{version}.dist-info

%changelog
