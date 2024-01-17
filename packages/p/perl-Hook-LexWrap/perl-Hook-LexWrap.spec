#
# spec file for package perl-Hook-LexWrap
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


Name:           perl-Hook-LexWrap
Version:        0.26
Release:        0
%define cpan_name Hook-LexWrap
Summary:        Lexically scoped subroutine wrappers
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Hook-LexWrap/
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
%{perl_requires}

%description
Hook::LexWrap allows you to install a pre- or post-wrapper (or both) around
an existing subroutine. Unlike other modules that provide this capacity
(e.g. Hook::PreAndPost and Hook::WrapSub), Hook::LexWrap implements
wrappers in such a way that the standard 'caller' function works correctly
within the wrapped subroutine.

To install a prewrappers, you write:

        use Hook::LexWrap;

        wrap 'subroutine_name', pre => \&some_other_sub;

   #or: wrap *subroutine_name,  pre => \&some_other_sub;

The first argument to 'wrap' is a string containing the name of the
subroutine to be wrapped (or the typeglob containing it, or a reference to
it). The subroutine name may be qualified, and the subroutine must already
be defined. The second argument indicates the type of wrapper being applied
and must be either ''pre'' or ''post''. The third argument must be a
reference to a subroutine that implements the wrapper.

To install a post-wrapper, you write:

        wrap 'subroutine_name', post => \&yet_another_sub;

   #or: wrap *subroutine_name,  post => \&yet_another_sub;

To install both at once:

        wrap 'subroutine_name',
             pre  => \&some_other_sub,
             post => \&yet_another_sub;

or:

        wrap *subroutine_name,
             post => \&yet_another_sub,  # order in which wrappers are
             pre  => \&some_other_sub;   # specified doesn't matter

Once they are installed, the pre- and post-wrappers will be called before
and after the subroutine itself, and will be passed the same argument list.

The pre- and post-wrappers and the original subroutine also all see the
same (correct!) values from 'caller' and 'wantarray'.

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
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
