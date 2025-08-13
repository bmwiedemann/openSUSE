#
# spec file for package python-pyupgrade
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
Name:           python-pyupgrade
Version:        3.20.0
Release:        0
Summary:        A tool to automatically upgrade syntax for newer versions
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/asottile/pyupgrade
Source:         https://github.com/asottile/pyupgrade/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module tokenize-rt >= 3.2.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-tokenize-rt >= 3.2.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch

%python_subpackages

%description
A tool to automatically upgrade syntax for newer versions of the Python
programming language.

%prep
%setup -q -n pyupgrade-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/pyupgrade

%check
%pytest

%post
%python_install_alternative pyupgrade

%postun
%python_uninstall_alternative pyupgrade

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/pyupgrade
%{python_sitelib}/pyupgrade
%{python_sitelib}/pyupgrade-%{version}.dist-info

%changelog
