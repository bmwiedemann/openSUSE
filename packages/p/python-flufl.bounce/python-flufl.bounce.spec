#
# spec file for package python-flufl.bounce
#
# Copyright (c) 2024 SUSE LLC
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
Version:        4.0
Release:        0
Summary:        Email bounce detectors
License:        Apache-2.0
URL:            https://fluflbounce.readthedocs.io/en/latest/
# https://gitlab.com/warsaw/flufl.bounce/merge_requests/10
Source0:        https://files.pythonhosted.org/packages/source/f/flufl.bounce/flufl.bounce-%{version}.tar.gz
Source1:        https://gitlab.com/warsaw/flufl.bounce/raw/master/LICENSE
# PATCH-FIX-UPSTREAM https://gitlab.com/warsaw/flufl.bounce/-/merge_requests/21
Patch0:         use-correct-assertion-methods.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
Requires:       python-atpublic
Requires:       python-zope.interface
# SECTION test requirements
BuildRequires:  %{python_module atpublic}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module zope.interface}
# /SECTION
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Email bounce detectors.

%prep
%autosetup -p1 -n flufl.bounce-%{version}

%build
cp %{SOURCE1} .
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
%{python_sitelib}/flufl.bounce-*.pth
%{python_sitelib}/flufl.bounce-%{version}.dist-info

%changelog
