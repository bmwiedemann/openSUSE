#
# spec file for package python-textile
#
# Copyright (c) 2020 SUSE LLC
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-textile
Version:        4.0.1
Release:        0
Summary:        Textile processing for python
License:        BSD-3-Clause
URL:            https://github.com/textile/python-textile
Source:         https://files.pythonhosted.org/packages/source/t/textile/textile-%{version}.tar.gz
BuildRequires:  %{python_module html5lib >= 1.0.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module regex >= 1.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-html5lib >= 1.0.1
Requires:       python-six
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-regex
%python_subpackages

%description
This is a Python implementation of the Textile
(http://textism.com/tools/textile) markup language.

Textile is a XHTML generator using a simple markup developed by Dean
Allen. This is a Python port with support for code validation, itex to
MathML translation, Python code coloring and much more.

%prep
%setup -q -n textile-%{version}
sed -i -e '/pytest-runner/d' setup.py

%build
%python_build

%check
rm pytest.ini
%pytest

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/pytextile
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative pytextile

%postun
%python_uninstall_alternative pytextile

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/*
%python_alternative %{_bindir}/pytextile

%changelog
