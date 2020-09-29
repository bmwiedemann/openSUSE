#
# spec file for package python-tinydb
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
Name:           python-tinydb
Version:        4.1.1
Release:        0
Summary:        A document-oriented database
License:        MIT
Group:          Productivity/Databases/Servers
URL:            https://github.com/msiemens/tinydb
Source:         https://files.pythonhosted.org/packages/source/t/tinydb/tinydb-%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module pytest-runner}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
TinyDB is a document oriented database written in
pure Python and has no external dependencies.
The target are small apps that would be “blown away” by a SQL-DB or an
external database server.

%prep
%setup -q -n tinydb-%{version}
sed -i '/pytest-cov/d' setup.py
chmod a-x LICENSE
dos2unix LICENSE

# Disable broken ujson support
# https://github.com/msiemens/tinydb/issues/262
sed -i 's/ujson/ujson_is_broken/' tinydb/storages.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst
%{python_sitelib}/tinydb*

%changelog
