#
# spec file for package python-dkimpy
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


%{?!python_module:%define python_module() python-%{**} python3-%{**}}
%define skip_python2 1
Name:           python-dkimpy
Version:        0.9.3
Release:        0
Summary:        DKIM (DomainKeys Identified Mail)
License:        BSD-2-Clause
URL:            https://launchpad.net/dkimpy
Source:         https://files.pythonhosted.org/packages/source/d/dkimpy/dkimpy-%{version}.tar.gz
Source99:       https://git.launchpad.net/dkimpy/plain/LICENSE
Patch0:         no-optional.patch
BuildRequires:  %{python_module setuptools}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-PyNaCl
Requires:       python-authres
Requires:       python-dnspython
Requires:       python-setuptools
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module PyNaCl}
BuildRequires:  %{python_module authres}
BuildRequires:  %{python_module dnspython}
BuildRequires:  %{python_module pytest}
# /SECTION
%python_subpackages

%description
DKIM (DomainKeys Identified Mail)

%prep
%setup -q -n dkimpy-%{version}
%patch0 -p1

cp %{SOURCE99} .

%build
cp %{SOURCE99} .
%python_build

%install
%python_install
%python_expand %fdupes %{buildroot}%{$python_sitelib}

%check
%pytest

%files %{python_files}
%doc ChangeLog README
%license LICENSE
%python3_only %{_bindir}/arcsign
%python3_only %{_bindir}/arcverify
%python3_only %{_bindir}/dkimsign
%python3_only %{_bindir}/dkimverify
%python3_only %{_bindir}/dknewkey
%{python_sitelib}/*
%python3_only %{_mandir}/man1/*.1*

%changelog
