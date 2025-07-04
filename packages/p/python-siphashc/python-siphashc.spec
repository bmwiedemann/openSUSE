#
# spec file for package python-siphashc
#
# Copyright (c) 2025 SUSE LLC
# Copyright (c) 2017 Matthias Fehring <buschmann23@opensuse.org>
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


Name:           python-siphashc
Version:        2.5
Release:        0
Summary:        Python C module to calculate SipHashes
License:        ISC
URL:            https://github.com/WeblateOrg/siphashc
Source:         https://files.pythonhosted.org/packages/source/s/siphashc/siphashc-%{version}.tar.gz
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Obsoletes:      python-siphashc3 < %{version}
Provides:       python-siphashc3 = %{version}
%python_subpackages

%description
A Python C module for siphash. SipHash is an add–rotate–xor (ARX)
based family of pseudorandom functions.

SipHash is fundamentally different from cryptographic hash functions
like SHA in that SipHash is only suitable as a message authentication
code.

%prep
%setup -q -n siphashc-%{version}

%build
export CFLAGS="%{optflags}"
%pyproject_wheel

%check
%pytest_arch

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%files %{python_files}
%license LICENSE.md
%doc README.rst CHANGES.rst
%{python_sitearch}/siphashc
%{python_sitearch}/siphashc.cpython-*-linux-gnu.so
%{python_sitearch}/siphashc-%{version}.dist-info

%changelog
