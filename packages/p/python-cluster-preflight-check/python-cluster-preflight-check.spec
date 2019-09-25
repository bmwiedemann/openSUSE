#
# spec file for package python-cluster-preflight-check
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Name:           python-cluster-preflight-check
Version:        0.0.33
Release:        0
Summary:        Standardized Testing of Basic Cluster Functionality
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/liangxin1300/cluster_preflight_check.git
Source:         cluster_preflight_check-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Obsoletes:      cluster-preflight-check < %{version}
BuildArch:      noarch
%if 0%{?suse_version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
%else
Requires(post): %{_sbindir}/update-alternatives
Requires(postun): %{_sbindir}/update-alternatives
%endif
%python_subpackages

%description
Tool for Standardized Testing of Basic Cluster Functionality.
It checks the environment, the current cluster state, and more.
The script creates a JSON output for each test case.

%prep
%setup -q -n cluster_preflight_check-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/ha-cluster-preflight-check
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative ha-cluster-preflight-check

%postun
%python_uninstall_alternative ha-cluster-preflight-check

%files %{python_files}
%doc AUTHORS README.md COPYING
%{python_sitelib}/cluster_preflight_check
%{python_sitelib}/cluster_preflight_check-%{version}*.egg-info
%python_alternative %{_bindir}/ha-cluster-preflight-check

%changelog
