#
# spec file for package python-Frozen-Flask
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
Name:           python-Frozen-Flask
Version:        0.15
Release:        0
Summary:        A Flask application into a set of static files
License:        BSD-2-Clause
Group:          Development/Languages/Python
Url:            https://github.com/Frozen-Flask/Frozen-Flask
Source:         https://files.pythonhosted.org/packages/source/F/Frozen-Flask/Frozen-Flask-%{version}.tar.gz
BuildRequires:  %{python_module Flask}
BuildRequires:  %{python_module Werkzeug}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
Requires:       python-Flask
Requires:       python-Werkzeug
BuildArch:      noarch
%python_subpackages

%description
Frozen-Flask freezes a Flask application into a set of static files.
The result can be hosted without any server-side software other than
a traditional web server.

%prep
%setup -q -n Frozen-Flask-%{version}

%build
%python_build

%install
%python_install

%check
export LANG=en_US.UTF-8
%python_exec -m flask_frozen.tests

%files %{python_files}
%defattr(-,root,root)
%doc README.rst LICENSE
%doc docs/build/html
%{python_sitelib}/flask_frozen/
%{python_sitelib}/Frozen_Flask-%{version}-py*.egg-info

%changelog
