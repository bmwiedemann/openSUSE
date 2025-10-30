#
# spec file for package python-simpleeval
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2015-2024 Dr. Axel Braun
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


%define modname simpleeval
%{?sle15_python_module_pythons}
Name:           python-%{modname}
Version:        1.0.3
Release:        0
Summary:        A simple, safe single expression evaluator library
License:        MIT
URL:            https://github.com/danthedeckie/simpleeval
Source0:        https://files.pythonhosted.org/packages/source/s/simpleeval/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.9}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
A quick single file library for easily adding evaluatable expressions
into python projects. Say you want to allow a user to set an alarm volume,
which could depend on the time of day, alarm level, how many previous alarms
had gone off, and if there is music playing at the time.

Or if you want to allow simple formulare in a web application, but don’t want
to give full eval() access, or don’t want to run in javascript on the client side.

%prep
%setup -q -n %{modname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENCE
%{python_sitelib}/simpleeval.py
%pycache_only %{python_sitelib}/__pycache__/simpleeval*pyc
%{python_sitelib}/simpleeval-%{version}.dist-info

%changelog
