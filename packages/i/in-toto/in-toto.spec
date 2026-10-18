#
# spec file for package in-toto
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


# we just build the application, not the modules
%define pythons python3
Name:           in-toto
Version:        3.1.0
Release:        0
Summary:        Framework to protect supply chain integrity
License:        Apache-2.0
URL:            https://in-toto.io
Source:         https://files.pythonhosted.org/packages/source/i/in-toto/in_toto-%{version}.tar.gz
BuildRequires:  %{python_module attrs}
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module iso8601}
BuildRequires:  %{python_module pathspec}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-dateutil}
BuildRequires:  %{python_module securesystemslib}
BuildRequires:  fdupes
BuildRequires:  gnupg
Requires:       python3-attrs
Requires:       python3-iso8601
Requires:       python3-pathspec
Requires:       python3-python-dateutil
Requires:       python3-securesystemslib >= 1.0
BuildArch:      noarch

%description
in-toto provides a framework to protect the integrity of the software supply chain. It does so by verifying that each task in the chain is carried out as planned, by authorized personnel only, and that the product is not tampered with in transit.

%prep
%setup -q -n in_toto-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%fdupes %{buildroot}%{python_sitelib}

%check
# demo layouts invoke bare "python" (absent on openSUSE); shim it for tests
mkdir -p test-bin
ln -s %{__python3} test-bin/python
export PATH=$PWD/test-bin:$PATH
python3 -m unittest discover -s tests

%files
%doc README.md
%license LICENSE
%{_bindir}/in-toto*
%{python_sitelib}/in_toto
%{python_sitelib}/in_toto-%{version}*-info

%changelog
