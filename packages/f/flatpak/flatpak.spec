#
# spec file for package flatpak
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


%global selinuxtype targeted
%define libname libflatpak0
%define bubblewrap_version 0.8.0
%define ostree_version 2020.8
%define xdg_dbus_proxy_version 0.1.0

# dbus only used config files in /etc until 1.9.18
%if %{pkg_vcmp dbus-1 < 1.9.18}
%define _dbusconfigdir %{_sysconfdir}/dbus-1/system.d
%else
%define _dbusconfigdir %{_datadir}/dbus-1/system.d
%endif
# systemd only supports environment generators since version 233
%if %{pkg_vcmp systemd < 233}
%define support_environment_generators 0
%else
%define support_environment_generators 1
%endif
Name:           flatpak
Version:        1.15.8
Release:        0
Summary:        OSTree based application bundles management
License:        LGPL-2.1-or-later
Group:          System/Packages
URL:            https://flatpak.github.io/
Source0:        https://github.com/flatpak/flatpak/releases/download/%{version}/%{name}-%{version}.tar.xz
Source1:        update-system-flatpaks.service
Source2:        update-system-flatpaks.timer
Source3:        update-user-flatpaks.service
Source4:        update-user-flatpaks.timer
Source5:        https://flathub.org/repo/flathub.flatpakrepo
# PATCH-FEATURE-OPENSUSE polkit_rules_usability.patch -- Make the rules comply with openSUSE expectations
Patch0:         polkit_rules_usability.patch
# PATCH-FIX-UPSTREAM libglnx.patch https://gitlab.gnome.org/GNOME/libglnx/-/merge_requests/57
Patch1:         libglnx.patch

BuildRequires:  bison
BuildRequires:  bubblewrap >= %{bubblewrap_version}
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gtk-doc
BuildRequires:  intltool >= 0.35.0
BuildRequires:  libcap-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libgpgme-devel >= 1.1.8
BuildRequires:  libtool
BuildRequires:  meson
BuildRequires:  pkgconfig
BuildRequires:  python3-pyparsing
BuildRequires:  selinux-policy-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  sysuser-tools
BuildRequires:  xdg-dbus-proxy >= %{xdg_dbus_proxy_version}
BuildRequires:  xmlto
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(appstream) >= 0.12.0
BuildRequires:  pkgconfig(dconf) >= 0.26
BuildRequires:  pkgconfig(fuse3) >= 3.1.1
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.46
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.40.0
BuildRequires:  pkgconfig(gobject-introspection-no-export-1.0) >= 1.40.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libarchive) >= 2.8.0
BuildRequires:  pkgconfig(libcurl) >= 7.29.0
BuildRequires:  pkgconfig(libelf) >= 0.8.12
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libxml-2.0) >= 2.4
BuildRequires:  pkgconfig(libzstd) >= 0.8.1
BuildRequires:  pkgconfig(ostree-1) >= %{ostree_version}
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(wayland-client) >= 1.15
BuildRequires:  pkgconfig(wayland-protocols) >= 1.32
BuildRequires:  pkgconfig(wayland-scanner) >= 1.15
BuildRequires:  pkgconfig(xau)
Requires:       %{libname} = %{version}
Requires:       bubblewrap >= %{bubblewrap_version}
Requires:       ostree >= %{ostree_version}
Requires:       xdg-dbus-proxy >= %{xdg_dbus_proxy_version}
Requires:       xdg-desktop-portal >= 0.10
Requires:       (flatpak-selinux = %{version} if selinux-policy-%{selinuxtype})
Requires:       user(flatpak)
# Remove after openSUSE Leap 42 is out of scope
Provides:       xdg-app = %{version}
Obsoletes:      xdg-app < %{version}

%description
flatpak is a system for building, distributing and running sandboxed desktop
applications on Linux. See https://wiki.gnome.org/Projects/SandboxedApps for
more information.

%package -n system-user-flatpak
Summary:        System user for the flatpak system helper
Group:          System/Base
BuildArch:      noarch
%sysusers_requires

%description -n system-user-flatpak
System user for the flatpak system helper.

%package -n %{libname}
Summary:        OSTree based application bundle management library
Group:          System/Libraries

%description -n %{libname}
flatpak is a system for building, distributing and running sandboxed desktop
applications on Linux. See https://wiki.gnome.org/Projects/SandboxedApps for
more information.

%package -n typelib-1_0-Flatpak-1_0
Summary:        Introspection bindings for the flatpak library
Group:          System/Libraries

%description -n typelib-1_0-Flatpak-1_0
flatpak is a system for building, distributing and running sandboxed desktop
applications on Linux. See https://wiki.gnome.org/Projects/SandboxedApps for
more information.

%package zsh-completion
Summary:        Zsh tab-completion for flatpak
Group:          System/Shells
Supplements:    (%{name} and zsh)
BuildArch:      noarch

%description zsh-completion
flatpak is a system for building, distributing and running sandboxed desktop
applications on Linux. See https://wiki.gnome.org/Projects/SandboxedApps for
more information.

This package provides zsh tab-completion for flatpak.

%package devel
Summary:        Development files for the flatpak library
Group:          Development/Languages/C and C++
Requires:       %{libname} = %{version}
Requires:       %{name} = %{version}
Requires:       typelib-1_0-Flatpak-1_0 = %{version}

%description devel
flatpak is a system for building, distributing and running sandboxed desktop
applications on Linux. See https://wiki.gnome.org/Projects/SandboxedApps for
more information.

%package remote-flathub
Summary:        Add Flathub repository to system flatpak
Group:          System/Packages
Requires:       flatpak
Requires(postun): flatpak
Requires(postun): sed
%if 0%{?suse_version} > 1600
Supplements:    flatpak
%endif
BuildArch:      noarch

%description remote-flathub
Flathub is a widely used repository for Flatpak applications. This package
adds the Flathub repository to the list of system flatpak remotes.

%package selinux
Summary:        SELinux policy module for flatpak
Group:          System Environment/Base
Requires:       flatpak
BuildArch:      noarch
%{?selinux_requires}

%description selinux
flatpak is a system for building, distributing and running sandboxed desktop
applications on Linux. See https://wiki.gnome.org/Projects/SandboxedApps for
more information.

This package provides the SELinux policy module for flatpak.

%postun remote-flathub
# upon uninstall
if [ $1 == 0 ]; then
# unregister the remote
flatpak remote-delete --system flathub
# and make sure it gets re-applied upon next install
sed -i "/^xa\.applied-remotes=/s/flathub[;]*//" %{_localstatedir}/lib/flatpak/repo/config
fi

%lang_package

%python3_fix_shebang

%prep
%autosetup -p1
sed -i -e '1s,#!%{_bindir}/env python3,#!%{_bindir}/python3,' scripts/flatpak-*

%build
%meson \
        -Dsystem_bubblewrap=%{_bindir}/bwrap \
        -Dhttp_backend=curl \
        -Ddbus_config_dir=%{_dbusconfigdir} \
        -Dsystem_dbus_proxy=%{_bindir}/xdg-dbus-proxy \
%if !%{support_environment_generators}
        -Dgdm_env_file=enabled \
%endif
        -Dgtkdoc=enabled \
        -Dwayland_security_context=enabled \
        -Dselinux_module=enabled \
        -Dtests=false \
        -Dmalcontent=disabled \
        %{nil}
%meson_build
%sysusers_generate_pre system-helper/flatpak.conf system-user-flatpak flatpak.conf

%install
%meson_install
find %{buildroot} -type f -name "*.la" -delete -print
mkdir -p %{buildroot}%{_sbindir}
ln -s service %{buildroot}%{_sbindir}/rcflatpak-system-helper
# add a 60- prefix to the rules file, otherwise it is not effective, because
# /etc/polkit-1/rules.d/90-default-privs.rules is executed first and if no
# polkit-default-privs rule grants access then an explicit reject is the
# result. This should fix bsc#984817, granting members of group wheel access
# w/o password entry.
mv %{buildroot}/%{_datadir}/polkit-1/rules.d/{,60-}org.freedesktop.Flatpak.rules

%if !%{support_environment_generators}
rm -Rf %{buildroot}%{_systemd_user_env_generator_dir}
rm -Rf %{buildroot}%{_systemd_system_env_generator_dir}
%endif

# System update Systemd service and timer units
install -D -m 644 -t %{buildroot}%{_unitdir} %{SOURCE1}
install -D -m 644 -t %{buildroot}%{_unitdir} %{SOURCE2}

# User update Systemd service and timer units
install -D -m 644 -t %{buildroot}%{_userunitdir} %{SOURCE3}
install -D -m 644 -t %{buildroot}%{_userunitdir} %{SOURCE4}

# Flathub remote repository
install -D -m 644 -t %{buildroot}%{_sysconfdir}/flatpak/remotes.d %{SOURCE5}

%find_lang %{name}

%pre -n system-user-flatpak -f system-user-flatpak.pre
%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%pre
%service_add_pre flatpak-system-helper.service
%service_add_pre update-system-flatpaks.service
%service_add_pre update-system-flatpaks.timer

%preun
%service_del_preun flatpak-system-helper.service
%service_del_preun update-system-flatpaks.service
%service_del_preun update-system-flatpaks.timer

%post
%service_add_post flatpak-system-helper.service
%service_add_post update-system-flatpaks.service
%service_add_post update-system-flatpaks.timer
# Remove any empty repo directory, which is seen as invalid by flatpak. After that, create a skeleton repository using "flatpak remotes".
if [ -e "%{_localstatedir}/lib/flatpak/repo" ] && [ -z "$(ls -A %{_localstatedir}/lib/flatpak/repo)" ]; then
rm -r %{_localstatedir}/lib/flatpak/repo
fi
%{_bindir}/flatpak remotes 1> /dev/null
%tmpfiles_create %{_tmpfilesdir}/flatpak.conf

%postun
%service_del_postun flatpak-system-helper.service
%service_del_postun update-system-flatpaks.service
%service_del_postun update-system-flatpaks.timer

%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/flatpak.pp.bz2

%preun selinux
%selinux_relabel_pre -s %{selinuxtype}

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} flatpak
    %selinux_relabel_post -s %{selinuxtype}
fi;

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}

%files -f %{name}.lang
%license COPYING
%{_bindir}/flatpak
%{_libexecdir}/flatpak-portal
%{_libexecdir}/flatpak-session-helper
%{_libexecdir}/flatpak-system-helper
%{_libexecdir}/flatpak-validate-icon
%{_libexecdir}/revokefs-fuse
%{_datadir}/bash-completion/completions/flatpak
%dir %{_datadir}/fish
%dir %{_datadir}/fish/vendor_conf.d
%{_datadir}/fish/vendor_conf.d/flatpak.fish
%dir %{_datadir}/fish/vendor_completions.d
%{_datadir}/fish/vendor_completions.d/flatpak.fish
# # Own dirs so we don't have to depend on dbus for building.
%dir %{_datadir}/dbus-1
%dir %{_datadir}/dbus-1/interfaces
%dir %{_datadir}/dbus-1/services
%{_datadir}/dbus-1/interfaces/org.freedesktop.Flatpak.xml
%{_datadir}/dbus-1/interfaces/org.freedesktop.portal.Flatpak.xml
%{_datadir}/dbus-1/services/org.freedesktop.Flatpak.service
%{_datadir}/dbus-1/services/org.freedesktop.portal.Flatpak.service
%{_datadir}/dbus-1/system-services/org.freedesktop.Flatpak.SystemHelper.service
%{_dbusconfigdir}/org.freedesktop.Flatpak.SystemHelper.conf
# policykit rules
%{_datadir}/polkit-1/actions/org.freedesktop.Flatpak.policy
%{_datadir}/polkit-1/rules.d/60-org.freedesktop.Flatpak.rules
%{_mandir}/man1/%{name}*.1%{?ext_man}
%{_mandir}/man5/flatpak-metadata.5%{?ext_man}
%{_mandir}/man5/flatpak-flatpakref.5%{?ext_man}
%{_mandir}/man5/flatpakref.5%{?ext_man}
%{_mandir}/man5/flatpak-flatpakrepo.5%{?ext_man}
%{_mandir}/man5/flatpakrepo.5%{?ext_man}
%{_mandir}/man5/flatpak-installation.5%{?ext_man}
%{_mandir}/man5/flatpak-remote.5%{?ext_man}
%{_datadir}/%{name}/
%config %{_sysconfdir}/profile.d/flatpak.sh
%dir %{_sysconfdir}/flatpak
%dir %{_sysconfdir}/flatpak/remotes.d
%{_unitdir}/flatpak-system-helper.service
%{_unitdir}/update-system-flatpaks.{service,timer}
%{_userunitdir}/update-user-flatpaks.{service,timer}
%{_sbindir}/rcflatpak-system-helper
%{_userunitdir}/flatpak-session-helper.service
%{_userunitdir}/flatpak-portal.service
%ghost %dir %{_localstatedir}/lib/flatpak
%if %{support_environment_generators}
%dir %{_systemd_user_env_generator_dir}
%{_systemd_user_env_generator_dir}/60-flatpak
%{_systemd_system_env_generator_dir}/60-flatpak-system-only
%else
# Own dirs so we don't have to depend on gdm for building.
%dir %{_datadir}/gdm/
%dir %{_datadir}/gdm/env.d/
%{_datadir}/gdm/env.d/flatpak.env
%endif
%{_libexecdir}/flatpak-oci-authenticator
%{_userunitdir}/flatpak-oci-authenticator.service
%{_datadir}/dbus-1/interfaces/org.freedesktop.Flatpak.Authenticator.xml
%{_datadir}/dbus-1/services/org.flatpak.Authenticator.Oci.service
%{_tmpfilesdir}/flatpak.conf

%files -n system-user-flatpak
%license COPYING
%{_sysusersdir}/flatpak.conf

%files -n %{libname}
%license COPYING
%{_libdir}/libflatpak.so.*

%files -n typelib-1_0-Flatpak-1_0
%license COPYING
%{_libdir}/girepository-1.0/Flatpak-1.0.typelib

%files zsh-completion
%license COPYING
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_flatpak

%files devel
%license COPYING
%doc %{_datadir}/gtk-doc/html/flatpak
%dir %{_datadir}/doc/flatpak
%doc %{_datadir}/doc/flatpak/docbook.css
%doc %{_datadir}/doc/flatpak/flatpak-docs.html
%{_bindir}/flatpak-bisect
%{_bindir}/flatpak-coredumpctl
%{_libdir}/pkgconfig/flatpak.pc
%{_includedir}/%{name}/
%{_libdir}/libflatpak.so
%{_datadir}/gir-1.0/Flatpak-1.0.gir

%files remote-flathub
%config %{_sysconfdir}/flatpak/remotes.d/flathub.flatpakrepo

%files selinux
%{_datadir}/selinux/devel/include/contrib/flatpak.if
%{_datadir}/selinux/packages/flatpak.pp.bz2

%changelog
