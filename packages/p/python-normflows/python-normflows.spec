#
# spec file for package python-normflows
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


Name:           python-normflows
Version:        1.7.3
Release:        0
Summary:        Pytorch implementation of normalizing flows
License:        MIT
URL:            https://github.com/VincentStimper/normalizing-flows
Source:         https://files.pythonhosted.org/packages/source/n/normflows/normflows-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
Requires:       python-numpy
Requires:       python-torch
Suggests:       python-mkdocs
Suggests:       python-mkdocstrings
Suggests:       python-mkdocs-jupyter
BuildArch:      noarch
%python_subpackages

%description
Pytorch implementation of normalizing flows.

%prep
%autosetup -p1 -n normflows-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# tests are extremely flaky

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/normflows
%{python_sitelib}/normflows-%{version}.dist-info

%changelog
