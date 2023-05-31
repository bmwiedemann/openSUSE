#
# spec file for package python-mesonpep517
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


Name:           python-mesonpep517
Version:        0.2
Release:        0
Summary:        PEP517 for the Meson build system
License:        Apache-2.0
URL:            https://gitlab.com/thiblahute/mesonpep517
Source:         https://files.pythonhosted.org/packages/source/m/mesonpep517/mesonpep517-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module toml}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  meson
BuildRequires:  python-rpm-macros
# Current hotdoc packages are broken; SR#1089855 should fix them
# BuildRequires:  python3-hotdoc
Requires:       meson
Requires:       python-setuptools
Requires:       python-toml
Requires:       python-wheel
BuildArch:      noarch
%python_subpackages

%description
This package contains a Python module that implements PEP517 for
the Meson build system.

%prep
%autosetup -p1 -n mesonpep517-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%files %{python_files}
%license COPYING
%doc README.md
%{python_sitelib}/mesonpep517
%{python_sitelib}/mesonpep517-%{version}.dist-info

%changelog
