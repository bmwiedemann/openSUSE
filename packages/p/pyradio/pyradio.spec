#
# spec file for package pyradio
#
# Copyright (c) 2020 SUSE LLC
# Copyright (c) 2019-2020 Malcolm J Lewis <malcolmlewis@opensuse.org>
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


Name:           pyradio
Version:        0.8.7
Release:        0
Summary:        Curses based internet radio player
License:        MIT
URL:            https://www.coderholic.com/pyradio
Source0:        https://github.com/coderholic/pyradio/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  fdupes
BuildRequires:  python-rpm-macros
BuildRequires:  python3-setuptools
## MANUAL BEGIN
Recommends:     vlc-noX
## MANUAL END
BuildArch:      noarch

%description
A command line Internet radio player based on curses, that uses external media
players to perform the actual playback. It currently supports the following
players: MPV, MPlayer and VLC.

%prep
%autosetup
mv LICENCE LICENSE

%build
export LC_ALL=en_US.utf8
%python3_build


%install
%python3_install
install -Dm0644 pyradio.1 %{buildroot}%{_mandir}/man1/pyradio.1
%python_expand %fdupes %{buildroot}%{python3_sitelib}/

%files
%doc Changelog README.md
%license LICENSE
%{_bindir}/pyradio
%{_mandir}/man1/pyradio.1%{?ext_man}
%{python3_sitelib}/*

%changelog
