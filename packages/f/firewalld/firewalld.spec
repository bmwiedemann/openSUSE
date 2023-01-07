#
# spec file for package firewalld
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


#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%if 0%{?suse_version} < 1550 && 0%{?sle_version} < 150400
# systemd-rpm-macros(or kmod) is wrong in 15.2 and 15.3
%define _modprobedir /lib/modprobe.d
%endif
%global modprobe_d_files firewalld-sysctls.conf

Name:           firewalld
Version:        1.3.0
Release:        0
Summary:        A firewall daemon with D-Bus interface providing a dynamic firewall
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Security
URL:            https://www.firewalld.org
Source0:        https://github.com/firewalld/firewalld/releases/download/v%{version}/firewalld-%{version}.tar.gz
Source1:        docker-zone.xml
Patch0:         0002-Disable-FlushAllOnReload-option.patch
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  docbook-xsl-stylesheets
# Adding tools to BuildRequires as well so they can be autodetected
# Else the configure tool will set them to /bin/false
BuildRequires:  fdupes
BuildRequires:  ebtables
BuildRequires:  gettext
BuildRequires:  glib2-devel
BuildRequires:  gobject-introspection
BuildRequires:  hicolor-icon-theme
BuildRequires:  intltool
BuildRequires:  ipset
BuildRequires:  iptables
BuildRequires:  libxslt-tools
BuildRequires:  python3-devel
BuildRequires:  systemd-rpm-macros
Recommends:     logrotate
Obsoletes:      firewalld-prometheus-config < 0.2
Provides:       firewalld-prometheus-config = 0.2
# Workaround: nftables seems to be a python3-nftables requirement,
# not of firewalld.
Requires:       nftables
Requires:       python3-firewall = %{version}
Requires:       python3-gobject
Requires:       python3-nftables
Requires(post): %fillup_prereq
Suggests:       susefirewall2-to-firewalld
BuildArch:      noarch
%{?systemd_ordering}

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

%package test
Summary:        Firewalld testsuite
Group:          Productivity/Networking/Security

%description test
This package provides the firewalld testsuite.

%package bash-completion
Summary:        Bash Completion for firewalld
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}-%{release}
Requires:       bash-completion
Supplements:    (%{name} and bash-completion)

%description bash-completion
Bash command line completion support for firewalld.

%package zsh-completion
Summary:        Zsh Completion for firewalld
Group:          Productivity/Networking/Security
Requires:       %{name} = %{version}-%{release}
Requires:       zsh
Supplements:    (%{name} and zsh)

%description zsh-completion
Zsh command line completion support for firewalld.

%lang_package

%prep
%autosetup -p1

# bsc#1078223
rm config/services/high-availability.xml

%build
export PYTHON="%{_bindir}/python3"
autoreconf -fiv
%configure \
  --enable-sysconfig \
  --enable-rpmmacros \
  --with-ifcfgdir="%{_sysconfdir}/sysconfig/network"

# Normally documentation is shipped but this will ensure that missing
# files will be generated.
%make_build

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

# add firewalld zone (rhbz#1817022)
install -dp %{buildroot}%{_prefix}/lib/firewalld/zones
install -p -m 644 %{SOURCE1} %{buildroot}%{_prefix}/lib/firewalld/zones/docker.xml

# No more /etc
mkdir -p %{buildroot}%{_modprobedir}
mv %{buildroot}%{_sysconfdir}/modprobe.d/* %{buildroot}%{_modprobedir}
%if 0%{?suse_version} >= 1550
mkdir -p %{buildroot}%{_distconfdir}/xdg/autostart
mkdir -p %{buildroot}%{_distconfdir}/logrotate.d
mv %{buildroot}%{_sysconfdir}/xdg/autostart/* %{buildroot}%{_distconfdir}/xdg/autostart
mv %{buildroot}%{_sysconfdir}/logrotate.d/firewalld %{buildroot}%{_distconfdir}/logrotate.d/firewalld
%endif

%fdupes %{buildroot}%{python3_sitelib}

%find_lang %{name} --all-name

%pre
%service_add_pre firewalld.service
# Avoid restoring outdated stuff in posttrans
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -f "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}.rpmsave.old" || :
done
%if 0%{?suse_version} > 1500
# Prepare for migration to /usr/etc; save any old .rpmsave
for i in logrotate.d/firewalld ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done
%endif

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
%service_del_postun_without_restart firewalld.service

%posttrans
# Migration of modprobe.conf files to _modprobedir
for _f in %{?modprobe_d_files}; do
    [ ! -f "/etc/modprobe.d/${_f}.rpmsave" ] || \
        mv -fv "/etc/modprobe.d/${_f}.rpmsave" "/etc/modprobe.d/${_f}" || :
done
%if 0%{?suse_version} > 1500
# Migration to /usr/etc, restore just created .rpmsave
for i in logrotate.d/firewalld ; do
   test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

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
%doc README.md
%license COPYING
%{_sbindir}/firewalld
%{_sbindir}/rcfirewalld
%{_bindir}/firewall-cmd
%{_bindir}/firewall-offline-cmd
%dir %{_prefix}/lib/firewalld
%dir %{_prefix}/lib/firewalld/icmptypes
%dir %{_prefix}/lib/firewalld/ipsets
%dir %{_prefix}/lib/firewalld/services
%dir %{_prefix}/lib/firewalld/zones
%dir %{_prefix}/lib/firewalld/helpers
%dir %{_prefix}/lib/firewalld/policies
%{_prefix}/lib/firewalld/icmptypes/*.xml
%{_prefix}/lib/firewalld/ipsets/README.md
%{_prefix}/lib/firewalld/services/*.xml
%{_prefix}/lib/firewalld/zones/*.xml
%{_prefix}/lib/firewalld/helpers/*.xml
%{_prefix}/lib/firewalld/policies/*.xml
%{_datadir}/polkit-1
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/system.d
%dir %{_modprobedir}
%{_modprobedir}/firewalld-sysctls.conf
%config(noreplace) %{_sysconfdir}/firewalld/firewalld.conf
%config(noreplace) %{_sysconfdir}/firewalld/lockdown-whitelist.xml
%if 0%{?suse_version} > 1550
%{_distconfdir}/logrotate.d/firewalld
%else
%config(noreplace) %{_sysconfdir}/logrotate.d/firewalld
%endif
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
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/config
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/core
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/core/io
%attr(0755,root,root) %dir %{python3_sitelib}/firewall/server
%attr(0755,root,root) %{python3_sitelib}/firewall/__pycache__
%attr(0755,root,root) %{python3_sitelib}/firewall/config/__pycache__
%attr(0755,root,root) %{python3_sitelib}/firewall/core/__pycache__
%attr(0755,root,root) %{python3_sitelib}/firewall/core/io/__pycache__
%attr(0755,root,root) %{python3_sitelib}/firewall/server/__pycache__
%{python3_sitelib}/firewall/*.py*
%{python3_sitelib}/firewall/config/*.py*
%{python3_sitelib}/firewall/server/*.py*
%{python3_sitelib}/firewall/core/io/*.py*
%{python3_sitelib}/firewall/core/*.py*

%files -n firewall-macros
%{_rpmmacrodir}/macros.firewalld

%files -n firewall-applet
%attr(0755,root,root) %{_bindir}/firewall-applet
%dir %{_sysconfdir}/firewall
%config(noreplace) %{_sysconfdir}/firewall/applet.conf
%if %{undefined _distconfdir}
%{_sysconfdir}/xdg/autostart/firewall-applet.desktop
%else
%{_distconfdir}/xdg/autostart/firewall-applet.desktop
%endif
%{_datadir}/icons/hicolor/*/apps/firewall-applet*.*
%{_mandir}/man1/firewall-applet*.1%{?ext_man}

%files -n firewall-config
%dir %{_datadir}/firewalld
%attr(0755,root,root) %{_bindir}/firewall-config
%{_datadir}/firewalld/firewall-config.glade
%attr(0755,root,root) %{_datadir}/firewalld/gtk3_chooserbutton.py*
%attr(0755,root,root) %{_datadir}/firewalld/gtk3_niceexpander.py*
%{_datadir}/applications/firewall-config.desktop
%{_datadir}/metainfo/firewall-config.appdata.xml
%{_datadir}/icons/hicolor/*/apps/firewall-config*.*
%{_datadir}/glib-2.0/schemas/org.fedoraproject.FirewallConfig.gschema.xml
%{_mandir}/man1/firewall-config*.1%{?ext_man}

%files test
%dir %{_datadir}/firewalld/testsuite
%{_datadir}/firewalld/testsuite/README.md
%{_datadir}/firewalld/testsuite/testsuite
%dir %{_datadir}/firewalld/testsuite/integration
%{_datadir}/firewalld/testsuite/integration/testsuite
%dir %{_datadir}/firewalld/testsuite/python
%attr(0755,root,root) %{_datadir}/firewalld/testsuite/python/*.py
%attr(0755,root,root) %{_datadir}/firewalld/testsuite/python/__pycache__

%files bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/firewall-cmd

%files zsh-completion
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_firewalld

%files lang -f %{name}.lang

%changelog
