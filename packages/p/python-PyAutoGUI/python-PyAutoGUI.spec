#
# spec file for package python-PyAutoGUI
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-PyAutoGUI
Version:        0.9.36
Release:        0
Summary:        A Python module for GUI automation that can control the keyboard and mouse
License:        BSD-3-Clause
URL:            https://github.com/asweigart/pyautogui
Source:         https://files.pythonhosted.org/packages/source/P/PyAutoGUI/PyAutoGUI-%{version}.tar.gz
Source99:       https://raw.githubusercontent.com/asweigart/pyautogui/master/LICENSE.txt
BuildRequires:  %{python_module python-xlib}
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-PyMsgBox
Requires:       python-PyScreeze
Requires:       python-PyTweening >= 1.0.1
Requires:       python-python-xlib
BuildArch:      noarch
%python_subpackages

%description
PyAutoGUI is a GUI automation Python module. It can be used to
programmatically control the mouse and keyboard.

%prep
%setup -q -n PyAutoGUI-%{version}
cp %{SOURCE99} .
# pyautogui can't be imported without a DISPLAY, so we force the version on setup.py
sed -i -e "s/version=__import__('pyautogui').__version__,/version='%{version}',/" setup.py
dos2unix README.md

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/*

%changelog
