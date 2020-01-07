#
# spec file for package suseprime-appindicator
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019 Stasiek Michalski <hellcp@opensuse.org>.
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


Name:           suseprime-appindicator
Version:        0.1.0
Release:        0
Summary:        SUSE Prime appindicator for switching between GPUs
License:        GPL-2.0-only
Group:          System/GUI/Other
URL:            https://github.com/openSUSE/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  hicolor-icon-theme
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base
Requires:       python3-gobject
Requires:       suse-prime
Supplements:    (xfce4-indicator-plugin and suse-prime)
BuildArch:      noarch

%description
SUSE Prime appindicator for switching between Nvidia/Intel GPUs.

%prep
%setup -q

%build
%python3_build

%install
%python3_install
%fdupes %{buildroot}%{python3_sitelib}

%files
%{_datadir}/icons/hicolor/symbolic/apps/*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/scripts
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/%{name}
%{python3_sitelib}/suseprimeindicator*

%changelog
