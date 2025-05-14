#
# spec file for package perl-Hook-LexWrap
#
# Copyright (c) 2025 SUSE LLC
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


%define cpan_name Hook-LexWrap
Name:           perl-Hook-LexWrap
Version:        0.260.0
Release:        0
# 0.26 -> normalize -> 0.260.0
%define cpan_version 0.26
License:        Artistic-1.0 OR GPL-1.0-or-later
Summary:        Lexically scoped subroutine wrappers
URL:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/%{cpan_name}-%{cpan_version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl-macros
Provides:       perl(Hook::LexWrap) = %{version}
%undefine       __perllib_provides
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
%autosetup  -n %{cpan_name}-%{cpan_version} -p1

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%perl_make_install
%perl_process_packlist
%perl_gen_filelist

%files -f %{name}.files
%doc Changes CONTRIBUTING README
%license LICENSE

%changelog
