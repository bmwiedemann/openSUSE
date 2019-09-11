#
# spec file for package python-oct2py
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


%bcond_with     test

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define         skip_python2 1
Name:           python-oct2py
Version:        5.0.4
Release:        0
Summary:        Python to GNU Octave bridge
License:        MIT
Group:          Development/Languages/Python
Url:            http://github.com/blink1073/oct2py
Source:         https://files.pythonhosted.org/packages/source/o/oct2py/oct2py-%{version}.tar.gz
BuildRequires:  %{python_module numpy >= 1.12}
BuildRequires:  %{python_module octave-kernel >= 0.30}
BuildRequires:  %{python_module scipy >= 0.17}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
Requires:       python-numpy >= 1.12
Requires:       python-octave-kernel >= 0.30
Requires:       python-scipy >= 0.17
BuildArch:      noarch

%python_subpackages

%description
Oct2Py allows you to seamlessly call M-files and Octave functions from Python.
It manages the Octave session for you, sharing data behind the scenes using
MAT files.

%prep
%setup -q -n oct2py-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

# Tests need gui
# %%check
# %%python_exec setup.py test
# %%endif

%files %{python_files}
%doc README.rst
%license LICENSE.txt licenses licenses/mlabwrap.txt licenses/octavemagic.txt licenses/ompc.txt
%{python_sitelib}/*

%changelog
