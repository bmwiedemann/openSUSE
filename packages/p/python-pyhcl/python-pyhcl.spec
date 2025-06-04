#
# spec file for package python-pyhcl
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
Name:           python-pyhcl
Version:        0.4.5
Release:        0
Summary:        HCL configuration parser for python
License:        MPL-2.0
URL:            https://github.com/virtuald/pyhcl
Source:         https://files.pythonhosted.org/packages/source/p/pyhcl/pyhcl-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
BuildArch:      noarch
%python_subpackages

%description
HCL configuration parser for python

%prep
%setup -q -n pyhcl-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/hcltool

%check
%pytest

%pre
# removing old update-alternatives entries
%python_libalternatives_reset_alternative hcltool

# post and postun alternatives calls are not needed with libalternatives

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE
%python_alternative %{_bindir}/hcltool
%{python_sitelib}/hcl
%{python_sitelib}/pyhcl-%{version}*-info

%changelog
