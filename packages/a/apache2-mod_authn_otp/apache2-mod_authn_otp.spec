#
# spec file for package apache2-mod_authn_otp
#
# Copyright (c) 2024 SUSE LLC
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
Version:        1.1.10
Release:        0
Summary:        Apache module for one-time password authentication
License:        Apache-2.0
Group:          Productivity/Networking/Web/Servers
URL:            https://github.com/archiecobbs/mod-authn-otp
Source:         https://s3.amazonaws.com/archie-public/mod-authn-otp/%{mod_name}-%{version}.tar.gz
BuildRequires:  apache-rpm-macros
BuildRequires:  apache2-devel
BuildRequires:  pkgconfig(openssl)
Requires:       %{apache_mmn}
Requires:       %{apache_suse_maintenance_mmn}
Provides:       otptool = %{version}

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

Also included are two command line utilities, otptool and genotpurl.
otptool is a one-time password command line utility. It can be used
on a simple call-out basis to integrate two-factor authentication
into any existing authentication solution. genotpurl generates URLs
for the Google Authenticator app.

%prep
%setup -q -n %{mod_name}-%{version}

%build
%configure
%make_build

%install
install -d %{buildroot}%{apache_libexecdir}
%make_install

%files
%license LICENSE
%doc CHANGES README users.sample
%{apache_libexecdir}/%{mod_name}.so
%{_bindir}/otptool
%{_bindir}/genotpurl
%{_mandir}/man1/otptool.1.gz
%{_mandir}/man1/genotpurl.1.gz

%changelog
