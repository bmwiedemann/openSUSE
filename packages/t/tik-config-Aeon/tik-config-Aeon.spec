#
# spec file for package tik-config-Aeon
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


Name:           tik-config-Aeon
Version:        20240502
Release:        0
Summary:        Aeon configuration for tik
License:        MIT
URL:            https://github.com/sysrich/tik
Source:         config
Source1:        LICENSE
BuildArch:      noarch
BuildRequires:  tik-config-generic
Conflicts:      tik-config
Provides:       tik-config

%description
Aeon configuration for tik.

%prep
cp -a %{SOURCE0} config
cp -a %{SOURCE1} LICENSE

%build

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_prefix}/lib/tik/config
install -D -m 644 %{_sysconfdir}/tik/config %{buildroot}%{_sysconfdir}/tik/config
install -d %{buildroot}%{_sysconfdir}/tik/modules/pre
install -d %{buildroot}%{_sysconfdir}/tik/modules/post

%files
%license LICENSE
%{_prefix}/lib/tik/config
%dir %{_sysconfdir}/tik
%dir %{_sysconfdir}/tik/modules
%dir %{_sysconfdir}/tik/modules/pre
%dir %{_sysconfdir}/tik/modules/post
%config(noreplace) %{_sysconfdir}/tik/config

%changelog
