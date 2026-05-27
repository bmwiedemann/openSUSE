#
# spec file for package python-python-discovery
#
# Copyright (c) 2026 SUSE LLC
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


Name:           python-python-discovery
Version:        1.3.1
Release:        0
Summary:        Python interpreter discovery
License:        MIT
URL:            https://github.com/tox-dev/python-discovery
Source:         https://files.pythonhosted.org/packages/source/p/python-discovery/python_discovery-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatch-vcs >= 0.5}
BuildRequires:  %{python_module hatchling >= 1.28}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module filelock >= 3.15.4}
BuildRequires:  %{python_module platformdirs >= 4.3.6}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytest-mock}
# /SECTION
BuildRequires:  fdupes
Requires:       python-filelock >= 3.15.4
Requires:       python-platformdirs >= 4.3.6
BuildArch:      noarch
%python_subpackages

%description
`python-discovery` is a library for discovering Python interpreters installed on your machine. You may have multiple
Python versions from system packages, pyenv, mise, asdf, uv, or the Windows registry (PEP 514). This library finds
the right one for you.

Give it a requirement like `python3.12` or `>=3.11,<3.13`, and it searches all known locations, verifies each candidate,
and returns detailed metadata about the match. Results are cached to disk so repeated lookups are fast.

%prep
%autosetup -p1 -n python_discovery-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest -v

%files %{python_files}
%license LICENSE
%{python_sitelib}/python_discovery
%{python_sitelib}/python_discovery-%{version}.dist-info

%changelog
