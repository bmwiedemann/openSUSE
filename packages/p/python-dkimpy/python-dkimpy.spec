#
# spec file for package python-dkimpy
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


%define commands arcsign arcverify dkimsign dkimverify dknewkey
%bcond_without libalternatives
%{?sle15_python_module_pythons}
Name:           python-dkimpy
Version:        1.1.8
Release:        0
Summary:        DKIM (DomainKeys Identified Mail)
License:        BSD-2-Clause
URL:            https://launchpad.net/dkimpy
Source:         https://files.pythonhosted.org/packages/source/d/dkimpy/dkimpy-%{version}.tar.gz
Patch0:         no-optional.patch
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module wheel}
BuildRequires:  alts
BuildRequires:  fdupes
BuildRequires:  openssl
BuildRequires:  python-rpm-macros
Requires:       alts
Requires:       python-PyNaCl
Requires:       python-authres
Requires:       python-dnspython >= 1.16
Requires:       python-setuptools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyNaCl}
BuildRequires:  %{python_module authres}
BuildRequires:  %{python_module dnspython >= 1.16}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
DKIM (DomainKeys Identified Mail)

%prep
%autosetup -p1 -n dkimpy-%{version}

%build
%pyproject_wheel

%install
%pyproject_install
for c in %{commands}; do
  %python_clone -a %{buildroot}%{_mandir}/man1/$c.1
  %python_clone -a %{buildroot}%{_bindir}/$c
done
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%pre
for c in %{commands}; do
  %python_libalternatives_reset_alternative $c
done

%files %{python_files}
%doc ChangeLog README.md
%license LICENSE
%python_alternative %{_bindir}/arcsign
%python_alternative %{_bindir}/arcverify
%python_alternative %{_bindir}/dkimsign
%python_alternative %{_bindir}/dkimverify
%python_alternative %{_bindir}/dknewkey
%python_alternative %{_mandir}/man1/arcsign.1%{?ext_man}
%python_alternative %{_mandir}/man1/arcverify.1%{?ext_man}
%python_alternative %{_mandir}/man1/dkimsign.1%{?ext_man}
%python_alternative %{_mandir}/man1/dkimverify.1%{?ext_man}
%python_alternative %{_mandir}/man1/dknewkey.1%{?ext_man}
%{python_sitelib}/dkim
%{python_sitelib}/dkimpy-%{version}.dist-info

%changelog
