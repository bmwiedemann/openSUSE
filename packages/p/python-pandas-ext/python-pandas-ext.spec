#
# spec file for package python-pandas-ext
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
%define         skip_python2 1
Name:           python-pandas-ext
Version:        0.5.1
Release:        0
Summary:        Extensions for pandas dataframes
License:        MIT
URL:            https://github.com/newsela/pandas_ext
Source:         https://files.pythonhosted.org/packages/source/p/pandas_ext/pandas_ext-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Jinja2 >= 2.10
Requires:       python-pandas >= 0.22
Requires:       python-requests >= 2.20.0
Requires:       python-s3fs >= 0.1.5
Requires:       python-setuptools >= 41.0.1
Recommends:     python-openpyxl
Recommends:     python-pyarrow
Recommends:     python-snowflake-sqlalchemy
Recommends:     python-xlsxwriter
Recommends:     python-xlwt
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 2.10}
BuildRequires:  %{python_module pandas >= 0.22}
BuildRequires:  %{python_module requests >= 2.20.0}
BuildRequires:  %{python_module s3fs >= 0.1.5}
# /SECTION
%python_subpackages

%description
Python Pandas extensions for pandas dataframes.

%prep
%setup -q -n pandas_ext-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
