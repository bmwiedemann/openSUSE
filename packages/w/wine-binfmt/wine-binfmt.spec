#
# spec file for package wine-binfmt
#
# Copyright (c) 2019 SUSE LINUX Products GmbH, Nuernberg, Germany.
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

Name:           wine-binfmt
Version:        1.2.1
Release:        0
Summary:        The binfmt_misc support for Windows
Group:          System/Emulators/PC
Url:            http://en.wikipedia.org/wiki/Binfmt_misc
License:        GPL-2.0
Source0:        wine-binfmt.conf
Source1:        wine-binfmt.service
Source2:        rpmlintrc
BuildRequires:  pkgconfig(systemd) 
BuildRequires:  systemd-rpm-macros
%{?systemd_requires}
Requires:       wine
BuildArch:      noarch

%description
Run Windows(tm) executables out of the box.

%package standalone
Summary:        Standalone binfmt_misc support for Windows
Group:          System/Emulators/PC
Url:            http://en.wikipedia.org/wiki/Binfmt_misc
License:        GPL-2.0
Requires:       wine-binfmt

%description standalone
Standalone variant for running Windows(tm) executables out of the box.
This package does not depend on systemd and dbus, which may not be
available on obs workers for example.

%prep
%setup -cT

%build

%install
%{__install} -d -m 0755 %{buildroot}%{_prefix}/lib/binfmt.d
%{__install} -m 0644 %{SOURCE0} %{buildroot}%{_prefix}/lib/binfmt.d/wine.conf
%{__install} -D -m 444 %{SOURCE1} %{buildroot}%{_unitdir}/wine-binfmt.service
%{__install} -d -m 0755 %{buildroot}%{_prefix}/sbin/
ln -s service %{buildroot}%{_prefix}/sbin/rcwine-binfmt

%pre
%service_add_pre wine-binfmt.service

%post
%service_add_post wine-binfmt.service

%preun
%service_del_preun wine-binfmt.service

%postun
%service_del_postun wine-binfmt.service

%post standalone
if ! test -f /proc/sys/fs/binfmt_misc/register; then
    # mount binfmt device
    mount binfmt_misc -t binfmt_misc /proc/sys/fs/binfmt_misc
fi
if ! test -f /proc/sys/fs/binfmt_misc/DOSWin; then
    # install binfmt
    cat /usr/lib/binfmt.d/wine.conf >/proc/sys/fs/binfmt_misc/register
fi

%preun standalone
if test -f /proc/sys/fs/binfmt_misc/DOSWin; then
    # uninstall binfmt
    echo -1 >/proc/sys/fs/binfmt_misc/DOSWin
fi
# do not unmount /proc/sys/fs/binfmt_misc
# as it might by used by other packages

%files
%defattr(-,root,root,644)
%{_prefix}/lib/binfmt.d/wine.conf
%{_prefix}/sbin/rcwine-binfmt
%{_unitdir}/wine-binfmt.service

%files standalone
%defattr(-,root,root,644)

%changelog
