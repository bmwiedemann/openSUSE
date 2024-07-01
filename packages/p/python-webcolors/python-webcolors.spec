#
# spec file for package python-webcolors
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
Name:           python-webcolors
Version:        24.6.0
Release:        0
Summary:        Support for color names and value formats defined by the HTML
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/ubernostrum/webcolors
Source:         https://files.pythonhosted.org/packages/source/w/webcolors/webcolors-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# test requirements
BuildRequires:  %{python_module pytest}
BuildArch:      noarch
%python_subpackages

%description
Webcolors is a simple Python module for working with HTML/CSS
color definitions.

Support is included for normalizing and converting between the
following formats (RGB colorspace only; conversion to/from HSL can be
handled by the ``colorsys`` module in the Python standard library):

* Specification-defined color names
* Six-digit hexadecimal
* Three-digit hexadecimal
* Integer ``rgb()`` triplet
* Percentage ``rgb()`` triplet

Implementations are also provided for the HTML5 color parsing and
serialization algorithms.

Full documentation is `available online <http://webcolors.readthedocs.org/>`_.

%prep
%setup -q -n webcolors-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test only the standard testsuite (python3 setup.py test launched two extra tests, one of them was unable to access the internet)
%pytest tests

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/webcolors
%{python_sitelib}/webcolors-%{version}.dist-info

%changelog
