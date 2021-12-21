#
# spec file for package python-pyicumessageformat
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-pyicumessageformat
Version:        1.0.0
Release:        0
Summary:        Library for Parsing ICU MessageFormat Messages
License:        MIT
URL:            https://github.com/sirstendec/pyicumessageformat
Source0:        https://files.pythonhosted.org/packages/source/p/pyicumessageformat/pyicumessageformat-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
An unopinionated library for parsing ICU MessageFormat messages
into both ASTs and, optionally, token lists.

This library is mainly a re-implementation of the JavaScript library
format-message-parse with a few extra configuration flags.

%prep
%setup -q -n pyicumessageformat-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/*

%changelog
