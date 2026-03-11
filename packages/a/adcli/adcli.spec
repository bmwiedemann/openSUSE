#
# spec file for package adcli
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


%global selinuxtype targeted
%global modulename adcli
%if 0%{?suse_version} >= 1600
%bcond_without selinux
%else
%bcond_with selinux
%endif

%define filehash 5a1c55410c0965835b81fbd28d820d46
%define sighash b680d6103309863ce62e9acae98fd5bf
Name:           adcli
Version:        0.9.3.1
Release:        0
Summary:        Tool for performing actions on an Active Directory domain
License:        LGPL-2.0-or-later
Group:          Productivity/Networking/Other
URL:            https://gitlab.freedesktop.org/realmd/adcli
Source0:        https://gitlab.freedesktop.org/-/project/1196/uploads/%{filehash}/%{name}-%{version}.tar.gz
Source1:        https://gitlab.freedesktop.org/-/project/1196/uploads/%{sighash}/%{name}-%{version}.tar.gz.sig
# https://keys.openpgp.org/vks/v1/by-fingerprint/287939DF062AD8C53876A535C2D7B98A934EEC17
Source3:        %{name}.keyring
Patch1:         0001-enroll-fix-issues-if-default-keytab-is-used.patch
Patch2:         0002-Fix-build-with-glibc-2.43.patch
BuildRequires:  automake
BuildRequires:  libxslt-tools
BuildRequires:  openldap2-devel
BuildRequires:  pkgconfig
BuildRequires:  xmlto
BuildRequires:  pkgconfig(libsasl2)
%if %{with selinux}
BuildRequires:  selinux-policy-devel
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  pkgconfig(systemd)
%endif
BuildRequires:  pkgconfig(mit-krb5)
BuildRequires:  pkgconfig(netapi)

%description
A command line tool that can perform actions in an Active Directory domain.
Among other things it can be used to join a computer to a domain.

%if %{with selinux}
%package selinux
Summary:        SELinux module for adcli
BuildArch:      noarch
Requires:       selinux-policy-%{selinuxtype}
Requires(post): selinux-policy-%{selinuxtype}
%{selinux_requires}

%description selinux
This package provides the SELinux policy module to ensure adcli
runs properly under an environment with SELinux enabled.
%endif

%package doc
Summary:        Documentation for adcli
Group:          Documentation/Other
BuildArch:      noarch

%description doc
A command line tool that can perform actions in an Active Directory domain.
Among other things it can be used to join a computer to a domain.

This package contains the documentation for adcli.

%prep
%autosetup -p1

%build
%configure \
%if %{without selinux}
	--disable-selinux-support \
%endif
	--disable-static \
	--disable-silent-rules \
	--enable-strict
%make_build

%install
%make_install
# Remove zero-length file.
rm %{buildroot}/%{_datadir}/doc/%{name}/adcli-docs.proc

%check
%make_build check

%if %{with selinux}
%pre selinux
%selinux_relabel_pre -s %{selinuxtype}

%post selinux
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{selinuxtype}/%{modulename}.pp

%postun selinux
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi

%posttrans selinux
%selinux_relabel_post -s %{selinuxtype}
%endif

%files
%license COPYING
%doc AUTHORS ChangeLog NEWS README
%{_sbindir}/%{name}
%{_mandir}/man8/adcli.8%{?ext_man}

%if %{with selinux}
%files selinux
%dir %{_datadir}/selinux/packages/targeted
%{_datadir}/selinux/packages/targeted/%{modulename}.pp
%ghost %verify(not md5 size mtime) %{_selinux_store_path}/%{selinuxtype}/active/modules/200/%{modulename}
%endif

%files doc
%license COPYING
%doc %{_datadir}/doc/%{name}

%changelog
