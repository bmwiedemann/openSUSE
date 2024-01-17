#
# spec file for package python-ldaptor
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


%define binaries ldaptor-fetchschema ldaptor-find-server ldaptor-getfreenumber ldaptor-ldap2dhcpconf ldaptor-ldap2dnszones ldaptor-ldap2maradns ldaptor-ldap2passwd ldaptor-ldap2pdns ldaptor-ldifdiff ldaptor-ldifpatch ldaptor-namingcontexts ldaptor-passwd ldaptor-rename ldaptor-search
%{?sle15_python_module_pythons}
Name:           python-ldaptor
Version:        21.2.0
Release:        0
Summary:        A Pure-Python Twisted library for LDAP
License:        MIT
Group:          Development/Languages/Python
URL:            https://github.com/twisted/ldaptor
Source:         https://files.pythonhosted.org/packages/source/l/ldaptor/ldaptor-%{version}.tar.gz
# PATCH-FIX-UPSTREAM remove-infinite-tmpfile-creation.patch -- gh#twisted/ldaptor#238
Patch1:         remove-infinite-tmpfile-creation.patch
BuildRequires:  %{python_module Twisted-tls}
BuildRequires:  %{python_module passlib}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pyparsing}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  %{python_module zope.interface}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-Twisted-tls
Requires:       python-passlib
Requires:       python-pyparsing
Requires:       python-zope.interface
Requires(post): update-alternatives
Requires(postun):update-alternatives
BuildArch:      noarch
%python_subpackages

%description
Ldaptor is a pure-Python library that implements:

- LDAP client logic
- separately-accessible LDAP and BER protocol message generation/parsing
- ASCII-format LDAP filter generation and parsing
- LDIF format data generation
- Samba password changing logic

%prep
%autosetup -p1 -n ldaptor-%{version}
sed -i '1 {/env python/ d}' ldaptor/ldapfilter.py
# six is not used anymore, remove from metadata
sed -i '/six/d' setup.cfg

%build
%pyproject_wheel

%install
# remove .egg for proper pip install in 15.4
rm -r ldaptor.egg-info
%pyproject_install
for b in %{binaries}; do
  %python_clone -a %{buildroot}%{_bindir}/$b
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%{python_expand # twisted.trial: see tox config
export PYTHONPATH=%{buildroot}/%{$python_sitelib}
$python -m twisted.trial ldaptor
}

%post
%{lua:for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_install_alternative " .. b .. "\n"))
end}

%postun
%{lua:for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_uninstall_alternative " .. b.. "\n"))
end}

%files %{python_files}
%doc README.rst
%license LICENSE
%{python_sitelib}/ldaptor
%{python_sitelib}/ldaptor-%{version}*-info
%{lua:for b in rpm.expand("%{binaries}"):gmatch("%S+") do
  print(rpm.expand("%python_alternative %{_bindir}/" .. b.. "\n"))
end}

%changelog
