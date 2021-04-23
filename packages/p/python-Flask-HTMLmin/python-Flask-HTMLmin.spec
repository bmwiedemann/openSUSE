#
# spec file for package python-Flask-HTMLmin
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
Name:           python-Flask-HTMLmin
Version:        2.0.2
Release:        0
Summary:        Flask minifier for HTML responses
License:        BSD-3-Clause
URL:            https://github.com/hamidfzm/Flask-HTMLmin
Source:         https://github.com/hamidfzm/Flask-HTMLmin/archive/v%{version}.tar.gz
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module htmlmin}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask
Requires:       python-htmlmin
BuildArch:      noarch
%python_subpackages

%description
Flask-HTMLmin minimizes HTML rendered by Flask.

%prep
%setup -q -n Flask-HTMLmin-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%dir %{python_sitelib}/flask_htmlmin
%{python_sitelib}/flask_htmlmin/*
%{python_sitelib}/Flask_HTMLmin-%{version}-*.egg-info

%changelog
