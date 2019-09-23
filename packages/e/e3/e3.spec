#
# spec file for package e3
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


Name:           e3
Version:        2.82
Release:        0
Summary:        Tiny Editor with Many Different Modes like Vi, Emacs, and Wordstar
License:        GPL-2.0+
Group:          Productivity/Text/Editors
Url:            https://sites.google.com/site/e3editor/
Source:         https://sites.google.com/site/e3editor/Home/e3-%{version}.tgz
BuildRequires:  nasm

%description
A very tiny editor, which offers many different modes like Vi, Emacs, and
Wordstar. Wordstar is the default mode.

%prep
%setup -q

%build
make -e EXMODE=SED %{?_smp_mflags}

%install
make -e PREFIX=%{buildroot}/%{_prefix} MANDIR=%{buildroot}%{_mandir}/man'$(MANSEC)' install
cd %{buildroot}%{_prefix}/bin
for e in e3*; do if test $e != e3; then ln -sf e3 $e; fi; done

%files
%defattr(-,root,root)
%doc COPYING.GPL COPYRIGHT ChangeLog README
%{_bindir}/e3
%{_bindir}/e3em
%{_bindir}/e3ne
%{_bindir}/e3pi
%{_bindir}/e3vi
%{_bindir}/e3ws
%{_mandir}/man1/e3.1%{ext_man}

%changelog
