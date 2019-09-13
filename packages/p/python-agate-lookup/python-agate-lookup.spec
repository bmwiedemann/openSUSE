#
# spec file for package python-agate-lookup
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%bcond_with     test
Name:           python-agate-lookup
Version:        0.3.1
Release:        0
License:        MIT
Summary:        Remote lookup tables for agate
Url:            http://agate-lookup.readthedocs.org/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/a/agate-lookup/agate-lookup-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/wireservice/agate-lookup/%{version}/COPYING
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module agate >= 1.5.0}
BuildRequires:  %{python_module PyYAML >= 3.11}
BuildRequires:  %{python_module requests >= 2.9.1}
%endif
Requires:       python-agate >= 1.5.0
Requires:       python-PyYAML >= 3.11
Requires:       python-requests >= 2.9.1
BuildArch:      noarch

%python_subpackages

%description
Agate-lookup adds one-line access to lookup tables to agate.

%prep
%setup -q -n agate-lookup-%{version}
cp %{SOURCE10} .
sed -i -e '/^#!\//, 1d' agatelookup/*.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%if %{with test}
%check
%python_exec setup.py test
%endif

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license COPYING
%{python_sitelib}/*

%changelog
