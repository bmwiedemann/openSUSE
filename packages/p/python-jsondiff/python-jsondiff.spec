#
# spec file for package python-jsondiff
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
Name:           python-jsondiff
Version:        2.2.0
Release:        0
Summary:        Module to diff JSON and JSON-like structures in Python
License:        MIT
URL:            https://github.com/ZoomerAnalytics/jsondiff
Source:         https://files.pythonhosted.org/packages/source/j/jsondiff/jsondiff-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module hypothesis}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Package to show differences between JSON and JSON-like structures in Python

%prep
%autosetup -p1 -n jsondiff-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/jdiff
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative jdiff

%postun
%python_uninstall_alternative jdiff

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/jsondiff
%{python_sitelib}/jsondiff-%{version}.dist-info
%python_alternative %{_bindir}/jdiff

%changelog
