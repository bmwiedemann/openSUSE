#
# spec file for package enlightenment
#
# Copyright (c) 2023 SUSE LLC
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


%define efl_version	1.26.0
%define systemd_present 1
# Wayland is broken with current efl waiting for a new e release
%define enable_wayland (0%{?suse_version} > 1520)
%define generate_manpages 0
# Fix this later
%define build_doc 0
Name:           enlightenment
Version:        0.25.4
Release:        0
Summary:        The window manager
License:        BSD-2-Clause
Group:          System/X11/Displaymanagers
URL:            http://enlightenment.org/
Source:         http://download.enlightenment.org/rel/apps/enlightenment/%{name}-%{version}.tar.xz
Source2:        enlightenment.pam
Source3:        system.conf
# PATCH-FEATURE_OPENSUSE feature-network-manager-wizard.patch simon@simotek.net adds nm-applet to startup apps if its present,
# this will be maybe upstreamed when upstream network manager applet supports app indicator - (1.1.0)
Source4:        network_manager_wizard.c
# PATCH-FIX-OPENSUSE - enlightenment-0.16.999.65256-dont_require_suidbit.patch sleep_walker@opensuse.org -- upstream insist on having suidbit
Patch0:         enlightenment-0.16.999.65256-dont_require_suidbit.patch
# PATCH-FEATURE-OPENSUSE dont_offer_updates.patch -- don't offer updates, that's up to package manager -- sleep_walker@opensuse.org
Patch1:         dont_offer_updates.patch
# boo#1003939 don't ask for language if we can use the current system one
Patch3:         feature-wizard-auto-lang.patch
Patch4:         feature-wizard-keylayout-from-sys.patch
Patch5:         feature-qt-apps-gtk2-theme.patch
# We'd rather log to the journal then e's log file.
Patch6:         feature-openSUSE-log-to-journal.patch
# boo#1170162 - disable the storage module thats not used on Linux for enhanced security
Patch7:         feature-openSUSE-disable-system-storage.patch
BuildRequires:  alsa-devel
BuildRequires:  cmake
BuildRequires:  doxygen
BuildRequires:  efl >= %{efl_version}
BuildRequires:  gettext-devel
BuildRequires:  hicolor-icon-theme
BuildRequires:  meson
BuildRequires:  pam-devel
BuildRequires:  pkgconfig
# configure scripts looks for Xwayland binary
%if %{enable_wayland}
BuildRequires:  xorg-x11-server-wayland
%endif
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(ecore) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-con) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-evas) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-file) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-ipc) >= %{efl_version}
BuildRequires:  pkgconfig(ecore-x) >= %{efl_version}
BuildRequires:  pkgconfig(eet) >= %{efl_version}
BuildRequires:  pkgconfig(efreet) >= %{efl_version}
BuildRequires:  pkgconfig(efreet-mime) >= %{efl_version}
BuildRequires:  pkgconfig(efreet-trash) >= %{efl_version}
BuildRequires:  pkgconfig(eina) >= %{efl_version}
BuildRequires:  pkgconfig(eio) >= %{efl_version}
BuildRequires:  pkgconfig(eldbus) >= %{efl_version}
BuildRequires:  pkgconfig(elementary) >= %{efl_version}
BuildRequires:  pkgconfig(emotion) >= %{efl_version}
BuildRequires:  pkgconfig(evas) >= %{efl_version}
BuildRequires:  pkgconfig(freetype2) >= 2.1.7
BuildRequires:  pkgconfig(xcb-keysyms)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xkbcommon)
# you'll need dbus-1 for default actions set in sysactions.conf
Requires:       dbus-1
Requires:       edje
Requires:       efl
Requires:       elementary
Requires:       enlightenment-branding >= 0.1
Requires:       evas-generic-loaders
%if 0%{?suse_version} > 1500
# dlopened at runtime
Recommends:     libddcutil3
%else
# dlopened at runtime
Recommends:     libddcutil2
%endif
# Require a Icon theme that will be detected by enlghtenment
Requires:       oxygen-icon-theme
# We use xdg-terminal, xdg-open and xdg-su in various places
Requires:       xdg-utils
Conflicts:      e17 > 0.17.3
# lets not have users complain about theme incompat
Conflicts:      e17-theme
Provides:       e_module-notification = 0.2.1
Obsoletes:      e_module-notification < 0.2.1
# Obsolete 12.3 and 13.1 users using e17.0 and e17.3 but not 13.2 users using e17.6 as they will
# have chosen e17 over e18 and later manually
# according to DimStar, obsoleting all will allow a smooth upgrade, only providing 0.17.4 or less will mean that
# older e17.3 users will update but anyone who manually installs e17.6 will stay
Obsoletes:      e17
Provides:       e17 > 0.17.4
%if 0%{?suse_version}
Requires(post): update-alternatives
Requires(postun):update-alternatives
Requires(post): permissions
%endif
%{?systemd_requires}
%if %{enable_wayland}
BuildRequires:  pkgconfig(ecore-wl2)
BuildRequires:  pkgconfig(uuid)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-server)
%endif
%if %{systemd_present}
BuildRequires:  pkgconfig(libsystemd)
%endif
%if 0%{?suse_version}
BuildRequires:  fdupes
BuildRequires:  update-desktop-files
%endif
%if 0%{?fedora} >= 18
Requires:       systemd
%endif
%if 0%{?suse_version}
Recommends:     NetworkManager-appindicator
# For acpid bindings
Recommends:     acpid
Recommends:     alsa-plugins-pulse
# Recommended to make NetworkManager Intergration work
Recommends:     gnome-keyring
Recommends:     pam_mount
# Recommended to make audio work out of the box boo#972912
Recommends:     pulseaudio
Recommends:     pulseaudio-module-bluetooth
Recommends:     pulseaudio-module-jack
Recommends:     pulseaudio-module-lirc
Recommends:     pulseaudio-module-x11
Recommends:     pulseaudio-module-zeroconf
Recommends:     pulseaudio-utils
# Recommend sni-qt to make Qt4/kde4 apps work with systray
Recommends:     sni-qt
# to have working automounting we need udisks
Recommends:     udisks
%endif

%description
Enlightenment window manager and desktop environment is really fast, configurable and beautiful.
This package will provide the latest released version of enlightenment, as opposed to e16 or e17.

%package devel
Summary:        Enightenment development files
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}
Requires:       efl-devel
Requires:       elementary-devel
Requires:       freetype2-devel >= 2.1.7
Requires:       pam-devel
Requires:       pkgconfig
Requires:       xorg-x11-libXext-devel
Requires:       pkgconfig(dbus-1)
Conflicts:      e17-devel > 0.17.3
Obsoletes:      e17-devel < 0.17.3
Provides:       e17-devel = 0.17.3

%description devel
Development files of Enlightenment package.

%package branding-upstream
Summary:        Enlightenment files for upstream branding
Group:          System/GUI/Other
Requires:       enlightenment-theme-upstream
Conflicts:      terminology-theme-openSUSE
Provides:       enlightenment-branding = 0.1
%if 0%{?suse_version}
Supplements:    packageand(enlightenment:branding-upstream)
Conflicts:      otherproviders(e17-branding)
Conflicts:      otherproviders(enlightenment-branding)
%endif

%description branding-upstream
Various files for Enlightenment provided by upstream but altered by openSUSE or Petite Linux.

%if %{build_doc}
%package doc-html
Summary:        HTML documentation of Enlightenment
Group:          Documentation/HTML
Conflicts:      e17-doc-html

%description doc-html
Documentation of Enlightenment in form of HTML pages.
%endif

%if %{generate_manpages}
%package doc-man
Summary:        Man documentation of Enlightenment
Group:          Documentation/Man

%description doc-man
Documentation of Enlightenment in form of man pages.
%endif

%prep
%autosetup -p1

# Copy In new Network Wizard
rm src/modules/wizard/page_110.c
cp -v %{SOURCE4} src/modules/wizard/page_110.c

%build
# fake time used for documentation
FAKE_DOCDATE=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%a %%b %%d %%Y')
FAKE_DOCYEAR=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%Y')
FAKE_DOCDATETIME=$(LC_ALL=C date -u -r %{_sourcedir}/%{name}.changes '+%%a %%b %%d %%Y %{T}')
sed -i "s/\$datetime/$FAKE_DOCDATETIME/g;s/\$date/$FAKE_DOCDATE/g;s/\$year/$FAKEDOCYEAR/g" doc/*.html

export CFLAGS="%{optflags}%{?mageia: -g}"

%meson \
%if %{enable_wayland}
    -Dwl=true \
    -Dwl-x11=true \
    -Dxwayland=true
%else
    -Dwayland=false
%endif

%meson_build

%install
%meson_install

%if %{enable_wayland}
# gdm doesn't show 2 desktop files with the same name
#rm %{buildroot}%{_datadir}/wayland-sessions/enlightenment.desktop
mkdir -p %{buildroot}%{_datadir}/wayland-sessions/
cp %{buildroot}%{_datadir}/xsessions/enlightenment.desktop \
 %{buildroot}%{_datadir}/wayland-sessions/enlightenment-wayland.desktop
%endif

%if %{build_doc}
# copy documentation manually
echo "Copying HTML documentation"
mkdir -p %{buildroot}%{_docdir}/%{name}
/bin/cp -vr doc/html %{buildroot}%{_docdir}/%{name}
%endif

%if %{generate_manpages}
echo "Copying MAN pages"
/bin/cp -vr doc/man/ %{buildroot}%{_mandir}/
%endif

find %{buildroot} -type f -name "*.la" -delete -print
%find_lang enlightenment
%if 0%{?suse_version}
# enlightenment_ckpasswd only needs suid bit on bsd's
chmod -s %{buildroot}%{_libdir}/enlightenment/utils/enlightenment_ckpasswd \
		 %{buildroot}%{_libdir}/enlightenment/utils/enlightenment_sys \
%endif

# copy PAM profile
%if 0%{?suse_version} > 1500
mkdir -p %{buildroot}%{_pam_vendordir}
cp %{SOURCE2} %{buildroot}%{_pam_vendordir}/enlightenment
%else
mkdir -p %{buildroot}%{_sysconfdir}/pam.d
cp %{SOURCE2} %{buildroot}%{_sysconfdir}/pam.d/enlightenment
%endif

# Install correct openSUSE rules for system.conf
mkdir -p %{buildroot}/%{_datadir}/%{name}/doc/
mv %{buildroot}/etc/enlightenment/system.conf %{buildroot}/%{_datadir}/%{name}/doc/
cp %{SOURCE3} %{buildroot}/etc/enlightenment/

%if 0%{?suse_version}
%suse_update_desktop_file -r -G mixer emixer "AudioVideo;Mixer;"
%if %{enable_wayland}
%suse_update_desktop_file -N "Unstable: Enlightenment (Wayland)" -G "Unstable: Enlightenment (Wayland)"  %{buildroot}%{_datadir}/wayland-sessions/enlightenment-wayland.desktop
%endif
# fdupes needs to be called after desktop files have been made unique
%fdupes -s %{buildroot}
%endif

# Remove unwanted wizard pages
# /usr/lib64/enlightenment/modules/wizard/linux-gnu-x86_64-ver-autocannoli-0.20/page_010.so

# Remove language / keyboard pages
# rm %{buildroot}%{_libdir}/enlightenment/modules/wizard/*/page_011.so
# Remove connman page
rm %{buildroot}%{_libdir}/enlightenment/modules/wizard/*/page_110.so
# Don't remove Updates 170 (We have a patch to ensure its disabled)
# Remove tasks page, with our profile its not needed
rm %{buildroot}%{_libdir}/enlightenment/modules/wizard/*/page_180.so

# remove files from not wanted place
rm %{buildroot}%{_datadir}/enlightenment/{COPYING,AUTHORS}

mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

%if 0%{?suse_version}
%post
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/enlightenment.desktop 20
%set_permissions %{_libdir}/enlightenment/utils/enlightenment_system

%postun
if [ ! -f %{_datadir}/xsessions/enlightenment.desktop ] ; then
  %{_sbindir}/update-alternatives  --remove default-xsession.desktop %{_datadir}/xsessions/enlightenment.desktop
fi

%verifyscript
%verify_permissions -e %{_libdir}/enlightenment/utils/enlightenment_system

%endif

%if 0%{?suse_version} > 1500
%pre
# Prepare for migration to /usr/lib; save any old .rpmsave
for i in pam.d/enlightenment ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i}.rpmsave.old ||:
done

%posttrans
# Migration to /usr/lib, restore just created .rpmsave
for i in pam.d/enlightenment ; do
     test -f %{_sysconfdir}/${i}.rpmsave && mv -v %{_sysconfdir}/${i}.rpmsave %{_sysconfdir}/${i} ||:
done
%endif

%files -f enlightenment.lang
%defattr(-,root,root)
%license COPYING README AUTHORS
%if %{build_doc}
%exclude %{_docdir}/%{name}/html
%endif
%{_datadir}/xsessions/enlightenment.desktop
%{_datadir}/xsessions/default.desktop
%if %{enable_wayland} && 0%{?suse_version} >= 1550
# This should be owned by something else
%{_datadir}/wayland-sessions/
%{_datadir}/wayland-sessions/enlightenment-wayland.desktop
%endif
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%ghost %{_sysconfdir}/alternatives/default.desktop
%{_datadir}/enlightenment/
%{_datadir}/applications/*.desktop
%{_datadir}/icons/hicolor/*
%{_libdir}/enlightenment
%verify(not user group mode) %attr(4755,root,root) %{_libdir}/enlightenment/utils/enlightenment_system
%config(noreplace) %{_sysconfdir}/enlightenment
%if 0%{?suse_version} > 1500
%{_pam_vendordir}/enlightenment
%else
%config(noreplace) %{_sysconfdir}/pam.d/enlightenment
%endif
%dir %{_sysconfdir}/xdg/menus
%config %{_sysconfdir}/xdg/menus/e-applications.menu
%{_bindir}/enlightenment*
%{_bindir}/emixer
%{_datadir}/icons/hicolor/128x128/apps/emixer.png
%{_datadir}/pixmaps/enlightenment-askpass.png

%if %{systemd_present}
%{_prefix}/lib/systemd/user/enlightenment.service
%endif
# excluded to be branded
%exclude %{_libdir}/enlightenment/modules/wizard/def-ibar.txt

%files branding-upstream
%defattr(-, root, root)
%{_libdir}/enlightenment/modules/wizard/def-ibar.txt

%files devel
%defattr(-, root, root)
%{_libdir}/pkgconfig/*.pc
%{_includedir}/enlightenment

%if %{build_doc}
%files doc-html
%defattr(-, root, root)
%{_docdir}/%{name}
%endif

%if %{generate_manpages}
%files doc-man
%defattr(-, root, root)
%{_mandir}/*/*
%endif

%changelog
