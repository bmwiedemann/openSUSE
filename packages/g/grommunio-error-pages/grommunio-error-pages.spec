#
# spec file for package grommunio-error-pages
#
# Copyright (c) 2023 SUSE LLC
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


Name:           grommunio-error-pages
Version:        1.0.6.9c50afb
Release:        0
Summary:        Grommunio-branded error pages for web servers
License:        CC-BY-SA-4.0
Group:          Productivity/Networking/Email/Servers
URL:            https://grommunio.com/
Source:         grommunio-error-pages-%version.tar.xz
BuildArch:      noarch

%description
Grommunio-branded error pages for web servers.

%prep
%autosetup

%build

%install
%make_install

%files
%_datadir/grommunio*
%license LICENSE.txt

%changelog
