#
# spec file for package python-softlayer
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
Name:           python-softlayer
Version:        5.7.2
Release:        0
Summary:        A set of Python libraries that assist in calling the SoftLayer API
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/softlayer/softlayer-python
Source:         https://github.com/softlayer/softlayer-python/archive/v%{version}.tar.gz
BuildRequires:  %{python_module PrettyTable >= 0.7.0}
BuildRequires:  %{python_module click}
BuildRequires:  %{python_module mock}
BuildRequires:  %{python_module prompt_toolkit >= 0.5.3}
BuildRequires:  %{python_module pygments >= 2.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.18.4}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module six >= 1.7.0}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module urllib3 >= 1.24}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PrettyTable >= 0.7.0
Requires:       python-click
Requires:       python-prompt_toolkit >= 0.5.3
Requires:       python-pygments >= 2.0.0
Requires:       python-requests >= 2.18.4
Requires:       python-setuptools
Requires:       python-six >= 1.7.0
Requires:       python-urllib3 >= 1.24
%python_subpackages

%description
This library provides a simple Python client to interact with SoftLayer's XML-RPC API.

%prep
%setup -q -n softlayer-python-%{version}

%build
%python_build

%install
%python_install
# do not install tests
%python_expand rm -rf %{buildroot}%{$python_sitelib}/tests/
%python_expand %fdupes -s %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%license LICENSE
%doc *.md
%{python_sitelib}/*
%python3_only %{_bindir}/sl
%python3_only %{_bindir}/slcli

%changelog
