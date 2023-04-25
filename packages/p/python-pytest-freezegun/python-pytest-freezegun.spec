#
# spec file for package python-pytest-freezegun
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
%{?sle15_python_module_pythons}
Name:           python-pytest-freezegun
Version:        0.4.2
Release:        0
Summary:        Fixtures in freeze_time
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ktosiek/pytest-freezegun
Source:         https://github.com/ktosiek/pytest-freezegun/archive/%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-freezegun > 0.3
Requires:       python-pytest >= 3.0.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module freezegun > 0.3}
BuildRequires:  %{python_module pytest >= 3.0.0}
# /SECTION
%python_subpackages

%description
Wrap tests with fixtures in freeze_time

%prep
%setup -q -n pytest-freezegun-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
