#
# spec file for package urxvt-perls
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


Name:           urxvt-perls
Version:        2.2
Release:        0
Summary:        Perl extensions for the rxvt-unicode terminal emulator
License:        GPL-2.0
Group:          System/X11/Utilities
Url:            https://github.com/muennich/urxvt-perls
Source:         https://github.com/muennich/%{name}/archive/%{version}.tar.gz
Requires:       xsel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
A small collection of perl extensions for the urxvt-unicode terminal emulator.
keyboard-select: Use keyboard shortcuts to select and copy text.
url-select: Use keyboard shortcuts to select URLs.
clipboard: Use keyboard shortcuts to copy the selection to the clipboard and
to paste the clipboard contents (optionally escaping all special characters).

%prep
%setup -q

%build

%install
install -D -m 644 clipboard %{buildroot}%{_libdir}/urxvt/perl/clipboard
install -D -m 644 keyboard-select %{buildroot}%{_libdir}/urxvt/perl/keyboard-select
install -D -m 644 url-select %{buildroot}%{_libdir}/urxvt/perl/url-select

%files
%defattr(-,root,root)
%doc README.md LICENSE
%dir %{_libdir}/urxvt
%dir %{_libdir}/urxvt/perl
%{_libdir}/urxvt/perl/clipboard
%{_libdir}/urxvt/perl/keyboard-select
%{_libdir}/urxvt/perl/url-select

%changelog
