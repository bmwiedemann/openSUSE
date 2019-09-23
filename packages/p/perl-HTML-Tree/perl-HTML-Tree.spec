#
# spec file for package perl-HTML-Tree
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


Name:           perl-HTML-Tree
Version:        5.07
Release:        0
%define cpan_name HTML-Tree
Summary:        Build and Scan Parse-Trees of Html
License:        Artistic-1.0 or GPL-1.0+
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/HTML-Tree/
Source0:        https://cpan.metacpan.org/authors/id/K/KE/KENTNL/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(HTML::Entities)
BuildRequires:  perl(HTML::Parser) >= 3.46
BuildRequires:  perl(HTML::Tagset) >= 3.02
BuildRequires:  perl(Module::Build) >= 0.280800
BuildRequires:  perl(Test::Fatal)
Requires:       perl(HTML::Entities)
Requires:       perl(HTML::Parser) >= 3.46
Requires:       perl(HTML::Tagset) >= 3.02
Recommends:     perl(HTML::FormatText)
Recommends:     perl(LWP::UserAgent) >= 5.815
%{perl_requires}

%description
HTML-Tree is a suite of Perl modules for making parse trees out of HTML
source. It consists of mainly two modules, whose documentation you should
refer to: HTML::TreeBuilder and HTML::Element.

HTML::TreeBuilder is the module that builds the parse trees. (It uses
HTML::Parser to do the work of breaking the HTML up into tokens.)

The tree that TreeBuilder builds for you is made up of objects of the class
HTML::Element.

If you find that you do not properly understand the documentation for
HTML::TreeBuilder and HTML::Element, it may be because you are unfamiliar
with tree-shaped data structures, or with object-oriented modules in
general. Sean Burke has written some articles for _The Perl Journal_
('www.tpj.com') that seek to provide that background. The full text of
those articles is contained in this distribution, as:

* HTML::Tree::AboutObjects

"User's View of Object-Oriented Modules" from TPJ17.

* HTML::Tree::AboutTrees

"Trees" from TPJ18

* HTML::Tree::Scanning

"Scanning HTML" from TPJ19

Readers already familiar with object-oriented modules and tree-shaped data
structures should read just the last article. Readers without that
background should read the first, then the second, and then the third.

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
%doc Changes README TODO
%license LICENSE

%changelog
