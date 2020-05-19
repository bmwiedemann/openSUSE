#
# spec file for package python-softlayer
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
%define skip_python2 1
Name:           python-softlayer
Version:        5.8.7
Release:        0
Summary:        A set of Python libraries that assist in calling the SoftLayer API
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/softlayer/softlayer-python
Source:         https://github.com/softlayer/softlayer-python/archive/v%{version}.tar.gz
BuildRequires:  %{python_module PrettyTable >= 0.7.0}
BuildRequires:  %{python_module click >= 7}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module prompt_toolkit >= 2}
BuildRequires:  %{python_module pygments >= 2.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.20.0}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.7.0}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module urllib3 >= 1.24}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PrettyTable >= 0.7.0
Requires:       python-click >= 7
Requires:       python-prompt_toolkit >= 2
Requires:       python-pygments >= 2.0.0
Requires:       python-requests >= 2.20.0
Requires:       python-setuptools
Requires:       python-six >= 1.7.0
Requires:       python-urllib3 >= 1.24
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
This library provides a simple Python client to interact with SoftLayer's XML-RPC API.

%prep
%setup -q -n softlayer-python-%{version}

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/slcli
%python_clone -a %{buildroot}%{_bindir}/sl
# do not install tests
%python_expand rm -r %{buildroot}%{$python_sitelib}/tests/
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative slcli
%python_install_alternative sl

%postun
%python_uninstall_alternative slcli
%python_uninstall_alternative sl

%files %{python_files}
%license LICENSE
%doc *.md
%{python_sitelib}/*
%python_alternative %{_bindir}/sl
%python_alternative %{_bindir}/slcli

%changelog
