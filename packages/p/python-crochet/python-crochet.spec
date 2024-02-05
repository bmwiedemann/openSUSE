#
# spec file for package python-crochet
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-crochet
Version:        2.1.1
Release:        0
Summary:        Use Twisted from any applications
License:        MIT
URL:            https://github.com/itamarst/crochet
Source:         https://files.pythonhosted.org/packages/source/c/crochet/crochet-%{version}.tar.gz
# PATCH-FIX-UPSTREAM gh#itamarst/crochet#150
Patch0:         update-versioneer.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted >= 16.0
Requires:       python-wrapt
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module Twisted >= 16.0}
BuildRequires:  %{python_module wrapt}
# /SECTION
%python_subpackages

%description
Crochet is an MIT-licensed library that makes it easier for blocking or
threaded applications like Flask or Django to use the Twisted networking
framework.

%prep
%autosetup -p1 -n crochet-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest

%files %{python_files}
%doc README.rst docs/*.rst
%license LICENSE
%{python_sitelib}/crochet
%{python_sitelib}/crochet-%{version}.dist-info

%changelog
