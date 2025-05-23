#
# spec file for package python-pytest-tornasync
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


%{?sle15_python_module_pythons}
Name:           python-pytest-tornasync
Version:        0.6.0.post2
Release:        0
License:        MIT
Summary:        PyTest plugin for testing Tornado code
URL:            https://github.com/eukaryote/pytest-tornasync
Source:         https://github.com/eukaryote/pytest-tornasync/archive/refs/tags/%{version}.tar.gz#/pytest-tornasync-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tornado >= 5.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-pytest
Requires:       python-tornado >= 5.0
BuildArch:      noarch

%python_subpackages

%description
A pytest plugin that provides some fixtures for testing Tornado
apps and handling of plain (undecoratored) native coroutine tests.

%prep
%setup -q -n pytest-tornasync-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
# We'll package this ourself
rm -f %{buildroot}%{_prefix}/LICENSE

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/pytest_tornasync
%{python_sitelib}/pytest_tornasync-%{version}.dist-info

%changelog
