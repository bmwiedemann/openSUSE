#
# spec file for package wofi-pass
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


Name:           wofi-pass
Version:        0.0~git.1646651169.572c0ef
Release:        0
Summary:        Wofi frontend for pass
License:        GPL-2.0-only
URL:            https://gitlab.com/muhq/wofi-pass
Source0:        wofi-pass-%{version}.tar.gz
Source99:       wofi-pass-rpmlintrc
# PATCH-FEATURE-OPENSUSE sway-branding.patch mcepl@suse.com
# Use branding stylesheet in /etc/wofi/style.css
Patch0:         sway-branding.patch
BuildRequires:  /bin/bash
BuildRequires:  findutils
BuildRequires:  pass-otp
BuildRequires:  password-store
BuildRequires:  util-linux
BuildRequires:  wl-clipboard
Recommends:     sway-branding
BuildArch:      noarch

%description
This script uses wofi and wtype to provide a completely
Wayland-native way to conveniently use pass (from
password-storage package). It provides the same search that
passmenu does, but shows a second dialogue that lets the user
choose which field to copy/print.

%prep
%setup -q

%build
:

%install
install -Dm0775 wofi-pass %{buildroot}%{_bindir}/wofi-pass

%files
%license LICENSE
%doc README.md
%{_bindir}/wofi-pass

%changelog
