#
# spec file for package python-python-bidi
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


%{?sle15_python_module_pythons}
Name:           python-python-bidi
Version:        0.6.7
Release:        0
Summary:        BiDi layout algorithm
License:        LGPL-3.0-only
URL:            https://github.com/MeirKriheli/python-bidi
Source:         https://files.pythonhosted.org/packages/source/p/python_bidi/python_bidi-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  %{python_module maturin > 1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  cargo-packaging
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires(post): update-alternatives
Requires(postun): update-alternatives
%python_subpackages

%description
A pure python implementation of the BiDi layout algorithm.

%prep
%autosetup -a1 -p1 -n python_bidi-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/pybidi
%python_expand %fdupes %{buildroot}%{$python_sitearch}

%check
mv bidi bidi-do-not-use
%pytest_arch
mv bidi-do-not-use bidi

%post
%python_install_alternative pybidi

%postun
%python_uninstall_alternative pybidi

%files %{python_files}
%doc AUTHORS.rst CHANGELOG.rst README.rst
%license COPYING COPYING.LESSER
%python_alternative %{_bindir}/pybidi
%{python_sitearch}/bidi
%{python_sitearch}/python_bidi-%{version}.dist-info

%changelog
