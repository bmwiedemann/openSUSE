#
# spec file for package python-suds-jurko
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
Name:           python-suds-jurko
Version:        0.6
Release:        0
Summary:        Lightweight SOAP client (Jurko's fork)
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://bitbucket.org/jurko/suds
Source:         https://pypi.io/packages/source/s/suds-jurko/suds-jurko-%{version}.tar.bz2
# CVE-2013-2217.
# Fixed upstream in https://bitbucket.org/jurko/suds/issues/15/
Patch0:         suds-insecure-cache-tempdir.patch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
#its a lie, but lets make this pass..
Provides:       python-suds = %{version}
Obsoletes:      python-suds < %{version}
# Test requirements
BuildRequires:  %{python_module pytest}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%python_subpackages

%description
This is hopefully just a temporary fork of the original suds Python
library project created because the original project development seems
to have stalled. Should be reintegrated back into the original project
if it ever gets revived again.

%prep
%setup -q -n suds-jurko-%{version}
%patch0

%build
%python_build

%install
%python_install
# remove tests/ dir from global site-packages
%python_expand rm -rf %{buildroot}/%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/suds*

%check
#python setup.py test

%files %{python_files}
%defattr(-,root,root,-)
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/suds
%{python_sitelib}/suds_jurko-%{version}-py%{python_version}.egg-info

%changelog
