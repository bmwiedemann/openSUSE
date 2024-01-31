#
# spec file for package trader
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2012-24 John Zaitseff <J.Zaitseff@zap.org.au>
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


# ***********************************************************************
# *                                                                     *
# *            Star Traders: A Game of Interstellar Trading             *
# *               Copyright (C) 1990-2024, John Zaitseff                *
# *                                                                     *
# ***********************************************************************

# Author: John Zaitseff <J.Zaitseff@zap.org.au>
# $Id: 5ea51da60ce864d2de82d656ebbb3ce70601059a $

# This file is distributed under the same licence as Star Traders itself:
# the GNU General Public License, version 3 or later.

%define upstream_version   7.20
%define normalised_version 7.20
%define rpm_release_num    1

Name:           trader
Version:        %{normalised_version}
Release:        %{rpm_release_num}%{?dist}
Summary:        Star Traders, a simple game of interstellar trading
License:        GPL-3.0-or-later
Group:          Amusements/Games/Strategy/Turn Based
URL:            https://www.zap.org.au/projects/trader/

Source0:        https://ftp.zap.org.au/pub/trader/unix/trader-%{upstream_version}.tar.xz
Source1:        https://ftp.zap.org.au/pub/trader/unix/trader-%{upstream_version}.tar.xz.sig
# Source2 downloaded from https://www.zap.org.au/~john/pubkey.asc
Source2:        trader.keyring

BuildRequires:  gcc
BuildRequires:  gettext
BuildRequires:  gperf
BuildRequires:  pkgconfig
BuildRequires:  update-desktop-files
BuildRequires:  pkgconfig(ncurses)

Requires(post): hicolor-icon-theme
Requires(postun):hicolor-icon-theme
Recommends:     %{name}-lang = %{version}

%description
Star Traders is a simple game of interstellar trading, where the objective
is to create companies, buy and sell shares, borrow and repay money, in
order to become the wealthiest player (the winner).

%lang_package

%prep
%setup -q -n %{name}-%{upstream_version}

%build
%configure
%make_build

%install
%make_install
%find_lang %{name}
%suse_update_desktop_file au.org.zap.%{name}

%files
%doc README NEWS
%license COPYING
%{_bindir}/%{name}
%{_mandir}/man6/trader.6%{?ext_man}
%{_datadir}/applications/au.org.zap.%{name}.desktop
%{_datadir}/metainfo/au.org.zap.%{name}.metainfo.xml
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%files lang -f %{name}.lang

%changelog
