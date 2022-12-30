#
# spec file for package keepass-plugin-HIBPOfflineCheck
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2020 Matthias Bach <marix@marix.org>.
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


%define _plugin_name HIBPOfflineCheck
Name:           keepass-plugin-%{_plugin_name}
Version:        1.7.9
Release:        0
Summary:        A KeePass plugin for Have I been pwned
License:        GPL-3.0-only
Group:          Productivity/Other
URL:            https://github.com/mihaifm/HIBPOfflineCheck
Source:         https://github.com/mihaifm/%{_plugin_name}/archive/%{version}.tar.gz#/%{_plugin_name}-%{version}.tar.gz
BuildRequires:  keepass >= 2.41
BuildRequires:  mono-devel
Requires:       keepass
BuildArch:      noarch

%description
A Keepass plugin that performs offline and online checks against HaveIBeenPwned passwords.
Check can be performed both during password generation and editing or in batch over the whole
database.

%prep
%setup -q -n %{_plugin_name}-%{version}
sed -i 's|<HintPath>.*KeePass.exe</HintPath>|<HintPath>%{_prefix}/lib/keepass/KeePass.exe</HintPath>|' %{_plugin_name}/%{_plugin_name}.csproj

%build
xbuild /target:%{_plugin_name} /property:Configuration=Release

%install
install -D -m 644 %{_plugin_name}/bin/Release/%{_plugin_name}.dll %{buildroot}%{_prefix}/lib/keepass/%{_plugin_name}.dll

%files
%license LICENSE
%doc readme.md
%{_prefix}/lib/keepass/%{_plugin_name}.dll

%changelog
