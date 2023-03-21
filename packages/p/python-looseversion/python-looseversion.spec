#
# spec file for package python-looseversion
#
# Copyright (c) 2023 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           python-looseversion
Version:        1.1.2 
Release:        0
Summary:        A backwards/forwards-compatible fork of distutils.version.LooseVersion
License:        PSF-2.0 
Group:          Development/Languages/Python 
Url:            https://github.com/effigies/looseversion
Source:         https://github.com/effigies/looseversion/archive/refs/tags/%{version}.tar.gz
BuildRequires:  %{python_module base > 3}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch: noarch

%python_subpackages

%description
A backwards/forwards-compatible fork of distutils.version.LooseVersion, for times when PEP-440 isn't what you need.

The goal of this package is to be a drop-in replacement for the original LooseVersion. It implements an identical interface and comparison logic to LooseVersion. The only major change is that a looseversion.LooseVersion is comparable to a distutils.version.LooseVersion, which means tools should not need to worry whether all dependencies that use LooseVersion have migrated.

If you are simply comparing versions of Python packages, consider moving to packaging.version.Version, which follows PEP-440. LooseVersion is better suited to interacting with heterogeneous version schemes that do not follow PEP-440.

%prep
%setup -q -n looseversion-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -v tests.py

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/looseversion
%{python_sitelib}/looseversion-*

%changelog

