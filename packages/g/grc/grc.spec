#
# spec file for package grc
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


Name:           grc
Version:        1.13
Release:        0
Summary:        Generic colouriser for everything
License:        GPL-2.0-or-later
Group:          System/Console
URL:            http://kassiopeia.juls.savba.sk/~garabik/software/grc.html
Source:         https://github.com/garabik/grc/archive/v%{version}.tar.gz#/v%{version}.tar.gz
# https://github.com/simotek/grc-osc-conf
Source1:        conf.osc
Patch0:         quilt-feature-osc-build.patch
BuildArch:      noarch

%description
Generic Colouriser is yet another colouriser for beautifying your
logfiles or commands output.

%prep
%setup -q
%patch0 -p1

%build
# Nothing to build.

%install
# fix wrong wrong-script-interpreter
find . -name 'grc' -exec sed -i "s|#! %{_bindir}/env python3$|#!%{_bindir}/python3|" {} +
find . -name 'grcat' -exec sed -i "s|#! %{_bindir}/env python3$|#!%{_bindir}/python3|" {} +
install -Dm 0755 grc %{buildroot}%{_bindir}/grc
install -Dm 0755 grcat %{buildroot}%{_bindir}/grcat
install -Dm 0644 grc.conf %{buildroot}%{_sysconfdir}/grc.conf
install -Dm 0644 grc.sh %{buildroot}%{_sysconfdir}/profile.d/grc.bash
install -Dm 0644 grc.1 %{buildroot}%{_mandir}/man1/grc.1
install -Dm 0644 grcat.1 %{buildroot}%{_mandir}/man1/grcat.1
mkdir -p %{buildroot}%{_datadir}/grc/
install -m 0644 colourfiles/conf.* %{buildroot}%{_datadir}/grc/
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/grc/

%files
%license COPYING debian/copyright
%doc CREDITS README.markdown TODO Regexp.txt debian/changelog
%config(noreplace) %{_sysconfdir}/grc.conf
%config %{_sysconfdir}/profile.d/grc.bash
%{_bindir}/grc*
%{_datadir}/grc/
%{_mandir}/man?/grc*

%changelog
