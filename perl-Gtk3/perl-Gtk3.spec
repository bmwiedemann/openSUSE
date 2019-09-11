#
# spec file for package perl-Gtk3
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


Name:           perl-Gtk3
Version:        0.035
Release:        0
%define cpan_name Gtk3
Summary:        Perl interface to the 3.x series of the gtk+ toolkit
License:        LGPL-2.1-or-later
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Gtk3/
Source0:        https://cpan.metacpan.org/authors/id/X/XA/XAOC/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Cairo::GObject) >= 1.000
BuildRequires:  perl(Glib::Object::Introspection) >= 0.043
BuildRequires:  perl(Test::Simple) >= 0.96
BuildRequires:  typelib(Gtk) = 3.0
Requires:       perl(Cairo::GObject) >= 1.000
Requires:       perl(Glib::Object::Introspection) >= 0.043
Requires:       perl(Test::Simple) >= 0.96
%{perl_requires}

%description
The 'Gtk3' module allows a Perl developer to use the gtk+ graphical user
interface library. Find out more about gtk+ at http://www.gtk.org.

The gtk+ reference manual is also a handy companion when writing 'Gtk3'
programs in Perl: http://developer.gnome.org/gtk3/stable/. The Perl
bindings follow the C API very closely, and the C reference documentation
should be considered the canonical source. The principles underlying the
mapping from C to Perl are explained in the documentation of
Glib::Object::Introspection, on which 'Gtk3' is based.

Glib::Object::Introspection also comes with the 'perli11ndoc' program which
displays the API reference documentation of all installed libraries
organized in accordance with these principles.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc NEWS perl-gtk3.doap README
%license LICENSE

%changelog
