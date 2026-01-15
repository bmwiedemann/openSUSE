#
# spec file for package python-pytest-textual-snapshot
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

%bcond_with test

Name:           python-pytest-textual-snapshot
Version:        1.1.0
Release:        0
Summary:        Snapshot testing for Textual apps
License:        MIT
URL:            https://github.com/Textualize/pytest-textual-snapshot
Source:         https://files.pythonhosted.org/packages/source/p/pytest-textual-snapshot/pytest_textual_snapshot-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module poetry-core >= 1.0.0}
# SECTION test requirements
BuildRequires:  %{python_module jinja2 >= 3.0.0}
BuildRequires:  %{python_module pytest >= 8.0.0}
BuildRequires:  %{python_module rich >= 12.0.0}
BuildRequires:  %{python_module syrupy >= 4.8.0}
BuildRequires:  %{python_module textual >= 0.28.0}
BuildRequires:  fdupes
%if %{with test}
# /SECTION
Requires:       python-jinja2 >= 3.0.0
Requires:       python-pytest >= 8.0.0
Requires:       python-rich >= 12.0.0
Requires:       python-syrupy >= 4.8.0
Requires:       python-textual >= 0.28.0
%endif
BuildArch:      noarch
%python_subpackages

%description
A pytest plugin for snapshot testing Textual applications.

A `pytest-textual-snapshot` test saves an SVG screenshot of a running
Textual app to disk. The next time the test runs, it takes another
screenshot and compares it to the saved one. If the new screenshot
differs from the old one, the test fails. This is a convenient way to
quickly and automatically detect visual regressions in your
applications.

%prep
%autosetup -p1 -n pytest_textual_snapshot-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%pytest
%endif

%files %{python_files}
%pycache_only %{python_sitelib}/__pycache__/pytest_textual_snapshot*.pyc
%{python_sitelib}/pytest_textual_snapshot.py
%{python_sitelib}/pytest_textual_snapshot-%{version}*-info

%changelog
