#
# spec file for package python-cilium-microscope
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define modname cilium-microscope
Name:           python-cilium-microscope
Version:        1.1.2
Release:        0
Summary:        Program to gather monitor data from CCilium nodes in a cluster
License:        Apache-2.0
Group:          Development/Languages/Python
URL:            https://github.com/cilium/microscope
Source:         https://github.com/cilium/microscope/archive/%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyYAML
Requires:       python-cachetools
Requires:       python-chardet
Requires:       python-google-auth
Requires:       python-idna
Requires:       python-kubernetes
Requires:       python-pyasn1
Requires:       python-pyasn1-modules
Requires:       python-python-dateutil
Requires:       python-requests
Requires:       python-rsa
Requires:       python-urwid
Requires:       python-websocket-client
Requires(post): update-alternatives
Requires(postun): update-alternatives
Provides:       %{modname} = %{version}
Obsoletes:      %{modname} < 1.1.1
BuildArch:      noarch
%python_subpackages

%description
Cilium microscope allows you to see cilium monitor output from all
your cilium nodes. This allows you to have one simple to use command
to interact with your cilium nodes within k8s cluster.

%prep
%setup -q -n microscope-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/microscope
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative microscope

%postun
%python_uninstall_alternative microscope

%files %{python_files}
%{python_sitelib}/*
%python_alternative %{_bindir}/microscope
%license LICENSE

%changelog
