#
# spec file for package lxqt-theme-openSUSE-leaper
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define	theme	openSUSE-leaper
%define	themedir	%{buildroot}%{_datadir}/lxqt/themes/openSUSE-leaper

Name:           lxqt-theme-%{theme}
Version:        0.1
Release:        0
Summary:        Leaper theme for LXQt
License:        CC-BY-SA-4.0
Group:          System/GUI/Other
Url:            http://lxqt.org
Source:         https://github.com/jubalh/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  lxqt-themes
Requires:       lxqt-themes
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
%{theme} for LXQt lightweight Qt desktop environment

%prep
%setup -q

%build

%install
mkdir -p %{themedir}
cp -r * %{themedir}
chmod 0755 %{themedir}
rm -rf %{themedir}/spacer-plugin/*
ln -sf %{_datadir}/lxqt/graphics/spacer-dark-dots.svg %{themedir}/spacer-plugin/spacer-dots.svg
ln -sf %{_datadir}/lxqt/graphics/spacer-dark-line.svg %{themedir}/spacer-plugin/spacer-line.svg

%files
%defattr(-,root,root)
%{_datadir}/lxqt/themes/openSUSE-leaper/

%changelog
