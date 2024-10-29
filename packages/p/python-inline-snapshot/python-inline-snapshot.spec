#
# spec file for package python-inline-snapshot
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


%{?sle15_python_module_pythons}
Name:           python-inline-snapshot
Version:        0.13.3
Release:        0
Summary:        Create and update inline snapshots in your Python code
License:        MIT
URL:            https://github.com/15r10nk/inline-snapshot/
Source:         https://files.pythonhosted.org/packages/source/i/inline-snapshot/inline_snapshot-%{version}.tar.gz
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module asttokens >= 2.0.5}
BuildRequires:  %{python_module black >= 23.3.0}
BuildRequires:  %{python_module click >= 8.1.4}
BuildRequires:  %{python_module dirty-equals >= 0.7.0}
BuildRequires:  %{python_module executing >= 2.0.0}
BuildRequires:  %{python_module hypothesis >= 6.75.5}
BuildRequires:  %{python_module mypy >= 1.2.0}
BuildRequires:  %{python_module pydantic}
BuildRequires:  %{python_module pyright >= 1.1.359}
BuildRequires:  %{python_module pytest-subtests >= 0.11.0}
BuildRequires:  %{python_module pytest-xdist}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module rich >= 13.7.1}
BuildRequires:  %{python_module time-machine >= 2.10.0}
BuildRequires:  %{python_module toml >= 0.10.2 if %python-base < 3.11}
BuildRequires:  %{python_module typing-extensions}
# /SECTION
BuildRequires:  fdupes
Requires:       python-asttokens >= 2.0.5
Requires:       python-black >= 23.3.0
Requires:       python-click >= 8.1.4
Requires:       python-executing >= 2.0.0
Requires:       python-rich >= 13.7.1
%if 0%{?python_version_nodots} < 311
Requires:       python-toml >= 0.10.2
Requires:       python-types-toml >= 0.10.8.7
%endif
Requires:       python-typing-extensions
BuildArch:      noarch
%python_subpackages

%description
Create and update inline snapshots in your Python code.

%prep
%autosetup -p1 -n inline_snapshot-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
#NOTE: disable test_typing because the underlying pyright module uses
# nodeenv, which required https connection to nodejs.org. This is not
# possible in OBS.
%pytest -v -k 'not test_typing'

%files %{python_files}
%{python_sitelib}/inline_snapshot
%{python_sitelib}/inline_snapshot-%{version}.dist-info

%changelog
