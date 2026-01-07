#
# spec file for package python-accessible-pygments
#
# Copyright (c) 2026 SUSE LLC and contributors
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
%{?sle15_python_module_pythons}
Name:           python-accessible-pygments
Version:        0.0.5
Release:        0
Summary:        A collection of accessible pygments styles
License:        BSD-3-Clause
URL:            https://github.com/Quansight-Labs/accessible-pygments
Source:         https://github.com/Quansight-Labs/accessible-pygments/archive/refs/tags/v%{version}.tar.gz#/accessible-pygments-%{version}-gh.tar.gz
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatch-vcs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-pygments >= 1.5
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pygments >= 1.5}
# /SECTION
%python_subpackages

%description
A collection of accessible pygments styles

%prep
%setup -q -n accessible-pygments-%{version}

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python test/render_html.py

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/a11y_pygments
%{python_sitelib}/accessible_pygments-%{version}.dist-info

%changelog
