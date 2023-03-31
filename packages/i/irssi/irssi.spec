#
# spec file for package irssi
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


Name:           irssi
Version:        1.4.4
Release:        0
Summary:        Modular IRC Client
License:        GPL-2.0-or-later
Group:          Productivity/Networking/IRC
URL:            http://www.irssi.org
Source:         https://github.com/irssi/irssi/releases/download/%{version}/irssi-%{version}.tar.xz
Source1:        irssi.desktop
Source2:        irssi.png
Source3:        https://github.com/irssi/irssi/releases/download/%{version}/irssi-%{version}.tar.xz.asc
# https://keyserver.ubuntu.com/pks/lookup?op=get&search=0x7EE65E3082A5FB06AC7C368D00CCB587DDBEF0E1
Source4:        %{name}.keyring
BuildRequires:  meson
BuildRequires:  glib2-devel
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  pkgconfig
BuildRequires:  xz
Conflicts:      %{name}-snapshot
%{perl_requires}
%{?libperl_requires}
# the OTR module is optional but the libotr version is too old
%if 0%{?suse_version} > 1330
BuildRequires:  libotr-devel
%endif
%if 0%{?suse_version} > 1330 && 0%{?sle_version} == 0
BuildRequires:  utf8proc-devel
%endif
%if 0%{?suse_version}
BuildRequires:  update-desktop-files
%endif

%description
Irssi is a modular IRC client that currently only has a text mode
user interface. However, 80–90%% of the code is not text mode
specific, so other UIs could be created. Irssi is not IRC specific;
there are SILC and ICB modules available.

Irssi is not using the ircII code.

%package devel
#
Summary:        Development package for irssi
Group:          Development/Languages/C and C++
Requires:       %{name} = %{version}
Requires:       dante-devel

%description devel
This package contains the development files for irssi. It allows to
compile plugins for the irssi package.

%prep
%setup -q

%build
%meson \
    -Ddocdir="%{_docdir}/%{name}" \
    -Denable-true-color=yes \
    -Dwith-proxy=yes \
    -Dwith-perl=yes \
    -Dwith-perl-lib=vendor \
    %if 0%{?suse_version} > 1330
    -Dwith-otr=yes \
    %endif
    -DPACKAGE_VERSION="%{version}" \
#
%meson_build

%install
%meson_install

install -D -m0644 "%{SOURCE1}" "%{buildroot}%{_datadir}/applications/%{name}.desktop"
install -D -m0644 "%{SOURCE2}" "%{buildroot}%{_datadir}/pixmaps/irssi.png"

%if 0%{?suse_version}
%suse_update_desktop_file -r "%{name}" Network IRCClient
%endif

%files
%{_bindir}/irssi
# modules
%dir %{_libdir}/irssi
%dir %{_libdir}/irssi/modules
%{_libdir}/irssi/modules/*.so*
# scripts & themes
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
# perl
%dir %{perl_vendorarch}/Irssi
%{perl_vendorarch}/Irssi.pm
%{perl_vendorarch}/Irssi/*
%{perl_vendorarch}/auto/Irssi
# docs
%dir %{_defaultdocdir}/irssi
%docdir %{_defaultdocdir}/irssi/
%doc %{_defaultdocdir}/irssi/*
%{_mandir}/man1/*.1%{?ext_man}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/irssi.png

%files devel
%{_includedir}/irssi/
%{_libdir}/pkgconfig/irssi*.pc

%changelog
