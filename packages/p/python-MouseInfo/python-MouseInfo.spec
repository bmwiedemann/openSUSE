#
# spec file for package python-MouseInfo
#
# Copyright (c) 2020 SUSE LLC
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
Name:           python-MouseInfo
Version:        0.1.3
Release:        0
Summary:        Display XY position and RGB color information for pixels
License:        GPL-3.0-or-later
Group:          Development/Languages/Python
URL:            https://github.com/asweigart/mouseinfo
Source:         https://files.pythonhosted.org/packages/source/M/MouseInfo/MouseInfo-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/asweigart/mouseinfo/master/LICENSE.txt
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module pyperclip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Pillow
Requires:       python-pyperclip
BuildArch:      noarch
%python_subpackages

%description
This application to display XY position and RGB color information for the pixel
currently under the mouse. Works on Python 2 and 3. This is useful for GUI
automation planning.

%prep
%setup -q -n MouseInfo-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license LICENSE.txt
%{python_sitelib}/*

%changelog
