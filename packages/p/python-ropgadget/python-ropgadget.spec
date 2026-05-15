#
# spec file for package python-ROPGadget
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

%if 0%{?suse_version} > 1500
%bcond_without libalternatives
%else
%bcond_with libalternatives
%endif

Name:           python-ropgadget
Version:        7.7
Release:        0
Summary:        This tool lets you search your gadgets on your binaries to facilitate your ROP exploitation
License:        BSD-3-Clause
URL:            https://github.com/JonathanSalwan/ROPgadget
Source:         https://files.pythonhosted.org/packages/source/r/ropgadget/ropgadget-%{version}.tar.gz
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python3-capstone >= 5.0.1
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  python3-capstone >= 5.0.1
# /SECTION
%if %{with libalternatives}
Requires:       alts
BuildRequires:  alts
%else
Requires(post): update-alternatives
Requires(postun):update-alternatives
%endif

%python_subpackages

%description
This tool lets you search your gadgets on your binaries to facilitate your ROP exploitation.

%prep
%autosetup -p1 -n ropgadget-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ROPgadget
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%pre
%if %{with libalternatives}
%python_libalternatives_reset_alternative <name>
%endif

%post
%python_install_alternative ROPgadget

%postun
%python_uninstall_alternative ROPgadget

%files %{python_files}
%doc AUTHORS README.md
%license LICENSE_BSD.txt
%python_alternative %{_bindir}/ROPgadget
%{python_sitelib}/ropgadget
%{python_sitelib}/ropgadget-%{version}.dist-info

%changelog
