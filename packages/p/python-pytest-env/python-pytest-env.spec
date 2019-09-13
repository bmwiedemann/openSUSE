#
# spec file for package python-pytest-env
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
Name:           python-pytest-env
Version:        0.6.2
Release:        0
Summary:        Pytest plugin to add environment variables
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/MobileDynasty/pytest-env
Source:         https://files.pythonhosted.org/packages/source/p/pytest-env/pytest-env-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/MobileDynasty/pytest-env/master/LICENSE
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 2.6.0
BuildArch:      noarch
%python_subpackages

%description
A py.test plugin that allows you to add environment variables.

%prep
%setup -q -n pytest-env-%{version}
cp %{SOURCE10} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
