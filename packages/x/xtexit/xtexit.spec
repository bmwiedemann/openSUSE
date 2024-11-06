#
# spec file for package xtexit
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


Name:           xtexit
BuildRequires:  imake
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xaw7)
BuildRequires:  pkgconfig(xt)
Requires:       xaw3d
Version:        0.42
Release:        0
Summary:        Prompt on exiting X
License:        MIT
Group:          System/X11/Utilities
Source:         xtexit.tar.gz
Patch0:         xtexit.dif
Patch1:         xtexit-Imakefile_comments.dif
Patch2:         xtexit-gcc14.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
%{expand: %%global _exec_prefix %(type -p pkg-config &>/dev/null && pkg-config --variable prefix x11 || echo /usr/X11R6)}
%if "%_exec_prefix" == "/usr/X11R6"
%define _x11data    %{_exec_prefix}/lib/X11
%define _appdefdir  %{_x11data}/app-defaults
%else
%define _x11data    %{_datadir}/X11
%define _appdefdir  %{_x11data}/app-defaults
%endif

%description
`xtexit` sends an request to all clients to shut down. If the
application still needs an user interaction (e.g., if a file should be
saved) this is possible.

If you answer by the affirmative, all applications will be closed. This
method is not fully waterproof, but better than killing each and every
client without being able to interfere.

xterm applications anyway are killed immediately!

If this package is installed, it will be automatically integrated into
the sample user fvwm menu.

%prep
%autosetup -p0 -n xtexit

%build
xmkmf -a
make

%install
make DESTDIR=%{buildroot} install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README README.SUSE
%{_bindir}/xtexit
%dir %{_appdefdir}
%config %{_appdefdir}/XTexit

%changelog
