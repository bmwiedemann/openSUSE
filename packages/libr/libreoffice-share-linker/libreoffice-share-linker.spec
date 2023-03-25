#
# spec file for package libreoffice-share-linker
#
# Copyright (c) 2023 SUSE LLC
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


Name:           libreoffice-share-linker
Version:        1
Release:        0
Summary:        Script to link/unlink files to libreoffice home
License:        MIT
Group:          Productivity/Office/Suite
URL:            http://www.opensuse.org/
Source0:        libreoffice-share-linker.py
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires:       python3
BuildArch:      noarch

%description
Script that links and unlinks files from %{_datadir} to libreoffice
home as libreoffice layout is not set up for noarch packages otherwise.

%prep
:

%build
:

%install
install -Dm 755 %{SOURCE0} %{buildroot}%{_bindir}/%{name}
# compat for migration from older releases openSUSE-13.1 and older
mkdir -p %{buildroot}%{_datadir}/libreoffice
pushd %{buildroot}%{_datadir}/libreoffice > /dev/null
ln -s %{_bindir}/%{name} libreoffice-share-linker.py
popd > /dev/null

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%dir %{_datadir}/libreoffice/
%{_datadir}/libreoffice/libreoffice-share-linker.py

%changelog
