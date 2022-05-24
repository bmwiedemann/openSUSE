#
# spec file for package python-Flask-Paranoid
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python36 1

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Flask-Paranoid
Version:        0.3.0
Release:        0
License:        MIT
Summary:        Flask user session protection
URL:            http://github.com/miguelgrinberg/flask-paranoid/
Group:          Development/Languages/Python
# Pypi sources don't include tests
#Source:         https://files.pythonhosted.org/packages/source/F/Flask-Paranoid/Flask-Paranoid-%%{version}.tar.gz
Source:         https://github.com/miguelgrinberg/flask-paranoid/archive/refs/tags/v%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/miguelgrinberg/flask-paranoid/master/LICENSE
# PATCH-FIX-OPENSUSE fix-ParanoidTests-fail.patch The minus sign is removed from HTTP headers in newer Python releases.
Patch0:         fix-ParanoidTests-fail.patch
BuildRequires:  %{python_module importlib-metadata}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
# Test requirements
BuildRequires:  %{python_module Flask >= 0.10}
# End of test requirements
Requires:       python-Flask >= 0.10
BuildArch:      noarch

%python_subpackages

%description
Flask-Paranoid is an extension for the Flask framework that protects the
application against certain attacks in which the user session cookie is stolen
and then used by the attacker.

The extension generates a "paranoid" token according to the IP address and user
agent when a client connects to the flask application.

%prep
%setup -q -n flask-paranoid-%{version}
%patch0 -p1
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%if 0%{?suse_version} > 1500
%pyunittest discover -v
%else
%python_exec setup.py test
%endif

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
