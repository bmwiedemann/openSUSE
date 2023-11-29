#
# spec file for package polybar
#
# Copyright (c) 2023 SUSE LLC
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


Name:           polybar
Version:        3.7.1
Release:        0
Summary:        A fast and easy-to-use status bar
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/polybar/polybar
Source:         https://github.com/polybar/polybar/releases/download/%{version}/%{name}-%{version}.tar.gz
Patch0:         cmake.patch
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.5
BuildRequires:  i3
BuildRequires:  i3-devel
BuildRequires:  libmpdclient-devel
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  python3-xml
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libnl-3.0)
BuildRequires:  pkgconfig(libnl-cli-3.0)
BuildRequires:  pkgconfig(libnl-genl-3.0)
BuildRequires:  pkgconfig(libnl-idiag-3.0)
BuildRequires:  pkgconfig(libnl-nf-3.0)
BuildRequires:  pkgconfig(libnl-route-3.0)
BuildRequires:  pkgconfig(libnl-xfrm-3.0)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(libuv) >= 1.3
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-cursor)
BuildRequires:  pkgconfig(xcb-ewmh)
BuildRequires:  pkgconfig(xcb-icccm)
BuildRequires:  pkgconfig(xcb-image)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcb-util)
BuildRequires:  pkgconfig(xcb-xrm)
DocDir:         %{_datadir}/doc

%description
A fast and easy-to-use status bar for tilling WM

%prep
%setup -q

%if 0%{?sle_version} == 150400 && 0%{?is_opensuse} || 0%{?sle_version} == 150500 && 0%{?is_opensuse}
    %autopatch -p1
%endif

%build
%cmake

%install
%cmake_install
rm -rf %{buildroot}/%{_docdir}/%{name}/.buildinfo

%files
%dir %{_datadir}/bash-completion/
%dir %{_datadir}/bash-completion/completions
%dir %{_datadir}/doc/%{name}
%dir %{_datadir}/zsh/
%dir %{_datadir}/zsh/site-functions
%dir %{_sysconfdir}/polybar
%{_bindir}/%{name}
%{_bindir}/%{name}-msg
%{_mandir}/man1/%{name}.1%?ext_man
%{_mandir}/man5/%{name}.5%?ext_man
%{_docdir}/%{name}/*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/zsh/site-functions/_%{name}_msg
%{_sysconfdir}/polybar/config.ini
%{_mandir}/man1/polybar-msg.1%{?ext_man}

%changelog
