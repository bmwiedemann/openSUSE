#
# spec file for package wp-cli
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


Name:           wp-cli
Version:        2.7.1
Release:        0
Summary:        WordPress command-line interface
License:        MIT
URL:            https://wp-cli.org/
Source0:        https://github.com/%{name}/%{name}/releases/download/v%{version}/%{name}-%{version}.phar
Source1:        https://raw.githubusercontent.com/%{name}/%{name}/v%{version}/utils/wp-completion.bash
Requires:       php >= 5.4
Requires:       php-json
Requires:       php-openssl
Requires:       php-phar
Requires:       php-zip
BuildArch:      noarch

%description
WP-CLI is the command-line interface for WordPress. You can update plugins,
configure multisite installations and much more, without using a web browser.

%prep
%setup -q -c -T

%build

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 %{SOURCE0} %{buildroot}%{_bindir}/wp
mkdir -p %{buildroot}%{_sysconfdir}/profile.d
install -m 0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/profile.d

%files
%defattr(-,root,root,0755)
%{_bindir}/wp
%config %{_sysconfdir}/profile.d/wp-completion.bash

%changelog
