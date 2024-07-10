#
# spec file for package gcalcli
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


%define pythons python3
Name:           gcalcli
Version:        4.3.0+git14.3e616f7
Release:        0
Summary:        Google Calendar Command Line Interface
License:        MIT
Group:          Productivity/Office/Organizers
URL:            https://github.com/insanum/gcalcli
Source:         %{name}-%{version}.tar.xz
BuildRequires:  python-rpm-macros
BuildRequires:  python3-dateutil
BuildRequires:  python3-google-api-python-client
BuildRequires:  python3-google-auth-oauthlib
BuildRequires:  python3-parsedatetime
BuildRequires:  python3-pytest
BuildRequires:  python3-setuptools
BuildRequires:  python3-vobject
Buildarch:      noarch
Requires:       python3-dateutil
Requires:       python3-google-api-python-client
Requires:       python3-google-auth-oauthlib
Requires:       python3-parsedatetime
Recommends:     python3-vobject

%description
gcalcli is a Python application that allows you to access your Google
Calendar(s) from a command line. It's easy to get your agenda, search for
events, add new events, delete events, edit events, see recently updated
events, and even import those annoying ICS/vCal invites from Microsoft Exchange
and/or other sources. Additionally, gcalcli can be used as a reminder service
and execute any application you want when an event is coming up.

%prep
%autosetup -p1

%build
%python3_build

%install
%python3_install

%check
%pytest

%files
%license LICENSE
%doc ChangeLog docs/README.md docs/*.png
%{_bindir}/gcalcli
%{_mandir}/man1/gcalcli.1%{?ext_man}
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}-*.egg-info

%changelog
