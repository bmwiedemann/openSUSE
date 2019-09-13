#
# spec file for package perl-Text-Markdown
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


Name:           perl-Text-Markdown
Version:        1.000031
Release:        0
%define cpan_name Text-Markdown
Summary:        Convert Markdown syntax to (X)HTML
License:        BSD-3-Clause
Group:          Development/Libraries/Perl
Url:            http://search.cpan.org/dist/Text-Markdown/
Source0:        https://cpan.metacpan.org/authors/id/B/BO/BOBTFISH/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Test::Differences)
BuildRequires:  perl(Test::Exception)
%{perl_requires}
# MANUAL BEGIN
%post
update-alternatives \
       --install %{_bindir}/markdown markdown %{_bindir}/Markdown.pl 30

%postun
if [ $1 -eq 0 ] ; then
       update-alternatives --remove markdown %{_bindir}/Markdown.pl
fi
# MANUAL END

%description
Markdown is a text-to-HTML filter; it translates an easy-to-read /
easy-to-write structured text format into HTML. Markdown's text format is
most similar to that of plain text email, and supports features such as
headers, *emphasis*, code blocks, blockquotes, and links.

Markdown's syntax is designed not as a generic markup language, but
specifically to serve as a front-end to (X)HTML. You can use span-level
HTML tags anywhere in a Markdown document, and you can use block level HTML
tags (like <div> and <table> as well).

%prep
%setup -q -n %{cpan_name}-%{version}
# MANUAL BEGIN
sed -i -e 's/use inc::Module::Install;/use lib q[.];\nuse inc::Module::Install;/' Makefile.PL
# MANUAL END

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make} %{?_smp_mflags}

%check
%{__make} test

%install
%perl_make_install
%perl_process_packlist
# MANUAL BEGIN
# update-alternatives
mkdir -p %{buildroot}%{_sysconfdir}/alternatives
touch %{buildroot}%{_sysconfdir}/alternatives/markdown
ln -sf %{_sysconfdir}/alternatives/markdown %{buildroot}%{_bindir}/markdown

echo "%ghost %{_sysconfdir}/alternatives/markdown" >> %{name}.files
echo "%{_bindir}/markdown" >> %{name}.files
# MANUAL END
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc Changes README Readme.text Todo
%license License.text

%changelog
