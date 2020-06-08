#
# spec file for package python-vdirsyncer
#
# Copyright (c) 2020 SUSE LLC
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


%define skip_python2 1
%{?!python_module:%define python_module() python-%{**} python3-%{**}}
Name:           python-vdirsyncer
Version:        0.16.7
Release:        0
Summary:        CalDAV and CardDAV synchronization module
License:        BSD-3-Clause
Group:          Productivity/Networking/News/Utilities
URL:            https://github.com/pimutils/vdirsyncer
Source0:        https://files.pythonhosted.org/packages/source/v/vdirsyncer/vdirsyncer-%{version}.tar.gz
Source1:        vdirsyncer.service
Source2:        vdirsyncer.timer
# https://github.com/pimutils/vdirsyncer/pull/779
# https://github.com/pimutils/vdirsyncer/issues/793
Patch0:         python-vdirsyncer-fix-tests.patch
# default deadline (200ms) is too short for obs
Patch1:         python-vdirsyncer-shift-deadline.patch
BuildRequires:  %{python_module atomicwrites}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(systemd)
Requires:       python-atomicwrites >= 0.1.7
Requires:       python-click >= 5.0
Requires:       python-click-log >= 0.3
Requires:       python-click-threading >= 0.2
Requires:       python-icalendar >= 3.6
Requires:       python-lxml
Requires:       python-python-dateutil
Requires:       python-pytz
Requires:       python-requests >= 2.4.1
Requires:       python-requests-toolbelt >= 0.4.0
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     python-requests-oauthlib
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module click-log >= 0.3}
BuildRequires:  %{python_module click-threading >= 0.2}
BuildRequires:  %{python_module hypothesis >= 3.1}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest-subtesthack}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.4.1}
BuildRequires:  %{python_module requests-toolbelt >= 0.4.40}
BuildRequires:  %{python_module urllib3}
# /SECTION
%ifpython3
Provides:       vdirsyncer = %{version}
Obsoletes:      vdirsyncer < %{version}
%endif
%python_subpackages

%description
Vdirsyncer synchronizes calendars and addressbooks between two
storages. The supported storages are CalDAV, CardDAV, arbitrary HTTP
resources, vdir and some more. It aims to be for CalDAV and CardDAV
what OfflineIMAP is for IMAP.

%prep
%setup -q -n vdirsyncer-%{version}
%patch0 -p1
%patch1 -p1
rm -rf vdirsyncer.egg-info

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/vdirsyncer
%python_expand %fdupes %{buildroot}/%{$python_sitelib}

mkdir -p %{buildroot}%{_userunitdir}
install -Dpm 0644 %{SOURCE0} %{buildroot}%{_userunitdir}/vdirsyncer.service
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_userunitdir}/vdirsyncer.timer

%check
export DETERMINISTIC_TESTS=true
# test_verbosity - click changed syntax and returns different quotes
%pytest -k 'not test_legacy_status and not test_open_graphical_browser and not test_verbosity'

%post
%python_install_alternative vdirsyncer

%postun
%python_uninstall_alternative vdirsyncer

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/vdirsyncer
%{python_sitelib}/*
%{_userunitdir}/vdirsyncer.service
%{_userunitdir}/vdirsyncer.timer

%changelog
