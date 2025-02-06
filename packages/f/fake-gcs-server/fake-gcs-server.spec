#
# spec file for package fake-gcs-server
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


# Please submit bugfixes or comments via https://bugs.opensuse.org/
#
%global provider_prefix github.com/fsouza/fake-gcs-server/fakestorage
%global import_path     %{provider_prefix}
Name:           fake-gcs-server
Version:        1.52.1
Release:        0
Summary:        Google Cloud Storage emulator & testing library
License:        BSD-2-Clause
URL:            https://github.com/fsouza/fake-gcs-server
Source0:        https://github.com/fsouza/%{name}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
BuildRequires:  fdupes
BuildRequires:  go >= 1.23.0
BuildRequires:  golang-packaging
BuildRequires:  xz
%{go_nostrip}
%{go_provides}

%description
fake-gcs-server provides an emulator for Google Cloud Storage API. It can be used as a library in Go projects and/or as a standalone binary/Docker image.

%prep
%autosetup -p1 -a1

%build
%goprep %{import_path}
go build

%install
%goinstall
install -Dm755 fake-gcs-server %{buildroot}%{_bindir}/fake-gcs-server
%gosrc

%fdupes %{buildroot}%{_datadir}/go

%{gofilelist}

%check
%gotest %{import_path}

%files -f file.lst
%license LICENSE
%doc README.md
%{_bindir}/fake-gcs-server

%changelog
