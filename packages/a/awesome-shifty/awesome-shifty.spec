#
# spec file for package awesome-shifty
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


%define gitversion git20140405

Name:           awesome-shifty
Version:        %{gitversion}
Release:        0
Summary:        Dynamic tagging library for awesome
License:        GPL-2.0+
Group:          System/GUI/Other
Url:            https://github.com/cdump/awesome-shifty
Source0:        %name-%{version}.tar.xz
Requires:       awesome >= 3.4.11
BuildArch:      noarch

%description
Shifty is an Awesome 3 extension that implements dynamic tagging. It also
implements fine client matching configuration allowing YOU to be the master
of YOUR desktop only by setting two simple config variables and some
keybindings! Here are a few ways of how shifty makes awesome awesomer:

- on-the-fly tag creation and disposal
- advanced client matching
- easy moving of clients between tags
- tag add/rename prompt in taglist (with completion, now configurable NEW )
- reordering tags and configurable positioning
- tag name guessing, automagic no-config client grouping
- customizable keybindings per client and tag -- NEW
- simple yet powerful configuration

%prep
%setup -q -n %name

%build
%install

install -d %{buildroot}%{_datadir}/awesome/lib/shifty
install -D -m644 init.lua %{buildroot}%{_datadir}/awesome/lib/shifty

%files
%defattr(-,root,root,-)
%doc example.rc.lua README.md
%{_datadir}/awesome/lib/shifty/init.lua
%dir %{_datadir}/awesome
%dir %{_datadir}/awesome/lib
%dir %{_datadir}/awesome/lib/shifty

%changelog
