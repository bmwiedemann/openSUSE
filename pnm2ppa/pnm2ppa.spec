#
# spec file for package pnm2ppa
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2012 Bernhard M. Wiedemann
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


Name:           pnm2ppa
Version:        1.13
Release:        0
Summary:        HP PPA GhostScript filter
License:        GPL-2.0+
Group:          System/Filesystems
Url:            http://sourceforge.net/projects/pnm2ppa/
Source0:        http://sourceforge.net/projects/pnm2ppa/files/pnm2ppa/%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.changes
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
pnm2ppa is a Ghostscript print filter which allows owners of HP DeskJet 710C, 712C, 720C, 722C, 820Cse, 820Cxi, 1000Cse, or 1000Cxi printers to print PostScript Level 2.

%prep
%setup -q
chmod a-x docs/en/LICENSE
sed -i -e 's/\r//' docs/en/LICENSE
# remove date and time
modified="$(sed -n '/^----/n;s/ - .*$//;p;q' "%{SOURCE1}")"
DATE="\"$(date -d "${modified}" "+%%b %%e %%Y")\""
TIME="\"$(date -d "${modified}" "+%%R")\""
find .  -name '*.[ch]' |\
    xargs sed -i "s/__DATE__/${DATE}/g;s/__TIME__/${TIME}/g"

%build
%configure
make %{?_smp_mflags}

%install
rm -f docs/en/INSTALL*
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-,root,root)
%{_bindir}/*ppa
%doc docs/en
%config(noreplace) %{_sysconfdir}/pnm2ppa.conf
%doc %{_mandir}/man1/pnm2ppa.1.gz

%changelog
