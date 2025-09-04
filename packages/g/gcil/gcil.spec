#
# spec file for package gcil
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           gcil
Version:        13.0.1
Release:        0
Summary:        Launch .gitlab-ci.yml jobs locally
License:        Apache-2.0
URL:            https://gitlab.com/RadianDevCore/tools/gcil
Source:         https://files.pythonhosted.org/packages/source/g/gitlabci_local/gitlabci_local-%{version}.tar.gz
# PATCH-FEATURE-OPENSUSE -- we don't have update_checker packaged. but its not important anyways
Patch0:         gcil-no-update.patch
BuildRequires:  python3-pip
BuildRequires:  python3-setuptools_scm
BuildRequires:  python3-wheel
BuildRequires:  python-rpm-macros
Requires:       python3-PyYAML
Requires:       python3-coloredlogs
Requires:       python3-importlib-metadata
Requires:       python3-packaging
Requires:       python3-prompt_toolkit
Requires:       python3-python-dotenv
Requires:       python3-requests
Requires:       python3-docker
Requires:       python3-questionary

%description
Launch .gitlab-ci.yml jobs locally, wrapped inside the specific images,
with inplace project volume mounts and adaptive user selections.

%prep
%autosetup -p1 -n gitlabci_local-%{version}

%build
%python3_build

%install
%python3_install

%files
%license LICENSE
%doc CHANGELOG.md README.md
%{_bindir}/gcil
%{_bindir}/gitlabci-local
%{python_sitelib}/gcil
%{python_sitelib}/gitlabci_local*

%changelog
