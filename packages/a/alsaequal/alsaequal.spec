#
# spec file for package alsaequal
#
# Copyright (c) 2020 SUSE LLC
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


Name:           alsaequal
Version:        0.7.1
Release:        0
Summary:        Equalizer plugin for ALSA
License:        LGPL-2.1-only
URL:            https://github.com/bassdr/alsaequal
Source0:        https://github.com/bassdr/alsaequal/archive/v%{version}.tar.gz
Source1:        99-equal.conf
BuildRequires:  alsa-devel
BuildRequires:  gcc
BuildRequires:  ladspa-devel
Requires:       ladspa-caps

%description
Alsaequal is a real-time adjustable equalizer plugin for ALSA

%prep
%setup -q

%build
%make_build LIBDIR=%_lib

%install
install -d %{buildroot}%{_sysconfdir}/alsa/conf.d
install -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/alsa/conf.d
mkdir -p %{buildroot}%{_libdir}/alsa-lib
%make_install LIBDIR=%_lib

%files
%license COPYING
%doc README.md
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/*.conf
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/*.so

%changelog
