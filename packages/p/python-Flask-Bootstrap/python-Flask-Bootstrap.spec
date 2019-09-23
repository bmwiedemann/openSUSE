#
# spec file for package python-Flask-Bootstrap
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

# Please submit bugfixes or comments via https://bugs.opensuse.org/
#


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-Flask-Bootstrap
Version:        3.3.7.1
Release:        0
Summary:        An extension that includes Bootstrap in your project
License:        BSD-2-Clause AND Apache-2.0
Group:          Development/Languages/Python
URL:            http://github.com/mbr/flask-bootstrap
Source:         https://github.com/mbr/flask-bootstrap/archive/%{version}.tar.gz
BuildRequires:  %{python_module Flask >= 0.8}
BuildRequires:  %{python_module dominate}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module visitor}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Flask >= 0.8
Requires:       python-dominate
Requires:       python-visitor
BuildArch:      noarch
%python_subpackages

%description
Flask-Bootstrap packages `Bootstrap
<http://getbootstrap.com>`_ into an extension that mostly consists
of a blueprint named 'bootstrap'. It can also create links to serve Bootstrap
from a CDN and works with no boilerplate code in your application.

%prep
%setup -q -n flask-bootstrap-%{version}
# pulls in flask deps we don't need here
rm tests/test_sample_app.py
# polls the web to validate it is equal
rm tests/test_versions_match.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=%{buildroot}%{$python_sitelib} py.test-%{$python_bin_suffix} -v

%files %{python_files}
%license LICENSE
%doc README.rst CHANGES
%{python_sitelib}/*

%changelog
