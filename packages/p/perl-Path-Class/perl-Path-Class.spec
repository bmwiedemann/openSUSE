#
# spec file for package perl-Path-Class
#
# Copyright (c) 2016 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Path-Class
Version:        0.37
Release:        0
%define cpan_name Path-Class
Summary:        Cross-platform path specification manipulation
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Path-Class/
Source0:        http://www.cpan.org/authors/id/K/KW/KWILLIAMS/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(File::Spec) >= 3.26
BuildRequires:  perl(Module::Build) >= 0.360100
BuildRequires:  perl(Perl::OSType)
BuildRequires:  perl(parent)
Requires:       perl(File::Spec) >= 3.26
Requires:       perl(Perl::OSType)
Requires:       perl(parent)
%{perl_requires}

%description
'Path::Class' is a module for manipulation of file and directory
specifications (strings describing their locations, like
''/home/ken/foo.txt'' or ''C:\Windows\Foo.txt'') in a cross-platform
manner. It supports pretty much every platform Perl runs on, including
Unix, Windows, Mac, VMS, Epoc, Cygwin, OS/2, and NetWare.

The well-known module File::Spec also provides this service, but it's sort
of awkward to use well, so people sometimes avoid it, or use it in a way
that won't actually work properly on platforms significantly different than
the ones they've tested their code on.

In fact, 'Path::Class' uses 'File::Spec' internally, wrapping all the
unsightly details so you can concentrate on your application code. Whereas
'File::Spec' provides functions for some common path manipulations,
'Path::Class' provides an object-oriented model of the world of path
specifications and their underlying semantics. 'File::Spec' doesn't create
any objects, and its classes represent the different ways in which paths
must be manipulated on various platforms (not a very intuitive concept).
'Path::Class' creates objects representing files and directories, and
provides methods that relate them to each other. For instance, the
following 'File::Spec' code:

 my $absolute = File::Spec->file_name_is_absolute(
                  File::Spec->catfile( @dirs, $file )
                );

can be written using 'Path::Class' as

 my $absolute = Path::Class::File->new( @dirs, $file )->is_absolute;

or even as

 my $absolute = file( @dirs, $file )->is_absolute;

Similar readability improvements should happen all over the place when
using 'Path::Class'.

Using 'Path::Class' can help solve real problems in your code too - for
instance, how many people actually take the "volume" (like 'C:' on Windows)
into account when writing 'File::Spec'-using code? I thought not. But if
you use 'Path::Class', your file and directory objects will know what
volumes they refer to and do the right thing.

The guts of the 'Path::Class' code live in the Path::Class::File and
Path::Class::Dir modules, so please see those modules' documentation for
more details about how to use them.

%prep
%setup -q -n %{cpan_name}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes LICENSE README

%changelog
