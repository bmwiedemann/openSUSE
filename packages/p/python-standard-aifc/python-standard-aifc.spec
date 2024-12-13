#
# spec file for package python-standard-aifc
#
# Copyright (c) 2024 SUSE LLC
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


%define pythons python313
Name:           python-standard-aifc
Version:        3.13.0
Release:        0
Summary:        Standard library aifc redistribution. "dead battery"
License:        Python-2.0
URL:            https://github.com/youknowone/python-deadlib
Source:         https://files.pythonhosted.org/packages/source/s/standard-aifc/standard_aifc-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module testsuite}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-audioop-lts
Requires:       python-standard-chunk
BuildArch:      noarch
%python_subpackages

%description
Standard library aifc redistribution. "dead battery".

%prep
%autosetup -p1 -n standard_aifc-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# testsuite broken with current release, fixed upstream

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/aifc
%{python_sitelib}/standard_aifc-%{version}.dist-info

%changelog
