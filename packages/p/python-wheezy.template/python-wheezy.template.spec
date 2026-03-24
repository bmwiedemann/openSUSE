#
# spec file for package python-wheezy.template
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
Name:           python-wheezy.template
Version:        3.2.5
Release:        0
Summary:        A lightweight template library
License:        MIT
URL:            https://github.com/akornatskyy/wheezy.template
Source:         https://files.pythonhosted.org/packages/source/w/wheezy_template/wheezy_template-%{version}.tar.gz#/wheezy.template-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 3.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools >= 61.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Suggests:       python-mock
Suggests:       python-pytest
Suggests:       python-pytest-cov
Suggests:       python-pytest-pep8
%python_subpackages

%description
A lightweight template library written in pure python.

%prep
%setup -q -n wheezy_template-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/wheezy.template
%python_expand rm %{buildroot}%{$python_sitearch}/wheezy/template/*.c
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%post
%python_install_alternative wheezy.template

%postun
%python_uninstall_alternative wheezy.template

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/wheezy.template
%dir %{python_sitearch}/wheezy
%{python_sitearch}/wheezy/template
%{python_sitearch}/wheezy_template-%{version}.dist-info

%changelog
