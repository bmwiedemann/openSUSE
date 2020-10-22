#
# spec file for package python-colorama
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
Name:           python-colorama
Version:        0.4.4
Release:        0
Summary:        Cross-platform colored terminal text
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/tartley/colorama
Source:         https://github.com/tartley/colorama/archive/%{version}.tar.gz
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
BuildArch:      noarch
%python_subpackages

%description
Makes ANSI escape character sequences, for producing colored terminal text and
cursor positioning, work under MS Windows.

ANSI escape character sequences have long been used to produce colored terminal
text and cursor positioning on Unix and Macs. Colorama makes this work on
Windows, too. It also provides some shortcuts to help generate ANSI sequences,
and works fine in conjunction with any other ANSI sequence generation library,
such as Termcolor.

This has the upshot of providing a simple cross-platform API for printing
colored terminal text from Python, and has the happy side-effect that existing
applications or libraries which use ANSI sequences to produce colored output on
Linux or Macs can now also work on Windows, simply by calling colorama.init().

%prep
%setup -q -n colorama-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand script -eqc "pytest-%{$python_version} -vv -s" /dev/null

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.rst README.rst
%doc demos/
%dir %{python_sitelib}/colorama
%{python_sitelib}/colorama/*
%dir %{python_sitelib}/colorama-%{version}-py*.egg-info
%{python_sitelib}/colorama-%{version}-py*.egg-info

%changelog
