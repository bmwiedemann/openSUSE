#
# spec file for package python-py-partiql-parser
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


Name:           python-py-partiql-parser
Version:        0.4.2
Release:        0
Summary:        Pure Python PartiQL Parser
License:        MIT
URL:            https://github.com/getmoto/py-partiql-parser
Source:         https://github.com/getmoto/py-partiql-parser/archive/refs/tags/%{version}.tar.gz#/py-partiql-parser-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools >= 59.0.0}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Pure Python PartiQL Parser

%prep
%autosetup -p1 -n py-partiql-parser-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/py_partiql_parser
%{python_sitelib}/py_partiql_parser-%{version}.dist-info

%changelog
