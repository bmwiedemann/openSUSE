#
# spec file for package python-validate_email
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


%{?sle15_python_module_pythons}
Name:           python-validate_email
Version:        1.3
Release:        0
Summary:        Verify if an email address is valid and really exists
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/syrusakbary/validate_email
Source:         https://files.pythonhosted.org/packages/source/v/validate_email/validate_email-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Validate_email is a package for Python that check if an email is valid,
properly formatted and really exists.

%prep
%setup -q -n validate_email-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/validate_email.py
%pycache_only %{python_sitelib}/__pycache__/validate_email*
%{python_sitelib}/validate_email-%{version}*-info

%changelog
