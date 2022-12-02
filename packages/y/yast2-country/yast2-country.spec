#
# spec file for package yast2-country
#
# Copyright (c) 2022 SUSE LLC
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


Name:           yast2-country
Version:        4.5.3
Release:        0
Summary:        YaST2 - Country Settings (Language, Keyboard, and Timezone)
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://github.com/yast/yast-country

Source0:        %{name}-%{version}.tar.bz2

BuildRequires:  update-desktop-files
BuildRequires:  yast2-devtools >= 4.2.2
BuildRequires:  yast2-perl-bindings
# For tests
BuildRequires:  glibc-locale
BuildRequires:  rubygem(%rb_default_ruby_abi:rspec)
BuildRequires:  rubygem(%rb_default_ruby_abi:yast-rake)
# Fix to bnc#891053 (proper reading of ".target.yast2" on chroots)
BuildRequires:  yast2-core >= 3.1.12
# yast/rspec/helpers.rb
BuildRequires:  yast2-ruby-bindings >= 4.4.7
# Yast2::CommandLine readonly parameter
BuildRequires:  yast2 >= 4.2.57
# systemd-mini does not add the xkb generated map which is needed by
# the Keyboards.all_keyboards unit/integration test
BuildRequires:  systemd

Requires:       timezone
Requires:       yast2-perl-bindings
Requires:       yast2-trans-stats
# Yast2::CommandLine readonly parameter
Requires:       yast2 >= 4.2.57
# Pkg::SetPackageLocale, Pkg::GetTextLocale
Requires:       yast2-pkg-bindings >= 2.15.3
# IconPath support for MultiSelectionBox
Requires:       yast2-core >= 2.16.28
Requires:       yast2-packager >= 2.23.3
# VMware detection (.probe.is_vmware)
Requires:       yast2-hardware-detection >= 3.1.6
Requires:       yast2-country-data
Requires:       yast2-ruby-bindings >= 1.0.0
Requires:       rubygem(%{rb_default_ruby_abi}:ruby-dbus)

# Y2Network::NtpServer
Conflicts:      yast2-ntp-client < 4.2.8

Supplements:    autoyast(language:keyboard:timezone)

%description
Country specific data and configuration modules (language, keyboard,
timezone) for yast2.

%package data
Requires:       yast2-ruby-bindings >= 1.0.0

Summary:        YaST2 - Data files for Country settings
Group:          System/YaST

%description data
Data files for yast2-country together with the most often used API
functions (Language module)

%prep
%setup -q

%check
rake test:unit

%build

%install
rake install DESTDIR="%{buildroot}"

%ifarch s390 s390x
rm -f %{buildroot}%{yast_desktopdir}/org.opensuse.yast.Keyboard.desktop
%endif

%yast_metainfo

# Policies
mkdir -p %{buildroot}%{_datadir}/polkit-1/actions

# common
%files
%doc %{yast_docdir}
%license COPYING
%{yast_moduledir}/Console.rb
%{yast_moduledir}/Keyboard.rb
%{yast_moduledir}/Timezone.rb
%dir %{yast_moduledir}/YaPI
%{yast_moduledir}/YaPI/TIME.pm
%{yast_moduledir}/YaPI/LANGUAGE.pm
%{yast_clientdir}/*.rb
%dir %{yast_libdir}/y2country
%{yast_libdir}/y2country/widgets
%{yast_libdir}/y2country/clients
%{yast_libdir}/y2keyboard
%{yast_ydatadir}/*.ycp
%{yast_ydatadir}/*.json
%{yast_yncludedir}
%{yast_scrconfdir}
%{yast_schemadir}
%{yast_desktopdir}
%{yast_metainfodir}
%{yast_icondir}

%files data
%dir %{yast_ydatadir}/languages
%{yast_ydatadir}/languages/*.ycp
%{yast_moduledir}/Language.rb
%dir %{yast_libdir}/y2country
%{yast_libdir}/y2country/language_dbus.rb

%changelog
