#
# spec file for package iso-country-flags
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define _name   flags
Name:           iso-country-flags
Version:        1.0.2
Release:        0
Summary:        ISO country flags
License:        GPL-3.0-or-later
Group:          System/GUI/Other
URL:            https://github.com/linuxmint/flags
Source:         https://github.com/linuxmint/%{_name}/archive/%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch

%description
A collection of country flags.

%package png
Summary:        ISO country flags in PNG
License:        SUSE-Public-Domain
Group:          System/GUI/Other

%description png
A collection of country flags in PNG.
They correspond to the fancy 4x3 set in 320x200 resolution.

%prep
%setup -q -n %{_name}-%{version}

%build
# Nothing to build.

%install
cp -a .%{_prefix}/ %{buildroot}%{_prefix}/

%files png
%license debian/copyright
%doc debian/changelog
%{_datadir}/iso-flag-png/

%changelog
