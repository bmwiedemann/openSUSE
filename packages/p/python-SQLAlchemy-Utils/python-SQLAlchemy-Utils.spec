#
# spec file for package python-SQLAlchemy-Utils
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
Name:           python-SQLAlchemy-Utils
Version:        0.36.5
Release:        0
Summary:        Various utility functions for SQLAlchemy
License:        BSD-3-Clause
URL:            https://github.com/kvesteri/sqlalchemy-utils
Source:         https://files.pythonhosted.org/packages/source/S/SQLAlchemy-Utils/SQLAlchemy-Utils-%{version}.tar.gz
BuildRequires:  %{python_module Babel >= 1.3}
BuildRequires:  %{python_module SQLAlchemy >= 1.0}
BuildRequires:  %{python_module anyjson >= 0.3.3}
BuildRequires:  %{python_module arrow >= 0.3.4}
BuildRequires:  %{python_module colour >= 0.0.4}
BuildRequires:  %{python_module cryptography >= 0.6}
BuildRequires:  %{python_module flexmock >= 0.9.7}
BuildRequires:  %{python_module furl >= 0.4.1}
BuildRequires:  %{python_module intervals >= 0.7.1}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module passlib >= 1.6}
BuildRequires:  %{python_module phonenumbers >= 5.9.2}
BuildRequires:  %{python_module pytest >= 2.7.1}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module pytz >= 2014.2}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-SQLAlchemy >= 1.0
Requires:       python-six
Recommends:     python-Babel >= 1.3
Recommends:     python-anyjson >= 0.3.3
Recommends:     python-arrow >= 0.3.4
Recommends:     python-colour >= 0.0.4
Recommends:     python-cryptography >= 0.6
Recommends:     python-dateutil
Recommends:     python-furl >= 0.4.1
Recommends:     python-intervals >= 0.7.1
Recommends:     python-passlib >= 1.6
Recommends:     python-phonenumbers >= 5.9.2
BuildArch:      noarch
%python_subpackages

%description
Various utility functions and custom data types for SQLAlchemy.

%prep
%setup -q -n SQLAlchemy-Utils-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# requires initialized pgsql database
#%%pytest

%files %{python_files}
%license LICENSE
%doc README.rst
%dir %{python_sitelib}/sqlalchemy_utils
%{python_sitelib}/sqlalchemy_utils/*
%{python_sitelib}/SQLAlchemy_Utils-%{version}-py*.egg-info

%changelog
