#
# spec file for package python-ldapdomaindump
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2020, Martin Hauke <mardnh@gmx.de>
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


Name:           python-ldapdomaindump
Version:        0.9.4
Release:        0
Summary:        Active Directory information dumper via LDAP
License:        MIT
URL:            https://github.com/dirkjanm/ldapdomaindump/
Source:         https://files.pythonhosted.org/packages/source/l/ldapdomaindump/ldapdomaindump-%{version}.tar.gz
# PATCH-FIX-UPSTREAM Based on gh#dirkjanm/ldapdomaindump#55
Patch0:         remove-future-requirement.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  dos2unix
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-dnspython
Requires:       python-ldap3 >= 2.5
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module ldap3 >= 2.5}
# /SECTION
%python_subpackages

%description
Active Directory information dumper via LDAP.

%prep
%autosetup -p1 -n ldapdomaindump-%{version}
sed -i 's|#!%{_bindir}/env python|#!%{_bindir}/python3|g' \
  bin/ldd2pretty \
  bin/ldapdomaindump \
  bin/ldd2bloodhound
sed -i '/^#!\//, 1d' ldapdomaindump/__main__.py
find . -type f -exec dos2unix {} \;

%build
%pyproject_wheel

%install
%pyproject_install
%python_clone -a %{buildroot}%{_bindir}/ldapdomaindump
%python_clone -a %{buildroot}%{_bindir}/ldd2bloodhound
%python_clone -a %{buildroot}%{_bindir}/ldd2pretty
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%post
%python_install_alternative ldapdomaindump ldd2bloodhound ldd2pretty

%postun
%python_uninstall_alternative ldapdomaindump ldd2bloodhound ldd2pretty

#%%check
# Upstream does not provide tests

%files %{python_files}
%license LICENSE
%doc Readme.md
%python_alternative %{_bindir}/ldapdomaindump
%python_alternative %{_bindir}/ldd2bloodhound
%python_alternative %{_bindir}/ldd2pretty
%{python_sitelib}/ldapdomaindump
%{python_sitelib}/ldapdomaindump-%{version}.dist-info

%changelog
