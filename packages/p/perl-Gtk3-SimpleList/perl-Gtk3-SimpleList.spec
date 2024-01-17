#
# spec file for package perl-Gtk3-SimpleList
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


Name:           perl-Gtk3-SimpleList
Version:        0.21
Release:        0
#Upstream: SUSE-Public-Domain
%define cpan_name Gtk3-SimpleList
Summary:        Simple interface to Gtk3's complex MVC list widget
License:        LGPL-2.1-only
Group:          Development/Libraries/Perl
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/T/TV/TVIGNAUD/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Gtk3)
Requires:       perl(Gtk3)
%{perl_requires}
# MANUAL BEGIN
BuildRequires:  typelib(Gtk) = 3.0
%if ( 0%{?sle_version} == 150200 && 0%{?is_opensuse} ) || 0%{?suse_version} >= 1550
BuildRequires:  typelib(GdkPixdata) = 2.0
%endif
# MANUAL END

%description
Gtk3 has a powerful, but complex MVC (Model, View, Controller) system used
to implement list and tree widgets. Gtk3::SimpleList automates the complex
setup work and allows you to treat the list model as a more natural list of
lists structure.

After creating a new Gtk3::SimpleList object with the desired columns you
may set the list data with a simple Perl array assignment. Rows may be
added or deleted with all of the normal array operations. You can treat the
'data' member of the list simplelist object as an array reference, and
manipulate the list data with perl's normal array operators.

A mechanism has also been put into place allowing columns to be Perl
scalars. The scalar is converted to text through Perl's normal mechanisms
and then displayed in the list. This same mechanism can be expanded by
defining arbitrary new column types before calling the new function.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license COPYING

%changelog
