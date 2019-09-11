#
# spec file for package python-jinja2-fsloader
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
Name:           python-jinja2-fsloader
Version:        0.1.1
Release:        0
Summary:        Jinja2 template loader using PyFilesystem2
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/althonos/jinja2-fsloader/
Source:         https://files.pythonhosted.org/packages/source/j/jinja2-fsloader/jinja2-fsloader-%{version}.zip
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-Jinja2 >= 2.0
Requires:       python-fs >= 2.1.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Jinja2 >= 2.0}
BuildRequires:  %{python_module contexter >= 0.1.4}
BuildRequires:  %{python_module fs >= 2.1.0}
BuildRequires:  %{python_module mock}
# /SECTION
%python_subpackages

%description
Jinja2 template loader using PyFilesystem2.

%prep
%setup -q -n jinja2-fsloader-%{version}
sed -i 's/,<[0-9.]*$//' setup.cfg

%build
%python_build

%install
%python_install
%{python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%fdupes %{buildroot}%{$python_sitelib}
}

%check
%python_exec setup.py test

%files %{python_files}
%license COPYING
%doc README.rst
%{python_sitelib}/*

%changelog
