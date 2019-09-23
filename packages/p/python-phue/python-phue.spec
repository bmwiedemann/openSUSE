#
# spec file for package python-phue
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-phue
Version:        1.1
Release:        0
Summary:        Philips Hue Python library
License:        MIT
Group:          Development/Languages/Python
Url:            https://github.com/studioimaginaire/phue
# https://github.com/studioimaginaire/phue/issues/152
Source0:        https://github.com/studioimaginaire/phue/archive/1.1.tar.gz#/phue-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module fixtures}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildArch:      noarch

%python_subpackages

%description
Full featured Python library to control the Philips Hue lighting system.

%prep
%setup -q -n phue-%{version}

%build
%python_build

%check
%pytest

%install
%python_install
%{python_expand chmod a+x %{buildroot}%{$python_sitelib}/phue.py
sed -i "s|^#!/usr/bin/python$|#!%__$python|" %{buildroot}%{$python_sitelib}/phue.py
$python -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}
$python -O -m compileall -d %{$python_sitelib} %{buildroot}%{$python_sitelib}
%fdupes %{buildroot}%{$python_sitelib}
}

%files %{python_files}
%defattr(-,root,root,-)
%doc *.md
%license LICENSE
%{python_sitelib}/phue.py*
%{python_sitelib}/phue-%{version}-py*.egg-info
%pycache_only %{python_sitelib}/__pycache__/phue*.py*

%changelog
