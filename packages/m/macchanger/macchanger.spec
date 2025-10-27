#
# spec file for package macchanger
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


Name:           macchanger
Version:        1.7.0
Release:        0
Summary:        Utility for viewing/manipulating the MAC address of network interfaces
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Other
URL:            https://github.com/alobbs/macchanger
Source:         https://github.com/alobbs/macchanger/releases/download/%{version}/%{name}-%{version}.tar.gz
Requires(pre):  %{install_info_prereq}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A GNU/Linux utility for viewing/manipulating the MAC address of network interfaces.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-, root, root)
%{_bindir}/macchanger
%doc README
%{_datadir}/macchanger
%{_infodir}/macchanger.info%{ext_info}
%{_mandir}/man1/macchanger.1%{ext_man}
%license COPYING

%post
%install_info --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%preun
%install_info_delete --info-dir=%{_infodir} %{_infodir}/%{name}.info.gz

%changelog
