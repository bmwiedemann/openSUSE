#
# spec file for package python-manuel
#
# Copyright (c) 2021 SUSE LLC
# Copyright (c) 2013-2018 LISA GmbH, Bingen, Germany.
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
Name:           python-manuel
Version:        1.10.1
Release:        0
Summary:        Python module to build tested documentation
License:        Apache-2.0
URL:            https://pypi.org/project/manuel/
Source:         https://files.pythonhosted.org/packages/source/m/manuel/manuel-%{version}.tar.gz
# add fixed sphinx config <hpj@urpla.net>
Source1:        conf.py
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-six
BuildArch:      noarch
# SECTION Documentation requirements:
BuildRequires:  python3-Sphinx
# /SECTION
# SECTION Testing requirements:
BuildRequires:  %{python_module zope.testing}
# /SECTION
%python_subpackages

%description
Manuel lets the user build tested documentation.

Documentation, a full list of included plug-ins, and examples are available
with the -doc package and at http://packages.python.org/manuel/.

%package        doc
Summary:        Build tested documentation

%description    doc
This package contains documentation files for %{name}.

%prep
%setup -q -n manuel-%{version}
cp %{SOURCE1} .

%build
%python_build
%{python_expand # build docs only one time with primary python3 flavor
if [ $(which $python) -ef $(which python3) ]; then
  $python setup.py build_sphinx
  rm build/sphinx/html/.buildinfo
fi
}

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest src/manuel/tests.py

%files %{python_files}
%license LICENSE.rst
%doc CHANGES.rst COPYRIGHT.rst PKG-INFO README.rst
%{python_sitelib}/manuel
%{python_sitelib}/manuel-%{version}*-info

%files %{python_files doc}
%doc build/sphinx/html

%changelog
