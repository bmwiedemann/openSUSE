#
# spec file for package grafana-piechart-panel
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


Name:           grafana-piechart-panel
Version:        1.6.1
Release:        0
Summary:        Grafana Piechart panel
License:        MIT
Group:          System/Monitoring
URL:            https://github.com/grafana/piechart-panel
Source:         piechart-panel-%{version}.tar.xz
Requires:       grafana
BuildRequires:  grafana
BuildRequires:  xz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Pie chart panel for grafana

%prep
%setup -q -n piechart-panel-%{version}

%build

%install
%define grafana_plugin_dir %{_localstatedir}/lib/grafana/plugins
%define plugin_subdir grafana-piechart-panel
%define destination %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/dist

install -Dd -m0755 %{destination}/img/
install -Dd -m0755 %{destination}/styles/
install -D -m0644 dist/img/*.png %{destination}/img/
install -D -m0644 dist/styles/*.css %{destination}/styles/
install -D -m0644 dist/dark.js* %{destination}/
install -D -m0644 dist/light.js* %{destination}/
install -D -m0644 dist/editor.html %{destination}/
install -D -m0644 dist/module.html %{destination}/
install -D -m0644 dist/module.js* %{destination}/
install -D -m0644 dist/plugin.json %{destination}/
install -D -m0644 dist/LICENSE %{destination}/
install -D -m0644 dist/MANIFEST.txt %{destination}/

install -D -m0644 README.md %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/dist
install -D -m0644 LICENSE %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/

%files
%attr(0755,grafana,grafana) %dir %{_localstatedir}/lib/grafana
%attr(0755,grafana,grafana) %dir %{_localstatedir}/lib/grafana/plugins

%doc README.md
%license LICENSE
%dir %{grafana_plugin_dir}/%{plugin_subdir}
%dir %{grafana_plugin_dir}/%{plugin_subdir}/dist
%dir %{grafana_plugin_dir}/%{plugin_subdir}/dist/img
%dir %{grafana_plugin_dir}/%{plugin_subdir}/dist/styles
%{grafana_plugin_dir}/%{plugin_subdir}/dist/editor.html
%{grafana_plugin_dir}/%{plugin_subdir}/dist/module.html
%{grafana_plugin_dir}/%{plugin_subdir}/dist/module.js*
%{grafana_plugin_dir}/%{plugin_subdir}/dist/plugin.json
%{grafana_plugin_dir}/%{plugin_subdir}/dist/dark.js*
%{grafana_plugin_dir}/%{plugin_subdir}/dist/light.js*
%{grafana_plugin_dir}/%{plugin_subdir}/dist/img/*.png
%{grafana_plugin_dir}/%{plugin_subdir}/dist/styles/*.css
%{grafana_plugin_dir}/%{plugin_subdir}/LICENSE
%{grafana_plugin_dir}/%{plugin_subdir}/dist/README.md
%{grafana_plugin_dir}/%{plugin_subdir}/dist/LICENSE
%{grafana_plugin_dir}/%{plugin_subdir}/dist/MANIFEST.txt

%changelog
