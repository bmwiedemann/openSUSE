#
# spec file for package python-agate-remote
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
Name:           python-agate-remote
Version:        0.2.0
Release:        0
License:        MIT
Summary:        Read support for remote files for agate
Url:            http://agate-remote.readthedocs.org/
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/a/agate-remote/agate-remote-%{version}.tar.gz
Source10:       https://raw.githubusercontent.com/wireservice/agate-remote/%{version}/COPYING
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with test}
BuildRequires:  %{python_module agate >= 1.5.0}
BuildRequires:  %{python_module requests >= 2.9.1}
%endif
Requires:       python-agate >= 1.5.0
Requires:       python-requests >= 2.9.1
BuildArch:      noarch

%python_subpackages

%description
Agate-remote adds read support for remote files to agate.

%prep
%setup -q -n agate-remote-%{version}
cp %{SOURCE10} .
sed -i -e '/^#!\//, 1d' agateremote/*.py

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
