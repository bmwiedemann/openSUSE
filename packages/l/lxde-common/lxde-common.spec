#
# spec file for package lxde-common
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           lxde-common
Version:        0.99.2
Release:        0
Summary:        This package provides a set of default configurations for LXDE
License:        GPL-2.0
Group:          System/GUI/LXDE
Url:            http://www.lxde.org/
Source0:        %{name}-%{version}.tar.xz
Source1:        lxde-new-wallpapers.tar.bz2
BuildRequires:  docbook-utils
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libxslt
BuildRequires:  update-desktop-files
Requires:       lxde-common-branding
Provides:       lxde-settings-daemon >= %{version}
Obsoletes:      lxde-settings-daemon < %{version}
Requires(post): update-alternatives
Requires(postun): update-alternatives
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Recommends:     gtk2-engines

%description
Lxde-common package provides a set of default configurations for LXDE.
It's an LXDE core package, since without it LXDE cannot run.

%package 		branding-upstream
Summary:        Upstream branding
Group:          System/GUI/LXDE
Supplements:    packageand(lxde-common:branding-upstream)
Provides:       lxde-common-branding = %{version}
Conflicts:      otherproviders(lxde-common-branding)

%description branding-upstream
This branding-style package sets default applications in LXDE in openSUSE.
This is a dumb package, which provides only upstream LXDE configurations as preferred defaults.
You most probably don't want this package. You probably want to install distribution default
lxde-common-branding and prefer openSUSE default settings.

%prep
%setup -q

%build
%configure --enable-man
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}
mkdir -p %{buildroot}%{_datadir}/applications
install -c -m 644 lxde-logout.desktop %{buildroot}/%{_datadir}/applications/lxde-logout.desktop
mv %{buildroot}/%{_datadir}/xsessions/{LXDE,lxde}.desktop
%suse_update_desktop_file %{buildroot}/%{_datadir}/applications/lxde-logout.desktop
%suse_update_desktop_file %{buildroot}/%{_datadir}/applications/lxde-screenlock.desktop
%suse_update_desktop_file %{buildroot}/%{_datadir}/xsessions/lxde.desktop
cd %{buildroot}/%{_datadir}/lxde/wallpapers
tar xjf %{SOURCE1}
mv %{buildroot}/%{_datadir}/lxde/wallpapers/lxde-new-wallpapers/* %{buildroot}/%{_datadir}/lxde/wallpapers/
rm -rf %{buildroot}/%{_datadir}/lxde/wallpapers/lxde-new-wallpapers

mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/default-xsession.desktop
ln -s %{_sysconfdir}/alternatives/default-xsession.desktop %{buildroot}%{_datadir}/xsessions/default.desktop

%fdupes -s %{buildroot}

%post
%desktop_database_post
%{_sbindir}/update-alternatives --install %{_datadir}/xsessions/default.desktop \
  default-xsession.desktop %{_datadir}/xsessions/lxde.desktop 20

%postun
%desktop_database_postun
[ -f %{_datadir}/xsessions/lxde.desktop ] || %{_sbindir}/update-alternatives \
  --remove default-xsession.desktop %{_datadir}/xsessions/lxde.desktop

%files
%defattr(-,root,root)
%{_bindir}/openbox-lxde
%{_bindir}/startlxde
%dir %{_datadir}/lxde
%dir %{_datadir}/lxde/wallpapers
%{_datadir}/lxde/wallpapers/*
%{_mandir}/man1/*
%ghost %{_sysconfdir}/alternatives/default-xsession.desktop
%{_datadir}/xsessions/*.desktop
%{_datadir}/applications/lxde-logout.desktop
%{_datadir}/applications/lxde-screenlock.desktop

%files branding-upstream
%defattr(-,root,root)
%{_bindir}/lxde-logout
%dir %{_datadir}/lxde/images
%{_datadir}/lxde/images/logout-banner.png
%{_datadir}/lxde/images/lxde-icon.png
%dir %{_sysconfdir}/xdg/lxsession
%dir %{_sysconfdir}/xdg/lxsession/LXDE
%dir %{_sysconfdir}/xdg/pcmanfm
%dir %{_sysconfdir}/xdg/pcmanfm/LXDE
%config %{_sysconfdir}/xdg/lxsession/LXDE/autostart
%config %{_sysconfdir}/xdg/lxsession/LXDE/desktop.conf
%config %{_sysconfdir}/xdg/pcmanfm/LXDE/pcmanfm.conf
%dir %{_sysconfdir}/xdg/lxpanel
%dir %{_sysconfdir}/xdg/lxpanel/LXDE
%dir %{_sysconfdir}/xdg/lxpanel/LXDE/panels
%dir %{_sysconfdir}/xdg/openbox
%dir %{_sysconfdir}/xdg/openbox/LXDE
%config %{_sysconfdir}/xdg/lxpanel/LXDE/config
%config %{_sysconfdir}/xdg/lxpanel/LXDE/panels/panel
%config %{_sysconfdir}/xdg/openbox/LXDE/menu.xml
%config %{_sysconfdir}/xdg/openbox/LXDE/rc.xml

%changelog
