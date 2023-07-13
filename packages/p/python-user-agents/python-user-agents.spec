#
# spec file for package python-user-agents
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


Name:           python-user-agents
Version:        2.2.0
Release:        0
Summary:        A library to identify device capabilities (phones, tablets)
License:        MIT
URL:            https://github.com/selwin/python-user-agents
Source:         https://github.com/selwin/python-user-agents/archive/v%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module ua-parser >= 0.10.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-ua-parser >= 0.10.0
BuildArch:      noarch
%python_subpackages

%description
Python library that can identify/detect devices like mobile phones,
tablets and their capabilities by parsing (browser/HTTP) user agent
strings.

%prep
%setup -q

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

%check
%pyunittest

%files %{python_files}
%license LICENSE.txt
%doc README.md
%{python_sitelib}/user_agents
%{python_sitelib}/user_agents-%{version}.dist-info

%changelog
