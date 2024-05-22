#
# spec file for package python-pygit2
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2019 Neal Gompa <ngompa13@gmail.com>.
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


%{?sle15_python_module_pythons}
Name:           python-pygit2
Version:        1.14.1
Release:        0
Summary:        Python bindings for libgit2
License:        GPL-2.0-only
URL:            https://github.com/libgit2/pygit2
Source:         https://files.pythonhosted.org/packages/source/p/pygit2/pygit2-%{version}.tar.gz
# PATCH-FIX-UPSTREAM pygit2-Upgrade_to_libgit2_v1_8_0.patch gh#libgit2/pygit2@6d539d76b53b
Patch0:         pygit2-Upgrade_to_libgit2_v1_8_0.patch
# PATCH-FIX-UPSTREAM - fixup for the libgit 1.8 support
Patch1:         Fix-CI.patch
# PATCH-FIX-UPSTREAM
Patch2:         pygit2-Upgrade_to_libgit2_v1_8_1.patch
# PATCH-FIX-UPSTREAM
Patch3:         pygit2-Upgrade_to_libgit2_v1_8_1-2.patch
# PATCH-FIX-UPSTREAM - happens to eliminate bogus pointer casts
Patch4:         Fix-leaks-in-fetch_refspecs-and-push_refspecs.patch
BuildRequires:  %{python_module cached-property}
BuildRequires:  %{python_module cffi >= 1.4.0}
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  ca-certificates
BuildRequires:  ca-certificates-mozilla
BuildRequires:  fdupes
BuildRequires:  libgit2-devel >= 1.1
BuildRequires:  libopenssl-devel
BuildRequires:  python-rpm-macros
Requires:       python-cached-property
%requires_eq    python-cffi
%python_subpackages

%description
Bindings for libgit2, a linkable C library for the Git version-control system.

%prep
%autosetup -p1 -n pygit2-%{version}
%if %{?pkg_vcmp:%pkg_vcmp libgit2-devel < 1.8}%{!?pkg_vcmp:1}
%patch -P 3 -p1 -R
%patch -P 2 -p1 -R
%patch -P 1 -p1 -R
%patch -P 0 -p1 -R
%endif

# do not add options to pytest
rm pytest.ini

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%pyproject_wheel

%install
%pyproject_install
%python_expand rm -rf %{buildroot}%{$python_sitearch}/pygit2/decl/
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
rm -rf pygit2
# test_no_context_lines failing on big endian
# https://github.com/libgit2/pygit2/issues/812
%pytest_arch -k 'not test_no_context_lines'

%files %{python_files}
%license COPYING
%doc README.md
%{python_sitearch}/pygit2
%{python_sitearch}/pygit2-%{version}.dist-info

%changelog
