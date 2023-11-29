#
# spec file for package sbctl
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


Name:           sbctl
Version:        0.12
Release:        0
Summary:        Secure Boot key manager
License:        MIT
Group:          System/Boot
URL:            https://github.com/Foxboron/sbctl
Source:         %{name}-%{version}.tar.gz
Source1:        vendor.tar.gz
Requires:       binutils
%if 0%{?suse_version}
Requires:       util-linux-systemd
%endif
%if 0%{?ubuntu}
Requires:       util-linux
%endif
BuildRequires:  asciidoc
BuildRequires:  binutils
%if 0%{?suse_version}
BuildRequires:  golang-packaging
%endif
%if 0%{?ubuntu}
BuildRequires:  golang
%endif

%description
sbctl intends to be a user-friendly secure boot key manager capable of setting
up secure boot, offer key management capabilities, and keep track of files that
needs to be signed in the boot chain.

%prep
%autosetup -a 1

%build
%make_build all

%install
%make_install BINDIR="%{_sbindir}" PREFIX="%{_prefix}"

%files
%doc README.md
%license LICENSE

%dir %{_prefix}/lib/kernel/
%dir %{_prefix}/lib/kernel/install.d/
%dir %{_datadir}/fish/
%dir %{_datadir}/fish/vendor_completions.d/
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions/

%{_prefix}/lib/kernel/install.d/91-sbctl.install
%{_mandir}/man8/sbctl.8*
%{_datadir}/bash-completion/completions/sbctl
%{_datadir}/fish/vendor_completions.d/sbctl.fish
%{_datadir}/zsh/site-functions/_sbctl
%{_sbindir}/sbctl

%changelog
