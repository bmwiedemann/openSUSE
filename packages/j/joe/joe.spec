#
# spec file for package joe
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           joe
Version:        4.6
Release:        0
Summary:        A Text Editor
License:        GPL-2.0-or-later
Group:          Productivity/Text/Editors
URL:            http://sourceforge.net/projects/joe-editor
Source:         http://downloads.sf.net/joe-editor/%{name}-%{version}.tar.gz
Source2:        de.po
Source3:        joe-rpmlintrc
Patch2:         joe-3.1-fix_isblanck_argument.patch
Patch3:         joe-3.3-warnings.patch
Patch7:         joe-3.7-additional_key_mappings.patch
Patch8:         joe-3.7-spec_association.patch
Patch10:        joe-sigiot.patch
Patch12:        joe-4.6-nonvoid-functions.patch
BuildRequires:  automake
BuildRequires:  libselinux-devel
BuildRequires:  ncurses-devel

%description
Joe is a powerful, easy to use, modeless text editor. It uses the same
WordStar keybindings used in Borland's development environment.

%prep
%setup -q
%patch2
%patch3
%patch7
%patch8
%patch10
%patch12 -p1

%build
autoreconf -fiv
export CFLAGS="%{optflags} -W -Wno-unused"
%configure \
  --docdir=%{_defaultdocdir}/%{name}
make %{?_smp_mflags}

%install
%make_install
for i in jmacs jpico jstar rjoe; do
  ln -s joe.1.gz %{buildroot}%{_mandir}/man1/$i.1.gz
done
rm -rf %{buildroot}/%{_datadir}/%{name}/lang

# Remove desktop entries to follow openSUSE guidelines for console applications
# See: https://lists.opensuse.org/opensuse-factory/2019-02/msg00377.html
rm -rf %{buildroot}%{_datadir}/applications/*.desktop

%files
%doc %{_defaultdocdir}/%{name}
%{_mandir}/man1/*
%{_mandir}/*/man1/*
%config %{_sysconfdir}/joe/*
%dir %{_sysconfdir}/joe
%dir %{_datadir}/%{name}
%dir %{_mandir}/ru
%dir %{_mandir}/ru/man1
%{_bindir}/*
%{_datadir}/%{name}/charmaps
%dir %{_datadir}/%{name}/syntax
%config(noreplace) %{_datadir}/%{name}/syntax/*
%{_datadir}/joe/colors
%{_datadir}/joe/colors/*.jcf

%changelog
