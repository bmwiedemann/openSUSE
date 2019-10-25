#
# spec file for package SUSEConnect
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           SUSEConnect
Version:        0.3.23
Release:        0
%define mod_name suse-connect
%define mod_full_name %{mod_name}-%{version}

# Does not build for i586 and s390 and is not supported on those architectures
ExcludeArch:    %ix86 s390

%if 0%{?fedora} || 0%{?rhel} || 0%{?centos_version}
Requires:       ca-certificates
%else
Requires:       ca-certificates-mozilla
%endif
Requires:       coreutils
Requires:       net-tools
Requires:       util-linux
Requires:       zypper
# Required by the rmt-client-setup script:
Recommends:     gawk
Recommends:     gpg2
Recommends:     grep
# Allows for installing openssl 1.0 without needing to remove SUSEConnect. See bsc#1101470.
%if 0%{?sle_version} < 120200
Recommends:     openssl
%else
Recommends:     openssl(cli)
%endif
Recommends:     sed
Recommends:     curl
Requires:       zypper(auto-agree-with-product-licenses)
%ifarch x86_64 aarch64
Requires:       dmidecode
%endif
Conflicts:      suseRegister, yast2-registration < 3.1.129.7

# In SLE12 GA we had a seperate rubygem-suse-connect package, which we need to obsolete now
%if (0%{?sle_version} > 0 && 0%{?sle_version} < 150000)
Obsoletes:      ruby2.1-rubygem-suse-connect < %{version}
Provides:       ruby2.1-rubygem-suse-connect = %{version}
%endif

# cross-distribution howto: https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto
%if 0%{?fedora} || 0%{?rhel} || 0%{?centos_version}
%define ruby_version ruby2.5
%global gem_base /usr/share/gems
%global debug_package %{nil}
%if 0%{?fedora} < 30
%define gem_install_options --bindir %{_bindir}
%else
%define gem_install_options --bindir %{buildroot}%{_bindir}
%endif
BuildRequires:  ruby
BuildRequires:  rubygems
%else
%define ruby_version %{rb_default_ruby_suffix}
%define gem_install_options %{nil}
BuildRequires:  %{ruby_version}
%endif

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Url:            https://github.com/SUSE/connect

Source:         %{mod_full_name}.gem
Source1:        %{name}.5
Source2:        %{name}.8
Source3:        %{name}.example
Patch0:         switch_server_cert_location_to_etc.patch

Summary:        Utility to register a system with the SUSE Customer Center
License:        LGPL-2.1
Group:          System/Management
Requires(post): /usr/sbin/update-alternatives


%description
This package provides a command line tool and rubygem library for connecting a
client system to the SUSE Customer Center. It will connect the system to your
product subscriptions and enable the product repositories/services locally.

%prep
for s in %{sources}; do
    cp -p $s .
done
for s in %{patches}; do
    cp -p $s .
done

%build

%install
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_bindir}
gem install --verbose --local --build-root=%{buildroot} --no-user-install -f --no-document %{gem_install_options} ./%{mod_full_name}.gem
mv %{buildroot}%{_bindir}/%{name}* %{buildroot}%{_sbindir}/%{name}
ln -s %{_sbindir}/%{name} %{buildroot}%{_bindir}/%{name}

# system certificate location changed to /etc/pki/trust/anchors/registration_server.pem, see bsc#1130864
# sle_version >= 150200 is matching SLES + Leap >= 15SP2, suse_version >= 1550 is Tumbleweed
%if (0%{?sle_version} >= 150200 || 0%{?suse_version} >= 1550)
patch -d %{buildroot}%{gem_base}/gems/%{mod_full_name} -p1 < switch_server_cert_location_to_etc.patch
%endif

install -D -m 644 %_sourcedir/SUSEConnect.5 %{buildroot}%_mandir/man5/SUSEConnect.5
install -D -m 644 %_sourcedir/SUSEConnect.8 %{buildroot}%_mandir/man8/SUSEConnect.8
install -D -m 644 %_sourcedir/SUSEConnect.example %{buildroot}%_sysconfdir/SUSEConnect.example

touch %{buildroot}%_sysconfdir/SUSEConnect
mkdir -p %{buildroot}%_sysconfdir/zypp/credentials.d/
touch %{buildroot}%_sysconfdir/zypp/credentials.d/SCCcredentials

%post
if [ -s /etc/zypp/credentials.d/NCCcredentials ] && [ ! -e /etc/zypp/credentials.d/SCCcredentials ]; then
    echo "Imported NCC system credentials to /etc/zypp/credentials.d/SCCcredentials"
    cp /etc/zypp/credentials.d/NCCcredentials /etc/zypp/credentials.d/SCCcredentials
fi

if [ -s /etc/suseRegister.conf ]; then
    reg_server=$(sed -n "s/^[[:space:]]*url[[:space:]]*=[[:space:]]*\(https\?:\/\/[^\/]*\).*/\1/p" /etc/suseRegister.conf)
    # if we have a custom regserver and no SCC config yet, write it
    if [ -n "$reg_server" ] && [ "$reg_server" != "https://secure-www.novell.com" ] && [ ! -e /etc/SUSEConnect ]; then
        echo "Imported /etc/suseRegister.conf registration server url to /etc/SUSEConnect"
        echo "url: $reg_server" > /etc/SUSEConnect
    fi
fi

# remove stale update-alternatives config left by previous split, versioned packaging of SUSEConnect
if update-alternatives --config SUSEConnect  &> /dev/null ; then
  update-alternatives --force --quiet --remove-all SUSEConnect
  ln -fs ../sbin/%{name} %{_bindir}/%{name}
fi

%files
%defattr(-,root,root,-)
%{_sbindir}/SUSEConnect
%{_bindir}/SUSEConnect
%{gem_base}/gems/%{mod_full_name}/
%{gem_base}/cache/%{mod_full_name}.gem
%{gem_base}/specifications/%{mod_full_name}.gemspec

%doc %{_mandir}/man5/SUSEConnect.5.*
%doc %{_mandir}/man8/SUSEConnect.8.*

%config(noreplace) %ghost %{_sysconfdir}/SUSEConnect
%config %{_sysconfdir}/SUSEConnect.example
%config %dir %{_sysconfdir}/zypp/
%config %dir %{_sysconfdir}/zypp/credentials.d/
%config(noreplace) %ghost %{_sysconfdir}/zypp/credentials.d/SCCcredentials

%changelog
