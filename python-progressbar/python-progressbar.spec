#
# spec file for package python-progressbar
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
Name:           python-progressbar
Version:        2.5
Release:        0
Summary:        Text Progressbar Library for Python
License:        LGPL-2.1-or-later OR BSD-3-Clause
Group:          Development/Libraries/Python
Url:            https://github.com/niltonvolpato/python-progressbar
Source:         https://files.pythonhosted.org/packages/source/p/progressbar/progressbar-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
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
%python_build

%install
%python_install

%files %{python_files}
%doc README.txt examples.py
%license LICENSE.txt
%{python_sitelib}/progressbar/
%{python_sitelib}/progressbar-%{version}-py*.egg-info

%changelog
