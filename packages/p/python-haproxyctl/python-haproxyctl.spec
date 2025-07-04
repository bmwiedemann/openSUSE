#
# spec file for package python-haproxyctl
#
# Copyright (c) 2025 SUSE LLC
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
Name:           python-haproxyctl
Version:        0.5
Release:        0
Summary:        HAProxy control tool
License:        GPL-3.0-only
Group:          Development/Languages/Python
URL:            https://github.com/neurogeek/haproxyctl
Source:         https://github.com/neurogeek/haproxyctl/archive/v%{version}.tar.gz#/haproxyctl-%{version}.tar.gz
Source1:        gpl-3.0.txt
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  unzip
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
Requires:       haproxy
BuildArch:      noarch
%python_subpackages

%description
This is a utility to control HAProxy features through its admin
socket. haproxyctl has the ability to disable/enable servers, fetch
info from the running instance and list available servers, together
with their status.

%prep
%autosetup -p1 -n haproxyctl-%{version}
# The package is under GPL-3.0, as expressed in setup.py, but the
# license file is not included in the source code.
cp %{SOURCE1} .

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a  %{buildroot}%{_bindir}/haproxyctl
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%{python_expand mkdir -p %{buildroot}%{_datadir}/$python-haproxyctl/
cp -a conf %{buildroot}%{_datadir}/$python-haproxyctl/}

%check
%{python_expand $python -m unittest discover -s haproxy/tests}

%if %{with libalternatives}
%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative <package-name>
%else

%post
%python_install_alternative haproxyctl

%postun
%python_uninstall_alternative haproxyctl
%endif

%files %{python_files}
%doc README.md
%license gpl-3.0.txt
%dir %{_datadir}/%{python_flavor}-haproxyctl
%{python_sitelib}/haproxy
%{python_sitelib}/haproxyctl-%{version}*-info
%python_alternative %{_bindir}/haproxyctl
%{_datadir}/%{python_flavor}-haproxyctl/*

%changelog
