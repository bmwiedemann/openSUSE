#
# spec file for package python-uv-build
#
# Copyright (c) 2025 SUSE LLC and contributors
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
Name:           python-uv-build
Version:        0.9.11
Release:        0
Summary:        The uv build backend
License:        MIT
URL:            https://github.com/astral-sh/uv
Source0:        https://files.pythonhosted.org/packages/source/u/uv-build/uv_build-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module maturin >= 1.0}
BuildRequires:  %{python_module pip}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
%if %{with libalternatives}
BuildRequires:  alts
Requires:       alts
%else
Requires(post): update-alternatives
Requires(postun): update-alternatives
%endif
%python_subpackages

%description
This package is a slimmed down version of uv containing only the build backend.

%prep
%autosetup -p1 -n uv_build-%{version} -a1

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/uv-build
%python_expand %fdupes %{buildroot}%{$python_sitearch}

# No testsuite shipped with package

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative uv-build

%post
%python_install_alternative uv-build

%postun
%python_uninstall_alternative uv-build

%files %{python_files}
%doc README.md
%license LICENSE-APACHE LICENSE-MIT
%python_alternative %{_bindir}/uv-build
%{python_sitearch}/uv_build
%{python_sitearch}/uv_build-%{version}.dist-info

%changelog
