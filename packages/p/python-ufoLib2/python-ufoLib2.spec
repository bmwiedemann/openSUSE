#
# spec file for package python-ufoLib2
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
Name:           python-ufoLib2
Version:        0.8.0
Release:        0
Summary:        UFO font processing library
License:        Apache-2.0
URL:            https://github.com/fonttools/ufoLib2
Source:         https://files.pythonhosted.org/packages/source/u/ufoLib2/ufoLib2-%{version}.zip
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
Requires:       python-FontTools >= 4.13.0
Requires:       python-attrs >= 19.3.0
Suggests:       python-lxml
Suggests:       python-typing_extensions
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module FontTools >= 4.0.0}
BuildRequires:  %{python_module attrs >= 19.2.0}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
ufoLib2 is a UFO font processing library.

%prep
%setup -q -n ufoLib2-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*

%changelog
