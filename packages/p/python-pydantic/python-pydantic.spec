#
# spec file for package python-pydantic
#
# Copyright (c) 2023 SUSE LLC
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


%{?!python_module:%define python_module() python3-%{**}}
%define skip_python2 1
Name:           python-pydantic
Version:        1.10.4
Release:        0
Summary:        Data validation and settings management using python type hinting
License:        MIT
URL:            https://github.com/pydantic/pydantic
Source:         https://github.com/pydantic/pydantic/archive/v%{version}.tar.gz#/pydantic-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Ignore DeprecationWarning until requests-toolbelt is fixed
# (Pulled in by email-validator)
Patch0:         ignore-urllib3-pyopenssl-warning.patch
BuildRequires:  %{python_module email-validator >= 1.0.3}
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dotenv >= 0.10.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module typing_extensions >= 4.2.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing_extensions >= 4.2.0
Suggests:       python-email-validator >= 1.0.3
Suggests:       python-python-dotenv >= 0.10.4
BuildArch:      noarch
%python_subpackages

%description
Data validation and settings management using Python type hinting.

%prep
%autosetup -p1 -n pydantic-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -k 'not test_multiple_env_file'

%files %{python_files}
%license LICENSE
%doc README.md HISTORY.md
%{python_sitelib}/pydantic
%{python_sitelib}/pydantic-%{version}*-info

%changelog
