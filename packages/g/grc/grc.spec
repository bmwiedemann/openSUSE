#
# spec file for package grc
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


Name:           grc
Version:        1.11.1
Release:        0
Summary:        Generic colouriser for everything
License:        GPL-2.0+
Group:          System/Console
Url:            http://kassiopeia.juls.savba.sk/~garabik/software/grc.html
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
%patch0

%build
# Nothing to build.

%install
install -Dm 0755 grc %{buildroot}%{_bindir}/grc
install -Dm 0755 grcat %{buildroot}%{_bindir}/grcat
install -Dm 0644 grc.conf %{buildroot}%{_sysconfdir}/grc.conf
install -Dm 0644 grc.bashrc %{buildroot}%{_sysconfdir}/profile.d/grc.bash
install -Dm 0644 grc.1 %{buildroot}%{_mandir}/man1/grc.1
install -Dm 0644 grcat.1 %{buildroot}%{_mandir}/man1/grcat.1
mkdir -p %{buildroot}%{_datadir}/grc/
install -m 0644 colourfiles/conf.* %{buildroot}%{_datadir}/grc/
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/grc/

%files
%defattr(-,root,root)
%doc COPYING CREDITS README.markdown TODO Regexp.txt debian/changelog debian/copyright
%config(noreplace) %{_sysconfdir}/grc.conf
%config %{_sysconfdir}/profile.d/grc.bash
%{_bindir}/grc*
%{_datadir}/grc/
%{_mandir}/man?/grc*

%changelog
