#
# spec file for package python-jaraco.ui
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
Name:           python-jaraco.ui
Version:        2.4.0
Release:        0
Summary:        User-Interface tools (mainly command-line)
License:        MIT
URL:            https://github.com/jaraco/jaraco.ui
Source:         https://files.pythonhosted.org/packages/source/j/jaraco.ui/jaraco_ui-%{version}.tar.gz
BuildRequires:  %{python_module named}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module setuptools_scm >= 3.4.1}
BuildRequires:  %{python_module typer}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module jaraco.classes}
BuildRequires:  %{python_module jaraco.text}
BuildRequires:  %{python_module pytest >= 3.5}
# /SECTION
BuildRequires:  fdupes
Requires:       python-jaraco.classes
Requires:       python-jaraco.text
Requires:       python-named
Requires:       python-typer
BuildArch:      noarch
%python_subpackages

%description
User-Interface tools (mainly command-line)

%prep
%autosetup -p1 -n jaraco_ui-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc NEWS.rst README.rst
%license LICENSE
%{python_sitelib}/jaraco/ui
%{python_sitelib}/jaraco.ui-%{version}.dist-info

%changelog
