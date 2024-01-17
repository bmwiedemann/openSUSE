#
# spec file for package in-toto
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


# we just build the application, not the modules
%define pythons python3
Name:           in-toto
Version:        1.2.0
Release:        0
Summary:        in-toto is a framework to protect supply chain integrity.
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://in-toto.io
Source:         https://files.pythonhosted.org/packages/source/i/in-toto/%{name}-%{version}.tar.gz
BuildRequires:  python3-recommonmark
BuildRequires:  python3-setuptools
BuildRequires:  python3-sphinx-argparse
BuildRequires:  python3-sphinx_rtd_theme
Requires:       python3-attrs
Requires:       python3-iso8601
Requires:       python3-pathspec
Requires:       python3-python-dateutil
Requires:       python3-securesystemslib
BuildArch:      noarch

%description
in-toto provides a framework to protect the integrity of the software supply chain. It does so by verifying that each task in the chain is carried out as planned, by authorized personnel only, and that the product is not tampered with in transit.

%prep
%setup -q

%build
%python_build

%install
%python_install

%check

%files
%doc README.md
%license LICENSE
%{_bindir}/in-toto*
%{python_sitelib}/*

%changelog
