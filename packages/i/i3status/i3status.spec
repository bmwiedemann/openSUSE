#
# spec file for package i3status
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2014 Thomas Pfeiffer <email@pfeiffer.pw>
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


Name:           i3status
Version:        2.12
Release:        0
Summary:        I3 Status Bar
License:        BSD-3-Clause
Group:          System/Monitoring
URL:            https://i3wm.org/i3status/
Source0:        https://i3wm.org/i3status/%{name}-%{version}.tar.bz2
BuildRequires:  alsa-devel
BuildRequires:  asciidoc
BuildRequires:  libasound2
BuildRequires:  libcap2
BuildRequires:  libconfuse-devel
BuildRequires:  libiw-devel
BuildRequires:  libnl3-devel
BuildRequires:  libpulse-devel
BuildRequires:  libxslt-devel
BuildRequires:  libyajl-devel

%description
i3status is a program for generating a status bar for i3bar, dzen2,
xmobar or similar programs. It issues a small number of system
calls, as one generally wants to update such status lines every
second so that the bar is updated even under load. It saves a bit of
energy by being more efficient than shell commands.

%prep
%setup -q
rm -fr yajl-fallback
chmod -x contrib/*.*

%build
make %{?_smp_mflags} \
    OPTFLAGS="%{optflags}"

%install
%make_install

%files
%license LICENSE
%doc CHANGELOG contrib/
%config(noreplace) %{_sysconfdir}/%{name}.conf
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}

%changelog
