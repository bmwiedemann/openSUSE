#
# spec file for package perl-Template-Tiny
#
# Copyright (c) 2013 SUSE LINUX Products GmbH, Nuernberg, Germany.
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


Name:           perl-Template-Tiny
Version:        1.12
Release:        0
%define cpan_name Template-Tiny
Summary:        Template Toolkit reimplemented in as little code as possible
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Template-Tiny/
Source:         http://www.cpan.org/authors/id/A/AD/ADAMK/%{cpan_name}-%{version}.tar.gz
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
#BuildRequires: perl(Template::Tiny)
%{perl_requires}

%description
*Template::Tiny* is a reimplementation of a subset of the functionality
from the Template manpage Toolkit in as few lines of code as possible.

It is intended for use in light-usage, low-memory, or low-cpu templating
situations, where you may need to upgrade to the full feature set in the
future, or if you want the retain the familiarity of TT-style templates.

For the subset of functionality it implements, it has fully-compatible
template and stash API. All templates used with *Template::Tiny* should be
able to be transparently upgraded to full Template Toolkit.

Unlike Template Toolkit, *Template::Tiny* will process templates without a
compile phase (but despite this is still quicker, owing to heavy use of the
Perl regular expression engine.

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
%doc Changes LICENSE README

%changelog
