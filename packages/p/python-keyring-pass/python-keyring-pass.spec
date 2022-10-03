#
# spec file for package keyring-pass
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-keyring-pass
Version:        0.7.1
Release:        0
Summary:        Pass backend for python-keyring
License:        MIT
URL:            https://github.com/nazarewk/keyring_pass
Source:         https://files.pythonhosted.org/packages/source/k/keyring_pass/keyring_pass-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-jaraco.classes
Requires:       python-keyring
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module jaraco.classes}
BuildRequires:  %{python_module keyring}
# /SECTION
%python_subpackages

%description
python-keyring backend getting data from pass.

%prep
%autosetup -p1 -n keyring_pass-%{version}

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%{python_sitelib}/keyring_pass-%{version}*-info
%{python_sitelib}/keyring_pass

%changelog
