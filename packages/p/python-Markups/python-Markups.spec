#
# spec file for package python-Markups
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


Name:           python-Markups
Version:        4.0.0
Release:        0
Summary:        A wrapper around various text markups
License:        BSD-3-Clause
URL:            https://github.com/mitya57/pymarkups
Source:         https://files.pythonhosted.org/packages/source/M/Markups/Markups-%{version}.tar.gz
BuildRequires:  %{python_module Markdown >= 3}
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module Pygments}
BuildRequires:  %{python_module docutils}
BuildRequires:  %{python_module lxml}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-markdown-math}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module textile}
BuildRequires:  %{python_module wheel}
BuildRequires:  asciidoc
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-python-markdown-math
BuildArch:      noarch
%python_subpackages

%description
This module provides a wrapper around the various text markup languages,
such as Markdown and reStructuredText (these two are supported by default).

%prep
%autosetup -p1 -n Markups-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pyunittest discover -v

%files %{python_files}
%license LICENSE
%doc README.rst changelog
%{python_sitelib}/markups
%{python_sitelib}/Markups-%{version}*-info

%changelog
