#
# spec file for package opendchub
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


Name:           opendchub
Version:        0.8.3
Release:        0
Summary:        DirectConnect++ Hub Server
License:        GPL-2.0+
Group:          Productivity/Networking/File-Sharing
Url:            http://opendchub.sf.net/

Source:         http://downloads.sf.net/opendchub/%name-%version.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  libcap-devel
BuildRequires:  libnsl-devel
%{?libperl_requires}

%description
Open DC hub is a Unix/Linux version of the hub software for the
Direct Connect network, a file distribution network made up by hubs,
to which clients can connect. Once connected to a hub, the user can
search for files on the hub or the network, or browse files of other
users connected to the hub.

%prep
%setup -q

%build
chmod a+x configure
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc COPYING Documentation/*
%_bindir/*

%changelog
