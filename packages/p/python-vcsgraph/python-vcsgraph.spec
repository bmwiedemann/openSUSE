#
# spec file for package python-vcsgraph
#
# Copyright (c) 2026 SUSE LLC and contributors
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


Name:           python-vcsgraph
Version:        0.2.0
Release:        0
Summary:        Graph algorithms optimized for version control systems
License:        GPL-2.0-or-later
URL:            https://github.com/breezy-team/vcsgraph
Source0:        https://github.com/breezy-team/vcsgraph/archive/refs/tags/v%{version}.tar.gz#/vcsgraph-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module base >= 3.10}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools-rust}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%python_subpackages

%description
vcsgraph is a high-performance graph algorithms library specifically
designed for working with version control system (VCS) data
structures. It provides efficient implementations of common graph
operations needed by VCS tools, with both pure Python and
Rust-accelerated implementations for performance-critical operations.

%prep
%autosetup -p1 -a1 -n vcsgraph-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
find %{buildroot} -name '_graph_rs*so' -exec cp {} vcsgraph \;
%pytest_arch

%files %{python_files}
%license COPYING.txt
%doc README.md
%{python_sitearch}/vcsgraph
%{python_sitearch}/vcsgraph-%{version}.dist-info

%changelog
