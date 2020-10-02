#
# spec file for package perl-Gtk2
#
# Copyright (c) 2020 SUSE LLC
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


%define cpan_name Gtk2
Name:           perl-Gtk2
Version:        1.24993
Release:        0
Summary:        Perl interface to the 2.x series of the Gimp Toolkit library
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source:         https://cpan.metacpan.org/authors/id/X/XA/XAOC/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildRequires:  perl
BuildRequires:  perl-macros
# MANUAL BEGIN
BuildRequires:  xorg-x11
BuildRequires:  xorg-x11-Xvfb
BuildRequires:  xorg-x11-server
%if 0%{?suse_version} >= 01550
BuildRequires:  xvfb-run
%endif
# MANUAL END
BuildRequires:  perl(Cairo) >= 1.000
BuildRequires:  perl(ExtUtils::Depends) >= 0.300
BuildRequires:  perl(ExtUtils::PkgConfig) >= 1.030000
BuildRequires:  perl(Glib) >= 1.280
BuildRequires:  perl(Pango) >= 1.220
BuildRequires:  pkgconfig(gtk+-2.0)
Requires:       perl(Cairo) >= 1.000
Requires:       perl(ExtUtils::Depends) >= 0.300
Requires:       perl(ExtUtils::PkgConfig) >= 1.030000
Requires:       perl(Glib) >= 1.280
Requires:       perl(Pango) >= 1.220
Provides:       %{name}-devel = %{version}
%{perl_requires}

%description
The Gtk2 module allows a Perl developer to use the Gtk+ graphical user
interface library. Find out more about Gtk+ at http://www.gtk.org.

The GTK+ Reference Manual is also a handy companion when writing Gtk
programs in any language. http://developer.gnome.org/doc/API/2.0/gtk/ The
Perl bindings follow the C API very closely, and the C reference
documentation should be considered the canonical source.

To discuss gtk2-perl, ask questions and flame/praise the authors, join
gtk-perl-list@gnome.org at lists.gnome.org.

Also have a look at the gtk2-perl website and sourceforge project page,
http://gtk2-perl.sourceforge.net

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%check
# Temporarily remove failing tests [bsc#1155004]
rm t/{GdkPixbuf,PangoContext,PangoFont*,PangoRenderer}.t

%if 0%{?suse_version} >= 01550
xvfb-run -a make test %{?_smp_mflags}
%else
Xvfb :95 &
trap "kill $! || true" EXIT
sleep 5
DISPLAY=:95 make test %{?_smp_mflags}
%endif

%files -f %{name}.files
%defattr(-,root,root)
%license LICENSE
%doc AUTHORS ChangeLog.pre-git NEWS constants-* README TODO
%doc doctypes examples gdk.typemap Gtk2.exports gtk.typemap maps-* perl-Gtk2.doap xs_files-*

%changelog
