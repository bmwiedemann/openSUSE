#
# spec file for package python-sphinx-argparse
#
# Copyright (c) 2023 SUSE LLC
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


%define skip_python2 1
Name:           python-sphinx-argparse
Version:        0.4.0
Release:        0
Summary:        Sphinx extension to document argparse commands and options
License:        MIT
URL:            https://github.com/ashb/sphinx-argparse
Source0:        https://files.pythonhosted.org/packages/source/s/sphinx-argparse/sphinx_argparse-%{version}.tar.gz
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
%autosetup -p1 -n sphinx_argparse-%{version}

%build
%python_build

%install
%python_install
# Remove test files, they are in a seperate 'test' module.
%python_expand rm -r %{buildroot}%{$python_sitelib}/test
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%{python_sitelib}/*

%changelog
