#
# spec file for package obs-service-go_modules
#
# Copyright (c) 2024 SUSE LLC
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


%define service go_modules
%if 0%{?suse_version} >= 1315 || 0%{?fedora_version} >= 29
%bcond_without python3
%else
%bcond_with    python3
%endif
# This list probably needs to be extended
# logic seems to be if python < 2.7 ; then needs_external_argparse ; fi
%if (0%{?centos_version} == 6) || (0%{?suse_version} && 0%{?suse_version} < 1315) || (0%{?fedora_version} && 0%{?fedora_version} < 26)
%bcond_without needs_external_argparse
%else
%bcond_with    needs_external_argparse
%endif
%if %{with python3}
%define use_python python3
%define use_test   test3
%else
%define use_python python
%define use_test   test
%endif
Name:           obs-service-%{service}
Version:        0.6.4
Release:        0
Summary:        An OBS source service: Download, verify and vendor Go module dependencies
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://github.com/openSUSE/obs-service-%{service}
Source:         %{name}-%{version}.tar.gz
BuildRequires:  go-md2man
Requires:       python3-libarchive-c
Requires:       golang(API) >= 1.22
BuildArch:      noarch
%if %{with needs_external_argparse}
BuildRequires:  %{use_python}-argparse
%endif
%if %{with python3}
BuildRequires:  %{use_python}
# Fix missing Requires in python3-pbr in Leap42.3
BuildRequires:  %{use_python}-setuptools
%endif

%description
An OBS Source Service that will download,
verify and vendor Go module dependency sources.

Using go.mod and go.sum present in a Go application,
the source service will call Go tools in sequence:

go mod download
go mod verify
go mod vendor

Then create a vendor.tar.gz populated with the contents of
vendor/

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
mkdir -p %{buildroot}%{_prefix}/lib/obs/service
install -m 0755 go_modules %{buildroot}%{_prefix}/lib/obs/service
install -m 0644 go_modules.service %{buildroot}%{_prefix}/lib/obs/service

# Build the man page from markdown documentation.
go-md2man -in README.md -out %{name}.1

# Install the man page.
install -D -m 0644 %{name}.1 "%{buildroot}/%{_mandir}/man1/%{name}.1"
rm %{name}.1

%files
%doc README.md
%license LICENSE
%dir %{_prefix}/lib/obs
%{_prefix}/lib/obs/service
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
