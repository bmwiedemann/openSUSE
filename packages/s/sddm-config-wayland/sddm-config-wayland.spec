# spec file for package sddm-config-wayland 
#
# Copyright (c) 2025 SUSE LLC
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

Name:           sddm-config-wayland
Version:        1.0
Release:        0%{?dist}
Summary:        Config to let SDDM run using wayland

License:        GPL-3.0
URL:            https://github.com/sddm/sddm
Source1:        11-wayland.conf
Source2:        LICENSE
BuildArch:      noarch

Requires:       sddm-qt6
BuildRequires:  sddm-qt6

%description
This package adds a config file to let SDDM run with wayland as backend
instead of X11.

%prep
cp %{SOURCE1} 11-wayland.conf
cp %{SOURCE2} LICENSE

%build

%install
install -D -m 644 11-wayland.conf %{buildroot}%{_prefix}/lib/sddm/sddm.conf.d/11-wayland.conf

%files
%license LICENSE
%{_prefix}/lib/sddm/sddm.conf.d/11-wayland.conf

%changelog
