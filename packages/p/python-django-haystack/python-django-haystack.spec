#
# spec file for package python-django-haystack
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
Name:           python-django-haystack
Version:        2.8.1
Release:        0
Summary:        Pluggable search for Django
License:        BSD-3-Clause
URL:            https://haystacksearch.org/
Source:         https://files.pythonhosted.org/packages/source/d/django-haystack/django-haystack-%{version}.tar.gz
#PATCH-FIX-UPSTREAM using six replace django six 
Patch0:         django3-support.patch
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Django >= 1.11
Requires:       python-six >= 1.12.0
Suggests:       python-Whoosh >= 2.5.4
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Django >= 1.11}
BuildRequires:  %{python_module GDAL}
BuildRequires:  %{python_module Whoosh >= 2.5.4}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module elasticsearch}
BuildRequires:  %{python_module geopy >= 0.95.1}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module nose}
BuildRequires:  %{python_module pysolr}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module six >= 1.12.0}
# /SECTION
%python_subpackages

%description
Pluggable search for Django.

%prep
%setup -q -n django-haystack-%{version}
%patch0 -p1

%build
sed -i 's:==:>=:' setup.py
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# skip test_rebuild_index_nocommit, django-admin.py does not have rebuild_index command
sed -i 's/\(.*from mock import.*\)/from unittest import skip\n\1/' test_haystack/test_management_commands.py
sed -i 's/\(.*def test_rebuild_index_nocommit.*\)/    @skip("disable because it is broken")\n\1/' test_haystack/test_management_commands.py
%python_exec test_haystack/run_tests.py

%files %{python_files}
%doc AUTHORS README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
