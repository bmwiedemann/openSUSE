
#
# spec file for package spice-html5
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           spice-html5
Version:        0.1.7
Release:        0
Summary:        Pure Javascript SPICE client
Group:          Productivity/Other

License:        LGPL-3.0
URL:            http://www.spice-space.org
Source0:        https://people.freedesktop.org/~jwhite/%{name}/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
%{name} is a Javascript SPICE client.  This includes a simple HTML
page to initiate a session, and the client itself.  It includes a configuration
file for Apache, but should work with any web server.

%prep
%setup -q


%build

%install
%make_install


%files
%{_datadir}/%{name}
%doc README TODO apache.conf.sample
%if 0%{?suse_version} > 1320 || 0%{?leap_version} >= 420200
%license COPYING COPYING.LESSER
%else
%doc COPYING COPYING.LESSER
%endif

%changelog
