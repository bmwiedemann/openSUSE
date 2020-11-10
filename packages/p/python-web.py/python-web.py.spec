#
# spec file for package python-web.py
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


%define skip_python2 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-web.py
Version:        0.62
Release:        0
Summary:        web.py: makes web apps
License:        SUSE-Public-Domain AND BSD-3-Clause
URL:            https://webpy.org/
Source:         https://files.pythonhosted.org/packages/source/w/web.py/web.py-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
Requires:       python-cheroot
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module cheroot}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{pythons}
# /SECTION
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

%check
%pytest

%files %{python_files}
%{python_sitelib}/*

%changelog
