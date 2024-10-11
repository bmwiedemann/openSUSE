#
# spec file for package python-textile
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
Name:           python-textile
Version:        4.0.3
Release:        0
Summary:        Textile processing for python
License:        BSD-3-Clause
URL:            https://github.com/textile/python-textile
Source:         https://files.pythonhosted.org/packages/source/t/textile/textile-%{version}.tar.gz
BuildRequires:  %{python_module html5lib >= 1.0.1}
BuildRequires:  %{python_module nh3}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module regex >= 1.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-nh3
Requires:       python-regex
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This is a Python implementation of the Textile
(http://textism.com/tools/textile) markup language.

Textile is a XHTML generator using a simple markup developed by Dean
Allen. This is a Python port with support for code validation, itex to
MathML translation, Python code coloring and much more.

%prep
%setup -q -n textile-%{version}

%build
%pyproject_wheel

%check
rm pytest.ini
%pytest

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pytextile
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pytextile

%postun
%python_uninstall_alternative pytextile

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/textile
%{python_sitelib}/textile-%{version}.dist-info
%python_alternative %{_bindir}/pytextile

%changelog
