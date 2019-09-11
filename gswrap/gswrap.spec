#
# spec file for package gswrap
#
# Copyright (c) 2019 SUSE Linux GmbH, Nuernberg, Germany.
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


Name:           gswrap
Version:        0.1
Release:        0
Summary:        The ghostscript container to wrap ghostscript within
License:        LGPL-2.1-or-later
Group:          Productivity/Security
URL:            https://github.com/bitstreamout/ghostscriptwrap
Source0:        gswrap
Requires:       /usr/bin/gs.bin
Requires:       bubblewrap
Requires:       coreutils
Requires:       sed
BuildRequires:  sed
BuildRequires:  update-alternatives
Requires(post): update-alternatives
Requires(preun): update-alternatives
BuildArch:      noarch
%define debug_package %nil

%description
If the option -dSAFER is used with gswrap, this script uses bwrap
from the "bubblewrap" package to embbedd the final ghostscript
command within a minimal container. For this, a new, completely empty
filesystem namespace on a tmpfs is populated with the required
libraries and files to run the ghostscript command.

%prep
%setup -q -c -T

%build
sed -r '/ghostscript=@@GS@@/{s^@@GS@@^/usr/bin/gs.bin^}' < %{S:0} > gs.wrap

%install
install -d %buildroot%{_bindir}
install -d %buildroot%{_sysconfdir}/alternatives
install -m 755 gs.wrap %buildroot%{_bindir}/gs.wrap
ln -sf %{_bindir}/gs.wrap %{buildroot}%{_sysconfdir}/alternatives/gs
ln -sf %{_sysconfdir}/alternatives/gs %{buildroot}%{_bindir}/gs

%post
%{_sbindir}/update-alternatives \
  --install %{_bindir}/gs gs %{_bindir}/gs.wrap 100

%preun
if test $1 -eq 0 ; then
    %{_sbindir}/update-alternatives \
    --remove gs %{_bindir}/gs.wrap
fi

%files
%defattr(-,root,root)
%_bindir/gs.wrap
%_bindir/gs
%ghost %config %{_sysconfdir}/alternatives/gs

%changelog
