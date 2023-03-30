#
# spec file
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2018 Matthias Fehring <buschmann23@opensuse.org>
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
%define _pkgname celery-batches
Name:           python-%{_pkgname}
Version:        0.7
Release:        0
Summary:        Django module to process multiple Celery task requests together
License:        BSD-3-Clause
Group:          Development/Languages/Python
URL:            https://github.com/percipient/celery-batches
Source:         https://github.com/percipient/%{_pkgname}/archive/v%{version}.tar.gz#/%{_pkgname}-%{version}.tar.gz
Patch0:         celery-fixtures.patch
BuildRequires:  %{python_module base >= 3.7}
BuildRequires:  %{python_module celery >= 4.4}
BuildRequires:  %{python_module coverage}
BuildRequires:  %{python_module pip}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module pytz}
BuildRequires:  %{python_module wheel}
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
Requires:       python-celery >= 4.4
BuildArch:      noarch
%python_subpackages

%description
An alternate way to have Django DRY forms. The developer can build
programmatic reusable layouts out of components, having control of
the rendered HTML without writing HTML in templates, without breaking
the standard way of doing things in Django, so that it still works
with any other form application.

%prep
%autosetup -p1 -n %{_pkgname}-%{version}

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest t/

%files %{python_files}
%doc README.rst CHANGELOG.rst
%license LICENSE
%{python_sitelib}/*

%changelog
