#
# spec file for package ikiwiki
#
# Copyright (c) 2020 SUSE LLC
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


# Basic requirements stated in Bundle::IkiWiki
%define base_requires perl(CGI) perl(CGI::FormBuilder) perl(CGI::Session) perl(Data::Dumper) perl(Date::Parse) perl(HTML::Parser) perl(HTML::Scrubber) perl(HTML::Template) perl(JSON) perl(Mail::Sendmail) perl(RPC::XML) perl(Text::Markdown) perl(URI) perl(XML::Simple) perl(YAML::XS)
# Basic plugin requirements stated in Bundle::IkiWiki::Extras
%define plugins_requires perl(Authen::Passphrase) perl(Crypt::SSLeay) perl(File::MimeInfo) perl(Gravatar::URL) perl(HTML::Tree) perl(Locale::gettext) perl(Net::INET6Glue) perl(Net::OpenID::Consumer) perl(Sort::Naturally) perl(Term::ReadLine::Gnu) perl(Text::CSV) perl(URI::Fetch) perl(XML::Feed) perl(XML::Writer)
# Additional requirements added based on code and docs searching
%define additional_requires perl(Cwd) perl(Digest::SHA) perl(Encode) perl(ExtUtils::MakeMaker) perl(File::Find) perl(File::chdir) perl(File::Path) perl(File::Spec) perl(Getopt::Long) perl(HTML::Entities) perl(HTML::TreeBuilder) perl(Image::Magick) perl(Locale::gettext) perl(Memoize) perl(Net::OpenID::VerifiedIdentity) perl(Storable) perl(URI::Escape) python3-docutils
# Requirements needed for tests
%define tests_requires cvs cvsps git-core mercurial perl(B) perl(Errno) perl(HTML::LinkExtor) perl(IPC::Run) perl(Test::More) perl(XML::Twig) subversion
# Currently unresolvable - enable when it becomes available
# - Net::Amazon::S3 - amazon_s3.pm
# - Text::Typography - typography.pm
# - Monotone - monotone.pm
# - Text::Markdown::Discount - base requires (but can be replaced by Text::Markdown), mdwn.pm
# - LWPx::ParanoidAgent - openid.pm, pinger.pm, blogspam.pm
# - Search::Xapian - search.pm
# - Text::Textile - textile.pm
# - Text::WikiFormat - wikitext.pm
# - Text::WikiCreole - creole.pm
# - Locale::Po4a::Chooser::new - po.t
Name:           ikiwiki
Version:        3.20200202.3
Release:        0
Summary:        A wiki compiler
License:        GPL-2.0-or-later AND BSD-2-Clause
Group:          Productivity/Networking/Web/Utilities
URL:            https://ikiwiki.info/
Source:         http://ftp.debian.org/debian/pool/main/i/%{name}/%{name}_%{version}.orig.tar.xz
BuildRequires:  %{additional_requires}
BuildRequires:  %{base_requires}
BuildRequires:  %{plugins_requires}
BuildRequires:  %{tests_requires}
BuildRequires:  fdupes
BuildRequires:  perl
BuildRequires:  perl-macros
Requires:       %{additional_requires}
Requires:       %{base_requires}
Requires:       %{plugins_requires}
BuildArch:      noarch
%{perl_requires}

%description
Ikiwiki is a wiki compiler. It converts wiki pages into HTML pages
suitable for publishing on a website. Ikiwiki stores pages and history
in a revision control system such as Subversion or Git. There are many
other features, including support for blogging and podcasting, as well
as a large array of plugins.

%package w3m
Summary:        Ikiwiki w3m cgi meta-wrapper
Group:          Productivity/Networking/Web/Utilities
Requires:       %{name} = %{version}-%{release}
Requires:       w3m

%description w3m
Enable to use all of ikiwiki's web features (page editing, etc) in
the w3m web browser without using a web server. w3m supports local
CGI scripts, and ikiwiki can be set up to run that way.

%files w3m
%doc README.w3m
%{cgi_bin}/ikiwiki-w3m.cgi

%prep
%setup -q -n ikiwiki-%{version}

# Create README for the w3m subpackage
cat << \EOF > README.w3m
See http://ikiwiki.info/w3mmode/ for more information about w3m mode
configuration
EOF

%build
perl Makefile.PL PREFIX=%{_prefix} INSTALLDIRS=vendor
%make_build

%check
%make_build test || :

%install
make pure_install DESTDIR=%{buildroot}

# remove shebang
sed -e '1{/^#!/d}' -i \
    %{buildroot}%{_sysconfdir}/ikiwiki/auto.setup \
    %{buildroot}%{_sysconfdir}/ikiwiki/auto-blog.setup \
    %{buildroot}%{_prefix}/lib/ikiwiki/plugins/proxy.py \
    %{buildroot}%{_prefix}/lib/ikiwiki/plugins/rst

%find_lang %{name}
%fdupes %{buildroot}

%files -f %{name}.lang
%license html/GPL
%doc debian/NEWS README debian/changelog
%doc doc/examples
%doc IkiWiki/Plugin/skeleton.pm.example
%{_bindir}/ikiwiki
%{_bindir}/ikiwiki-comment
%{_bindir}/ikiwiki-transition
%{_bindir}/ikiwiki-makerepo
%{_bindir}/ikiwiki-calendar
%{_bindir}/ikiwiki-update-wikilist
%{_sbindir}/ikiwiki-mass-rebuild
%{_mandir}/man1/ikiwiki*
%{_mandir}/man8/ikiwiki*
%{_prefix}/lib/ikiwiki
%{_datadir}/ikiwiki
%dir %{_sysconfdir}/ikiwiki
%config(noreplace)%{_sysconfdir}/ikiwiki/wikilist
%config(noreplace)%{_sysconfdir}/ikiwiki/auto.setup
%config(noreplace)%{_sysconfdir}/ikiwiki/auto-blog.setup
%{perl_vendorlib}/IkiWiki*
%exclude %{perl_vendorlib}/IkiWiki*/Plugin/skeleton.pm.example
%exclude %{perl_vendorarch}
%exclude %{_datadir}/ikiwiki/examples

%files w3m
%doc README.w3m
%dir %{_prefix}/lib/w3m
%dir %{_prefix}/lib/w3m/cgi-bin
%{_prefix}/lib/w3m/cgi-bin/ikiwiki-w3m.cgi

%changelog
