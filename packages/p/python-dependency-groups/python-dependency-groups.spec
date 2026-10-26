#
# spec file for package python-dependency-groups
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


Name:           python-dependency-groups
Version:        1.3.2
Release:        0
Summary:        A tool for resolving PEP 735 Dependency Group data
License:        MIT
URL:            None
Source:         https://files.pythonhosted.org/packages/source/d/dependency-groups/dependency_groups-%{version}.tar.gz
BuildRequires:  %{python_module flit-core >= 3.11}
BuildRequires:  %{python_module pip}
BuildRequires:  python-rpm-macros
# SECTION test requirements
BuildRequires:  %{python_module packaging}
BuildRequires:  %{python_module pytest}
# /SECTION
BuildRequires:  fdupes
Requires:       python-packaging
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildArch:      noarch
%python_subpackages

%description
An implementation of Dependency Groups (`PEP 735 <https://peps.python.org/pep-0735/>`_).

This is a library which is able to parse dependency groups, following includes,
and provide that data as output.

%prep
%autosetup -p1 -n dependency_groups-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/lint-dependency-groups
%python_clone -a %{buildroot}%{_bindir}/pip-install-dependency-groups
%python_clone -a %{buildroot}%{_bindir}/dependency-groups
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
%python_libalternatives_reset_alternative lint-dependency-groups
%python_libalternatives_reset_alternative pip-install-dependency-groups
%python_libalternatives_reset_alternative dependency-groups

%post
%python_install_alternative lint-dependency-groups pip-install-dependency-groups dependency-groups

%postun
%python_uninstall_alternative lint-dependency-groups pip-install-dependency-groups dependency-groups

%files %{python_files}
%license LICENSE.txt
%python_alternative %{_bindir}/lint-dependency-groups
%python_alternative %{_bindir}/pip-install-dependency-groups
%python_alternative %{_bindir}/dependency-groups
%{python_sitelib}/dependency_groups
%{python_sitelib}/dependency_groups-%{version}.dist-info

%changelog
