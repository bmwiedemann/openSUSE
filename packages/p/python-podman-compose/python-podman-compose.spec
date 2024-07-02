#
# spec file for package python-podman-compose
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
%global src_name podman-compose
Name:           python-%{src_name}
Version:        1.2.0
Release:        0
Summary:        A script to run docker-compose using podman
License:        GPL-2.0-only
Group:          Development/Languages/Python
URL:            https://github.com/containers/%{src_name}
Source0:        %{src_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/containers/%{src_name}/v%{version}/LICENSE
BuildRequires:  %{python_module PyYAML}
BuildRequires:  %{python_module python-dotenv}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       podman
Requires:       python-PyYAML
Requires:       python-python-dotenv
Requires:       python-setuptools
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
Provides:       podman-compose = %{version}
Obsoletes:      podman-compose < %{version}
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
%setup  -n %{src_name}-%{version}
cp %{SOURCE1} .

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/podman-compose
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_expand sed -i '1d' %{buildroot}%{$python_sitelib}/podman_compose.py

# %%check
# FIXME: we don't run upstream's tests, because those are currently only
# docker-compose files that are run via podman-compose to check the
# compatibility in a non-automated fashion.

%post
%python_install_alternative podman-compose

%postun
%python_uninstall_alternative podman-compose

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*
%python_alternative %{_bindir}/%{src_name}

%changelog
