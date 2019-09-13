#
# spec file for package python-piexif
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
Name:           python-piexif
Version:        1.1.3
Release:        0
Summary:        EXIF manipulations with python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hMatoba/Piexif
Source:         https://files.pythonhosted.org/packages/source/p/piexif/piexif-%{version}.zip
BuildRequires:  %{python_module Pillow}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
%python_subpackages

%description
EXIF manipulations with python. Writing, reading, and more.

%prep
%setup -q -n piexif-%{version}
sed -i 's/\r$//' README.rst

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%doc README.rst
%license LICENSE.txt
%dir %{python_sitelib}/piexif
%{python_sitelib}/piexif/*
%{python_sitelib}/piexif-%{version}-py*.egg-info

%changelog
