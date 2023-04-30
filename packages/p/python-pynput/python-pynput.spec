#
# spec file for package python-pynput
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

%global skip_python2 1
%global pythons %{primary_python}

%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-pynput
Version:        1.7.6
Release:        0
License:        LGPL-3.0
Summary:        Monitor and control user input devices
Url:            https://github.com/moses-palmer/pynput
Source:         https://files.pythonhosted.org/packages/source/p/pynput/pynput-%{version}.tar.gz
Patch0:         unicode.patch
Patch1:         no-setuptools-lint.patch
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six}
BuildRequires:  python3-Sphinx >= 1.3.1
# SECTION test requirements
BuildRequires:  %{python_module six}
# /SECTION
BuildRequires:  fdupes
Requires:       python-six
Suggests:       python-evdev >= 1.3
Suggests:       python-python-xlib >= 0.17
Suggests:       python-pyobjc-framework-Quartz >= 7.0
BuildArch:      noarch

%python_subpackages

%description
Monitor and control user input devices

%prep
%setup -q -n pynput-%{version}
%autopatch -p1

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING.LGPL
%doc README.rst
%{python_sitelib}/*

%changelog
