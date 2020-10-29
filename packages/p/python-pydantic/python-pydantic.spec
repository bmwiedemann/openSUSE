#
# spec file for package python-pydantic
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019, Martin Hauke <mardnh@gmx.de>
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
%define skip_python2 1
Name:           python-pydantic
Version:        1.6.1
Release:        0
Summary:        Data validation and settings management using python type hinting
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/samuelcolvin/pydantic
Source:         https://github.com/samuelcolvin/pydantic/archive/v%{version}.tar.gz#/pydantic-%{version}.tar.gz
# PATCH-FIX-UPSTREAM https://github.com/samuelcolvin/pydantic/commit/9c4860ce964a4eb2e22eedc21f21d406c596a82f Valdiate arguments config (#1663)
Patch0:         validate-config.patch
BuildRequires:  %{python_module email_validator >= 1.0.3}
BuildRequires:  %{python_module mypy}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dotenv >= 0.10.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions >= 3.7.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Recommends:     python-typing_extensions >= 3.7.2
Suggests:       python-email_validator >= 1.0.3
Suggests:       python-python-dotenv >= 0.10.4
BuildArch:      noarch
%python_subpackages

%description
Data validation and settings management using Python type hinting.

%prep
%setup -q -n pydantic-%{version}
%patch0 -p1
sed -i /dataclasses/d setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md HISTORY.md
%{python_sitelib}/*

%changelog
