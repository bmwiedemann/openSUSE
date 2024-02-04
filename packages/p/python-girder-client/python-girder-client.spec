#
# spec file for package python-girder-client
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
Name:           python-girder-client
Version:        3.2.1
Release:        0
Summary:        Python Girder client
License:        Apache-2.0
URL:            https://girder.readthedocs.io/en/latest/python-client.html
Source:         https://files.pythonhosted.org/packages/source/g/girder-client/girder-client-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 6.7
Requires:       python-diskcache
Requires:       python-requests >= 2.4.2
Requires:       python-requests-toolbelt
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Girder is a web-based data management platform.

This package provides the client for interacting
with Girder servers

%prep
%setup -q -n girder-client-%{version}
sed -i -e '/^#!\//, 1d' girder_client/*.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/girder-client
%python_clone -a %{buildroot}%{_bindir}/girder-cli
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative girder-client
%python_install_alternative girder-cli

%postun
%python_uninstall_alternative girder-client
%python_uninstall_alternative girder-cli

%files %{python_files}
%doc README.rst
%python_alternative %{_bindir}/girder-cli
%python_alternative %{_bindir}/girder-client
%{python_sitelib}/*

%changelog
