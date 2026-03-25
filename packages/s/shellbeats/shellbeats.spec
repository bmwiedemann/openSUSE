#
# spec file for package shellbeats
#
# Copyright (c) 2026 SUSE LLC and contributors
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

%global commit 280e5cabcc2e84a6a5f4b91c70c99f7b094a0c3f
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Name:           shellbeats
Version:        0.6
Release:        0
Summary:        Terminal music player for YouTube
License:        GPL-3.0-only
Group:          Productivity/Multimedia/Other
URL:            https://shellbeats.com
Source0:        https://github.com/lalo-space/shellbeats/archive/%{commit}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  pkgconfig(ncurses)
Requires:       mpv
Requires:       yt-dlp
Recommends:     curl

%description
A terminal music player that integrates with YouTube. It allows users to search, stream, and
download tracks directly from the command line using mpv and yt-dlp as backend tools.The interface supports shuffle mode, seek controls, and background downloads.

%prep
%setup -q -n %{name}-%{commit}
%build
%make_build

%install
# The MAKEFILE uses /usr/local/bin, override to /usr/bin for RPM standards.
install -D -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
%check
test -x %{buildroot}%{_bindir}/shellbeats
%files
%{_bindir}/%{name}
%license LICENSE
%doc README.md YOUTUBE_PLAYLIST_GUIDE.md

%changelog
