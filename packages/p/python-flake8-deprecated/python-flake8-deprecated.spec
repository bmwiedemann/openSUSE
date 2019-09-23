#
# spec file for package python-flake8-deprecated
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
Name:           python-flake8-deprecated
Version:        1.3
Release:        0
License:        GPL-2.0-only
Summary:        Flake8 deprecations plugin
Url:            https://github.com/gforcada/flake8-deprecated
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/f/flake8-deprecated/flake8-deprecated-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
# SECTION test requirements
BuildRequires:  %{python_module flake8 >= 3.0.0}
# /SECTION
BuildRequires:  fdupes
Requires:       python-flake8 >= 3.0.0
BuildArch:      noarch

%python_subpackages

%description
This flake8 plugin helps you keeping up with method deprecations and giving hints about what
they should be replaced with.

%prep
%setup -q -n flake8-deprecated-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE LICENSE.rst
%doc CHANGES.rst README.rst
%{python_sitelib}/*

%changelog
