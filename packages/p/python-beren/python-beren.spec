#
# spec file for package python-beren
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2019 Dr. Axel Braun <DocB@opensuse.org>
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

%define modname beren
Name:           python-%{modname}
Version:        0.6.2
Release:        0
Summary:        Provides a REST client targeted at Orthanc REST API endpoints
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/teffalump/beren
Source:         https://files.pythonhosted.org/packages/source/b/%{modname}/%{modname}-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module apiron >= 2.5.0 }
BuildRequires:  fdupes

Requires:       python-apiron >= 2.5.0

%python_subpackages

%description
python-beren provides a REST client targeted at Orthanc REST API endpoints

%prep
%setup -q -n %{modname}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{python_sitelib}

%files %{python_files}
%license LICENSE
%doc README.md
%{python3_sitelib}/*

%changelog
