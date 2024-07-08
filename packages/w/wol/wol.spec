#
# spec file for package wol
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


Name:           wol
Version:        0.7.1
Release:        0
Summary:        Wake On Lan client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Boot/Utilities
URL:            https://sourceforge.net/projects/wake-on-lan
Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.rules
Patch0:         wol-0.7.1-Fix-config.h-test-consumption.patch
Patch1:         wol-0.7.1-Fix-malloc-detection.patch
Patch2:         wol-0.7.1-linux-headers.patch
BuildRequires:  autoconf
BuildRequires:  automake
Requires(post): %{install_info_prereq}
Requires(preun): %{install_info_prereq}

%description
The Wake On Lan client wakes up magic packet compliant machines such as
boxes with wake-on-lan ethernet-cards. Some workstations provide
SecureON which extends wake-on-lan with a password. This feature is
also provided by wol.

%package udev-rules
Summary:        Udev rules for activate %{name} via a magic packet on ethernet devices
Group:          System/Kernel
Requires:       ethtool
Requires:       udev
BuildArch:      noarch

%description udev-rules
This package contains the udev rule file for configuring ethernet devices for activate %{name} via a magic packet.

%lang_package

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure --disable-rpath
%make_build

%install
%make_install
install -Dpm0644 %{SOURCE1} %{buildroot}%{_udevrulesdir}/90-%{name}.rules
%find_lang %{name}

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info%{ext_info}

%files
%license COPYING
%doc ABOUT-NLS AUTHORS ChangeLog NEWS README TODO
%{_bindir}/%{name}*
%{_infodir}/%{name}.info%{?ext_info}
%{_mandir}/man?/%{name}.?%{ext_man}

%files udev-rules
%dir %{_udevrulesdir}
%{_udevrulesdir}/90-%{name}.rules

%files -f %{name}.lang lang

%changelog
