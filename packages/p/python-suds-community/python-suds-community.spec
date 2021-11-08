#
# spec file for package python-suds-community
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
%global skip_python2 1
Name:           python-suds-community
Version:        1.0.0
Release:        0
Summary:        Lightweight SOAP client (Jurko's fork)
License:        LGPL-3.0-or-later
Group:          Development/Languages/Python
URL:            http://bitbucket.org/community/suds
Source:         https://files.pythonhosted.org/packages/source/s/suds-community/suds-community-%{version}.tar.gz
BuildRequires:  %{python_module devel}
# Test requirements
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module xml}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Provides:       python-suds-jurko = %{version}
Obsoletes:      python-suds-jurko < %{version}
BuildArch:      noarch
%python_subpackages

%description
This is hopefully just a temporary fork of the original suds Python
library project created because the original project development seems
to have stalled. Should be reintegrated back into the original project
if it ever gets revived again.

%prep
%setup -q -n suds-community-%{version}

%build
%python_build

%install
%python_install
# remove tests/ dir from global site-packages
%python_expand rm -rf %{buildroot}/%{$python_sitelib}/tests
%python_expand %fdupes %{buildroot}/%{$python_sitelib}/suds*

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/suds
%{python_sitelib}/suds_community-%{version}-py%{python_version}.egg-info

%changelog
