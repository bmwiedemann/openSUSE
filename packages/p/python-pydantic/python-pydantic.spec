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
Version:        1.5.1
Release:        0
Summary:        Data validation and settings management using python type hinting
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/samuelcolvin/pydantic
Source:         https://github.com/samuelcolvin/pydantic/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pytest < 5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-email-validator >= 1.0.3
Suggests:       python-ujson >= 1.35
BuildArch:      noarch
%python_subpackages

%description
Data validation and settings management using Python type hinting.

%prep
%setup -q -n pydantic-%{version}

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
