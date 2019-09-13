#
# spec file for package python-simpleeval
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2015 Dr. Axel Braun
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
%define modname simpleeval
Name:           python-%{modname}
Version:        0.9.8
Release:        0
Summary:        A simple, safe single expression evaluator library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/danthedeckie/simpleeval
Source0:        https://files.pythonhosted.org/packages/source/s/simpleeval/%{modname}-%{version}.tar.gz
# https://github.com/danthedeckie/simpleeval/issues/55
Source1:        https://raw.githubusercontent.com/danthedeckie/simpleeval/master/LICENCE
BuildRequires:  %{python_module setuptools}
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
rm -f %{modname}.egg-info/*.orig
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
rm -rf %{buildroot}%{python_sitelib}/%{mod2nam}/tests # Don't install tests
rm -rf %{buildroot}%{python_sitelib}/%{mod2nam}/*.exe # Remove unneeded files

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENCE
%{python_sitelib}/*

%changelog
