#
# spec file for package grafana-status-panel
#
# Copyright (c) 2019 SUSE LLC, Nuernberg, Germany.
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


Name:           grafana-status-panel
Version:        1.0.9
Release:        0
Summary:        Grafana Status panel
License:        Apache-2.0
Group:          System/Monitoring
Url:            https://github.com/Vonage/Grafana_Status_panel
Source:         grafana_status_panel-%{version}.tar.xz
Requires:       grafana
BuildRequires:  fdupes
BuildRequires:  grafana
BuildRequires:  xz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
This is a plugin meant to be used as a centralized view for the status of
component in a glance. It is very similar to the Single Stat panel, but it
can hold multiple values from the same data source. Each value can be used
to customize the panel in different ways:

Mark the severity of the component
Mark if the component is disabled
Show extra data in the panel about the component


%prep
%setup -q -n grafana_status_panel-%{version}

%build

%install
%define grafana_plugin_dir %{_localstatedir}/lib/grafana/plugins
install -Dd -m0755 %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/dist/css
install -Dd -m0755 %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/src/css
install -Dd -m0755 %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/dist/img
install -Dd -m0755 %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/src/img
install -D -m0644 package.json %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/
install -D -m0644 package-lock.json %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/
install -D -m0644 Gruntfile.js %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/
install -D -m0644 dist/editor.html %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/dist
install -D -m0644 dist/module.html %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/dist
install -D -m0644 dist/module.js %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/dist
install -D -m0644 dist/module.js.map %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/dist
install -D -m0644 dist/plugin.json %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/dist
install -D -m0644 dist/status_ctrl.js %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/dist
install -D -m0644 dist/status_ctrl.js.map %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/dist
install -D -m0644 dist/css/* %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/dist/css
install -D -m0644 dist/img/* %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/dist/img
install -D -m0644 src/editor.html %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/src
install -D -m0644 src/module.html %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/src
install -D -m0644 src/module.js %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/src
install -D -m0644 src/plugin.json %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/src
install -D -m0644 src/status_ctrl.js %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/src
install -D -m0644 src/css/* %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/src/css
install -D -m0644 src/img/* %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/src/img
%fdupes -s %{buildroot}%{grafana_plugin_dir}/vonage-status-panel/

%files
%attr(0755,grafana,grafana) %dir %{_localstatedir}/lib/grafana
%attr(0755,grafana,grafana) %dir %{_localstatedir}/lib/grafana/plugins

%doc README.md
%license LICENSE.txt
%dir %{grafana_plugin_dir}/vonage-status-panel
%dir %{grafana_plugin_dir}/vonage-status-panel/dist
%dir %{grafana_plugin_dir}/vonage-status-panel/dist/css
%dir %{grafana_plugin_dir}/vonage-status-panel/dist/img
%dir %{grafana_plugin_dir}/vonage-status-panel/src
%dir %{grafana_plugin_dir}/vonage-status-panel/src/css
%dir %{grafana_plugin_dir}/vonage-status-panel/src/img
%{grafana_plugin_dir}/vonage-status-panel/Gruntfile.js
%{grafana_plugin_dir}/vonage-status-panel/package.json
%{grafana_plugin_dir}/vonage-status-panel/package-lock.json
%{grafana_plugin_dir}/vonage-status-panel/dist/editor.html
%{grafana_plugin_dir}/vonage-status-panel/dist/module.html
%{grafana_plugin_dir}/vonage-status-panel/dist/module.js
%{grafana_plugin_dir}/vonage-status-panel/dist/module.js.map
%{grafana_plugin_dir}/vonage-status-panel/dist/plugin.json
%{grafana_plugin_dir}/vonage-status-panel/dist/status_ctrl.js
%{grafana_plugin_dir}/vonage-status-panel/dist/status_ctrl.js.map
%{grafana_plugin_dir}/vonage-status-panel/src/editor.html
%{grafana_plugin_dir}/vonage-status-panel/src/module.html
%{grafana_plugin_dir}/vonage-status-panel/src/module.js
%{grafana_plugin_dir}/vonage-status-panel/src/plugin.json
%{grafana_plugin_dir}/vonage-status-panel/src/status_ctrl.js
%{grafana_plugin_dir}/vonage-status-panel/dist/css/*
%{grafana_plugin_dir}/vonage-status-panel/src/css/*
%{grafana_plugin_dir}/vonage-status-panel/dist/img/*
%{grafana_plugin_dir}/vonage-status-panel/src/img/*

%changelog
