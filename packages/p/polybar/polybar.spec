#
# spec file for package polybar
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


Name:           polybar
Version:        3.4.3
Release:        0
Summary:        A fast and easy-to-use status bar
License:        MIT
Group:          System/GUI/Other
URL:            https://github.com/polybar/polybar
Source:         https://github.com/polybar/polybar/releases/download/%{version}/%{name}-%{version}.tar
BuildRequires:  c++_compiler
BuildRequires:  cmake >= 3.1
BuildRequires:  pkgconfig
BuildRequires:  python3-Sphinx
BuildRequires:  python3-xml
BuildRequires:  xcb-util-image-devel
BuildRequires:  xcb-util-wm-devel
BuildRequires:  xcb-util-xrm-devel
# optional dependency
BuildRequires:  pkgconfig(alsa)
# main dependency
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(jsoncpp)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xcb-proto)
BuildRequires:  pkgconfig(xcb-util)
DocDir:         %{_datadir}/doc
%if 0%{?suse_version} <= 1315
BuildRequires:  i3-devel
%else
BuildRequires:  i3-gaps-devel
%endif
%if 0%{?suse_version}
BuildRequires:  libiw-devel
%else
BuildRequires:  wireless-tools-devel
%endif

%description
A fast and easy-to-use status bar for tilling WM

%prep
%setup -n %{name}

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
%{_bindir}/%{name}
%{_bindir}/%{name}-msg
%{_mandir}/man1/%{name}.1%?ext_man
%{_docdir}/%{name}/*
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/zsh/site-functions/_%{name}
%{_datadir}/zsh/site-functions/_%{name}_msg

%changelog
