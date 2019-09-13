#
# spec file for package python-csvkit
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
Name:           python-csvkit
Version:        1.0.4
Release:        0
Summary:        A library of utilities for working with CSV
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/wireservice/csvkit
Source:         https://files.pythonhosted.org/packages/source/c/csvkit/csvkit-%{version}.tar.gz
BuildRequires:  %{python_module SQLAlchemy >= 0.9.3}
BuildRequires:  %{python_module Sphinx >= 1.0.7}
BuildRequires:  %{python_module aenum}
BuildRequires:  %{python_module agate >= 1.6.1}
BuildRequires:  %{python_module agate-dbf >= 0.2.0}
BuildRequires:  %{python_module agate-excel >= 0.2.2}
BuildRequires:  %{python_module agate-sql >= 0.5.3}
BuildRequires:  %{python_module dbf >= 0.9.3}
BuildRequires:  %{python_module et_xmlfile}
BuildRequires:  %{python_module jdcal}
BuildRequires:  %{python_module openpyxl >= 2.2.0.b1}
BuildRequires:  %{python_module python-dateutil >= 2.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.6.1}
BuildRequires:  %{python_module xlrd >= 0.9.2}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module coverage >= 3.5.1b1}
BuildRequires:  %{python_module nose >= 1.1.2} 
BuildRequires:  python-mock >= 1.3.0
# /SECTION
BuildArch:      noarch

%python_subpackages

%description
CSVkit is a library of utilities for working with CSV. It is inspired
by pdftk, gdal and the original csvcut utility by Joe Germuska and
Aaron Bycoffe.

%prep
%setup -q -n csvkit-%{version}
# find and remove unneeded shebangs
find csvkit -name "*.py" | xargs sed -i '1 {/^#!/ d}'

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
# gh#wireservice/csvkit#1027
%python_expand nosetests-%{$python_bin_suffix} -v -e 'test_(before_after_insert|linenumbers|no_header_row|unicode)'

%files %python_files
%license COPYING
%doc AUTHORS.rst CHANGELOG.rst README.rst
%python3_only %{_bindir}/*
%{python_sitelib}/csvkit-%{version}-py*.egg-info
%{python_sitelib}/csvkit/

%changelog
