#
# spec file for package systemd-repart-dracut
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
# icecream 0


%if 0%{?_build_in_place}
%define git_version %(git log '-n1' '--date=format:%Y%m%d' '--no-show-signature' "--pretty=format:+git%cd.%h")
BuildRequires:  git-core
%else
# this is required for obs' source validator. It's
# 20-files-present-and-referenced ignores all conditionals. So the
# definition of git_version actually happens always.
%define git_version %{nil}
%endif

Name:           systemd-repart-dracut
Version:        1+git20260128.1b0de2b%{git_version}
Release:        0
Summary:        Systemd-repart service dracut module
License:        MIT
URL:            https://github.com/openSUSE/systemd-repart-dracut
Source:         systemd-repart-dracut-%{version}.tar
BuildRequires:  systemd-rpm-macros
ExclusiveArch:  aarch64 ppc64le powerpc64le riscv64 x86_64
BuildArch:      noarch
%{?systemd_requires}

%description

Dracut module which is calling systemd-repart before encryption.

%prep
%setup -q

%build

%install
mkdir -p %buildroot/usr/lib/dracut/modules.d/94systemd-repart-dracut
for i in systemd-repart-dracut{,.service} module-setup.sh; do
  cp "$i" %buildroot/usr/lib/dracut/modules.d/94systemd-repart-dracut/"$i"
done
mkdir -p %buildroot/usr/bin
ln -s ../lib/dracut/modules.d/94systemd-repart-dracut/systemd-repart-dracut %buildroot/usr/bin

%files
%license LICENSE
/usr/bin/systemd-repart-dracut
%dir /usr/lib/dracut
%dir /usr/lib/dracut/modules.d
/usr/lib/dracut/modules.d/94systemd-repart-dracut

%changelog
