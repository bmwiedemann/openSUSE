#
# spec file for package python-labels
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
Name:           python-labels
Version:        20.1.0
Release:        0
Summary:        CLI app for managing GitHub labels
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hackebrot/labels
Source:         https://github.com/hackebrot/labels/archive/%{version}.tar.gz#/labels-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-attrs
Requires:       python-click
Requires:       python-pytoml
Requires:       python-requests
BuildRequires:  alts
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module pytest-mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytoml}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module responses}
# /SECTION
%python_subpackages

%description
CLI app for managing GitHub labels.

%prep
%setup -q -n labels-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/labels
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%pre
# removing old update-alternatives entries
%python_libalternatives_reset_alternative labels

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/labels
%{python_sitelib}/labels
%{python_sitelib}/labels-%{version}*-info

%changelog
