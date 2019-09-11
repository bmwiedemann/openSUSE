#
# spec file for package lpe
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


Name:           lpe
Version:        1.2.8
Release:        0
Summary:        Programming text editor
License:        GPL-2.0
Group:          Productivity/Editors/Other
Url:            https://github.com/AdamMajer/lpe
Source:         https://github.com/AdamMajer/lpe/archive/v%version.tar.gz
Patch:          drop_gettext_version.patch
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  slang-devel
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
LPE is meant as an acronym for "lightweight programmer's editor".
It recognizes a few programming languages for syntax highlighting.
The function keys are reminiscient of pico's choices.

%prep
%setup -q
%patch -p1

%build
%configure
make %{?_smp_mflags}

%install
make DESTDIR="%{buildroot}" \
   docdir="%{_defaultdocdir}/%{name}/" \
   exdir="%{_defaultdocdir}/%{name}/" \
   install
rm %{buildroot}%{_libdir}/lpe/*.la
%find_lang %{name} --with-man

%files -f %{name}.lang
%defattr(-,root,root)
%doc %{_defaultdocdir}/%{name}/
%{_bindir}/lpe
%dir %{_libdir}/lpe/
%{_libdir}/lpe/*mode.so
%dir %{_datadir}/lpe
%{_datadir}/lpe/conv.sl
%{_datadir}/lpe/conv.slc
%{_datadir}/lpe/init.sl
%{_datadir}/lpe/init.slc
%{_mandir}/man1/lpe.1*
%dir %{_mandir}/bg/
%dir %{_mandir}/bg/man1

%changelog
