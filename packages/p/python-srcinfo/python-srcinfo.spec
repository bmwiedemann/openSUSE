#
# spec file for package python-srcinfo
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


%bcond_without libalternatives
Name:           python-srcinfo
Version:        0.1.2
Release:        0
Summary:        Python library to parse Arch SRCINFO files
License:        ISC
URL:            https://github.com/kyrias/python-srcinfo
Source:         https://files.pythonhosted.org/packages/source/s/srcinfo/srcinfo-%{version}.tar.gz
# PATCH-FIX-OPENSUSE Do not use deprecated sections in pyproject.toml
Patch0:         support-new-poetry.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-parse >= 1.19.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module parse >= 1.19.0}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
Python library to parse Arch .SRCINFO files.

%prep
%autosetup -p1 -n srcinfo-%{version}
mv test/__init__.py test_srcinfo.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/parse_srcinfo
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
%python_libalternatives_reset_alternative parse_srcinfo

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/parse_srcinfo
%{python_sitelib}/srcinfo
%{python_sitelib}/srcinfo-%{version}.dist-info

%changelog
