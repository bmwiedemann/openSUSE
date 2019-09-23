#
# spec file for package urxvt-font-size
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           urxvt-font-size
Version:        1.1
Release:        0
Summary:        Extension for rxvt-unicode that allows changing the font size on the fly
License:        MIT
Group:          System/X11/Utilities
Url:            http://github.com/majutsushi/urxvt-font-size
Source:         http://github.com/majutsushi/%{name}/archive/v%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A perl extension for rxvt-unicode that allows changing the font size on the fly
with keyboard shortcuts. It has the following features:
 - Supports both xft and X11 fonts; X11 fonts work in both full form and as
   aliases.
 - Supports all four font settings: font, boldFont, italicFont and
   boldItalicFont and changes them in accordance with the base font (the first
   one from font).
 - Can apply the font change globally for the whole server, so that new
   terminals will inherit the same size, and even save it to ~/.Xresources to
   be able to survive a reboot.
 - Should work even with complicated font setups like the example in the urxvt
   man-page.

%prep
%setup -q

%build

%install
install -D -m 644 font-size %{buildroot}%{_libdir}/urxvt/perl/font-size

%files
%defattr(-,root,root)
%doc README.markdown LICENSE
%dir %{_libdir}/urxvt
%dir %{_libdir}/urxvt/perl
%{_libdir}/urxvt/perl/font-size

%changelog
