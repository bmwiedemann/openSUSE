#
# spec file for package kubic-dex-branding
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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

Name:           kubic-dex-branding
Version:        0.0.0
Release:        0
Summary:        Branding for caasp-dex
License:        Apache-2.0
Group:          Applications/Internet
Url:            https://github.com/kubic-project/dex-branding
Source:         %{name}-%{version}.tar.xz
Provides:       caasp-dex-branding = %{version}

ExcludeArch:    %ix86

%description
Branding themes for caasp-dex

%prep
%setup -q

%build
%install
# Install the web content
install -d -m 0755 %{buildroot}/%{_datadir}/caasp-dex
install -d -m 0755 %{buildroot}/%{_datadir}/caasp-dex/web
install -d -m 0755 %{buildroot}/%{_datadir}/caasp-dex/web/themes
install -d -m 0755 %{buildroot}/%{_datadir}/caasp-dex/web/themes/caasp
cp -R kubic-dex-branding/* %{buildroot}/%{_datadir}/caasp-dex/web/themes/caasp

%files
%defattr(-,root,root)
%dir %{_datadir}/caasp-dex
%dir %{_datadir}/caasp-dex/web
%dir %{_datadir}/caasp-dex/web/themes
%dir %{_datadir}/caasp-dex/web/themes/caasp
%{_datadir}/caasp-dex/web/themes/caasp/*

%changelog
