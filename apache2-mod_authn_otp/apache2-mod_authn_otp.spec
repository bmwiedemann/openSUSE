#
# spec file for package apache2-mod_authn_otp
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Archie L. Cobbs <archie@dellroad.org>
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


%define mod_name           mod_authn_otp
Name:           apache2-%{mod_name}
Version:        1.1.9
Release:        0
Summary:        Apache module for one-time password authentication
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
Url:            http://mod-authn-otp.googlecode.com/
Source:         https://s3.amazonaws.com/archie-public/mod-authn-otp/%{mod_name}-%{version}.tar.gz
BuildRequires:  apache-rex
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
%apache_rex_deps
Requires:       %{apache_mmn}
Requires:       %{apache_suse_maintenance_mmn}
Provides:       otptool = %{version}
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%if 0%{?suse_version} >= 1100
BuildRequires:  libopenssl-devel
BuildRequires:  openssl
%else
BuildRequires:  openssl-devel
%endif

%description
mod_authn_otp is an Apache web server module for two-factor authentication
using one-time passwords (OTP) generated via the HOTP/OATH algorithm
defined in RFC 4226. This creates a simple way to protect a web site with
one-time passwords, using any RFC 4226-compliant hardware or software
token device. mod_authn_otp also supports the Mobile-OTP algorithm.

mod_authn_otp supports both event and time based one-time passwords. It
also supports "lingering" which allows the repeated re-use of a previously
used one-time password up to a configurable maximum linger time. This
allows one-time passwords to be used directly in HTTP authentication
without forcing the user to enter a new one-time password for every
page load.

mod_authn_otp supports both basic and digest authentication, and will
auto-synchronize with the user's token within a configurable maximum
offset (auto-synchronization is not supported with digest authentication).

mod_authn_otp is especially useful for setting up protected web sites
that require more security than simple username/password authentication
yet also don't require users to install special VPN software, and is
compatible with software tokens that run on cell phones.

Also included is otptool, a one-time password command line utility.
otptool can be used on a simple call-out basis to integrate two-factor
authentication into any existing authentication solution.

%prep
%setup -q -n %{mod_name}-%{version}

%build
%configure
make %{?_smp_mflags}

%install
install -d %{buildroot}%{apache_libexecdir}
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%check
%apache_rex_check -m .libs/ -b . mod_authn_otp-basic

%files
%defattr(-,root,root,-)
%{apache_libexecdir}/%{mod_name}.so
%{_bindir}/otptool
%{_bindir}/genotpurl
%{_mandir}/man1/otptool.1.gz
%{_mandir}/man1/genotpurl.1.gz
%doc CHANGES LICENSE README users.sample

%changelog
