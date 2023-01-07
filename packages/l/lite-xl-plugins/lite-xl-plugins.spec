#
# spec file for package lite-xl-plugins
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

%define programname lite-xl
Name:           lite-xl-plugins
Version:        git20221231.bf3a3b7
Release:        0
Summary:        Additional plugins for %{programname}
License:        MIT
URL:            https://github.com/lite-xl/lite-xl-plugins
Source0:        %{name}-%{version}.tar.gz
### https://raw.githubusercontent.com/lite-xl/console/master/init.lua ==> console.lua
Source1:        console.lua
### https://github.com/yamatsum/nonicons/raw/master/dist/nonicons.ttf
Source2:        nonicons.ttf
### https://raw.githubusercontent.com/vincens2005/lite-xl-gitdiff-highlight/master/init.lua
Source3:        gitdiff_highlight-init.lua
### https://raw.githubusercontent.com/vincens2005/lite-xl-gitdiff-highlight/master/gitdiff.lua
Source4:        gitdiff_highlight-gitdiff.lua
Source5:        smb-addl-nonicons.txt
Patch0:         nonicons-userdir.diff
Recommends:     words
Requires:       lite-xl
Requires:       lite-xl-widgets
BuildArch:      noarch

%description
Plugins for the Lite XL text editor, originally forked from the lite plugins repository.

%prep
%setup -q
%patch0

%build
sed -i '/  -- Following without special icon:/ r %{SOURCE5}' %{_builddir}/%{name}-%{version}/plugins/nonicons.lua

%install
mkdir -p %{buildroot}%{_datadir}/%{programname}/plugins
mkdir -p %{buildroot}%{_datadir}/%{programname}/plugins/editorconfig/tests/{glob,parser,properties}
mkdir -p %{buildroot}%{_datadir}/%{programname}/plugins/profiler
mkdir -p %{buildroot}%{_datadir}/%{programname}/plugins/gitdiff_highlight
mkdir -p %{buildroot}%{_datadir}/%{programname}/fonts
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
### 'console.lua' seems to exist independent of what git repo provides/
cp -v %{SOURCE1} plugins/
#####
### 20221005, throwing error
#rm -v plugins/ipc.lua
# in ~/.config/lite-xl/init.lua:
# config.plugins.ipc = false
#####
install -D -m644 plugins/*.lua %{buildroot}%{_datadir}/%{programname}/plugins
install -D -m644 plugins/editorconfig/{*.md,*.lua} %{buildroot}%{_datadir}/%{programname}/plugins/editorconfig
install -D -m644 plugins/editorconfig/tests/*.lua %{buildroot}%{_datadir}/%{programname}/plugins/editorconfig/tests
install -D -m644 plugins/editorconfig/tests/glob/{*.in,*.lua} %{buildroot}%{_datadir}/%{programname}/plugins/editorconfig/tests/glob
install -D -m644 plugins/editorconfig/tests/parser/{*.in,*.lua} %{buildroot}%{_datadir}/%{programname}/plugins/editorconfig/tests/parser
install -D -m644 plugins/editorconfig/tests/properties/{*.in,*.lua} %{buildroot}%{_datadir}/%{programname}/plugins/editorconfig/tests/properties
install -D -m644 plugins/profiler/* %{buildroot}%{_datadir}/%{programname}/plugins/profiler
install -D -m644 %{SOURCE2} %{buildroot}%{_datadir}/%{programname}/fonts
install -D -m644 %{SOURCE3} %{buildroot}%{_datadir}/%{programname}/plugins/gitdiff_highlight/init.lua
install -D -m644 %{SOURCE4} %{buildroot}%{_datadir}/%{programname}/plugins/gitdiff_highlight/gitdiff.lua
install -D -m644 LICENSE %{buildroot}%{_datadir}/doc/%{name}/LICENSE
install -D -m644 README.md %{buildroot}%{_datadir}/doc/%{name}/README.md

%files
%dir %{_datadir}/%{programname}
%dir %{_datadir}/%{programname}/plugins
%dir %{_datadir}/%{programname}/plugins/gitdiff_highlight
%dir %{_datadir}/%{programname}/fonts
%dir %{_datadir}/doc/%{name}
%{_datadir}/%{programname}/plugins/*
%{_datadir}/%{programname}/fonts/*
%{_datadir}/doc/%{name}/LICENSE
%{_datadir}/doc/%{name}/README.md

%changelog

