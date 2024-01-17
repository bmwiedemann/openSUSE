#
# spec file for package python-rpcq
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


Name:           python-rpcq
Version:        3.10.0
Release:        0
Summary:        The RPC framework and message specification for Rigetti QCS
License:        Apache-2.0
URL:            https://github.com/rigetti/rpcq
Source:         https://github.com/rigetti/rpcq/archive/v%{version}.tar.gz#/rpcq-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.6}
BuildRequires:  %{python_module msgpack >= 0.6}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module python-rapidjson}
BuildRequires:  %{python_module pyzmq >= 17}
BuildRequires:  %{python_module ruamel.yaml}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-msgpack >= 0.6
Requires:       python-python-rapidjson
Requires:       python-pyzmq >= 17
Requires:       python-ruamel.yaml
# SECTION test
BuildRequires:  %{python_module numpy}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest}

# /SECTION
BuildArch:      noarch
%python_subpackages

%description
The RPC framework and message specification for Rigetti QCS.

%prep
%setup -q -n rpcq-%{version}
# Fix non-executable-script
sed -i '/^#!/d' rpcq/core_messages.py
sed -i '/^#!/d' rpcq/messages.py
# unpin msgpack and ignore gh#rigetti/pyqui#1178
sed -i '/msgpack/ s/,<1.0//' setup.py

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
# test_client_warning stall for unknown reason.
%pytest -k "not (test_client_warning)"

%files %{python_files}
%doc README.md
%license LICENSE
%{python_sitelib}/rpcq-%{version}.dist-info
%{python_sitelib}/rpcq

%changelog
