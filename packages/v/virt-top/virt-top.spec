#
# spec file for package virt-top
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


Name:           virt-top
Version:        1.0.8
Release:        0
%{ocaml_preserve_bytecode}
Summary:        Utility like top(1) for displaying virtualization stats
License:        GPL-2.0+
Group:          System/Management
Url:            http://people.redhat.com/~rjones/virt-top/
Source0:        https://people.redhat.com/~rjones/virt-top/files/%{name}-%{version}.tar.gz
Patch0:         virt-top.bytecode.patch
## Update configure for aarch64 (bz #926701)
Patch1:         virt-top-aarch64.patch
## Don't warn about immutable strings (OCaml 4.02).
Patch2:         virt-top-no-immutable-warning.patch
BuildRequires:  gawk
# For msgfmt:
BuildRequires:  gettext
# Non-OCaml BRs.
BuildRequires:  libvirt-devel
BuildRequires:  ocaml >= 3.10.2
BuildRequires:  ocaml-calendar-devel
BuildRequires:  ocaml-camlp4
BuildRequires:  ocaml-csv-devel
BuildRequires:  ocaml-rpm-macros >= 4.02.1
# Need the ncurses / ncursesw (--enable-widec) fix.
BuildRequires:  ocaml-curses-devel >= 1.0.3
BuildRequires:  ocaml-extlib-devel
BuildRequires:  ocaml-fileutils-devel
BuildRequires:  ocaml-findlib-devel
# Tortuous list of BRs for gettext.
BuildRequires:  ocaml-gettext-devel >= 0.3.5
BuildRequires:  ocaml-gettext-stub-devel >= 0.3.5
# Need support for virDomainGetCPUStats (fixed in 0.6.1.2).
BuildRequires:  ncurses-devel
BuildRequires:  ocaml-libvirt-devel >= 0.6.1.2-5
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-xml-light-devel
BuildRequires:  perl
BuildRequires:  strace
BuildRequires:  perl(Pod::Perldoc)
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
virt-top is a 'top(1)'-like utility for showing stats of virtualized
domains.  Many keys and command line options are the same as for
ordinary 'top'.

It uses libvirt so it is capable of showing stats across a variety of
different virtualization systems.

%prep
%setup -q
%patch0 -p1

## Update configure for aarch64 (bz #926701)
%patch1 -p1

%patch2 -p1

chmod -x COPYING

%build
%configure
make %{?_smp_mflags} all
%if %{ocaml_native_compiler}
make %{?_smp_mflags} opt
%endif

# Build translations.
make %{?_smp_mflags} -C po

# Force rebuild of man page.
rm -f virt-top/virt-top.1
make %{?_smp_mflags} -C virt-top virt-top.1

%install
make DESTDIR=%{buildroot} install %{?_smp_mflags}

# Install translations.
mkdir -p %{buildroot}%{_datadir}/locale
make -C po install PODIR="%{buildroot}%{_datadir}/locale"
%find_lang %{name}

# Install virt-top manpage by hand for now.
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 virt-top/virt-top.1 %{buildroot}%{_mandir}/man1

%files -f %{name}.lang
%defattr(-,root,root,-)
%doc COPYING README TODO ChangeLog
%{_bindir}/virt-top
%{_mandir}/man1/virt-top.1*
%if 0%{?rhel} >= 6
%{_bindir}/processcsv.py
%{_mandir}/man1/processcsv.py.1*
%endif

%changelog
