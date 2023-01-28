#
# spec file for package tmux
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


Name:           tmux
Version:        3.3a
Release:        0
Summary:        Terminal multiplexer
License:        ISC AND BSD-3-Clause AND BSD-2-Clause
Group:          System/Console
URL:            https://tmux.github.io/
Source0:        https://github.com/tmux/tmux/releases/download/%{version}/%{name}-%{version}.tar.gz
Source1:        bash_completion_tmux.sh
# PATCH-FIX-OPENSUSE crrodriguez@opensuse.org -- Use /run/tmux instead of /tmp as the default socket path, this add some robustness against accidental deletion via systemd-tmpfiles-clean, tmpwatch, or similar
Patch0:         tmux-socket-path.patch
# CVE-2022-47016 [bsc#1207393], Null pointer dereference in window.c
Patch1:         tmux-CVE-2022-47016.patch
BuildRequires:  pkgconfig
BuildRequires:  utempter-devel
BuildRequires:  pkgconfig(libutf8proc)
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(libevent) >= 2.0
%{?systemd_ordering}
%if 0%{?suse_version} >= 1320
BuildRequires:  pkgconfig(ncurses)
%else
BuildRequires:  ncurses-devel
%endif

%description
tmux is a terminal multiplexer: it enables a number of terminals (or windows),
each running a separate program, to be created, accessed, and controlled from a
single screen. tmux may be detached from a screen and continue running in the
background, then later reattached. tmux is intended to be a modern,
BSD-licensed alternative to programs such as GNU screen.

tmux uses a client-server model. The server holds multiple sessions and each
window is a independent entity which may be freely linked to multiple sessions,
moved between sessions and otherwise manipulated. Each session may be attached
to (display and accept keyboard input from) multiple clients.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure --enable-utf8proc --with-TERM=screen-256color --enable-systemd
%if 0%{?suse_version} >= 1320
%make_build
%else
make %{?_smp_mflags}
%endif

%install
%make_install

# bash completion
install -d -m 0755 %{buildroot}%{_datadir}/bash-completion/completions/
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/bash-completion/completions/tmux

install -d -m 0755 %{buildroot}%{_tmpfilesdir}
echo "d /run/tmux 1777 root root -" > %{buildroot}%{_tmpfilesdir}/tmux.conf

%post
%tmpfiles_create %{_tmpfilesdir}/%{name}.conf

%files
%license COPYING
%doc CHANGES
%if 0%{?suse_version} < 1320
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%endif
%{_datadir}/bash-completion/completions/tmux
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1%{?ext_man}
%{_tmpfilesdir}/%{name}.conf
%ghost /run/tmux

%changelog
