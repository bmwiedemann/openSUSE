#
# spec file for package python-ufoProcessor
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-ufoProcessor
Version:        1.14.1
Release:        0
Summary:        Read, write and generate UFOs with designspace data
License:        MIT
URL:            https://github.com/LettError/ufoProcessor
Source:         https://files.pythonhosted.org/packages/source/u/ufoprocessor/ufoprocessor-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-FontTools >= 3.32.0
Requires:       python-defcon >= 0.6.0
Requires:       python-fontMath >= 0.4.9
Requires:       python-fontParts >= 0.8.2
Requires:       python-lxml >= 4.0
Requires:       python-mutatorMath >= 2.1.2
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module FontTools >= 3.32.0}
BuildRequires:  %{python_module defcon >= 0.6.0}
BuildRequires:  %{python_module fontMath >= 0.4.9}
BuildRequires:  %{python_module fontParts >= 0.8.2}
BuildRequires:  %{python_module lxml >= 4.0}
BuildRequires:  %{python_module mutatorMath >= 2.1.2}
# /SECTION
%python_subpackages

%description
Read, write and generate UFOs with designspace data.

%prep
%setup -q -n ufoprocessor-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand PYTHONPATH=./Lib $python Tests/tests.py

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/ufoProcessor
%{python_sitelib}/ufo[Pp]rocessor-%{version}.dist-info

%changelog
