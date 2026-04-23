#
# spec file for package python-sphinx-llms-txt
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


Name:           python-sphinx-llms-txt
Version:        0.7.1
Release:        0
Summary:        Sphinx generator for lms-full.txt
License:        MIT
URL:            https://github.com/jdillard/sphinx-llms-txt
Source:         https://github.com/jdillard/sphinx-llms-txt/archive/refs/tags/v%{version}.tar.gz#/sphinx_llms_txt-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module Sphinx}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-Sphinx
BuildArch:      noarch
%python_subpackages

%description
A Sphinx extension that generates a summary llms.txt file and a single
combined documentation llms-full.txt file.

%prep
%autosetup -p1 -n sphinx-llms-txt-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc README.md
%{python_sitelib}/sphinx_llms_txt
%{python_sitelib}/sphinx_llms_txt-%{version}.dist-info

%changelog
