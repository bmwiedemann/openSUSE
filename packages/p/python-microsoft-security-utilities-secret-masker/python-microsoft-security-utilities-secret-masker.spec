#
# spec file for package python-microsoft-security-utilities-secret-masker
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


%define realversion 1.0.0b4

%{?sle15_python_module_pythons}
Name:           python-microsoft-security-utilities-secret-masker
Version:        1.0.0~b4
Release:        0
Summary:        A tool for detecting and masking secrets
License:        MIT
URL:            None
Source:         https://files.pythonhosted.org/packages/source/m/microsoft-security-utilities-secret-masker/microsoft_security_utilities_secret_masker-%{realversion}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
A tool for detecting and masking secrets

%prep
%autosetup -p1 -n microsoft_security_utilities_secret_masker-%{realversion}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc HISTORY.rst README.rst
%{python_sitelib}/microsoft_security_utilities_secret_masker
%{python_sitelib}/microsoft_security_utilities_secret_masker-%{realversion}.dist-info

%changelog
