#
# spec file for package python-web.py
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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
#

%{?!python_module:%define python_module() python-%{**} python3-%{**}}

Name:           python-web.py
Version:        0.40
Release:        0
Url:            http://webpy.org/
Summary:        web.py: makes web apps
License:        SUSE-Public-Domain and BSD-3-Clause
Group:          Development/Languages/Python
Source:         https://pypi.io/packages/source/w/web.py/web.py-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  python-devel
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildArch:      noarch
%python_subpackages

%description
Think about the ideal way to write a web app. Write the code to make it happen.

%prep
%setup -q -n web.py-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%defattr(-,root,root,-)
%{python_sitelib}/*

%changelog
