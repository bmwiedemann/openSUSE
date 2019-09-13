#
# spec file for package python-tkreadonly
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-tkreadonly
Version:        0.6.1
Release:        0
License:        BSD-3-Clause
Summary:        A set of Tkinter widgets to display readonly text and code
Url:            http://github.org/pybee/tkreadonly
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/t/tkreadonly/tkreadonly-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module idle}
BuildRequires:  %{python_module tk}
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module Pygments >= 1.5}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Pygments >= 1.5
Requires:       python-idle
Requires:       python-tk
BuildArch:      noarch

%python_subpackages

%description
A set of Tkinter widgets to display readonly text and code.

%prep
%setup -q -n tkreadonly-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/*

%changelog
