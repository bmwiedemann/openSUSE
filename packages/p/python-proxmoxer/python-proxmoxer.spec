#
# spec file for package python-proxmoxer
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
Name:           python-proxmoxer
Version:        2.2.0
Release:        0
Summary:        Python Wrapper for the Proxmox 2x API (HTTP and SSH)
License:        MIT
URL:            https://github.com/proxmoxer/proxmoxer/
# the Pypi tarball does not contain the tests directory
Source:         proxmoxer-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros

# Tests
BuildRequires:  %{python_module paramiko}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests-toolbelt}
BuildRequires:  %{python_module requests}
BuildRequires:  %{python_module responses}

BuildArch:      noarch
%python_subpackages

%description
Python Wrapper for the Proxmox 2.x API (HTTP and SSH)

%prep
%setup -q -n proxmoxer-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# remove tests that need the ancient openssh-wrapper module
rm -f ./tests/test_openssh.py
IGNORED_CHECKS="test_timeout"
IGNORED_CHECKS="${IGNORED_CHECKS} or test_repr_openssh"
%pytest -k "not (${IGNORED_CHECKS})" --cov ./tests/

%files %{python_files}
%doc CHANGELOG.md README.rst
%license LICENSE.txt
%{python_sitelib}/proxmoxer
%{python_sitelib}/proxmoxer-%{version}*-info

%changelog
