#
# spec file for package python-sphinx-argparse
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-sphinx-argparse
Version:        0.3.1
Release:        0
Summary:        Sphinx extension to document argparse commands and options
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/ashb/sphinx-argparse
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx-argparse/sphinx-argparse-%{version}.tar.gz
# https://github.com/ashb/sphinx-argparse/commit/fdb7e448b2776986415cb724d9bb3eed424e23b2
Patch0:         python-sphinx-argparse-python310.patch
BuildRequires:  %{python_module CommonMark}
BuildRequires:  %{python_module Sphinx >= 1.2.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Sphinx extension that automatically documents argparse commands and options.

%prep
%autosetup -p1 -n sphinx-argparse-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
