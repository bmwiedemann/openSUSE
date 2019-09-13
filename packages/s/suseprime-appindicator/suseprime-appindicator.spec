#
# spec file for package suseprime-appindicator
#
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           suseprime-appindicator
Version:        0.1.0
Release:        0
Summary:        SUSE Prime appindicator for switching between GPUs
Group:          System/GUI/Other
License:        GPL-2.0
Url:            https://github.com/openSUSE/%{name}
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  hicolor-icon-theme
BuildRequires:  python-setuptools
BuildRequires:  python3

Requires:       suse-prime
Requires:       python3-gobject

Supplements:    (xfce4-indicator-plugin and suse-prime)
BuildArch:      noarch

%description
SUSE Prime appindicator for switching between Nvidia/Intel GPUs.

%prep
%setup -q

%build
# Skip build

%install
python3 setup.py install --root=%{buildroot}

%files
%{_datadir}/icons/hicolor/symbolic/apps/*
%dir %{_datadir}/%{name}/
%{_datadir}/%{name}/scripts
%{_sysconfdir}/xdg/autostart/%{name}.desktop
%{_bindir}/%{name}
%{python3_sitelib}/suseprimeindicator*

%changelog