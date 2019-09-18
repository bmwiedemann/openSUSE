#
# spec file for package perl-Locale-Maketext-Gettext
#
# Copyright (c) 2019 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           perl-Locale-Maketext-Gettext
Version:        1.30
Release:        0
%define cpan_name Locale-Maketext-Gettext
Summary:        Joins the gettext and Maketext frameworks
License:        Artistic-1.0 OR GPL-1.0-or-later
Group:          Development/Libraries/Perl
Url:            https://metacpan.org/release/%{cpan_name}
Source0:        https://cpan.metacpan.org/authors/id/I/IM/IMACAT/%{cpan_name}-%{version}.tar.gz
Source1:        cpanspec.yml
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  perl(Module::Build)
%{perl_requires}

%description
Locale::Maketext::Gettext joins the GNU gettext and Maketext frameworks. It
is a subclass of Locale::Maketext(3) that follows the way GNU gettext
works. It works seamlessly, _both in the sense of GNU gettext and
Maketext_. As a result, you _enjoy both their advantages, and get rid of
both their problems, too._

You start as an usual GNU gettext localization project: Work on PO files
with the help of translators, reviewers and Emacs. Turn them into MO files
with _msgfmt_. Copy them into the appropriate locale directory, such as
_/usr/share/locale/de/LC_MESSAGES/myapp.mo_.

Then, build your Maketext localization class, with your base class changed
from Locale::Maketext(3) to Locale::Maketext::Gettext. That is all.

%prep
%setup -q -n %{cpan_name}-%{version}
find . -type f ! -name \*.pl -print0 | xargs -0 chmod 644

%build
perl Build.PL installdirs=vendor
./Build build flags=%{?_smp_mflags}

%check
./Build test

%install
./Build install destdir=%{buildroot} create_packlist=0
%perl_gen_filelist

%files -f %{name}.files
%defattr(-,root,root,755)
%doc BUGS Changes README THANKS TODO
%license Artistic COPYING

%changelog
