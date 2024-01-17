#
# spec file for package yast2-usbauth
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2018 Stefan Koch <stefan.koch10@gmail.com>
# Copyright (c) 2015 SUSE LLC. All Rights Reserved.
# Author: Stefan Koch <skoch@suse.de>
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


Name:           yast2-usbauth
Version:        0.9
Release:        0

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.bz2
Url:            https://github.com/kochstefan/yast-usbauth

BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools
BuildRequires:  yast2-ruby-bindings
BuildRequires:  rubygem(yast-rake)
Requires:       libusbauth-configparser1
Requires:       xdg-utils
Requires:       yast2
Requires:       yast2-ruby-bindings
Requires:       rubygem(ffi)
Recommends:     usbauth

BuildArch:      noarch

Summary:        YaST2 component for usbauth configuration
License:        GPL-2.0-only
Group:          System/YaST

%description
YaST module that helps to create an usbauth firewall config file

%prep
%setup -n %{name}-%{version}

%install
rake install DESTDIR="%{buildroot}"

%files
%defattr(-,root,root)
%{yast_dir}/clients/*.rb
%{yast_dir}/lib
%{yast_desktopdir}

%license COPYING

%build

%changelog
