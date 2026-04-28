#
# spec file for package susedialog
#
# Copyright (c) 2026 SUSE LLC and contributors
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

Name:           susedialog
Version:        20260427.b33f52d
Release:        0
Summary:        Fancy dialog replacement for openSUSE
License:        MIT
URL:            https://github.com/openSUSE/susedialog
Source0:        %{name}-%{version}.tar.xz
Source1:        vendor.tar.zst
BuildRequires:  go >= 1.23
BuildRequires:  golang-packaging
BuildRequires:  zstd

%global import_path github.com/openSUSE/susedialog
%define goipath %{import_path}

%description
openSUSE-focused, Bubble Tea-based compatibility shim for classic dialog
widgets. It is intended for shell-driven openSUSE tools such as
opensuse-migration-tool and jeos-firstboot.

The tool draws its interface on stdout and returns selected values on stderr,
matching the calling convention expected by many shell scripts that already use
dialog.

%prep
%autosetup -n %{name}-%{version} -a1

%build
export CGO_ENABLED=0
export GOFLAGS="-mod=vendor"
go build -o %{name} .

%install
install -Dpm0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1
install -Dpm0644 susedialog.config %{buildroot}%{_sysconfdir}/%{name}/config
install -Dpm0644 completion/bash/%{name} %{buildroot}%{_datadir}/bash-completion/completions/%{name}

%files
%license LICENSE
%doc README.md
%{_bindir}/susedialog
%{_mandir}/man1/susedialog.1%{?ext_man}
%{_datadir}/bash-completion/completions/%{name}
%dir %{_sysconfdir}/susedialog
%config(noreplace) %{_sysconfdir}/susedialog/config

%changelog

