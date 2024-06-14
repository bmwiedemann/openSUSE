#
# spec file for package python-xdoctest
#
# Copyright (c) 2024 SUSE LLC
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


Name:           python-xdoctest
Version:        1.1.5
Release:        0
Summary:        Enhanced Python builtin doctest module
License:        Apache-2.0
URL:            https://github.com/Erotemic/xdoctest
Source:         https://github.com/Erotemic/xdoctest/archive/refs/tags/v%{version}.tar.gz#/xdoctest-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pygments}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-pygments
BuildArch:      noarch
%python_subpackages

%description
A rewrite of the builtin doctest module with a pytest plugin.

%prep
%autosetup -p1 -n xdoctest-%{version}

%build
sed -i '1{/^#!/d}' src/xdoctest/__main__.py
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/xdoctest
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative xdoctest

%postun
%python_uninstall_alternative xdoctest

%check
%pytest

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/xdoctest
%{python_sitelib}/xdoctest
%{python_sitelib}/xdoctest-%{version}.dist-info

%changelog
