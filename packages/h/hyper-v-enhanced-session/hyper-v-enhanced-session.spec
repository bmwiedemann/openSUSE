#
# spec file for package hyper-v-enhanced-session
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


Name:           hyper-v-enhanced-session
Version:        1.0.1
Release:        0
Summary:        Hyper-V Enhanced session setup for openSUSE
BuildArch:      noarch
License:        GPL-2.0-only
URL:            https://github.com/sbradnick/%{name}
Source:         %{name}-%{version}.tar.gz
BuildRequires:  systemd-rpm-macros
Requires:       hyper-v
# ---
#Requires:       lightdm
Requires:       (lightdm or gdm or kdm)
Suggests:       lightdm
Conflicts:      sddm
# ---
Requires:       xrdp
Requires:       vncmanager
Requires:       xmessage
Requires:       xorg-x11-Xvnc-novnc
Requires:       xorgxrdp
Recommends:     icewm-default
Suggests:       xfce4-session
Suggests:       gnome-session-core
Suggests:       plasma5-session

%description
* Completes pre-requisite setup for an openSUSE VM on Hyper-V to be able to use "Enhanced session".
* Works with lightdm, NOT sddm. gdm isn't an issue and is difficult to remove from a Gnome install.
* In PowerShell, run 'Set-VM -VMName <name of vm> -EnhancedSessionTransportType HvSocket' to enable.
* Provides /etc/xrdp/startwm.sh.userwindowmanager-sample to use in '$HOME'.

%prep
%setup

%build

%install
mkdir -p %{buildroot}%{_presetdir}
mkdir -p %{buildroot}%{_sysconfdir}/X11
mkdir -p %{buildroot}%{_sysconfdir}/xrdp
mkdir -p %{buildroot}%{_modulesloaddir}
install -m 0644 91-default-xrdp.preset "%{buildroot}%{_presetdir}/91-default-xrdp.preset"
install -m 0644 startwm.sh "%{buildroot}%{_sysconfdir}/xrdp/startwm.sh.userwindowmanager-sample"
install -m 0644 xrdp.ini "%{buildroot}%{_sysconfdir}/xrdp/xrdp.ini.enhanced"
install -m 0644 sesman.ini "%{buildroot}%{_sysconfdir}/xrdp/sesman.ini.enhanced"
install -m 0644 hv_sock.conf "%{buildroot}%{_modulesloaddir}/hv_sock.conf"
install -m 0644 Xwrapper.config "%{buildroot}%{_sysconfdir}/X11/Xwrapper.config"

%pre
# ---
if [ -e %{_sysconfdir}/xrdp/xrdp.ini ];
then
  cp %{_sysconfdir}/xrdp/xrdp.ini %{_sysconfdir}/xrdp/xrdp.ini.pre-enhanced
fi
# ---
if [ -e %{_sysconfdir}/xrdp/sesman.ini ];
then
  cp %{_sysconfdir}/xrdp/sesman.ini %{_sysconfdir}/xrdp/sesman.ini.pre-enhanced
fi
# ---
if [ -e %{_sysconfdir}/X11/Xwrapper.config ];
then
  cp %{_sysconfdir}/X11/Xwrapper.config %{_sysconfdir}/X11/Xwrapper.config.pre-enhanced
fi
# ---
if [ -e %{_sysconfdir}/sysconfig/displaymanager ];
then
  cp %{_sysconfdir}/sysconfig/displaymanager %{_sysconfdir}/sysconfig/displaymanager.pre-enhanced
  sed -i 's/DISPLAYMANAGER_REMOTE_ACCESS="no"/DISPLAYMANAGER_REMOTE_ACCESS="yes"/g' %{_sysconfdir}/sysconfig/displaymanager
  sed -i 's/DISPLAYMANAGER_ROOT_LOGIN_REMOTE="no"/DISPLAYMANAGER_ROOT_LOGIN_REMOTE="yes"/g' %{_sysconfdir}/sysconfig/displaymanager
fi

%post
# ---
if [ -e %{_sysconfdir}/xrdp/xrdp.ini.enhanced ];
then
  %{_bindir}/cp -f %{_sysconfdir}/xrdp/xrdp.ini.enhanced %{_sysconfdir}/xrdp/xrdp.ini
fi
# ---
if [ -e %{_sysconfdir}/xrdp/sesman.ini.enhanced ];
then
  %{_bindir}/cp -f %{_sysconfdir}/xrdp/sesman.ini.enhanced %{_sysconfdir}/xrdp/sesman.ini
fi
# ---
if [ -e %{_bindir}/firewall-cmd ];
then
  for service in ms-wbt tigervnc tigervnc-https
  do
    if [ $(%{_bindir}/firewall-cmd --query-service=$service) = "no" ];
    then
      printf "\nAdding firewall rules for $service:\n"
      %{_bindir}/firewall-cmd --add-service=$service
      %{_bindir}/firewall-cmd --add-service=$service --permanent
    fi
  done
fi
# ---
# This is required for services to be enabled at [next] boot.
if [ -e %{_bindir}/systemctl ];
then
  printf "\nRunning systemctl preset commands for xrdp, xrdp-sesman, xvnc-novnc, and vncmanager:\n"
  %{_bindir}/systemctl preset xrdp.service
  %{_bindir}/systemctl preset xrdp-sesman.service
  %{_bindir}/systemctl preset xvnc-novnc.socket
  %{_bindir}/systemctl preset vncmanager.service
fi
# ---
printf "\n\n***    ALERT: POWER THE VM DOWN AND CLOSE CONSOLE WINDOW.\n\n"
printf "*** REQUIRED: In PowerShell, run 'Set-VM -VMName <name of vm> -EnhancedSessionTransportType HvSocket' to enable.\n"
printf "***     NOTE: Copy /etc/xrdp/startwm.sh.userwindowmanager-sample to <your home dir>/startwm.sh, chmod +x, and customize to preference."

%files
%dir %{_sysconfdir}/xrdp
%dir %{_modulesloaddir}
%config %{_sysconfdir}/xrdp/startwm.sh.userwindowmanager-sample
%config %{_sysconfdir}/xrdp/xrdp.ini.enhanced
%config %{_sysconfdir}/xrdp/sesman.ini.enhanced
%config %{_sysconfdir}/X11/Xwrapper.config
%{_modulesloaddir}/hv_sock.conf
%{_presetdir}/91-default-xrdp.preset

%changelog
