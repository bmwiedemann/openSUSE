#
# spec file for package python-Markups
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
Name:           python-Markups
Version:        3.0.0
Release:        0
Summary:        A wrapper around various text markups
License:        BSD-3-Clause
URL:            https://github.com/mitya57/pymarkups
Source:         https://files.pythonhosted.org/packages/source/M/Markups/Markups-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-markdown-math
BuildArch:      noarch
# SECTION Required for %%check
BuildRequires:  %{python_module markdown-math}
# /SECTION
%python_subpackages

%description
This module provides a wrapper around the various text markup languages,
such as Markdown and reStructuredText (these two are supported by default).

%prep
%setup -q -n Markups-%{version}

%build
%python_build

%install
%python_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_exec setup.py test

%files %{python_files}
%license LICENSE
%doc README.rst changelog
%{python_sitelib}/*

%changelog
