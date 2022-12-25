#
# spec file for package wavemon
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


Name:           wavemon
Version:        0.9.4
Release:        0
Summary:        An ncurses monitoring application for wireless network devices
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Diagnostic
URL:            https://github.com/uoaerg/wavemon
Source:         https://github.com/uoaerg/wavemon/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  libpcap-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libnl-3.0) >= 3.2
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(ncursesw)

%description
wavemon is a wireless device monitoring application that allows you to
watch signal and noise levels, packet statistics, device configuration
and network parameters of your wireless network hardware. It has
currently only been tested with the Lucent Orinoco series of cards,
although it *should* work (though with varying features) with all
devices supported by the wireless kernel extensions by Jean Tourrilhes.

%prep
%autosetup -p1

%build
export CFLAGS="%{optflags} `pkg-config --cflags libnl-3.0` -DNCURSES_WIDECHAR -pthread"

%configure \
  --docdir=%{_docdir}/%{name}
%make_build

%install
%make_install
mkdir -p %{buildroot}%{_docdir}
mv %{buildroot}%{_datadir}/%{name} %{buildroot}%{_docdir}/

%files
%license LICENSE
%doc README.md
%{_bindir}/wavemon
%{_mandir}/man1/wavemon.1%{?ext_man}
%{_mandir}/man5/wavemonrc.5%{?ext_man}
%{_docdir}/%{name}

%changelog
