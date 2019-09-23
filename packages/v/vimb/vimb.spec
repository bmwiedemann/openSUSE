#
# spec file for package vimb
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           vimb
Version:        3.5.0
Release:        0
Summary:        The vim-like browser
License:        GPL-3.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            https://fanglingsu.github.io/vimb/
Source:         https://github.com/fanglingsu/vimb/archive/%{version}.tar.gz
BuildRequires:  gtk3-devel
BuildRequires:  webkit2gtk3-devel >= 2.20

%description
vimb is a WebKit-based web browser that behaves like the vimperator
plugin for Firefox, and has usage paradigms from the editor vim.

%prep
%setup -q

%build
make %{?_smp_mflags} PREFIX=%{_prefix}

%install
%make_install PREFIX=%{_prefix}

%files
%{_bindir}/vimb
%dir %{_prefix}/lib/vimb
%{_prefix}/lib/vimb/webext_main.so
%{_datadir}/applications/vimb.desktop
%{_mandir}/man1/vimb.1%{?ext_man}

%changelog
