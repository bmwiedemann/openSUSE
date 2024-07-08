#
# spec file for package vimb
#
# Copyright (c) 2024 SUSE LLC
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


Name:           vimb
Version:        3.7.0
Release:        0
Summary:        The vim-like browser
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            https://fanglingsu.github.io/vimb/
Source:         https://github.com/fanglingsu/vimb/archive/%{version}.tar.gz
BuildRequires:  desktop-file-utils
BuildRequires:  appstream-glib
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(webkit2gtk-4.1)

%description
vimb is a WebKit-based web browser that behaves like the vimperator
plugin for Firefox, and has usage paradigms from the editor vim.

%prep
%autosetup -p1

%build
%make_build PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}

%check
make test
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_datadir}/metainfo/vimb.metainfo.xml
 
%files
%{_bindir}/vimb
%dir %{_prefix}/lib/vimb
%{_prefix}/lib/vimb/webext_main.so
%{_datadir}/applications/vimb.desktop
%{_datadir}/metainfo/vimb.metainfo.xml
%{_mandir}/man1/vimb.1%{?ext_man}

%changelog
