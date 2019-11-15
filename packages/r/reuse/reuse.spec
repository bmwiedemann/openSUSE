#
# spec file for package reuse
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2017 Free Software Foundation Europe e.V.
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


Name:           reuse
Version:        0.5.0
Release:        0
Summary:        A tool for compliance with the REUSE recommendations
License:        GPL-3.0-or-later AND CC-BY-SA-4.0 AND Apache-2.0 AND CC0-1.0
Group:          Development/Languages/Python
Url:            https://git.fsfe.org/reuse/reuse
Source:         https://files.pythonhosted.org/packages/source/f/fsfe-reuse/fsfe-reuse-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  git
BuildRequires:  python-rpm-macros
BuildRequires:  python3 >= 3.6
BuildRequires:  python3-Jinja2
BuildRequires:  python3-binaryornot
BuildRequires:  python3-boolean.py
BuildRequires:  python3-debian
BuildRequires:  python3-devel
BuildRequires:  python3-license-expression
BuildRequires:  python3-pytest
BuildRequires:  python3-requests
BuildRequires:  python3-setuptools
Requires:       python3 >= 3.6
Requires:       python3-Jinja2
Requires:       python3-binaryornot
Requires:       python3-boolean.py
Requires:       python3-debian
Requires:       python3-license-expression
Requires:       python3-requests
Recommends:     git
BuildArch:      noarch

%description
A tool for compliance with the REUSE recommendations.  Essentially,
it is a linter that checks for a project's compliance, and a compiler that
generates a project's bill of materials.

%prep
%setup -q -n fsfe-reuse-%{version}

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{$python3_sitelib}

%check
PYTHONDONTWRITEBYTECODE=1 LC_ALL=C.UTF-8 LANG=C.UTF-8 PYTHONPATH=%{buildroot}%{python3_sitelib} py.test tests/

%files
%defattr(-,root,root,-)
%doc  README.md CHANGELOG.md
%license LICENSES/*
%{_bindir}/reuse
%{python3_sitelib}/*

%changelog
