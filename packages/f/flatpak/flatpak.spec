#
# spec file for package flatpak
#
# Copyright (c) 2021 SUSE LLC
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


%define libname libflatpak0
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
Version:        1.11.1
Release:        0
Summary:        OSTree based application bundles management
License:        LGPL-2.1-or-later
Group:          System/Packages
URL:            https://flatpak.github.io/
Source0:        https://github.com/flatpak/flatpak/releases/download/%{version}/%{name}-%{version}.tar.xz
Patch0:         polkit_rules_usability.patch
BuildRequires:  bison
BuildRequires:  bubblewrap >= 0.4.1
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  gtk-doc
BuildRequires:  intltool >= 0.35.0
BuildRequires:  libcap-devel
BuildRequires:  libdwarf-devel
BuildRequires:  libgpg-error-devel
BuildRequires:  libgpgme-devel >= 1.1.8
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  sysuser-tools
BuildRequires:  xdg-dbus-proxy >= 0.1.0
BuildRequires:  xsltproc
BuildRequires:  pkgconfig(appstream-glib)
BuildRequires:  pkgconfig(dconf) >= 0.26
BuildRequires:  pkgconfig(fuse) >= 2.9.2
BuildRequires:  pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gio-unix-2.0)
BuildRequires:  pkgconfig(glib-2.0) >= 2.44
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.40.0
BuildRequires:  pkgconfig(gobject-introspection-no-export-1.0) >= 1.40.0
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libarchive) >= 2.8.0
BuildRequires:  pkgconfig(libelf) >= 0.8.12
BuildRequires:  pkgconfig(libseccomp)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libzstd) >= 0.8.1
BuildRequires:  pkgconfig(ostree-1) >= 2020.8
BuildRequires:  pkgconfig(polkit-gobject-1)
BuildRequires:  pkgconfig(systemd)
BuildRequires:  pkgconfig(xau)
Requires:       %{libname} = %{version}
Requires:       bubblewrap >= 0.4.1
Requires:       ostree >= 2020.8
Requires:       xdg-dbus-proxy >= 0.1.0
Requires:       xdg-desktop-portal >= 0.10
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
Supplements:    packageand(%{name}:%(rpm -q --qf '%%{NAME}' --whatprovides zsh))

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

%lang_package

%prep
%autosetup -p1
sed -i -e '1s,#!%{_bindir}/env python3,#!%{_bindir}/python3,' scripts/flatpak-*

%build
%configure \
	--disable-silent-rules \
	--enable-gtk-doc \
	--with-system-bubblewrap \
	--with-priv-mode=none \
	--with-dbus-config-dir=%{_dbusconfigdir} \
        --with-system-dbus-proxy=%{_bindir}/xdg-dbus-proxy \
%if !%{support_environment_generators}
        --enable-gdm-env-file \
%endif
	%{nil}
%make_build
%sysusers_generate_pre system-helper/flatpak.conf system-user-flatpak

%install
%make_install
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

mkdir -p %{buildroot}%{_sysconfdir}/flatpak/remotes.d

%find_lang %{name}

%pre -n system-user-flatpak -f system-user-flatpak.pre
%post   -n %{libname} -p /sbin/ldconfig
%postun -n %{libname} -p /sbin/ldconfig

%pre
%service_add_pre flatpak-system-helper.service

%preun
%service_del_preun flatpak-system-helper.service

%post
%service_add_post flatpak-system-helper.service
# Remove any empty repo directory, which is seen as invalid by flatpak. After that, create a skeleton repository using "flatpak remotes".
if [ -e "%{_localstatedir}/lib/flatpak/repo" ] && [ -z "$(ls -A %{_localstatedir}/lib/flatpak/repo)" ]; then
rm -r %{_localstatedir}/lib/flatpak/repo
fi
%{_bindir}/flatpak remotes 1> /dev/null

%postun
%service_del_postun flatpak-system-helper.service

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
%{_mandir}/man5/flatpak-flatpakrepo.5%{?ext_man}
%{_mandir}/man5/flatpak-installation.5%{?ext_man}
%{_mandir}/man5/flatpak-remote.5%{?ext_man}
%{_datadir}/%{name}/
%config %{_sysconfdir}/profile.d/flatpak.sh
%{_sysconfdir}/flatpak
%{_unitdir}/flatpak-system-helper.service
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

%files -n system-user-flatpak
%{_sysusersdir}/flatpak.conf

%files -n %{libname}
%{_libdir}/libflatpak.so.*

%files -n typelib-1_0-Flatpak-1_0
%{_libdir}/girepository-1.0/Flatpak-1.0.typelib

%files zsh-completion
%dir %{_datadir}/zsh/site-functions
%{_datadir}/zsh/site-functions/_flatpak

%files devel
%{_bindir}/flatpak-bisect
%{_bindir}/flatpak-coredumpctl
%{_libdir}/pkgconfig/flatpak.pc
%{_datadir}/gtk-doc/
%{_includedir}/%{name}/
%{_libdir}/libflatpak.so
%{_datadir}/gir-1.0/Flatpak-1.0.gir

%changelog
