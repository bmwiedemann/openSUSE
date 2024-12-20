#
# spec file for package mobile-broadband-provider-info
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


Name:           mobile-broadband-provider-info
Version:        20240407
Release:        0
Summary:        Mobile Service Provider Database
License:        SUSE-Public-Domain
Group:          Productivity/Networking/System
URL:            http://live.gnome.org/NetworkManager/MobileBroadband/ServiceProviders
# No full URL, as this is a git snapshot (using _service)
Source0:        %{name}-%{version}.tar.xz
Source1:        mobile-broadband-provider-info-rpmlintrc

BuildRequires:  libxml2-tools
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  xsltproc
BuildArch:      noarch

%description
This package contains mobile broadband settings for different service
providers in different countries.

%prep
%autosetup -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%doc README
%{_datadir}/pkgconfig/mobile-broadband-provider-info.pc
%{_datadir}/%{name}/

%changelog
