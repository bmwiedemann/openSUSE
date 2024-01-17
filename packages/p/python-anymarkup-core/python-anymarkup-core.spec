#
# spec file for package python-anymarkup-core
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020 SUSE Software Solutions Germany GmbH.
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
Name:           python-anymarkup-core
Version:        0.8.1
Release:        0
Summary:        Core library for anymarkup
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/bkabrda/anymarkup-core
Source0:        https://github.com/bkabrda/anymarkup-core/archive/v%{version}/anymarkup-core-%{version}.tar.gz
Patch0:         xml-to-dict-0.13.patch
# PATCH-FIX-UPSTREAM drop-python2-support.patch gh#bkabrda/anymarkup-core#7
Patch1:         drop-python2-support.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Suggests:       python-PyYAML
Suggests:       python-configobj
Suggests:       python-json5
Suggests:       python-toml
Suggests:       python-xmltodict
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module configobj}
BuildRequires:  %{python_module flexmock}
BuildRequires:  %{python_module json5}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module xmltodict}
# /SECTION
%python_subpackages

%description
This is the core library that implements functionality of
python-anymarkup.

%prep
%autosetup -p1 -n anymarkup-core-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/anymarkup_core
%{python_sitelib}/anymarkup_core-%{version}*-info

%changelog
