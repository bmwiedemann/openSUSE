#
# spec file for package python-textile
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
%bcond_without test
Name:           python-textile
Version:        3.0.4
Release:        0
Summary:        Textile processing for python
License:        BSD-3-Clause
Group:          Development/Languages/Python
Url:            http://github.com/textile/python-textile
Source:         https://files.pythonhosted.org/packages/source/t/textile/textile-%{version}.tar.gz
Requires:       python-Pillow
Requires:       python-html5lib >= 0.999999999
Requires:       python-six
Recommends:     python-regex
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
%if %{with test}
# not needed as the test requires internet connection
#BuildRequires:  %%{python_module Pillow}
BuildRequires:  %{python_module html5lib >= 0.999999999}
%endif
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

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
%python_build

%if %{with test}
%check
%python_exec setup.py test
%endif

%install
%python_install
%fdupes %buildroot

%files %{python_files}
%defattr(-,root,root,-)
%{python_sitelib}/*
%python3_only %{_bindir}/pytextile

%changelog
