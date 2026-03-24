#
# spec file for package python-sfs
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
Name:           python-sfs
Version:        0.6.3
Release:        0
Summary:        Sound Field Synthesis toolbox for Python
License:        MIT
URL:            https://github.com/sfstoolbox/
Source:         https://files.pythonhosted.org/packages/source/s/sfs/sfs-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-numpy >= 2
Requires:       python-scipy >= 1.16
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module matplotlib >= 3}
BuildRequires:  %{python_module numpy >= 2}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module scipy >= 1.16}
# /SECTION
%python_subpackages

%description
The Sound Field Synthesis Toolbox for Python gives you the
possibility to create numercial simulations of sound field
synthesis methods like wave field synthesis (WFS) or
near-field compensated higher order Ambisonics (NFC-HOA).

%prep
%autosetup -p1 -n sfs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%{python_sitelib}/sfs
%{python_sitelib}/sfs-%{version}.dist-info

%changelog
