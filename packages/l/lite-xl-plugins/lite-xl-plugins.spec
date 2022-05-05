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
Version:        git20220501.7bee960
Release:        0
Summary:        Additional plugins for %{programname}
License:        MIT
URL:            https://github.com/lite-xl/lite-xl-plugins
Source0:        %{name}-%{version}.tar.gz
### https://raw.githubusercontent.com/lite-xl/console/master/init.lua ==> console.lua
Source1:        console.lua
### https://github.com/yamatsum/nonicons/raw/master/dist/nonicons.ttf
Source2:        nonicons.ttf
### https://github.com/lite-xl/lite-xl-plugins/issues/40#issuecomment-1059862448
Source3:        indentguide.lua
### https://raw.githubusercontent.com/vincens2005/lite-xl-gitdiff-highlight/master/init.lua
Source4:        gitdiff_highlight-init.lua
### https://raw.githubusercontent.com/vincens2005/lite-xl-gitdiff-highlight/master/gitdiff.lua
Source5:        gitdiff_highlight-gitdiff.lua
Source6:        smb-addl-nonicons.txt
Patch0:         datetimestamps.patch
Patch1:         nonicons.patch
Recommends:     words
BuildArch:      noarch

%description
Plugins for the Lite XL text editor, originally forked from the lite plugins repository.

%prep
%setup -q
%patch0
%patch1

%build
sed -i '/  -- Following without special icon:/ r %{SOURCE6}' %{_builddir}/%{name}-%{version}/plugins/nonicons.lua

%install
mkdir -p %{buildroot}%{_datadir}/%{programname}/plugins
mkdir -p %{buildroot}%{_datadir}/%{programname}/plugins/gitdiff_highlight
mkdir -p %{buildroot}%{_datadir}/%{programname}/fonts
mkdir -p %{buildroot}%{_datadir}/doc/%{name}
### Already provided by base package; conflicts if included.
rm plugins/language_cpp.lua
### 'console.lua' seems to be independent of what git repo provides/
cp -v %{SOURCE1} plugins/
### 'indentguide.lua' seems broken otherwise.
cp -v %{SOURCE3} plugins/
#####
install -D -m644 plugins/* %{buildroot}%{_datadir}/%{programname}/plugins
install -D -m644 %{SOURCE2} %{buildroot}%{_datadir}/%{programname}/fonts
install -D -m644 %{SOURCE4} %{buildroot}%{_datadir}/%{programname}/plugins/gitdiff_highlight/init.lua
install -D -m644 %{SOURCE5} %{buildroot}%{_datadir}/%{programname}/plugins/gitdiff_highlight/gitdiff.lua
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

