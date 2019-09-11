#
# spec file for package mobile-broadband-provider-info
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           mobile-broadband-provider-info
Version:        20190618
Release:        0
Summary:        Mobile Service Provider Database
License:        SUSE-Public-Domain
Group:          Productivity/Networking/System
URL:            http://live.gnome.org/NetworkManager/MobileBroadband/ServiceProviders
# No full URL, as this is a git snapshot (using _service)
Source0:        %{name}-%{version}.tar.xz
Source1:        mobile-broadband-provider-info-rpmlintrc
# PATCH-FIX-UPSTREAM mobile-broadband-provider-info-tmobile-reorder.patch boo#899028 dimstar@opensuse.org -- Move internet.t-d1.de to the bottom
Patch0:         mobile-broadband-provider-info-tmobile-reorder.patch
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildArch:      noarch

%description
This package contains mobile broadband settings for different service
providers in different countries.

%prep
%setup -q
%patch0 -p1

%build
# Needed, as we have a git snapshot
NOCONFIGURE=1 ./autogen.sh
%configure

%install
%make_install

%files
%license COPYING
%doc README
%{_datadir}/pkgconfig/mobile-broadband-provider-info.pc
%{_datadir}/%{name}/

%changelog
