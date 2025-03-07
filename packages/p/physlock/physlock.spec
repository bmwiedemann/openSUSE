#
# spec file for package physlock
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2020 SUSE Software Solutions Germany GmbH, Nuernberg, Germany.
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


%if ! %{defined _pam_vendordir}
%define _pam_vendordir %{_sysconfdir}/pam.d
%endif

Name:           physlock
Version:        13
Release:        0
Summary:        Lightweight linux console locking tool
URL:            https://github.com/muennich/physlock
Group:          Productivity/Security
License:        GPL-2.0-only
Source0:        https://github.com/muennich/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-rpmlintrc
Patch0:         %{name}-%{version}.dif
Patch1:         nofreeze.patch
Patch2:         allow_cmd_before_and_after.patch
Patch3:         resume_hybernate.patch
Patch4:         set_PAM_TTY.patch
BuildRequires:  glibc-devel
BuildRequires:  pam-devel
BuildRequires:  permissions-config
BuildRequires:  pkgconfig(libsystemd)
Requires(pre):  group(trusted)
Requires(post): permissions
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Control physical access to a linux computer by locking all of its virtual
terminals / consoles.

physlock is an alternative to vlock, it is equivalent to `vlock -an'. It is
written because vlock blocks some linux kernel mechanisms like hibernate and
suspend and can therefore only be used with some limitations. physlock is
designed to be more lightweight, it does not have a plugin interface and it is
not started using a shell script wrapper.

With permission mode easy all users, which are members of the group called
trusted, can use physlock as well.

%prep
%setup -q
%autopatch -p0

%build
export CFLAGS="%{optflags} -fPIE -DHAVE_SYSTEMD"
export LDFLAGS="-pie"
make %{?_smp_mflags}

%install
%make_install PREFIX=%{_prefix}
mkdir -p %{buildroot}%{_pam_vendordir}
cat > %{buildroot}%{_pam_vendordir}/physlock <<-'EOF'
	auth		required	pam_unix.so	nis try_first_pass
	account		required	pam_unix.so	nis try_first_pass
	password	required	pam_unix.so	nis try_first_pass
	session		required	pam_unix.so	nis try_first_pass
	EOF

%post
%set_permissions %{_bindir}/%{name}

%verifyscript
%verify_permissions -e %{_bindir}/%{name}

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE
%{_pam_vendordir}/physlock
%verify(not mode group) %attr(04750,root,trusted) %{_bindir}/%{name}
%{_mandir}/man?/%{name}.?%{ext_man}

%changelog
