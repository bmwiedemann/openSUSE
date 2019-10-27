#
# spec file for package yast2-firstboot
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           yast2-firstboot
Version:        4.2.4
Release:        0
Summary:        YaST2 - Initial System Configuration
License:        GPL-2.0-only
Group:          System/YaST
Url:            https://github.com/yast/yast-firstboot

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  libxslt
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.2.2

PreReq:         %fillup_prereq
# yast2/NeworkDevices -> yast2/NetworkInterfaces
Requires:       yast2 >= 2.16.23
# Language::SwitchToEnglishIfNeeded
Requires:       yast2-country >= 2.19.5
# Rely on the YaST2-Firstboot.service for halting the system on failure
Requires:       yast2-installation >= 4.1.2
# Updated DNS API (unneeded write_hostname= method does not exist anymore)
Requires:       yast2-configuration-management >= 4.1.3
Requires:       yast2-network >= 4.2.14
Requires:       yast2-ruby-bindings >= 1.0.0

BuildArch:      noarch

%description
The YaST firstboot utility runs after installation is completed.  It
guides the user through a series of steps that allows for easier
configuration of the machine.

YaST firstboot does not run by default and has	to be configured to run
by the user or the system administrator. It is useful for image
deployments where the system in the image is completely configured,
however some last steps like root password and user logins have to be
created to personalize the system.

%prep
%setup -q

%build
%yast_build

%install
%yast_install
%yast_metainfo

mkdir -p $RPM_BUILD_ROOT/usr/share/firstboot/scripts

%post
%{fillup_only -n firstboot}

%files
%{yast_ystartupdir}
%{yast_clientdir}
%{yast_libdir}
%{yast_yncludedir}
%{yast_moduledir}
%{yast_scrconfdir}
%{_fillupdir}
%{_datadir}/firstboot
%doc %{yast_docdir}
%license COPYING
%{_sysconfdir}/YaST2
%{_datadir}/autoinstall
%{yast_schemadir}
%{yast_icondir}
%{yast_metainfodir}

%changelog
