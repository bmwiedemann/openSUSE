#
# spec file for package perl-Data-Hierarchy
#
# Copyright (c) 2011 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Data-Hierarchy
Version:        0.34
Release:        0
%define cpan_name Data-Hierarchy
Summary:        Handle data in a hierarchical structure
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Data-Hierarchy/
Source:         http://www.cpan.org/authors/id/C/CL/CLKAO/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl(Test::Exception)
BuildRequires:  perl-macros
Requires:       perl(Test::Exception)
%{perl_requires}

%description
the Data::Hierarchy manpage provides a simple interface for manipulating
inheritable data attached to a hierarchical environment (like a
filesystem).

One use of the Data::Hierarchy manpage is to allow an application to
annotate paths in a real filesystem in a single compact data structure.
However, the hierarchy does not actually need to correspond to an actual
filesystem.

Paths in a hierarchy are referred to in a Unix-like syntax; '"/"' is the
root "directory". (You can specify a different separator character than the
slash when you construct a Data::Hierarchy object.) With the exception of
the root path, paths should never contain trailing slashes. You can
associate properties, which are arbitrary name/value pairs, with any path.
(Properties cannot contain the undefined value.) By default, properties are
inherited by child paths: thus, if you store some data at '/some/path':

    $tree->store('/some/path', {color => 'red'});

you can fetch it again at a '/some/path/below/that':

    print $tree->get('/some/path/below/that')->{'color'};
    # prints red

On the other hand, properties whose names begin with dots are uninherited,
or "sticky":

    $tree->store('/some/path', {'.color' => 'blue'});
    print $tree->get('/some/path')->{'.color'};            # prints blue
    print $tree->get('/some/path/below/that')->{'.color'}; # undefined

Note that you do not need to (and in fact, cannot) explicitly add "files"
or "directories" to the hierarchy; you simply add and delete properties to
paths.

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
%doc CHANGES README

%changelog
