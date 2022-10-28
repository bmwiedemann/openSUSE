#
# spec file for package yast2-firstboot
#
# Copyright (c) 2022 SUSE LLC
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


Name:           yast2-firstboot
Version:        4.5.5
Release:        0
Summary:        YaST2 - Initial System Configuration
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-firstboot
Source0:        %{name}-%{version}.tar.bz2
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  hicolor-icon-theme
BuildRequires:  libxslt
BuildRequires:  ruby
BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.2.2
# UI::Wizards::Layout
Requires:       yast2 >= 4.3.16
# Use Yast::Lan.write_config to write hostname changes
Requires:       yast2-configuration-management >= 4.1.3
# Language::SwitchToEnglishIfNeeded
# new keyboard client code layout needed
Requires:       yast2-country >= 4.3.10
# Rely on the YaST2-Firstboot.service for halting the system on failure
Requires:       yast2-installation >= 4.1.2
Requires:       yast2-network >= 4.3.34
Requires:       yast2-ruby-bindings >= 1.0.0
PreReq:         %fillup_prereq
# bsc #1165646
Recommends:     (icewm if libyui-qt)
Supplements:    autoyast(firstboot)
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

%package wsl
Summary:        YaST2 firstboot settings for WSL images
Group:          System/YaST

Requires:       %{name} = %{version}

%description wsl
YaST2 firstboot settings for WSL images

%prep
%setup -q

%build
%yast_build
# enable registration by default on SLE (bsc#1162846)
%if !0%{?is_opensuse}
# lets explain this sed. At first it is address which match line with name
# registration and +1 for next line and then here change false to true
sed -i '/<name>registration/,+1s/false/true/' control/firstboot.xml
sed -i '/<name>registration/,+1s/false/true/' wsl/firstboot.ycontrol.xml
sed -i '/<name>firstboot_wsl_product_selection/,+1s/false/true/' wsl/firstboot.ycontrol.xml
%endif

%install
%yast_install
%yast_metainfo

mkdir -p %{buildroot}%{_datadir}/firstboot/scripts

mkdir -p %{buildroot}%{yast_ydatadir}

install -m 644 wsl/firstboot.ycontrol.xml %{buildroot}%{_sysconfdir}/YaST2/firstboot-wsl.xml
install -m 644 wsl/welcome.txt %{buildroot}%{yast_ydatadir}

%check
# verify defaults for registration
ruby -r rexml/document -e '
  %if !0%{?is_opensuse}
    expected = "true"
  %else
    expected = "false"
  %endif
  document = REXML::Document.new(File.new("control/firstboot.xml"))
  # get value of enabled element in registration module in control.xml to verify it has expected value
  if document.root.elements["//module[name[text()=\"registration\"]]"].elements["enabled"].get_text != expected
    STDERR.puts "Wrong default for registration module"
    exit 1
  end'

%post
%{fillup_only -n firstboot}

%post wsl
sed -i -E 's/(FIRSTBOOT_CONTROL_FILE=).+/\1"\/etc\/YaST2\/firstboot-wsl.xml"/' /etc/sysconfig/firstboot

%postun wsl
sed -i -E 's/(FIRSTBOOT_CONTROL_FILE=).+/\1""/' /etc/sysconfig/firstboot

%files
%license COPYING
%doc %{yast_docdir}
%{yast_ystartupdir}
%{yast_clientdir}
%{yast_libdir}
%{yast_yncludedir}
%{yast_moduledir}
%{yast_scrconfdir}
%{yast_schemadir}
%{_fillupdir}/sysconfig.firstboot
%{_datadir}/firstboot
%{_datadir}/autoinstall
%{_datadir}/icons/hicolor/*/apps/yast-firstboot*
%dir %{_sysconfdir}/YaST2
%{_sysconfdir}/YaST2/firstboot.xml

%files wsl
%{_sysconfdir}/YaST2/firstboot-wsl.xml
%{yast_ydatadir}/welcome.txt

%changelog
