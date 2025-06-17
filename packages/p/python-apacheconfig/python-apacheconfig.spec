#
# spec file for package python-apacheconfig
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
%{?sle15_python_module_pythons}
Name:           python-apacheconfig
Version:        0.3.2
Release:        0
Summary:        Apache config file parser
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/etingof/apacheconfig
Source:         https://files.pythonhosted.org/packages/source/a/apacheconfig/apacheconfig-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-ply >= 3.4
Requires:       python-six
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module ply >= 3.4}
BuildRequires:  %{python_module six}
# /SECTION
%python_subpackages

%description
Apache / Config::General configuration file parser

%prep
%autosetup -p1 -n apacheconfig-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/apacheconfigtool
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
#CHOOSE: %%pytest OR %%pyunittest -v OR CUSTOM
%pyunittest -v

%pre
%python_libalternatives_reset_alternative apacheconfigtool

%files %{python_files}
%doc CHANGES.rst README.md
%license LICENSE.rst
%python_alternative %{_bindir}/apacheconfigtool
%{python_sitelib}/apacheconfig
%{python_sitelib}/apacheconfig-%{version}.dist-info

%changelog
