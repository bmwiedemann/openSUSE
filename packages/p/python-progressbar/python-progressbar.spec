#
# spec file for package python-progressbar
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


%{?sle15_python_module_pythons}
Name:           python-progressbar
Version:        2.5
Release:        0
Summary:        Text Progressbar Library for Python
License:        BSD-3-Clause OR LGPL-2.1-or-later
Group:          Development/Libraries/Python
URL:            https://github.com/niltonvolpato/python-progressbar
Source:         https://files.pythonhosted.org/packages/source/p/progressbar/progressbar-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
This library provides a text mode progressbar. This is tipically used to
display the progress of a long running operation, providing a visual clue that
processing is underway.

%prep
%setup -q -n progressbar-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%files %{python_files}
%doc README.txt examples.py
%license LICENSE.txt
%{python_sitelib}/progressbar/
%{python_sitelib}/progressbar-%{version}*-info

%changelog
