#
# spec file for package dfc
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2013 Asterios Dramis <asterios.dramis@gmail.com>.
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


Name:           dfc
Version:        3.1.1
Release:        0
Summary:        Display file system space usage using graphs and colors
License:        BSD-3-Clause
URL:            https://github.com/rolinh/dfc
Source0:        https://github.com/rolinh/dfc/releases/download/v%{version}/dfc-%{version}.tar.gz
BuildRequires:  cmake

%description
dfc is a simple tool that displays file system space usage using graphs and
colors.

%lang_package

%prep
%autosetup

%build
%cmake \
  -DSYSCONFDIR=%{_sysconfdir} \
  -DDFC_DOC_PATH=%{_docdir}/%{name}
%cmake_build

%install
%cmake_install
rm -rf %{buildroot}%{_docdir}/%{name}/LICENSE
%find_lang %{name} --with-man

%files
%license LICENSE
%doc AUTHORS.md CHANGELOG.md README.md HACKING.md TRANSLATORS.md
%dir %{_sysconfdir}/xdg/dfc/
%config(noreplace) %{_sysconfdir}/xdg/dfc/dfcrc
%{_bindir}/dfc
%{_mandir}/man1/dfc.1%{?ext_man}

%files lang -f %{name}.lang
%dir %{_sysconfdir}/xdg/dfc/
%dir %{_sysconfdir}/xdg/dfc/fr/
%config(noreplace) %{_sysconfdir}/xdg/dfc/fr/dfcrc
%dir %{_sysconfdir}/xdg/dfc/nl/
%config(noreplace) %{_sysconfdir}/xdg/dfc/nl/dfcrc

%changelog
