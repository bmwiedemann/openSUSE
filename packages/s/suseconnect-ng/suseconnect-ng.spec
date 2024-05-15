#
# spec file for package suseconnect-ng
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


%global project github.com/SUSE/connect-ng

Name:           suseconnect-ng
Version:        1.9.0
Release:        0
URL:            https://github.com/SUSE/connect-ng
License:        LGPL-2.1-or-later
Summary:        Utility to register a system with the SUSE Customer Center
Group:          System/Management
Source:         suseconnect-ng-%{version}.tar.xz
Source1:        %{name}-rpmlintrc

# Build against latest golang in Tumbleweed and
# go1.18-openssl on all other distributions
%if 0%{?suse_version} > 1600
BuildRequires:  golang(API)
%else
BuildRequires:  go1.21-openssl
%endif

BuildRequires:  ruby-devel
BuildRequires:  zypper

ExcludeArch:    %ix86 s390 ppc64

Obsoletes:      SUSEConnect < 1.1.0
Provides:       SUSEConnect = %version
Obsoletes:      zypper-migration-plugin < 0.99
Provides:       zypper-migration-plugin = 0.99
Obsoletes:      zypper-search-packages-plugin < 0.99
Provides:       zypper-search-packages-plugin = 0.99

%if 0%{?suse_version}
Requires:       ca-certificates-mozilla
%else
Requires:       ca-certificates
%endif

Requires:       coreutils
# ExclusiveArch from this package
%ifarch ia64 x86_64 %arm aarch64
Requires:       dmidecode
%endif
# ExclusiveArch from this package
%ifarch s390x
Requires:       s390-tools
%endif
Requires:       zypper
# lscpu is only used on those
%ifarch aarch64
Requires:       util-linux
%endif
Recommends:     systemd

%description
This package provides a command line tool for connecting a
client system to the SUSE Customer Center. It will connect the system to your
product subscriptions and enable the product repositories/services locally.
suseconnect-ng reduces the size of its runtime dependencies compared to the
replaced SUSEConnect.

%package -n libsuseconnect
Summary:        C interface to suseconnect-ng
Group:          System/Management
# the CLI is not used by libsuseconnect but it has the same dependencies and it's easier to keep one list above
Requires:       suseconnect-ng

%description -n libsuseconnect
This package contains library which provides C interface to selected
suseconnect-ng functions.

%package -n suseconnect-ruby-bindings
Summary:        Ruby bindings for libsuseconnect library
Group:          System/Management
Requires:       libsuseconnect
# Adding the rubygem provides, to work as a drop-in replacement for Ruby SUSEConnect on SLE15<SP4
%if (0%{?sle_version} > 0 && 0%{?sle_version} < 150400)
Provides:       rubygem(ruby:2.5.0:suse-connect)
%endif

%description -n suseconnect-ruby-bindings
This package provides bindings needed to use libsuseconnect from Ruby scripts.

%prep
%autosetup -p 1 -n %{name}-%{version}

%build
# the binary
echo %{version} > internal/connect/version.txt
go build -v -ldflags "-s -w" -buildmode=pie -o bin/suseconnect %{project}/suseconnect

# the library
mkdir -p %_builddir/go/lib
go build -v -ldflags "-s -w" -buildmode=c-shared -o lib/libsuseconnect.so %{project}/libsuseconnect

%install
# Install binary + symlinks
install -D -m 0755 bin/suseconnect %{buildroot}/%{_bindir}/suseconnect
install -d -m 0755 %{buildroot}/%{_sbindir} %{buildroot}/usr/lib/zypper/commands
ln -s %{_bindir}/suseconnect %{buildroot}/%{_bindir}/SUSEConnect
ln -s %{_bindir}/suseconnect %{buildroot}/%{_sbindir}/SUSEConnect
ln -s %{_bindir}/suseconnect %{buildroot}/usr/lib/zypper/commands/zypper-migration
ln -s %{_bindir}/suseconnect %{buildroot}/usr/lib/zypper/commands/zypper-search-packages

# Install library + ruby bindings
install -D -m 0755 lib/libsuseconnect.so %{buildroot}/%{_libdir}/libsuseconnect.so
install -d -m 0755 %{buildroot}/%{_libdir}/ruby/vendor_ruby/%{rb_ver}
cp -r yast/lib/* %{buildroot}/%{_libdir}/ruby/vendor_ruby/%{rb_ver}

# Install metadata
install -D -m 644 man/SUSEConnect.5 %{buildroot}/%{_mandir}/man5/SUSEConnect.5
install -D -m 644 man/SUSEConnect.8 %{buildroot}/%{_mandir}/man8/SUSEConnect.8
install -D -m 644 man/zypper-migration.8 %{buildroot}/%{_mandir}/man8/zypper-migration.8
install -D -m 644 man/zypper-search-packages.8 %{buildroot}/%{_mandir}/man8/zypper-search-packages.8
install -D -m 644 SUSEConnect.example %{buildroot}%{_sysconfdir}/SUSEConnect.example

# Install the SUSEConnect --keepalive timer and service.
install -D -m 644 suseconnect-keepalive.timer %{buildroot}/%{_unitdir}/suseconnect-keepalive.timer
install -D -m 644 suseconnect-keepalive.service %{buildroot}/%{_unitdir}/suseconnect-keepalive.service
ln -sf service %{buildroot}/%{_sbindir}/rcsuseconnect-keepalive

# we currently do not ship the source for any go module
rm -rf %{buildroot}/usr/share/go

%pre
%service_add_pre suseconnect-keepalive.service suseconnect-keepalive.timer

# in pre blocks the old version is still installed. This way we can detect
# if --keepalive was already present before
kainfo=0
helptext=$(test -x "$(type -p SUSEConnect)" && SUSEConnect --help)
if [ $? -eq 0 ]; then
    echo "$helptext" | grep -q keepalive
    kainfo=$?
fi

if [ $kainfo -ne 0 ]; then
  cat << EOF
Empowering you with enriched system visibility in the SUSE Customer Center

SUSE is committed to helping provide better insights into the consumption of
SUSE subscriptions regardless of where they are running; physical or virtual,
on-prem or in the cloud.

SUSE has been working on several improvements to the SUSE Customer Center (SCC),
RMT, and SUSE Manager to provide a clearer picture of your system landscape:

- SUSE Manager v4.1+ now sends system information to SCC.
- SCC now captures which products are activated on systems that sit behind RMT
  or SMT.
- This update will enable your system to "ping" SCC/RMT daily to
  confirm the system's active status. This will help you identify or filter out
  systems in SCC that are no longer running or decommissioned. As always, the
  choice is yours, you can disable the daily ping by disabling the
  suseconnect-keepalive systemd timer.

We will continue improving our products to make it easier for you to view and
manage your subscription consumption. As always, we'd love to hear your feedback
about these improvements and any ideas you might have.
EOF
fi

# If the keepalive timer exists on package install (not upgrade), then we are replacing SUSEConnect.
# Record the enabled and active statuses so they can be restored in posttrans macro.
if [ "$1" -eq 1 ]; then
  /usr/bin/systemctl is-enabled suseconnect-keepalive.timer >/dev/null 2>&1 && touch /run/suseconnect-keepalive.timer.is-enabled || :
  /usr/bin/systemctl is-active suseconnect-keepalive.timer >/dev/null 2>&1 && touch /run/suseconnect-keepalive.timer.is-active || :
fi

%post
# Randomize schedule time for SLES12. SLES12 systemd does not support RandomizedDelaySec.
%if (0%{?sle_version} > 0 && 0%{?sle_version} < 150000)
    TIMER_HOUR=$(( RANDOM % 24 ))
    TIMER_MINUTE=$(( RANDOM % 60 ))
    sed -i '/RandomizedDelaySec*/d' %{_unitdir}/suseconnect-keepalive.timer
    sed -i "s/OnCalendar=daily/OnCalendar=*-*-* $TIMER_HOUR:$TIMER_MINUTE:00/" %{_unitdir}/suseconnect-keepalive.timer
%endif
%service_add_post suseconnect-keepalive.service suseconnect-keepalive.timer

%preun
%service_del_preun suseconnect-keepalive.service suseconnect-keepalive.timer

%postun
%service_del_postun suseconnect-keepalive.service suseconnect-keepalive.timer

%posttrans
if [ -e /run/suseconnect-keepalive.timer.is-enabled ]; then
   /usr/bin/systemctl enable suseconnect-keepalive.timer >/dev/null 2>&1 || :
   rm /run/suseconnect-keepalive.timer.is-enabled ||:
fi
if [ -e /run/suseconnect-keepalive.timer.is-active ]; then
  /usr/bin/systemctl start suseconnect-keepalive.timer >/dev/null 2>&1 || :
  rm /run/suseconnect-keepalive.timer.is-active ||:
fi

%files
%license LICENSE LICENSE.LGPL
%doc README.md
%{_bindir}/suseconnect
%{_bindir}/SUSEConnect
%{_sbindir}/SUSEConnect
%{_sbindir}/rcsuseconnect-keepalive
/usr/lib/zypper/commands
%{_mandir}/man8/*
%{_mandir}/man5/*
%{_unitdir}/suseconnect-keepalive.service
%{_unitdir}/suseconnect-keepalive.timer
%config %{_sysconfdir}/SUSEConnect.example

%files -n libsuseconnect
%license LICENSE LICENSE.LGPL
%{_libdir}/libsuseconnect.so

%files -n suseconnect-ruby-bindings
%doc yast/README.md
%{_libdir}/ruby/vendor_ruby/%rb_ver/suse

%changelog
