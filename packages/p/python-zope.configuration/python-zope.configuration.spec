#
# spec file for package python-zope.configuration
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2013 LISA GmbH, Bingen, Germany.
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-zope.configuration%{psuffix}
Version:        4.3.1
Release:        0
Summary:        Zope Configuration Markup Language (ZCML)
License:        ZPL-2.1
Group:          Development/Languages/Python
URL:            http://www.python.org/pypi/zope.configuration
Source:         https://files.pythonhosted.org/packages/source/z/zope.configuration/zope.configuration-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-zope.i18nmessageid
Requires:       python-zope.interface
Requires:       python-zope.schema >= 4.9
BuildArch:      noarch
%if %{with test}
BuildRequires:  %{python_module manuel}
BuildRequires:  %{python_module zope.i18nmessageid}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  %{python_module zope.schema >= 4.9}
BuildRequires:  %{python_module zope.testing}
BuildRequires:  %{python_module zope.testrunner}
%endif
%python_subpackages

%description
The zope configuration system provides an extensible system for supporting
various kinds of configurations.

It is based on the idea of configuration directives. Users of the configuration
system provide configuration directives in some language that express
configuration choices. The intent is that the language be pluggable. An XML
language is provided by default.

%prep
%setup -q -n zope.configuration-%{version}
rm -rf zope.configuration.egg-info

%build
%python_build

%install
%if !%{with test}
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
%check
%python_expand PYTHONPATH=src %{_bindir}/zope-testrunner-%{$python_bin_suffix} -vvv --test-path src
%endif

%if !%{with test}
%files %{python_files}
%license LICENSE.txt
%doc CHANGES.rst COPYRIGHT.txt README.rst
%{python_sitelib}/*
%endif

%changelog
