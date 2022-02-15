#
# spec file for package fcitx5-lua-migration-reminder
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


Name:           fcitx5-lua-migration-reminder
Version:        1.0.1
Release:        0
Summary:        Fcitx5 Lua addon to guide users to migrate their fcitx4 configurations
License:        GPL-3.0-or-later
URL:            https://github.com/openSUSE-zh/fcitx5-lua-migration-reminder
Source:         %{name}-%{version}.tar.gz
BuildRequires:  fcitx5-lua
Requires:       fcitx5-configtool
Requires:       fcitx5-lua
Requires:       lua54-lgi
Supplements:    fcitx5

%description
Fcitx5 Lua addon to guide users to migrate their fcitx4 configurations.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/fcitx5/addon
mkdir -p %{buildroot}%{_datadir}/fcitx5/lua/migration-reminder
install -m 0644 migration-reminder.conf.in %{buildroot}%{_datadir}/fcitx5/addon/migration-reminder.conf
install -m 0644 reminder.lua %{buildroot}%{_datadir}/fcitx5/lua/migration-reminder/reminder.lua
install -m 0644 addon.lua %{buildroot}%{_datadir}/fcitx5/lua/migration-reminder/addon.lua

%files
%license LICENSE
%dir %{_datadir}/fcitx5
%dir %{_datadir}/fcitx5/addon
#%dir %{_datadir}/fcitx5/lua
%{_datadir}/fcitx5/addon/migration-reminder.conf
%{_datadir}/fcitx5/lua/migration-reminder

%changelog
