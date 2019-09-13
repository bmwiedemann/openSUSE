#
# spec file for package ocaml-calendar
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


# Ignore all generated modules *except* CalendarLib, since everything
# now appears in that namespace.
%global __ocaml_requires_opts -i Calendar_builder -i Calendar_sig -i Date -i Date_sig -i Fcalendar -i Ftime -i Period -i Printer -i Time -i Time_sig -i Time_Zone -i Utils -i Version
%global __ocaml_provides_opts -i Calendar_builder -i Calendar_sig -i Date -i Date_sig -i Fcalendar -i Ftime -i Period -i Printer -i Time -i Time_sig -i Time_Zone -i Utils -i Version

Name:           ocaml-calendar
Version:        2.04
Release:        0
%{?ocaml_preserve_bytecode}
Summary:        Objective Caml library for managing dates and times
License:        LGPL-2.0
Group:          Development/Languages/OCaml
Url:            http://calendar.forge.ocamlcore.org/
Source0:        http://forge.ocamlcore.org/frs/download.php/1481/calendar-2.04.tar.gz
Patch1:         calendar-2.04-enable-debug.patch
Patch2:         ocaml-calendar-buildcompare.patch
BuildRequires:  gawk
BuildRequires:  ocaml >= 4.00.1
BuildRequires:  ocaml-findlib-devel >= 1.3.3-3
BuildRequires:  ocaml-ocamldoc
BuildRequires:  ocaml-rpm-macros >= 4.02.1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
Objective Caml library for managing dates and times.

%package        devel
Summary:        Development files for %{name}
Group:          Development/Languages/OCaml
Requires:       %{name} = %{version}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.

%prep
%setup -q -n calendar-%{version}
%patch1 -p1
%patch2 -p1

%build
./configure --libdir=%{_libdir}
make %{?_smp_mflags}
make %{?_smp_mflags} doc

mv TODO TODO.old
iconv -f iso-8859-1 -t utf-8 < TODO.old > TODO

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}%{_libdir}/ocaml
mkdir -p $OCAMLFIND_DESTDIR
make DESTDIR=%{buildroot} install %{?_smp_mflags}

%files
%defattr(-,root,root,-)
%doc CHANGES README TODO LGPL COPYING
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.cmxs
%endif

%files devel
%defattr(-,root,root,-)
%doc CHANGES README TODO LGPL COPYING doc/*
%dir %{_libdir}/ocaml
%dir %{_libdir}/ocaml/*
%if 0%{?ocaml_native_compiler}
%{_libdir}/ocaml/*/*.a
%{_libdir}/ocaml/*/*.cmx
%{_libdir}/ocaml/*/*.cmxa
%{_libdir}/ocaml/*/*.o
%endif
%{_libdir}/ocaml/*/*.cma
%{_libdir}/ocaml/*/*.cmi
%{_libdir}/ocaml/*/*.cmo
%{_libdir}/ocaml/*/*.mli
%{_libdir}/ocaml/*/META

%changelog
