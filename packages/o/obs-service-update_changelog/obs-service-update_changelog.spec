#
# spec file for package obs-service-update_changelog
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

%{?sle15_python_module_pythons}
Name:           obs-service-update_changelog
Version:        0.6.1
Release:        0
Summary:        An OBS source service: Update spec file version
License:        GPL-2.0+
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/obs-service-update_changelog
Source:         %{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  %{python_module devel}
BuildRequires:  %{python_module setuptools}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module GitPython}
BuildRequires:  %{python_module Jinja2 >= 2.9}
BuildRequires:  %{python_module py}
BuildRequires:  %{python_module pytz}
BuildRequires:  python-rpm-macros
BuildRequires:  fdupes
Requires(post): update-alternatives
Requires(postun): update-alternatives
Requires:       python-GitPython
Requires:       python-Jinja2 >= 2.9
Requires:       python-py
Requires:       python-pytz
%python_subpackages

%description
This is a source service for openSUSE Build Service.

Service to update the changelog from git commits.

%prep
%setup -q -n %{name}-%{version}

%build
%python_build

%check
%pytest

%install
%python_install
%makeinstall

rm %{buildroot}%{_bindir}/update_changelog

%python_expand %fdupes %{buildroot}/%{$python_sitelib}/updatechangelog

%python_clone -a %{buildroot}/usr/lib/obs/service/update_changelog
%python_clone -a %{buildroot}/usr/lib/obs/service/update_changelog.service

%post
%{python_install_alternative /usr/lib/obs/service/update_changelog /usr/lib/obs/service/update_changelog.service}

%postun
%python_uninstall_alternative update_changelog

%files %{python_files}
%dir /usr/lib/obs
%dir /usr/lib/obs/service
%{python_sitelib}/updatechangelog
%{python_sitelib}/updatechangelog-*.egg-info
%python_alternative /usr/lib/obs/service/update_changelog.service
%python_alternative /usr/lib/obs/service/update_changelog

%changelog
