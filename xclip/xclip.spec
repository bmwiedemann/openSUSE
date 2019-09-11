#
# spec file for package xclip
#
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           xclip
Version:        0.13
Release:        0
Summary:        Command Line Interface to the X11 Clipboard
License:        GPL-2.0+
Group:          System/X11/Utilities
Url:            https://github.com/astrand/xclip
Source:         https://github.com/astrand/%{name}/archive/%{version}.tar.gz#./%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  xorg-x11-libICE-devel
BuildRequires:  xorg-x11-libX11-devel
BuildRequires:  xorg-x11-libXext-devel
BuildRequires:  xorg-x11-libXmu-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
xclip is a command line interface to the X11 clipboard. It can also be used
for copying files, as an alternative to sftp/scp, thus avoiding password
prompts when X11 forwarding has already been setup.

%prep
%setup -q

%build
bash ./bootstrap
%configure \
	 --x-includes="%{_usr}/include" \
	 --x-libraries="%{_usr}/%{_lib}" \
	 --with-x
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{_bindir}/xclip
%{_bindir}/xclip-copyfile
%{_bindir}/xclip-cutfile
%{_bindir}/xclip-pastefile
%{_mandir}/man1/xclip.1*
%{_mandir}/man1/xclip-copyfile.1%{ext_man}

%changelog
