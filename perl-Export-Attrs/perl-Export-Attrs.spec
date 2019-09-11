#
# spec file for package perl-Export-Attrs
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


Name:           perl-Export-Attrs
Version:        0.1.0
Release:        0
%define cpan_name Export-Attrs
Summary:        The Perl 6 'is export(...)' trait as a Perl 5 attribute
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Export-Attrs/
Source0:        https://cpan.metacpan.org/authors/id/P/PO/POWERMAN/%{cpan_name}-v%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build::Tiny) >= 0.034
BuildRequires:  perl(PadWalker)
Requires:       perl(PadWalker)
%{perl_requires}

%description
*NOTE:* This module is a fork of Perl6::Export::Attrs created to restore
compatibility with Perl6::Export::Attrs version 0.0.3.

Implements a Perl 5 native version of what the Perl 6 symbol export
mechanism will look like (with some unavoidable restrictions).

It's very straightforward:

  * If you want a subroutine or package variable to be capable of being
exported (when explicitly requested in the 'use' arguments), you mark it
with the ':Export' attribute.

  * If you want a subroutine or package variable to be automatically exported
when the module is used (without specific overriding arguments), you mark
it with the ':Export(:DEFAULT)' attribute.

  * If you want a subroutine or package variable to be automatically exported
when the module is used (even if the user specifies overriding arguments),
you mark it with the ':Export(:MANDATORY)' attribute.

  * If the subroutine or package variable should also be exported when
particular export groups are requested, you add the names of those export
groups to the attribute's argument list.

That's it.

%prep
%setup -q -n %{cpan_name}-v%{version}

%build
%{__perl} Build.PL --installdirs=vendor
./Build build --flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install --destdir=%{buildroot} --create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README
%license LICENSE

%changelog
