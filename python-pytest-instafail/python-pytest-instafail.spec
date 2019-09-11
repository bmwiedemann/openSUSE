#
# spec file for package python-pytest-instafail
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
Name:           python-pytest-instafail
Version:        0.4.1
Release:        0
Summary:        Pytest Plugin to Show Failures Instantly
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/jpvanhal/pytest-instafail
Source:         https://files.pythonhosted.org/packages/source/p/pytest-instafail/pytest-instafail-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pytest >= 2.9
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest >= 2.9}
# /SECTION
%python_subpackages

%description
Pytest-instafail is a plugin for py.test that shows
failures and errors instantly instead of waiting
until the end of test session.

%prep
%setup -q -n pytest-instafail-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export PYTHONDONTWRITEBYTECODE=1
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v

%files %{python_files}
%doc CHANGES.rst README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
