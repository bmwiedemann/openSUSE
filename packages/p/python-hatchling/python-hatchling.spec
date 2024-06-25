#
# spec file for package python-hatchling
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


%{?sle15_python_module_pythons}
Name:           python-hatchling
Version:        1.25.0
Release:        0
Summary:        Build backend used by Hatch
License:        MIT
URL:            https://hatch.pypa.io/latest/
Source0:        https://files.pythonhosted.org/packages/source/h/hatchling/hatchling-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.8}
BuildRequires:  %{python_module packaging >= 21.3}
BuildRequires:  %{python_module pathspec >= 0.10.1}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pluggy >= 1.0.0}
BuildRequires:  %{python_module tomli >= 1.2.2 if %python-base < 3.11}
BuildRequires:  %{python_module trove-classifiers}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-packaging >= 21.3
Requires:       python-pathspec >= 0.10.1
Requires:       python-pluggy >= 1.0.0
Requires:       python-trove-classifiers
Requires:       (python-tomli >= 1.2.2 if python-base < 3.11)
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
This is the extensible, standards compliant build backend used by Hatch.

%prep
%autosetup -n hatchling-%{version} -p1

%build
%pyproject_wheel

%install
%pyproject_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}
%python_clone -a %{buildroot}%{_bindir}/hatchling

%check
# The tests provided in the tarball relies on internet access to run
# (git clone, pip install ...), so they cannot work on obs
# see tests/downstream/integrate.py for details

%post
%python_install_alternative hatchling

%postun
%python_uninstall_alternative hatchling

%files %{python_files}
%doc README.md
%license LICENSE.txt
%{python_sitelib}/hatchling
%{python_sitelib}/hatchling-%{version}.dist-info
%python_alternative %{_bindir}/hatchling

%changelog
