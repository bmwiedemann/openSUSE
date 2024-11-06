#
# spec file for package python-tinyhtml5
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
Name:           python-tinyhtml5
Version:        2.0.0
Release:        0
Summary:        HTML parser based on the WHATWG HTML specification
License:        MIT
URL:            None
Source:         https://files.pythonhosted.org/packages/source/t/tinyhtml5/tinyhtml5-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module flit-core >= 3.2}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module webencodings >= 0.5.1}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module ruff}
# /SECTION
BuildRequires:  fdupes
Requires:       python-webencodings >= 0.5.1
Suggests:       python-sphinx
Suggests:       python-sphinx_rtd_theme
BuildArch:      noarch
%python_subpackages

%description
**A tiny HTML5 parser**

tinyhtml5 is a HTML5 parser that transforms a possibly malformed HTML document
into an ElementTree tree.

This module is a simplified fork of html5lib, written and maintained by James
Graham, Sam Sneddon, Łukasz Langa and Will Kahn-Greene.

* Free software: MIT license
* For Python 3.9+, tested on CPython and PyPy
* Documentation: https://doc.courtbouillon.org/tinyhtml5
* Changelog: https://github.com/CourtBouillon/tinyhtml5/releases
* Code, issues, tests: https://github.com/CourtBouillon/tinyhtml5
* Code of conduct: https://www.courtbouillon.org/code-of-conduct
* Professional support: https://www.courtbouillon.org
* Donation: https://opencollective.com/courtbouillon

Copyrights are retained by their contributors, no copyright assignment is
required to contribute to tinyhtml5. Unless explicitly stated otherwise, any
contribution intentionally submitted for inclusion is licensed under the MIT
license, without any additional terms or conditions. For full authorship
information, see the version control history.


%prep
%autosetup -p1 -n tinyhtml5-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/tinyhtml5
%{python_sitelib}/tinyhtml5-%{version}.dist-info

%changelog
