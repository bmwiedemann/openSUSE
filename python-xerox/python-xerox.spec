#
# spec file for package python-xerox
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
#%%define skip_python2 1
Name:           python-xerox
Version:        0.4.1
Release:        0
License:        MIT
Summary:        Simple Copy + Paste in Python
Url:            http://github.com/kennethreitz/xerox
Group:          Development/Languages/Python
Source:         https://files.pythonhosted.org/packages/source/x/xerox/xerox-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  xclip
BuildRequires:  xvfb-run
Requires:       xclip
BuildArch:      noarch

%python_subpackages

%description
Python copy and paste library supporting OS X, X11 (Linux, BSD, etc.), and Windows.

%prep
%setup -q -n xerox-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand xvfb-run $python -m pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%python3_only %{_bindir}/xerox
%{python_sitelib}/*

%changelog
