#
# spec file for package perl-GooCanvas2
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

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#


Name:           perl-GooCanvas2
Version:        0.06
Release:        0
%define cpan_name GooCanvas2
Summary:        Perl binding for GooCanvas2 widget using Glib::Object::Introspection
License:        GPL-1.0+ or Artistic-1.0
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/GooCanvas2/
Source0:        https://cpan.metacpan.org/authors/id/P/PE/PERLMAX/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Gtk3)
BuildRequires:  typelib(GooCanvas) = 2.0
Requires:       perl(Gtk3)
%{perl_requires}

%description
GooCanvas2 is a new canvas widget for use with Gtk3 that uses the Cairo 2d
library for drawing. This is a simple and basic implementation of this
wonderful Canvas widget.

For more informations see
https://wiki.gnome.org/action/show/Projects/GooCanvas

For instructions, how to use GooCanvas2, please study the API reference at
https://developer.gnome.org/goocanvas/unstable/ for now. A perl-specific
documentation will perhaps come in later versions. But applying the C
documentation should be no problem.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README

%changelog
