#
# spec file for package alsaequal
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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
Version:        0.6
Release:        0
Summary:        Equalizer plugin for ALSA
License:        LGPL-2.1-only
URL:            https://github.com/bassdr/alsaequal
Source0:        %{name}-%{version}.tar.xz
Source1:        99-equal.conf
Patch0:         lib64.patch
BuildRequires:  alsa-devel
BuildRequires:  gcc
BuildRequires:  ladspa-caps

%description
Alsaequal is a real-time adjustable equalizer plugin for ALSA

%prep
%setup -q -n %{name}
%if %{?_lib} == lib64
%patch0 -p1
%endif

%build
%make_build

%install
install -d %{buildroot}%{_sysconfdir}/alsa/conf.d
install -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/alsa/conf.d
mkdir -p %{buildroot}%{_libdir}/alsa-lib
%make_install

%files
%license COPYING
%doc README
%dir %{_sysconfdir}/alsa
%dir %{_sysconfdir}/alsa/conf.d
%config(noreplace) %{_sysconfdir}/alsa/conf.d/*.conf
%dir %{_libdir}/alsa-lib
%{_libdir}/alsa-lib/*.so

%changelog
