#
# spec file for package python-cysignals
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


%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif
%{?sle15_python_module_pythons}
%define skip_python311 1
Name:           python-cysignals
Version:        1.12.6
Release:        0
Summary:        Interrupt and signal handling for Cython
License:        GPL-3.0-only
URL:            https://github.com/sagemath/cysignals
Source:         https://files.pythonhosted.org/packages/source/c/cysignals/cysignals-%{version}.tar.gz
BuildRequires:  %{python_module Cython >= 3.1.4}
BuildRequires:  %{python_module build >= 1.3.0}
BuildRequires:  %{python_module meson-python >= 0.18.0}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest >= 8.4.2}
BuildRequires:  fdupes
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  meson
BuildRequires:  ninja
BuildRequires:  pkgconf
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
When writing Cython code, special care must be taken to ensure that
the code can be interrupted with <CTRL-C>. Since Cython optimizes
for speed, Cython normally does not check for interrupts. For example,
code like the following cannot be interrupted in Cython::

    while True:
        pass

The cysignals package provides mechanisms to handle interrupts (and
other signals and errors) in Cython code.

%prep
%autosetup -p1 -n cysignals-%{version}

%build
%pyproject_wheel

%check
%pytest_arch

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/cysignals-CSI
%{python_expand %fdupes %{buildroot}%{$python_sitearch}}

%pre
# If libalternatives is used: Removing old update-alternatives entries.
%python_libalternatives_reset_alternative cysignals-CSI

%post
%python_install_alternative cysignals-CSI

%postun
%python_uninstall_alternative cysignals-CSI

%files %{python_files}
%python_alternative %{_bindir}/cysignals-CSI
%{python_sitearch}/cysignals
%{python_sitearch}/cysignals-%{version}.dist-info

%changelog
