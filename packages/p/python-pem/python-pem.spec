#
# spec file for package python-pem
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


%{?sle15_python_module_pythons}
Name:           python-pem
Version:        23.1.0
Release:        0
Summary:        PEM file parsing in Python
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/hynek/pem
Source0:        https://files.pythonhosted.org/packages/source/p/pem/pem-%{version}.tar.gz
BuildRequires:  %{python_module Twisted-tls}
BuildRequires:  %{python_module certifi}
BuildRequires:  %{python_module hatch-fancy-pypi-readme}
BuildRequires:  %{python_module hatch_vcs}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pretend}
BuildRequires:  %{python_module pyOpenSSL}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
pem is a Python module for parsing and splitting of PEM files,
i.e. Base64 encoded DER keys and certificates.

%prep
%setup -q -n pem-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand rm %{buildroot}/%{$python_sitelib}/pem/py.typed #zero length

%check
%pytest tests

%files %{python_files}
%license LICENSE
%doc README.md CHANGELOG.md
%{python_sitelib}/pem
%{python_sitelib}/pem-%{version}.dist-info

%changelog
