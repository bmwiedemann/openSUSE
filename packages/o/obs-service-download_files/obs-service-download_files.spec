#
# spec file
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


%define service download_files
%if 0%{?fedora} || 0%{?rhel}
%define build_pkg_name obs-build
%else
%define build_pkg_name build
%endif
Name:           obs-service-%{service}
Version:        0.9.2
Release:        0
Summary:        An OBS source service: download files
License:        GPL-2.0-or-later
URL:            https://github.com/openSUSE/obs-service-%{service}
Source0:        %{url}/archive/refs/tags/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  %{build_pkg_name}
BuildRequires:  bzip2
BuildRequires:  tar
BuildRequires:  (curl or curl-minimal)
BuildRequires:  perl(File::Type)
BuildRequires:  perl(FindBin)
BuildRequires:  perl(HTTP::Server::Simple)
BuildRequires:  perl(Path::Class)
# provides: /usr/bin/prove
BuildRequires:  perl(Test::Harness)
BuildRequires:  perl(Test::More)
Requires:       %{build_pkg_name} >= 2012.08.24
Requires:       curl
Requires:       diffutils
# for appimage parser:
Requires:       perl(YAML::XS)
BuildArch:      noarch

%description
This is a source service for openSUSE Build Service.

This service is parsing all spec files and downloads all Source files which are specified via a http, https or ftp url.

%prep
%autosetup

%build
perl -p -i -e "s{#!%{_bindir}/env bash}{#!/bin/bash}" download_files

%install
%make_install

%check
%make_build test

%files
%doc README.md
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service
%dir %{_sysconfdir}/obs
%dir %{_sysconfdir}/obs/services
%config(noreplace) %{_sysconfdir}/obs/services/*

%changelog
