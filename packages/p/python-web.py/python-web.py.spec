#
# spec file for package python-web.py
#
# Copyright (c) 2025 SUSE LLC
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


Name:           python-web.py
Version:        0.62
Release:        0
Summary:        web.py: makes web apps
License:        BSD-3-Clause AND SUSE-Public-Domain
URL:            https://webpy.org/
Source:         https://files.pythonhosted.org/packages/source/w/web.py/web.py-%{version}.tar.gz
BuildRequires:  %{python_module legacy-cgi if %python-base >= 3.13}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-cheroot
%if %{python_version_nodots} >= 313
Requires:       python-legacy-cgi
%endif
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
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# gh#webpy/webpy#712
%pytest -k 'not test_routing'

%files %{python_files}
%doc README.md
%{python_sitelib}/web
%{python_sitelib}/web[_.]py-%{version}.dist-info

%changelog
