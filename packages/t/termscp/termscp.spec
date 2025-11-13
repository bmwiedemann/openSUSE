#
# spec file for package termscp
#
# Copyright (c) 2025 SUSE LLC and contributors
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


Name:           termscp
Version:        0.19.0
Release:        0
Summary:        Feature rich terminal UI file transfer and explorer
License:        MIT
URL:            https://github.com/veeso/termscp
Source0:        %{name}-%{version}.tar.gz
Source1:        vendor.tar.zst
BuildRequires:  cargo >= 1.84
BuildRequires:  cargo-packaging
BuildRequires:  zstd
BuildRequires:  pkgconfig(dbus-1)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(smbclient)

# error[E0063]: missing fields `bavail`, `bfree`, `blocks` and 3 other fields in initializer of `types::stat::SmbStatVfs`
#
ExcludeArch:    i586 ppc64le s390x

%description
Termscp is a feature rich terminal file transfer and explorer, with support for
SCP/SFTP/FTP/Kube/S3/WebDAV. So basically is a terminal utility with an TUI to
connect to a remote server to retrieve and upload files and to interact with
the local file system. It is Linux, MacOS, FreeBSD, NetBSD and Windows
compatible.

%prep
%autosetup -a 1 -p 1

%build
%{cargo_build}

%install
install -D -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 %{_builddir}/%{name}-%{version}/target/release/%{name} %{buildroot}%{_bindir}/%{name}

%check
# skip two tests that need network connectivity
%{cargo_test} \
        --features isolated-tests \
        -- --skip 'system::auto_update::test::test_should_check_whether_github_api_is_reachable' \
        --skip 'system::logging::test::test_system_logging_setup'

%files
%{_bindir}/%{name}

%changelog
