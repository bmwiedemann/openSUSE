#
# spec file for package python-dnslib
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-dnslib
Version:        0.9.23
Release:        0
Summary:        Simple library to encode/decode DNS wire-format packets
License:        BSD-2-Clause
Group:          Development/Languages/Python
URL:            https://github.com/paulc/dnslib
Source:         https://files.pythonhosted.org/packages/source/d/dnslib/dnslib-%{version}.tar.gz
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildArch:      noarch
%python_subpackages

%description
Simple library to encode/decode DNS wire-format packets.

%prep
%setup -q -n dnslib-%{version}
sed -i '1{/^#!/d}' dnslib/test_decode.py

%build
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%python_expand VERSIONS="$python" sh ./run_tests.sh

%files %{python_files}
%doc README
%license LICENSE
%{python_sitelib}/*

%changelog
