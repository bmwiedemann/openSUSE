#
# spec file for package python-findpython
#
# Copyright (c) 2023 SUSE LLC
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


Name:           python-findpython
Version:        0.2.4
Release:        0
Summary:        Utility to find python versions on your system
License:        MIT
URL:            https://github.com/frostming/findpython
Source:         https://files.pythonhosted.org/packages/source/f/findpython/findpython-%{version}.tar.gz
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module packaging >= 20}
BuildRequires:  %{python_module pdm-pep517}
BuildRequires:  %{python_module pip}
BuildRequires:  fdupes
BuildRequires:  git
BuildRequires:  python-rpm-macros
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module pytest}
# /SECTION
Requires(post): update-alternatives
Requires(postun):update-alternatives
Requires:       python-packaging >= 20
%python_subpackages

%description
Discover which versions of the Python interpreter are present on your
system.

%prep
%autosetup -p1 -n findpython-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/findpython
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%post
%python_install_alternative findpython

%postun
%python_uninstall_alternative findpython

%files %{python_files}
%doc README.md
%license LICENSE
%python_alternative %{_bindir}/findpython
%{python_sitelib}/findpython
%{python_sitelib}/findpython-%{version}*-info

%changelog
