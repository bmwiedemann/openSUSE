#
# spec file for package python-shtab
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


%{?sle15_python_module_pythons}
Name:           python-shtab
Version:        1.8.0
Release:        0
Summary:        Automagic shell tab completion for Python CLI applications
License:        Apache-2.0
URL:            https://github.com/iterative/shtab
Source:         https://files.pythonhosted.org/packages/source/s/shtab/shtab-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 42}
BuildRequires:  %{python_module setuptools_scm >= 3.4}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
Requires(post): update-alternatives
Requires(postun): update-alternatives
# Section Tests
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-timeout}
BuildRequires:  %{python_module pytest}
# /Section
%python_subpackages

%description
Automagic shell tab completion for Python CLI applications

%prep
%autosetup -p1 -n shtab-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/shtab
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative shtab

%postun
%python_uninstall_alternative shtab

%files %{python_files}
%doc README.rst
%python_alternative %{_bindir}/shtab
%{python_sitelib}/shtab
%{python_sitelib}/shtab-%{version}.dist-info

%changelog
