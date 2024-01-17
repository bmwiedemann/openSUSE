#
# spec file for package live-langset-data
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


Name:           live-langset-data
Version:        2.0
Release:        0
Summary:        Scripts and data to allow locale switching in live media
License:        GPL-2.0-only
Group:          System/YaST
URL:            https://build.opensuse.org/package/show/openSUSE:Factory:Live/live-langset-data
Source1:        langset.sh
Source2:        langset.service
Source3:        getcountrydata.rb
Source4:        gpl-2.0.txt
BuildRequires:  coreutils
BuildRequires:  systemd-rpm-macros
BuildRequires:  yast2-country
# Needed for X11 keyboard data
BuildRequires:  yast2-x11
# Support for /etc/sysconfig/language was dropped
%if 0%{?suse_version} < 1500
BuildRequires:  newer-distro
%endif
Requires:       sed
Requires:       systemd
BuildArch:      noarch
%{?systemd_requires}

%description
This package contains scripts and data to allow setting the locale (+ console font and keyboard
layout) on live media.

%prep
%setup -q -T -c
cp %{SOURCE4} .

%build
mkdir output
OUTPUTDIR=$PWD/output %{_prefix}/lib/YaST2/bin/y2start %{SOURCE3} UI

%install
pushd output
for i in *; do
    install -Dm 644 $i %{buildroot}/%{_datadir}/langset/${i/.UTF-8}
done
popd
install -Dm 755 %{SOURCE1} %{buildroot}%{_sbindir}/langset.sh
install -Dm 644 %{SOURCE2} %{buildroot}%{_unitdir}/langset.service

%pre
%service_add_pre langset.service

%post
%service_add_post langset.service

%preun
%service_del_preun langset.service

%postun
%service_del_postun langset.service

%files
%doc gpl-2.0.txt
%{_datadir}/langset
%{_sbindir}/langset.sh
%{_unitdir}/langset.service

%changelog
