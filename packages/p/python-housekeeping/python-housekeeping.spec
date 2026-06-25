#
# spec file for package python-housekeeping
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-housekeeping
Version:        1.1
Release:        0
Summary:        Decorators for managing deprecations in Python projects
License:        MIT
URL:            https://github.com/beanbaginc/python-housekeeping
Source:         https://files.pythonhosted.org/packages/source/h/housekeeping/housekeeping-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-typing_extensions >= 4.4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module typing_extensions >= 4.4}
# /SECTION
%python_subpackages

%description
A small library providing decorators and helpers for managing
deprecations of functions, methods, parameters and modules across the
lifecycle of a Python project.

%prep
%autosetup -p1 -n housekeeping-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
# force hash-based .pyc (avoid python-bytecode-inconsistent-mtime)
%python_expand $python -m compileall -q -f -o 0 -o 1 --invalidation-mode unchecked-hash %{buildroot}%{$python_sitelib}/housekeeping
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest housekeeping

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/housekeeping
%{python_sitelib}/housekeeping-%{version}.dist-info

%changelog
