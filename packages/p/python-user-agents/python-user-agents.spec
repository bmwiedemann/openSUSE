#
# spec file for package python-user-agents
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
Name:           python-user-agents
Version:        2.0
Release:        0
Summary:        A library to identify device capabilities (phones, tablets)
License:        MIT
URL:            https://github.com/selwin/python-user-agents
Source:         https://github.com/selwin/python-user-agents/archive/v%{version}.tar.gz
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module ua-parser >= 0.8.0}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-ua-parser >= 0.8.0
BuildArch:      noarch
%python_subpackages

%description
Python library that can identify/detect devices like mobile phones,
tablets and their capabilities by parsing (browser/HTTP) user agent
strings.

%prep
%setup -q

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
%python_expand $python -m unittest discover ||:

%files %{python_files}
%license LICENSE.txt
%doc README.rst
%{python_sitelib}/*

%changelog
