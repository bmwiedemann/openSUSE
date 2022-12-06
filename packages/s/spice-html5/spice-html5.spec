#
# spec file for package spice-html5
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


Name:           spice-html5
Version:        0.3.0
Release:        0
Summary:        Pure Javascript SPICE client
License:        LGPL-3.0-only
Group:          Productivity/Other
URL:            https://www.spice-space.org
Source0:        https://gitlab.freedesktop.org/spice/%{name}/-/archive/%{name}-%{version}/%{name}-%{name}-%{version}.tar.gz
BuildArch:      noarch

%description
%{name} is a Javascript SPICE client.  This includes a simple HTML
page to initiate a session, and the client itself.  It includes a configuration
file for Apache, but should work with any web server.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build

%install
%make_install

%files
%{_datadir}/%{name}
%license COPYING COPYING.LESSER
%doc README TODO apache.conf.sample

%changelog
