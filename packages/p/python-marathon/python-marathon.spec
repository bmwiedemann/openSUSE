#
# spec file for package python-marathon
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
Name:           python-marathon
Version:        0.13.0
Release:        0
Summary:        Marathon Client Library
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/thefactory/marathon-python
Source:         https://files.pythonhosted.org/packages/source/m/marathon/marathon-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-requests >= 2.4.0
Requires:       python-requests-toolbelt >= 0.4.0
BuildArch:      noarch
%python_subpackages

%description
Python interface to the Mesos Marathon REST API.

%prep
%setup -q -n marathon-%{version}

%build
%python_build

%install
%python_install

%check
# requires Docker and Marathon server installed there

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
