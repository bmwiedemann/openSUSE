#
# spec file for package python-rpcq
#
# Copyright (c) 2021 SUSE LLC
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


%define packagename rpcq
%define skip_python2 1
%define skip_python36 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-rpcq
Version:        3.9.1
Release:        0
Summary:        The RPC framework and message specification for Rigetti QCS
License:        Apache-2.0
URL:            https://github.com/rigetti/rpcq
Source:         https://github.com/rigetti/rpcq/archive/v%{version}.tar.gz#/%{packagename}-%{version}.tar.gz
BuildRequires:  %{python_module msgpack >= 0.6}
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module python-rapidjson}
BuildRequires:  %{python_module pyzmq >= 17}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-msgpack >= 0.6
Requires:       python-numpy
Requires:       python-python-rapidjson
Requires:       python-pyzmq >= 17
Requires:       python-ruamel.yaml
BuildArch:      noarch
%python_subpackages

%description
The RPC framework and message specification for Rigetti QCS.

%prep
%setup -q -n %{packagename}-%{version}
# Fix non-executable-script
sed -i '/^#!/d' %{packagename}/core_messages.py
sed -i '/^#!/d' %{packagename}/messages.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_client_warning stall for unknown reason.
%pytest -k "not (test_client_warning)"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/*egg-info
%{python_sitelib}/%{packagename}

%changelog
