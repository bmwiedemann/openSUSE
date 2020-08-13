#
# spec file for package python-pygaljs
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
Name:           python-pygaljs
Version:        1.0.2
Release:        0
Summary:        Python package providing assets pygaljs
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/ionelmc/python-pygaljs
Source:         https://files.pythonhosted.org/packages/source/p/pygaljs/pygaljs-%{version}.tar.gz
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Python package providing assets from https://github.com/Kozea/pygal.js

%prep
%setup -q -n pygaljs-%{version}
sed -i -e 's/\[pytest\]/\[tools:pytest\]/g' setup.cfg

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc CHANGELOG.rst README.rst
%{python_sitelib}/*

%changelog
