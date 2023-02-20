#
# spec file for package python-softlayer
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


Name:           python-softlayer
Version:        6.1.4
Release:        0
Summary:        A set of Python libraries that assist in calling the SoftLayer API
License:        MIT
URL:            https://github.com/softlayer/softlayer-python
Source:         https://github.com/softlayer/softlayer-python/archive/v%{version}.tar.gz
BuildRequires:  %{python_module click >= 8.0.4}
BuildRequires:  %{python_module prettytable >= 2.5.0}
BuildRequires:  %{python_module prompt_toolkit >= 2}
BuildRequires:  %{python_module pygments >= 2.0.0}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.20.0}
BuildRequires:  %{python_module rich >= 12.5.1}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module softlayer-zeep >= 5.0.0}
BuildRequires:  %{python_module testtools}
BuildRequires:  %{python_module typing_extensions}
BuildRequires:  %{python_module urllib3 >= 1.24}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-click >= 8.0.4
Requires:       python-prettytable >= 2.5.0
Requires:       python-prompt_toolkit >= 2
Requires:       python-pygments >= 2.0.0
Requires:       python-requests >= 2.20.0
Requires:       python-rich >= 12.5.1
Requires:       python-setuptools
Requires:       python-softlayer-zeep >= 5.0.0
Requires:       python-typing_extensions
Requires:       python-urllib3 >= 1.24
Conflicts:      sl
Requires(post): update-alternatives
Requires(postun):update-alternatives
%python_subpackages

%description
This library provides a simple Python client to interact with SoftLayer's XML-RPC API.

%prep
%autosetup -p1 -n softlayer-python-%{version}

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
# We do not want TKinter
%pytest -k 'not test_getpass_issues1436 and not TestSoapAPICall'

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
