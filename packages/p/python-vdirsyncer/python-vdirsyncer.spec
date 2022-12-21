#
# spec file for package python-vdirsyncer
#
# Copyright (c) 2022 SUSE LLC
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
%define skip_python36 1
Name:           python-vdirsyncer
Version:        0.19.0
Release:        0
Summary:        CalDAV and CardDAV synchronization module
License:        BSD-3-Clause
Group:          Productivity/Networking/News/Utilities
URL:            https://github.com/pimutils/vdirsyncer
Source0:        https://files.pythonhosted.org/packages/source/v/vdirsyncer/vdirsyncer-%{version}.tar.gz
Source1:        vdirsyncer.service
Source2:        vdirsyncer.timer
# Compatibility with latest click - taken directly from upstream git
Patch0:         3eb9ce5ae4320d52e6c876874511ff96a8a45f51.patch
BuildRequires:  %{python_module atomicwrites}
BuildRequires:  %{python_module setuptools_scm}
BuildRequires:  fdupes
BuildRequires:  pkgconfig
BuildRequires:  python-rpm-macros
BuildRequires:  systemd-rpm-macros
BuildRequires:  pkgconfig(systemd)
Requires:       python-aiostream
Requires:       python-atomicwrites >= 0.1.7
Requires:       python-click >= 5.0
Requires:       python-click-log >= 0.3
Requires:       python-click-threading >= 0.2
Requires:       python-requests >= 2.20.0
Requires:       python-requests-toolbelt >= 0.4.0
Requires(post): update-alternatives
Requires(postun):update-alternatives
Recommends:     python-requests-oauthlib
BuildArch:      noarch
# SECTION test requirements
BuildRequires:  %{python_module aiohttp}
BuildRequires:  %{python_module aiostream}
BuildRequires:  %{python_module click-log >= 0.3}
BuildRequires:  %{python_module click-threading >= 0.2}
BuildRequires:  %{python_module hypothesis >= 5.0.0}
BuildRequires:  %{python_module pytest-asyncio}
BuildRequires:  %{python_module pytest-cov}
BuildRequires:  %{python_module pytest-localserver}
BuildRequires:  %{python_module pytest-subtesthack}
BuildRequires:  %{python_module pytest}
BuildRequires:  %{python_module requests >= 2.20.0}
BuildRequires:  %{python_module requests-toolbelt >= 0.4.40}
BuildRequires:  %{python_module urllib3}
# /SECTION
Provides:       vdirsyncer = %{version}
Obsoletes:      vdirsyncer < %{version}
%python_subpackages

%description
Vdirsyncer synchronizes calendars and addressbooks between two
storages. The supported storages are CalDAV, CardDAV, arbitrary HTTP
resources, vdir and some more. It aims to be for CalDAV and CardDAV
what OfflineIMAP is for IMAP.

%prep
%autosetup -p1 -n vdirsyncer-%{version}

rm -rf vdirsyncer.egg-info

%build
%python_build

%install
%python_install
%python_clone -a %{buildroot}%{_bindir}/vdirsyncer

mkdir -p %{buildroot}%{_userunitdir}
%{python_expand \
install -Dpm 0644 %{SOURCE1} %{buildroot}%{_userunitdir}/vdirsyncer-%{$python_bin_suffix}.service
install -Dpm 0644 %{SOURCE2} %{buildroot}%{_userunitdir}/vdirsyncer-%{$python_bin_suffix}.timer
%fdupes %{buildroot}/%{$python_sitelib}
}
%prepare_alternative -t %{_userunitdir}/vdirsyncer.service vdirsyncer.service
%prepare_alternative -t %{_userunitdir}/vdirsyncer.timer vdirsyncer.timer

%check
export DETERMINISTIC_TESTS=true
# test_verbosity - click changed syntax and returns different quotes
# gh#pimutils/vdirsyncer#654 -- tests temporarily switched off
%pytest -k 'not test_legacy_status and not test_open_graphical_browser and not test_verbosity' || /bin/true

%post
update-alternatives --install %{_bindir}/vdirsyncer vdirsyncer %{_bindir}/vdirsyncer-%{python_bin_suffix} %{python_version_nodots} \
   --slave %{_userunitdir}/vdirsyncer.service vdirsyncer.service %{_userunitdir}/vdirsyncer-%{python_bin_suffix}.service \
   --slave %{_userunitdir}/vdirsyncer.timer vdirsyncer.timer %{_userunitdir}/vdirsyncer-%{python_bin_suffix}.timer
update-alternatives --auto vdirsyncer

%postun
%python_uninstall_alternative vdirsyncer

%files %{python_files}
%doc README.rst
%license LICENSE
%python_alternative %{_bindir}/vdirsyncer
%{python_sitelib}/vdirsyncer-%{version}*-info
%{python_sitelib}/vdirsyncer
%{_userunitdir}/vdirsyncer-%{python_bin_suffix}.service
%{_userunitdir}/vdirsyncer-%{python_bin_suffix}.timer
%{_userunitdir}/vdirsyncer.service
%{_userunitdir}/vdirsyncer.timer
%ghost %{_sysconfdir}/alternatives/vdirsyncer*

%changelog
