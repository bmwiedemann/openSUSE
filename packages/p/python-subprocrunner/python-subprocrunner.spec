#
# spec file for package python-subprocrunner
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


Name:           python-subprocrunner
Version:        2.0.1
Release:        0
Summary:        A Python wrapper library for subprocess module
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/thombashi/subprocrunner
Source:         https://files.pythonhosted.org/packages/source/s/subprocrunner/subprocrunner-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 38.3.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-loguru >= 0.4.1
Requires:       python-mbstrdecoder >= 1.0.0
Requires:       python-typepy
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module loguru >= 0.4.1}
BuildRequires:  %{python_module mbstrdecoder >= 1.0.0}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typepy}
BuildRequires:  hostname
# /SECTION
%python_subpackages

%description
A Python wrapper library for subprocess module.

%prep
%setup -q -n subprocrunner-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/subprocrunner*

%changelog
