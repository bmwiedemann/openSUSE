#
# spec file for package python-flufl.bounce
#
# Copyright (c) 2026 SUSE LLC and contributors
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
Name:           python-flufl.bounce
Version:        5.0.1
Release:        0
Summary:        Email bounce detectors
License:        Apache-2.0
URL:            https://fluflbounce.readthedocs.io/en/latest/
# https://gitlab.com/warsaw/flufl.bounce/merge_requests/10
Source0:        https://files.pythonhosted.org/packages/source/f/flufl.bounce/flufl_bounce-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
Requires:       python-atpublic
# SECTION test requirements
BuildRequires:  %{python_module atpublic}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module sybil}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Email bounce detectors.

%prep
%autosetup -p1 -n flufl_bounce-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%dir %{python_sitelib}/flufl
%{python_sitelib}/flufl/bounce
%{python_sitelib}/flufl_bounce-%{version}.dist-info

%changelog
