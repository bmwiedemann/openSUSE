#
# spec file for package python-pynput
#
# Copyright (c) 2023 SUSE LLC
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

Name:           python-pynput
Version:        1.7.6
Release:        0
Summary:        Monitor and control user input devices
License:        LGPL-3.0-only
URL:            https://github.com/moses-palmer/pynput
Source:         https://files.pythonhosted.org/packages/source/p/pynput/pynput-%{version}.tar.gz
BuildRequires:  %{python_module Sphinx >= 1.3.1}
BuildRequires:  %{python_module pip}
# this is part of the auto generated spec file, but opensuse
# BuildRequires:  %%{python_module setuptools-lint >= 0.5}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module evdev}
BuildRequires:  %{python_module python-xlib}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
# /SECTION
BuildRequires:  fdupes
Requires:       python-evdev >= 1.3
Requires:       python-six
Suggests:       python-enum34
Suggests:       python-pyobjc-framework-ApplicationServices >= 8.0
Suggests:       python-pyobjc-framework-Quartz >= 8.0
BuildArch:      noarch
%python_subpackages

%description
Monitor and control user input devices

%prep
%autosetup -p1 -n pynput-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.rst
%license COPYING.LGPL
%{python_sitelib}/pynput
%{python_sitelib}/pynput-%{version}.dist-info

%changelog
