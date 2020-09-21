#
# spec file for package firewalld
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
Name:           firewalld
Version:        0.9.0
Release:        0
Summary:        A firewall daemon with D-Bus interface providing a dynamic firewall
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
Url:            http://www.firewalld.org
Source:         https://github.com/firewalld/firewalld/releases/download/v%{version}/firewalld-%{version}.tar.gz
Patch0:         0001-firewall-backend-Switch-default-backend-to-iptables.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-xsl-stylesheets
# Adding tools to BuildRequires as well so they can be autodetected
# even though it is probably unlikely for paths to change in the future
BuildRequires:  ebtables
BuildRequires:  fdupes
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  ipset
BuildRequires:  iptables
BuildRequires:  libxslt-tools
BuildRequires:  nftables
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
Requires:       ebtables
Requires:       ipset
Requires:       iptables
Requires:       logrotate
Requires:       nftables
Requires:       python3-firewall = %{version}
Requires:       python3-nftables
Requires:       sysconfig
Requires(post): %fillup_prereq
Suggests:       susefirewall2-to-firewalld
BuildArch:      noarch
%{?systemd_requires}

%description
firewalld is a firewall service daemon that provides a dynamic customizable
firewall with a D-Bus interface.

%package -n python3-firewall
Summary:        Python3 bindings for FirewallD
Group:          Productivity/Networking/Security
Requires:       dbus-1-python3
Requires:       python3-decorator
Requires:       python3-gobject
Requires:       python3-slip-dbus

%description -n python3-firewall
The python3 bindings for firewalld.

%package -n firewall-macros
Summary:        FirewallD RPM macros
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}-%{release}

%description -n firewall-macros
This package provides the firewalld RPM macros file needed by packages
which provide their own firewalld service files.

%package -n firewall-applet
Summary:        Firewall panel applet
Group:          Productivity/Networking/Security
Requires:       firewall-config = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       python3-gobject
Requires:       python3-qt5

%description -n firewall-applet
The firewall panel applet provides a status information of firewalld and also
the firewall settings.

%package -n firewall-config
Summary:        Firewall configuration application
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}-%{release}
Requires:       hicolor-icon-theme
Requires:       python3-gobject-Gdk

%description -n firewall-config
The firewall configuration application provides an configuration interface for
firewalld.

%lang_package

%prep
%autosetup -p1

# bsc#1078223
rm config/services/high-availability.xml

%build
export PYTHON="%{_bindir}/python3"
./autogen.sh
%configure \
  --enable-sysconfig \
  --enable-rpmmacros \
  --with-ifcfgdir="%{_sysconfdir}/sysconfig/network"

# Normally documentation is shipped but this will ensure that missing
# files will be generated.
make %{?_smp_mflags}

%install
%make_install

%py3_compile %{buildroot}

# remove files that shouldn't exist in the final rpms
rm -r %{buildroot}%{_datadir}/%{name}/__pycache__

desktop-file-install --delete-original \
  --dir %{buildroot}%{_sysconfdir}/xdg/autostart \
  %{buildroot}%{_sysconfdir}/xdg/autostart/firewall-applet.desktop

desktop-file-install --delete-original \
  --dir %{buildroot}%{_datadir}/applications \
  %{buildroot}%{_datadir}/applications/firewall-config.desktop

# fillup_only will take care of that
%{_bindir}/install -c -D -m 600 %{buildroot}%{_sysconfdir}/sysconfig/firewalld %{buildroot}%{_fillupdir}/sysconfig.%{name}
rm %{buildroot}%{_sysconfdir}/sysconfig/firewalld

ln -sf %{_sbindir}/service %{buildroot}/%{_sbindir}/rcfirewalld

%fdupes %{buildroot}%{python3_sitelib}

%find_lang %{name} --all-name

%pre
%service_add_pre firewalld.service

%post
%service_add_post firewalld.service
%fillup_only firewalld

%preun
%service_del_preun firewalld.service

%postun
# We might a have runtime configuration which we haven't
# made it permanent yet so restarting the service could be
# dangerous. It's safer to not touch the firewall ourselves but
# Let the user restart it whenever he feels like it.
export DISABLE_RESTART_ON_UPDATE=yes
%service_del_postun firewalld.service

%post -n firewall-applet
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun -n firewall-applet
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    %{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans -n firewall-applet
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%post -n firewall-config
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun -n firewall-config
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    %{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
    %{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

%posttrans -n firewall-config
%{_bindir}/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
%{_bindir}/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :

%files
%doc README
%license COPYING
%{_sbindir}/firewalld
%{_sbindir}/rcfirewalld
%{_bindir}/firewall-cmd
%{_bindir}/firewall-offline-cmd
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/firewall-cmd
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_firewalld
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/icmptypes
%dir %{_prefix}/lib/firewalld/ipsets
%dir %{_prefix}/lib/firewalld/services
%dir %{_prefix}/lib/firewalld/zones
%dir %{_prefix}/lib/firewalld/helpers
%dir %{_prefix}/lib/firewalld/policies
%{_prefix}/lib/firewalld/icmptypes/*.xml
%{_prefix}/lib/firewalld/ipsets/README
%{_prefix}/lib/firewalld/services/*.xml
%{_prefix}/lib/firewalld/zones/*.xml
%{_prefix}/lib/firewalld/helpers/*.xml
%{_prefix}/lib/firewalld/policies/*.xml
%{_datadir}/polkit-1
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/system.d
%dir %{_sysconfdir}/modprobe.d
%config(noreplace) %{_sysconfdir}/modprobe.d/firewalld-sysctls.conf
%config(noreplace) %{_sysconfdir}/firewalld/firewalld.conf
%config(noreplace) %{_sysconfdir}/firewalld/lockdown-whitelist.xml
%config(noreplace) %{_sysconfdir}/logrotate.d/firewalld
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/icmptypes
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/services
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/zones
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/ipsets
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/helpers
%attr(0750,root,root) %dir %{_sysconfdir}/firewalld/policies
%{_unitdir}/firewalld.service
%{_fillupdir}/sysconfig.%{name}
%{_datadir}/dbus-1/system.d/FirewallD.conf
%{_mandir}/man1/firewall*cmd*.1%{?ext_man}
%{_mandir}/man1/firewalld*.1%{?ext_man}
%{_mandir}/man5/firewall*.5%{?ext_man}

%files -n python3-firewall
%attr(0755,root,root) %dir %{python3_sitelib}/firewall
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/__pycache__
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/config
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/config/__pycache__
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/core
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/core/__pycache__
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/core/io
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/core/io/__pycache__
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/server
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/server/__pycache__
%{python3_sitelib}/firewall/__pycache__/*.py*
%{python3_sitelib}/firewall/*.py*
%{python3_sitelib}/firewall/config/*.py*
%{python3_sitelib}/firewall/config/__pycache__/*.py*
%{python3_sitelib}/firewall/core/*.py*
%{python3_sitelib}/firewall/core/__pycache__/*.py*
%{python3_sitelib}/firewall/core/io/*.py*
%{python3_sitelib}/firewall/core/io/__pycache__/*.py*
%{python3_sitelib}/firewall/server/*.py*
%{python3_sitelib}/firewall/server/__pycache__/*.py*

%files -n firewall-macros
%{_rpmmacrodir}/macros.firewalld

%files -n firewall-applet
%attr(0755,root,root) %{_bindir}/firewall-applet
%dir %{_sysconfdir}/firewall
%config(noreplace) %{_sysconfdir}/firewall/applet.conf
%{_sysconfdir}/xdg/autostart/firewall-applet.desktop
%{_datadir}/icons/hicolor/*/apps/firewall-applet*.*
%{_mandir}/man1/firewall-applet*.1%{?ext_man}

%files -n firewall-config
%dir %{_datadir}/firewalld
%attr(0755,root,root) %{_bindir}/firewall-config
%{_datadir}/firewalld/firewall-config.glade
%attr(0755,root,root) %{_datadir}/firewalld/gtk3_chooserbutton.py*
%attr(0755,root,root) %{_datadir}/firewalld/gtk3_niceexpander.py*
%{_datadir}/applications/firewall-config.desktop
%dir %{_datadir}/metainfo
%{_datadir}/metainfo/firewall-config.appdata.xml
%{_datadir}/icons/hicolor/*/apps/firewall-config*.*
%{_datadir}/glib-2.0/schemas/org.fedoraproject.FirewallConfig.gschema.xml
%{_mandir}/man1/firewall-config*.1%{?ext_man}

%files lang -f %{name}.lang

%changelog
