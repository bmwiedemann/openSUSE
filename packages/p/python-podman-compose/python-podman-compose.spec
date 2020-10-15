#
# spec file for package python-podman-compose
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


%global src_name podman-compose
%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-%{src_name}
Version:        0.1.5
Release:        0
Summary:        A script to run docker-compose using podman
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/containers/%{src_name}
Source0:        https://files.pythonhosted.org/packages/source/p/%{src_name}/%{src_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/containers/%{src_name}/v%{version}/LICENSE
# PATCH-FIX-UPSTREAM 0001-podman-volume-inspect-mountPoint-Mountpoint.patch fcrozat@suse.com -- handle various podman version
Patch0:         0001-podman-volume-inspect-mountPoint-Mountpoint.patch
# PATCH-FIX-UPSTREAM 0001-Add-support-for-devices-in-a-service.patch fcrozat@suse.com -- support --devices
Patch1:         0001-Add-support-for-devices-in-a-service.patch
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       podman
Requires:       python-PyYAML
BuildArch:      noarch
%python_subpackages

%description
An implementation of `docker-compose` with podman backend.
The main objective of this project is to be able to run `docker-compose.yml`
unmodified and rootless.  This project is aimed to provide drop-in replacement
for `docker-compose`, and it's very useful for certain cases because:

- can run rootless
- only depend on `podman` and Python3 and PyYAML
- no daemon, no setup
- can be used by developers to run single-machine containerized stacks using
  single familiar YAML file

%prep
%autosetup  -n %{src_name}-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand sed -i '1d' %{buildroot}%{$python_sitelib}/podman_compose.py

# %%check
# FIXME: we don't run upstream's tests, because those are currently only
# docker-compose files that are run via podman-compose to check the
# compatibility in a non-automated fashion.

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*
%{_bindir}/%{src_name}

%changelog
