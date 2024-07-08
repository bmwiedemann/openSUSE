#
# spec file for package xclip
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


%define rversion 0.13
%define gitdate 20220129
%define githash b372f73579d30f9ba998ffd0a73694e7abe2c313

Name:           xclip
Version:        %{rversion}+git%{gitdate}
Release:        0
Summary:        Command Line Interface to the X11 Clipboard
License:        GPL-2.0-or-later
Group:          System/X11/Utilities
URL:            https://github.com/astrand/xclip
Source:         https://github.com/astrand/xclip/archive/%{githash}.tar.gz#/%{name}-%{githash}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xmu)

%description
xclip is a command line interface to the X11 clipboard. It can also be used
for copying files, as an alternative to sftp/scp, thus avoiding password
prompts when X11 forwarding has already been setup.

%prep
%autosetup -n %{name}-%{githash}

%build
bash ./bootstrap
%configure \
	 --x-includes="%{_usr}/include" \
	 --x-libraries="%{_usr}/%{_lib}" \
	 --with-x
%make_build

%install
%make_install

%check

%files
%license COPYING
%doc ChangeLog README
%{_bindir}/xclip
%{_bindir}/xclip-copyfile
%{_bindir}/xclip-cutfile
%{_bindir}/xclip-pastefile
%{_mandir}/man1/xclip.1%{?ext_man}*
%{_mandir}/man1/xclip-copyfile.1%{?ext_man}*

%changelog
