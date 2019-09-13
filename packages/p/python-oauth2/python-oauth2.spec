#
# spec file for package python-oauth2
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


%define modname oauth2
%{?!python_module:%define python_module() python-%{**} python3-%{**}}

Name:           python-%{modname}
Version:        1.9.0.post1
Release:        0
Summary:        A fully tested, abstract interface to creating OAuth clients and servers
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/joestump/python-oauth2
Source:         https://files.pythonhosted.org/packages/source/o/oauth2/%{modname}-%{version}.tar.gz
Patch0:         oauth2-drop-tests-with-net-access.patch
Patch1:         hidePythonRequires.patch
Patch2:         addTestPath.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Test requirements:
BuildRequires:  %{python_module httplib2}
BuildRequires:  %{python_module mock}
BuildArch:      noarch
Requires:       python-httplib2
%python_subpackages

%description
This code was originally forked from Leah Culver and Andy Smith's oauth.py code.
Some of the tests come from a fork by Vic Fryzel, while a revamped Request
class and more tests were merged in from Mark Paschal's fork. After a hiatus
the project was taken over by Daniel Holmes the current maintainer

%prep
%setup -q -n %{modname}-%{version}
%patch0
%patch1
%patch2

%build
%python_build

%install
%python_install
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} $python tests/test_oauth.py

%files %{python_files}
%{python_sitelib}/oauth2*

%changelog
