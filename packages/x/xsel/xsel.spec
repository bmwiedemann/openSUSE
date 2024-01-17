#
# spec file for package xsel
#
# Copyright (c) 2023 SUSE LLC
# Copyright (c) 2010 Guido Berhoerster.
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


Name:           xsel
Version:        1.2.0
Release:        0
Summary:        Command-line Program for Getting and Setting the Contents of the X Selection
License:        MIT
Group:          System/X11/Utilities
Source:         http://www.kfish.org/software/xsel/download/xsel-%{version}.tar.gz
Patch0:         disable-werror.patch
URL:            http://www.kfish.org/software/xsel/
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xt)

%description
XSel is a command-line program for getting and setting the contents of the X
selection. Normally this is only accessible by manually highlighting
information and pasting it with the middle mouse button.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%doc AUTHORS ChangeLog README
%doc %{_mandir}/man1/xsel.1x*
%{_bindir}/xsel

%changelog
