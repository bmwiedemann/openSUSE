#
# spec file for package gcin-branding-openSUSE
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           gcin-branding-openSUSE
Version:        12.1
Release:        0
Summary:        openSUSE branding of gcin
License:        LGPL-2.1
Group:          System/I18n/Chinese
Url:            http://hyperrate.com
Source:         gcin-kai-mono.tar.bz2
BuildRequires:  gcin
BuildRequires:  gcin-branding-upstream
%define gcin_version %(rpm -q --qf '%%{version}-%%{release}' gcin)
Provides:       gcin-branding = %{gcin_version}
Conflicts:      otherproviders(gcin-branding)
Supplements:    packageand(gcin:branding-openSUSE)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       gcin

%description
This package provides openSUSE Look and Feel for gcin

%prep
%setup -n gcin-kai-mono

%install
# use small icons
mkdir -p %{buildroot}%{_datadir}/icons/gcin
install -D 22/* %{buildroot}%{_datadir}/icons/gcin/

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%post

%postun

%files
%defattr(-,root,root)
%doc COPYING
%{_datadir}/icons/gcin/*

%changelog
