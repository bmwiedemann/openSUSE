#
# spec file for package lightdm-gtk-greeter
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Guido Berhoerster.
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


%define _version 2.0
Name:           lightdm-gtk-greeter
Version:        2.0.6
Release:        0
Summary:        Simple display manager (GTK+ greeter)
License:        GPL-3.0-or-later
Group:          System/X11/Displaymanagers
URL:            https://launchpad.net/lightdm-gtk-greeter
Source:         https://launchpad.net/%{name}/%{_version}/%{version}/+download/%{name}-%{version}.tar.gz
Source1:        https://launchpad.net/%{name}/%{_version}/%{version}/+download/%{name}-%{version}.tar.gz.asc
Source2:        %{name}.keyring
BuildRequires:  autoconf
BuildRequires:  autoconf-archive
BuildRequires:  automake
BuildRequires:  exo-tools
BuildRequires:  fdupes
BuildRequires:  intltool
BuildRequires:  libtool
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gmodule-export-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 0.9.5
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(liblightdm-gobject-1) >= 1.3.5
BuildRequires:  pkgconfig(x11)
Requires:       %{name}-branding >= %{version}
Requires:       lightdm
Requires(post): update-alternatives
Requires(postun): update-alternatives
Recommends:     %{name}-lang
Recommends:     gnome-themes-accessibility
Provides:       lightdm-greeter

%description
A LightDM greeter that uses the GTK+ toolkit.
This is the reference implementation of a LightDM greeter based on the Gtk
toolkit.

%package branding-upstream
Summary:        Upstream branding of %{name}
Group:          System/X11/Displaymanagers
Requires:       %{name} = %{version}
Supplements:    packageand(%{name}:branding-upstream)
Conflicts:      otherproviders(%{name}-branding)
Provides:       %{name}-branding = %{version}
BuildArch:      noarch
#BRAND: /etc/lightdm/lightdm-gtk-greeter.conf: Determines a number of greeter
#BRAND: settings, in particular the background image.

%description branding-upstream
This package provides the upstream look and feel for lightdm-gtk-greeter.

%lang_package

%prep
%setup -q
sed -i 's|$(datadir)/doc|%{_docdir}|g' data/Makefile.am

# Remove __DATE__ and __TIME__.
BUILD_TIME=$(LC_ALL=C date -ur %{_sourcedir}/%{name}.changes +'%{H}:%{M}')
BUILD_DATE=$(LC_ALL=C date -ur %{_sourcedir}/%{name}.changes +'%{b} %{d} %{Y}')
sed -i "s/__TIME__/\"$BUILD_TIME\"/" $(grep -rl '__TIME__')
sed -i "s/__DATE__/\"$BUILD_DATE\"/" $(grep -rl '__DATE__')

%build
%if 0%{?suse_version} < 1500
export CFLAGS="%{optflags} -std=gnu99"
%endif
NOCONFIGURE=1 ./autogen.sh
%configure
make %{?_smp_mflags} V=1

%install
%make_install

%if 0%{?suse_version} >= 1320
mkdir -p %{buildroot}%{_sysconfdir}/alternatives/
touch %{buildroot}%{_sysconfdir}/alternatives/lightdm-default-greeter.desktop
ln -s %{_sysconfdir}/alternatives/lightdm-default-greeter.desktop \
  %{buildroot}%{_datadir}/xgreeters/lightdm-default-greeter.desktop
%endif

%fdupes %{buildroot}
%find_lang %{name} %{?no_lang_C}

%post
update-alternatives --install \
  %{_datadir}/xgreeters/lightdm-default-greeter.desktop \
  lightdm-default-greeter.desktop \
  %{_datadir}/xgreeters/lightdm-gtk-greeter.desktop \
  20

%postun
if [ "$1" = 0 ]; then
    update-alternatives --remove \
      lightdm-default-greeter.desktop \
      %{_datadir}/xgreeters/lightdm-gtk-greeter.desktop
fi

%files
%license COPYING
%doc AUTHORS ChangeLog README
%doc %{_docdir}/%{name}/
%{_sbindir}/%{name}
%{_datadir}/icons/hicolor/*/places/*
%dir %{_datadir}/xgreeters/
%{_datadir}/xgreeters/lightdm-gtk-greeter.desktop
%if 0%{?suse_version} >= 1320
%{_datadir}/xgreeters/lightdm-default-greeter.desktop
%else
%ghost %attr(0644,root,root) %{_datadir}/xgreeters/lightdm-default-greeter.desktop
%endif
%ghost %attr(0644,root,root) %{_sysconfdir}/alternatives/lightdm-default-greeter.desktop

%files branding-upstream
%dir %{_sysconfdir}/lightdm/
%config(noreplace) %{_sysconfdir}/lightdm/lightdm-gtk-greeter.conf

%files lang -f %{name}.lang

%changelog
