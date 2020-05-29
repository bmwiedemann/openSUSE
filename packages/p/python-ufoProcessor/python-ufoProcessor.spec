#
# spec file for package python-ufoProcessor
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
Name:           python-ufoProcessor
Version:        1.9.0
Release:        0
Summary:        Read, write and generate UFOs with designspace data
License:        MIT
URL:            https://github.com/LettError/ufoProcessor
Source:         https://files.pythonhosted.org/packages/source/u/ufoProcessor/ufoProcessor-%{version}.zip
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-FontTools >= 3.32.0
Requires:       python-defcon >= 0.6.0
Requires:       python-fontMath >= 0.4.9
Requires:       python-fontParts >= 0.8.2
Requires:       python-fontPens >= 0.1.0
Requires:       python-lxml >= 4.0
Requires:       python-mutatorMath >= 2.1.2
Requires:       python-unicodedata2 >= 13.0
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module FontTools >= 3.32.0}
BuildRequires:  %{python_module defcon >= 0.6.0}
BuildRequires:  %{python_module fontMath >= 0.4.9}
BuildRequires:  %{python_module fontParts >= 0.8.2}
BuildRequires:  %{python_module fontPens >= 0.1.0}
BuildRequires:  %{python_module lxml >= 4.0}
BuildRequires:  %{python_module mutatorMath >= 2.1.2}
BuildRequires:  %{python_module unicodedata2 >= 13.0}
# /SECTION
%python_subpackages

%description
Read, write and generate UFOs with designspace data.

%prep
%setup -q -n ufoProcessor-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=./Lib $python Tests/tests.py

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
