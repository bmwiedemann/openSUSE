#
# spec file for package python-flufl.i18n
#
# Copyright (c) 2021 SUSE LLC
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
%define pythons python3
Name:           python-flufl.i18n
Version:        3.2
Release:        0
Summary:        High level API for internationalizing Python libraries and applications
License:        Apache-2.0
URL:            https://flufli18n.readthedocs.io
Source:         https://files.pythonhosted.org/packages/source/f/flufl.i18n/flufl.i18n-%{version}.tar.gz
Patch0:         python-flufl.i18n-fix-setup.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module atpublic}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module six}
BuildRequires:  %{python_module sybil}
BuildRequires:  %{python_module typing_extensions}
# /SECTION
BuildRequires:  fdupes
Requires:       python-atpublic
Suggests:       python-typing_extensions
BuildArch:      noarch
%python_subpackages

%description
High level API for internationalizing Python libraries and applications.

%prep
%autosetup -n flufl.i18n-%{version} -p1

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
%{python_sitelib}/*

%changelog
