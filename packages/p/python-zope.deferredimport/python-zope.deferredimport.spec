#
# spec file for package python-zope.deferredimport
#
# Copyright (c) 2025 SUSE LLC and contributors
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
Name:           python-zope.deferredimport
Version:        6.0
Release:        0
Summary:        On-demand import name resolver
License:        ZPL-2.1
URL:            https://github.com/zopefoundation/zope.deferredimport
Source:         https://files.pythonhosted.org/packages/source/z/zope.deferredimport/zope_deferredimport-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zope.proxy}
BuildRequires:  %{python_module zope.testrunner}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-setuptools
Requires:       python-zope.proxy
BuildArch:      noarch
%python_subpackages

%description
Often, especially for package modules, you want to import names for
convenience, but not actually perform the imports until necessary.
The zope.deferredimport package provided facilities for defining names
in modules that will be imported from somewhere else when used.  You
can also cause deprecation warnings to be issued when a variable is
used.

Documentation is hosted at https://zopedeferredimport.readthedocs.io/

%prep
%setup -q -n zope_deferredimport-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=src %{_bindir}/zope-testrunner-%{$python_bin_suffix} -vvv --test-path src

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/zope/deferredimport
%{python_sitelib}/zope[_.]deferredimport-%{version}.dist-info

%changelog
