#
# spec file for package dnf5-actions-snapper
#
# Copyright (c) 2024 SUSE LLC
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

%global dnf5_minver 5.4.0.0

Name:           dnf5-actions-snapper
Version:        0.1
Release:        0
Summary:        A plugin for dnf5 to create snapper plugins
License:        GPL-2.0-or-later
URL:            https://dnf5.readthedocs.io/en/latest/libdnf5_plugins/actions.8.html#an-example-actions-file
Source0:        dnf5-actions-snapper.actions
Requires:       libdnf5-plugin-actions >= %{dnf5_minver}
BuildRequires:  libdnf5-plugin-actions >= %{dnf5_minver}
BuildRequires:  dnf5 >= %{dnf5_minver}
Requires:       dnf5 >= %{dnf5_minver}
Requires:       snapper
Supplements:    (dnf5 and snapper)
BuildArch:      noarch

%description
This plugin allows DNF5 to create snapper plugins
before and after every transaction like zypper would do.

%prep
# Nothing to do

%build
# Nothing to do

%install
mkdir -p %{buildroot}%{_datadir}/dnf5/libdnf.plugins.conf.d/actions.d
install -m 644 %{SOURCE0} %{buildroot}%{_datadir}/dnf5/libdnf.plugins.conf.d/actions.d/dnf5-actions-snapper.actions

%files
%dir %{_datadir}/dnf5/libdnf.plugins.conf.d/actions.d
%{_datadir}/dnf5/libdnf.plugins.conf.d/actions.d/dnf5-actions-snapper.actions

%changelog
