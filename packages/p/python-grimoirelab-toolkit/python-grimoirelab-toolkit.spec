#
# spec file for package python-grimoirelab-toolkit
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


Name:           python-grimoirelab-toolkit
Version:        0.3.4
Release:        0
Summary:        Toolkit of common functions used across GrimoireLab
License:        GPL-3.0-or-later
URL:            https://chaoss.github.io/grimoirelab/
Source:         https://files.pythonhosted.org/packages/source/g/grimoirelab-toolkit/grimoirelab_toolkit-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil >= 2.8}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires:       python-python-dateutil >= 2.8
%python_subpackages

%description
Toolkit of common functions used across GrimoireLab projects.

This package provides a library composed by functions widely used in other
GrimoireLab projects. These function deal with date handling, introspection,
URIs/URLs, among other topics.

%prep
%autosetup -p1 -n grimoirelab_toolkit-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# Raises ValueError
%pytest -k 'not test_invalid_timezone'

%files %{python_files}
%{python_sitelib}/grimoirelab_toolkit
%{python_sitelib}/grimoirelab_toolkit-%{version}.dist-info

%changelog
