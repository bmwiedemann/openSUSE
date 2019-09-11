#
# spec file for package python-Flask-Paranoid
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Flask-Paranoid
Version:        0.2.0
Release:        0
License:        MIT
Summary:        Flask user session protection
Url:            http://github.com/miguelgrinberg/flask-paranoid/
Group:          Development/Languages/Python
# Pypi sources don't include tests
#Source:         https://files.pythonhosted.org/packages/source/F/Flask-Paranoid/Flask-Paranoid-%%{version}.tar.gz
Source:         https://github.com/miguelgrinberg/flask-paranoid/archive/v0.2.tar.gz
Source99:       https://raw.githubusercontent.com/miguelgrinberg/flask-paranoid/master/LICENSE
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
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
%setup -q -n flask-paranoid-0.2
cp %{SOURCE99} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
