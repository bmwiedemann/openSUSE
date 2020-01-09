#
# spec file for package grafana-piechart-panel
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


Name:           grafana-piechart-panel
Version:        1.3.9
Release:        0
Summary:        Grafana Piechart panel
License:        MIT
Group:          System/Monitoring
Url:            https://github.com/grafana/piechart-panel
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
install -Dd -m0755 %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/src/img
install -Dd -m0755 %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/src/lib
install -Dd -m0755 %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/src/styles
install -D -m0644 package.json %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/
install -D -m0644 yarn.lock %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/
install -D -m0644 tsconfig.json %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/
install -D -m0644 src/editor.html %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/src
install -D -m0644 src/legend.ts %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/src
install -D -m0644 src/module.html %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/src
install -D -m0644 src/module.ts %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/src
install -D -m0644 src/plugin.json %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/src
install -D -m0644 src/piechart_ctrl.ts %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/src
install -D -m0644 src/rendering.ts %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/src
install -D -m0644 src/img/*.png %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/src/img
install -D -m0644 src/lib/*.js %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/src/lib
install -D -m0644 src/styles/*.scss %{buildroot}%{grafana_plugin_dir}/%{plugin_subdir}/src/styles

%files
%attr(0755,grafana,grafana) %dir %{_localstatedir}/lib/grafana
%attr(0755,grafana,grafana) %dir %{_localstatedir}/lib/grafana/plugins

%doc README.md
%license LICENSE
%dir %{grafana_plugin_dir}/%{plugin_subdir}
%dir %{grafana_plugin_dir}/%{plugin_subdir}/src
%dir %{grafana_plugin_dir}/%{plugin_subdir}/src/img
%dir %{grafana_plugin_dir}/%{plugin_subdir}/src/lib
%dir %{grafana_plugin_dir}/%{plugin_subdir}/src/styles
%{grafana_plugin_dir}/%{plugin_subdir}/package.json
%{grafana_plugin_dir}/%{plugin_subdir}/yarn.lock
%{grafana_plugin_dir}/%{plugin_subdir}/tsconfig.json
%{grafana_plugin_dir}/%{plugin_subdir}/src/editor.html
%{grafana_plugin_dir}/%{plugin_subdir}/src/module.html
%{grafana_plugin_dir}/%{plugin_subdir}/src/legend.ts
%{grafana_plugin_dir}/%{plugin_subdir}/src/module.ts
%{grafana_plugin_dir}/%{plugin_subdir}/src/rendering.ts
%{grafana_plugin_dir}/%{plugin_subdir}/src/plugin.json
%{grafana_plugin_dir}/%{plugin_subdir}/src/piechart_ctrl.ts
%{grafana_plugin_dir}/%{plugin_subdir}/src/img/*.png
%{grafana_plugin_dir}/%{plugin_subdir}/src/lib/*.js
%{grafana_plugin_dir}/%{plugin_subdir}/src/styles/*.scss

%changelog
