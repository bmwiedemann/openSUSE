#
# spec file for package python-radon
#
# Copyright (c) 2022 SUSE LLC
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
Name:           python-radon
Version:        5.1.0
Release:        0
Summary:        Code Metrics in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/rubik/radon
Source:         https://files.pythonhosted.org/packages/source/r/radon/radon-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-colorama >= 0.4.1
Requires:       python-future
Requires:       python-mando >= 0.6
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module colorama >= 0.4.1}
BuildRequires:  %{python_module future}
BuildRequires:  %{python_module mando >= 0.6}
BuildRequires:  %{python_module pytest >= 2.7}
BuildRequires:  %{python_module pytest-mock}
# /SECTION
%python_subpackages

%description
Radon is a Python tool that computes various metrics from the source code.
Radon can compute:

* McCabe's complexity**, i.e. cyclomatic complexity
* raw metrics (these include SLOC, comment lines, blank lines, &c.)
* Halstead metrics (all of them)
* Maintainability Index (the one used in Visual Studio)

%prep
%setup -q -n radon-%{version}
# unpin mando
sed -i -E 's/(mando.*),<0\.7/\1/' setup.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%python_clone -a %{buildroot}%{_bindir}/radon

%check
%pytest

%post
%python_install_alternative radon

%postun
%python_uninstall_alternative radon

%files %{python_files}
%doc CHANGELOG README.rst
%license LICENSE
%python_alternative %{_bindir}/radon
%{python_sitelib}/radon
%{python_sitelib}/radon-%{version}*-info

%changelog
