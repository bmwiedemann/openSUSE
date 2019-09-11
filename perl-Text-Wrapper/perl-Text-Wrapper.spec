#
# spec file for package perl-Text-Wrapper
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Text-Wrapper
Version:        1.05
Release:        0
%define         cpan_name Text-Wrapper
Summary:        Word wrap text by breaking long lines
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Text-Wrapper/
Source:         http://www.cpan.org/authors/id/C/CJ/CJM/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(Text::Wrapper)
%{perl_requires}

%description
Text::Wrapper provides simple word wrapping. It breaks long lines, but does
not alter spacing or remove existing line breaks. If you're looking for
more sophisticated text formatting, try the the Text::Format manpage
module.

Reasons to use Text::Wrapper instead of Text::Format:

* *

  Text::Wrapper is significantly smaller.

* *

  It does not alter existing whitespace or combine short lines. It only
  breaks long lines.

Again, if Text::Wrapper doesn't meet your needs, try Text::Format.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f -print0 | xargs -0 chmod 644

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
%doc Changes example LICENSE README

%changelog
