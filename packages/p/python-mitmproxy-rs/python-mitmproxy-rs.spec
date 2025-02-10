#
# spec file for package python-mitmproxy-rs
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


Name:           python-mitmproxy-rs
Version:        0.11.1
Release:        0
Summary:        Rust bits for mitmproxy
License:        MIT
URL:            https://github.com/mitmproxy/mitmproxy_rs
Source:         https://files.pythonhosted.org/packages/source/m/mitmproxy-rs/mitmproxy_rs-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  %{python_module maturin >= 1}
BuildRequires:  %{python_module pip}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
This package contains mitmproxy's Rust bits.

%prep
%autosetup -a1 -p1 -n mitmproxy_rs-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# no tests in the tarball

%files %{python_files}
%{python_sitearch}/mitmproxy_rs
%{python_sitearch}/mitmproxy_rs-%{version}.dist-info

%changelog
