#
# spec file for package python-rich-click
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
Name:           python-rich-click
Version:        1.7.4
Release:        0
Summary:        Format click help output nicely with rich
License:        MIT
URL:            https://github.com/ewels/rich-click
Source:         https://files.pythonhosted.org/packages/source/r/rich-click/rich-click-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-click >= 8
Requires:       python-rich >= 10.7.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click >= 8}
BuildRequires:  %{python_module rich >= 10.7.0}
# /SECTION
%python_subpackages

%description
Format click help output nicely with rich.

%prep
%setup -q -n rich-click-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/rich-click
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
%python_libalternatives_reset_alternative rich-click

#%%check
# No tests yet https://github.com/ewels/rich-click/issues/25

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/rich-click
%{python_sitelib}/*rich[_-]click*/

%changelog
