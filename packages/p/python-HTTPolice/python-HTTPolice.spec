#
# spec file for package python-HTTPolice
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-HTTPolice
Version:        0.9.0
Release:        0
Summary:        Validator for HTTP
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/vfaronov/httpolice
Source:         https://files.pythonhosted.org/packages/source/H/HTTPolice/HTTPolice-%{version}.tar.gz
BuildRequires:  %{python_module Brotli >= 1.0.1}
BuildRequires:  %{python_module bitstring >= 3.1.4}
BuildRequires:  %{python_module defusedxml >= 0.5.0}
BuildRequires:  %{python_module dominate >= 2.2.0}
BuildRequires:  %{python_module lxml >= 4.1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Brotli >= 1.0.1
Requires:       python-bitstring >= 3.1.4
Requires:       python-defusedxml >= 0.5.0
Requires:       python-dominate >= 2.2.0
Requires:       python-lxml >= 4.1.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
HTTPolice is a validator or linter for HTTP requests and responses.
It can spot bad header syntax, inappropriate status codes, and other potential
problems in your HTTP server or client.

%prep
%setup -q -n HTTPolice-%{version}
rm pytest.ini

%build
export LANG=en_US.UTF-8
%python_build

%install
export LANG=en_US.UTF-8
%python_install
%python_clone -a %{buildroot}%{_bindir}/httpolice
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
export LANG=en_US.UTF-8
%pytest

%post
%python_install_alternative httpolice

%postun
%python_uninstall_alternative httpolice

%files %{python_files}
%license LICENSE.txt
%doc CHANGELOG.rst README.rst
%python_alternative %{_bindir}/httpolice
%{python_sitelib}/*

%changelog
