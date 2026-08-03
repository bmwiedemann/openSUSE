#
# spec file for package obs-service-update_changelog
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


%{?sle15_python_module_pythons}
Name:           obs-service-update_changelog
Version:        0.6.1
Release:        0
Summary:        An OBS source service: Update spec file version
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/obs-service-update_changelog
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-GitPython
BuildRequires:  python3-Jinja2 >= 2.9
BuildRequires:  python3-devel
BuildRequires:  python3-pip
BuildRequires:  python3-py
BuildRequires:  python3-pytest
BuildRequires:  python3-pytz
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       python3-GitPython
Requires:       python3-Jinja2 >= 2.9
Requires:       python3-py
Requires:       python3-pytz
# Renaming a package
Provides:       python3-obs-service-update_changelog = %{version}
Obsoletes:      python3-obs-service-update_changelog < %{version}
Provides:       %{primary_python}-obs-service-update_changelog = %{version}
Obsoletes:      %{primary_python}-obs-service-update_changelog < %{version}
# changed from singlespec/multiflavor to single flavor on 2026/07
Obsoletes:      python311-obs-service-update_changelog <= 0.6.1
Obsoletes:      python314-obs-service-update_changelog <= 0.6.1

%description
This is a source service for openSUSE Build Service.

Service to update the changelog from git commits.

%prep
%autosetup -p1 -n %{name}-%{version}

%build
%python3_pyproject_wheel

%check
%python3_pytest

%install
%python3_pyproject_install
%makeinstall

rm %{buildroot}%{_bindir}/update_changelog

%fdupes %{buildroot}/%{python3_sitelib}/updatechangelog

%files
%dir /usr/lib/obs
%dir /usr/lib/obs/service
%{python3_sitelib}/updatechangelog
%{python3_sitelib}/updatechangelog-%{version}*-info
/usr/lib/obs/service/update_changelog.service
/usr/lib/obs/service/update_changelog

%changelog
