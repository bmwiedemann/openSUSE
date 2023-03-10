#
# spec file for package python-accessible-pygments
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


%define modname accessible-pygments
Name:           python-accessible-pygments
Version:        0.0.3
Release:        0
Summary:        A collection of accessible pygments styles
License:        BSD-3-Clause
URL:            https://github.com/Quansight-Labs/accessible-pygments
Source:         https://files.pythonhosted.org/packages/source/a/accessible-pygments/accessible-pygments-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pygments >= 1.5}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pygments >= 1.5
BuildArch:      noarch
%python_subpackages

%description
A collection of accessible pygments styles

%prep
%setup -q -n accessible-pygments-%{version}

%build
%python_build

%install
%python_install
%python_expand rm -rf %{buildroot}%{$python_sitelib}/test

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/a11y_pygments
%{python_sitelib}/accessible_pygments-%{version}*-info

%changelog
