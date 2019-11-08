#
# spec file for package python-PyTweening
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
Name:           python-PyTweening
Version:        1.0.3
Release:        0
Summary:        A collection of tweening / easing functions
License:        BSD-3-Clause
URL:            https://github.com/asweigart/pytweening
Source:         https://files.pythonhosted.org/packages/source/P/PyTweening/PyTweening-%{version}.zip
Source99:       https://raw.githubusercontent.com/asweigart/pytweening/master/LICENSE.txt
BuildRequires:  %{python_module setuptools}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
%python_subpackages

%description
A collection of tweening / easing functions implemented in Python.

%prep
%setup -q -n PyTweening-%{version}
cp %{SOURCE99} .
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
