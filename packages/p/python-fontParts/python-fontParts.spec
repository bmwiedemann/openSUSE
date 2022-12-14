#
# spec file
#
# Copyright (c) 2022 SUSE LLC
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


%global flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "test"
%define psuffix -test
%bcond_without test
%else
%define psuffix %{nil}
%bcond_with test
%endif
%define skip_python2 1
%define skip_python36 1
Name:           python-fontParts%{psuffix}
Version:        0.11.0
Release:        0
Summary:        API for interacting with the parts of fonts
License:        MIT
URL:            https://github.com/robotools/fontParts
Source:         https://files.pythonhosted.org/packages/source/f/fontParts/fontParts-%{version}.zip
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
# install_requires = [FontTools[ufo,lxml,unicode]
Requires:       python-FontTools >= 4.28.5
Requires:       python-fs >= 2.2.0
Requires:       python-lxml >= 4.0
%if %python_version_nodots < 39
Requires:       python-unicodedata2
%endif
Requires:       python-booleanOperations >= 0.9.0
Requires:       python-defcon >= 0.10.0
Requires:       python-fontMath >= 0.9.1
BuildArch:      noarch
%if %{with test}
# SECTION test requirements
BuildRequires:  %{python_module FontTools >= 4.28.5}
BuildRequires:  %{python_module booleanOperations >= 0.9.0}
BuildRequires:  %{python_module defcon >= 0.10.0}
BuildRequires:  %{python_module fontMath >= 0.9.1}
BuildRequires:  %{python_module fontPens >= 0.2.4}
BuildRequires:  %{python_module fs >= 2.2.0}
BuildRequires:  %{python_module lxml >= 4.0}
BuildRequires:  %{python_module unicodedata2 if %python-base < 3.9}
# /SECTION
%endif
%python_subpackages

%description
An API for interacting with the parts of fonts during the font development process.

%prep
%setup -q -n fontParts-%{version}

%build
export LANG=C.UTF-8
%python_build

%install
%if !%{with test}
export LANG=C.UTF-8
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%endif

%if %{with test}
# fontParts tests requires fontPens and fontPens' tests require fontParts
%check
export LANG=C.UTF-8
export PYTHONDONTWRITEBYTECODE=1
%python_expand PYTHONPATH=./Lib $python Lib/fontParts/fontshell/test.py
%endif

%if !%{with test}
%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/fontParts
%{python_sitelib}/fontParts-%{version}*-info
%endif

%changelog
