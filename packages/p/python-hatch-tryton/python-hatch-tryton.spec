#
# spec file for package python-hatch-tryton
#
# Copyright (c) 2026 Dr. Axel Braun <docb@opensuse.org>
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


Name:           python-hatch-tryton
Version:        0.1.0
Release:        0
Summary:        A hatchling plugin for Tryton
License:        MIT
URL:            https://www.tryton.org/
Source:         https://files.pythonhosted.org/packages/source/h/hatch-tryton/hatch_tryton-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatchling >= 1}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-hatchling
BuildArch:      noarch
%python_subpackages

%description
A ``hatchling`` plugin to manage Tryton dependencies.

%prep
%autosetup -p1 -n hatch_tryton-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license COPYRIGHT LICENSE
%{python_sitelib}/hatch_tryton
%{python_sitelib}/hatch_tryton-%{version}.dist-info

%changelog
