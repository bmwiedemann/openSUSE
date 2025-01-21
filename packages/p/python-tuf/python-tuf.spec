#
# spec file for package python-tuf
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


Name:           python-tuf
Version:        5.1.0
Release:        0
Summary:        A secure updater framework for Python
License:        MIT
URL:            https://github.com/theupdateframework/python-tuf
Source:         https://github.com/theupdateframework/python-tuf/archive/v%{version}.tar.gz#/tuf-%{version}.tar.gz
BuildRequires:  python-rpm-macros
BuildRequires:  %{python_module hatchling}
BuildRequires:  %{python_module pip}
# SECTION test requirements
BuildRequires:  %{python_module requests >= 2.19.1}
BuildRequires:  %{python_module securesystemslib >= 1.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module cryptography}
BuildRequires:  %{python_module ed25519}
# /SECTION
BuildRequires:  fdupes
# /SECTION
BuildRequires:  fdupes
Requires:       python-requests >= 2.19.1
Requires:       python-securesystemslib >= 1.0
BuildArch:      noarch
%python_subpackages

%description
The Update Framework (TUF) is a framework for secure content delivery
and updates. It protects against various types of supply chain attacks
and provides resilience to compromise.

%prep
%autosetup -p1 -n python-tuf-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
pushd tests
%pytest
popd

%files %{python_files}
%doc README.md
%license LICENSE LICENSE-MIT
%{python_sitelib}/tuf
%{python_sitelib}/tuf-%{version}.dist-info

%changelog
