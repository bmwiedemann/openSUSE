#
# spec file for package python-blurb
#
# Copyright (c) 2021 SUSE LLC
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
Name:           python-blurb
Version:        1.0.8
Release:        0
Summary:        Command-line tool to manage CPython Misc/NEWS.d entries
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/python/core-workflow/tree/master/blurb
Source:         https://files.pythonhosted.org/packages/source/b/blurb/blurb-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.5}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Command-line tool to manage CPython Misc/NEWS.d entries.

%prep
%setup -q -n blurb-%{version}

%build
%python_build

%check
mkdir blurb
mv tests blurb
%pytest blurb.py

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%{python_sitelib}/*

%changelog
