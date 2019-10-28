#
# spec file for package python-relatorio
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2016-2019 Dr. Axel Braun
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
%define         mod_name relatorio
Name:           python-relatorio
Version:        0.9.0
Release:        0
Summary:        Python module to create reports from Python objects
License:        GPL-3.0-or-later
Group:          Productivity/Office/Management
URL:            https://pypi.python.org/pypi/relatorio
Source:         https://pypi.io/packages/source/r/%{mod_name}/%{mod_name}-%{version}.tar.gz
BuildRequires:  %{python_module Genshi}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module python-magic}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Genshi
Requires:       python-PyYAML
Requires:       python-lxml
Requires:       python-pycha
Requires:       python-python-magic
BuildArch:      noarch
%python_subpackages

%description
This is a Python module to create reports from Python objects.
Output plugins to several formats are included, such
as documents (odt, ods, pdf) or images (png, svg).

%prep
%setup -q -n %{mod_name}-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README AUTHORS
%{python_sitelib}/*

%changelog
