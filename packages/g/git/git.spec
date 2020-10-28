#
# spec file for package git
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


%define gitexecdir %{_libexecdir}/git
%if 0%{?suse_version} < 1500
%define _fwdefdir %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services
%define SuSEfirewall2 1
%endif

#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
%bcond_without git_gnome_keyring
%bcond_without git_libsecret
%bcond_without docs
%if 0%{?suse_version} >= 1500 && %{with docs}
%bcond_without asciidoctor
%else
%bcond_with    asciidoctor
%endif

Name:           git
Version:        2.29.1
Release:        0
Summary:        Fast, scalable, distributed revision control system
License:        GPL-2.0-only
Group:          Development/Tools/Version Control
URL:            http://git-scm.com
Source0:        https://www.kernel.org/pub/software/scm/git/%{name}-%{version}.tar.xz
Source1:        apache2-gitweb.conf
Source2:        sysconfig.git-daemon
Source3:        git-daemon.service
Source5:        usr.share.git-web.gitweb.cgi
Source6:        susefirewall-git-daemon
Source7:        https://www.kernel.org/pub/software/scm/git/%{name}-%{version}.tar.sign
Source8:        %{name}.keyring
Source9:        %{name}-gui.desktop
Source10:       %{name}-gui.png
Patch3:         completion-wordbreaks.diff
# CVE-2011-2186, bnc#698456
Patch4:         git-prevent_xss-default.diff
# cook up tcsh completion to be installable (bnc#853183)
Patch6:         git-tcsh-completion-fixes.diff
# adapt paths in zsh completion (bnc#853183)
Patch7:         git-zsh-completion-fixes.diff
Patch8:         git-asciidoc.patch
Patch10:        setup-don-t-fail-if-commondir-reference-is-deleted.patch

BuildRequires:  fdupes
BuildRequires:  gpg2
BuildRequires:  libcurl-devel
BuildRequires:  libexpat-devel
BuildRequires:  libopenssl-devel
BuildRequires:  pcre2-devel
BuildRequires:  perl-Error
BuildRequires:  perl-MailTools
BuildRequires:  python3-base
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcsh
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  zlib-devel
Requires:       git-core = %{version}
Recommends:     git-cvs
Recommends:     git-email
Recommends:     git-gui
Recommends:     git-svn
Recommends:     gitk
Suggests:       git-daemon
Suggests:       git-web
%if %{with docs}
BuildRequires:  sgml-skel
BuildRequires:  xmlto
%if %{with asciidoctor}
BuildRequires:  docbook5-xsl-stylesheets
BuildRequires:  rubygem(asciidoctor)
%else
BuildRequires:  asciidoc
%endif
%endif
%if %{with git_gnome_keyring}
BuildRequires:  libgnome-keyring-devel
%endif
%if %{with git_libsecret}
BuildRequires:  libsecret-devel
%endif
%if 0%{?suse_version} > 1320
BuildRequires:  libsha1detectcoll-devel
%endif

%description
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations and
full access to internals.

This package itself only provides the README of git but with the
packages it requires, it brings you a complete Git environment
including GTK and email interfaces and tools for importing source code
repositories from other revision control systems such as subversion,
CVS, and GNU arch.

%package core
Summary:        Core git tools
Group:          Development/Tools/Version Control
Requires:       less
Requires:       openssh
Requires:       perl-Error
Requires:       rsync
Obsoletes:      git-remote-helpers < %{version}
%{perl_requires}

%description core
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations and
full access to internals.

These are the core tools with minimal dependencies.

%package doc
Summary:        Documentation for the Git version control system
Group:          Documentation/HTML
BuildArch:      noarch

%description doc
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations and
full access to internals.

This subpackage contains Git's documentation in text/plain and
text/html formats. (The manpages are in the main package.)

%package svn
Summary:        Git tools for importing Subversion repositories
Group:          Development/Tools/Version Control
Requires:       git-core = %{version}
Requires:       perl-Term-ReadKey
Requires:       subversion
Requires:       subversion-perl

%description svn
Tools for importing Subversion repositories to the Git version control
system.

%package cvs
Summary:        Git tools for importing CVS repositories
Group:          Development/Tools/Version Control
Requires:       cvs
Requires:       cvsps
Requires:       git-core = %{version}
Requires:       perl-DBD-SQLite

%description cvs
Tools for importing CVS repositories to the Git version control system.

%package credential-gnome-keyring
Summary:        Git credential backend using the GNOME keyring as storage
Group:          Development/Tools/Version Control
Requires:       git-core = %{version}
Requires:       gnome-keyring

%description credential-gnome-keyring
A Git credential backend which uses the GNOME keyring as storage.

%package credential-libsecret
Summary:        Git credential backend using libsecret to access keyring
Group:          Development/Tools/Version Control
Requires:       git-core = %{version}

%description credential-libsecret
A Git credential backend which uses libsecret API to acces keyrings such as
kwallet or GNOME keyring.

%package arch
Summary:        Git tools for importing Arch repositories
Group:          Development/Tools/Version Control
Requires:       git-core = %{version}
# Requires:       tla

%description arch
Tools for importing GNU Arch repositories to the GIT version control
system.

%package p4
Summary:        Git tools for importing Perforce repositories
Group:          Development/Tools/Version Control
Requires:       git-core = %{version}
Requires:       python2-base

%description p4
Tools for importing Perforce repositories to the GIT version control
system.

%package email
Summary:        Git tools for sending email
Group:          Development/Tools/Version Control
Requires:       git-core = %{version}
# For sending mails over secure SMTP:
Requires:       perl-Authen-SASL
Requires:       perl-MailTools
Requires:       perl-Net-SMTP-SSL

%description email
Email interface for the GIT version control system.

%package daemon
Summary:        Simple Server for Git Repositories
Group:          Development/Tools/Version Control
Requires:       git-core = %{version}
Requires(pre):  %fillup_prereq
Requires(pre):  %{_sbindir}/useradd
Requires(pre):  shadow
%{?systemd_requires}
%if 0%{?suse_version} >= 1500
Requires(pre):  group(nogroup)
%endif

%description daemon
A really simple TCP git daemon. In the default configuration it allows
read only access to repositories in /srv/git/ that contain the
'git-daemon-export-ok' file.

%package -n gitk
Summary:        Git revision tree visualiser
Group:          Development/Tools/Version Control
Requires:       git-core = %{version}
Requires:       tk >= 8.4
Supplements:    packageand(git-core:tk)

%description -n gitk
Grapical tool for visualization of revision trees of projects
maintained in the Git version control system. It name gitk indicates
that it's written using the Tk Widget set.

A simple Tk based graphical interface for common Git operations is
found in the package git-gui.

%package gui
Summary:        Grapical tool for common git operations
Group:          Development/Tools/Version Control
Requires:       git-core = %{version}
Requires:       tk >= 8.4
Supplements:    packageand(git-core:tk)

%description gui
A Tcl/Tk based graphical user interface to Git. git-gui focuses on
allowing users to make changes to their repository by making new
commits, amending existing ones, creating branches, performing local
merges, and fetching/pushing to remote repositories.

Unlike gitk, git-gui focuses on commit generation and single file
annotation, and does not show project history. It does however supply
menu actions to start a gitk session from within git-gui.

%package web
Summary:        Git Web Interface
Group:          Development/Tools/Version Control
Requires:       git-core = %{version}
Requires:       perl-CGI
Supplements:    packageand(git-core:apache2)

%description web
CGI script that allows browsing git repositories via web interface.

The apache2 configuration contained in this package installs a virtual
directory /git/ that calls the cgi script.

%prep
%setup -q
%patch3 -p1
%patch4 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch10 -p1

%build
cat > .make <<'EOF'
#!/bin/bash
make %{?_smp_mflags} CFLAGS="%{optflags}" \
       GITWEB_CONFIG="%{_sysconfdir}/gitweb.conf" \
       GITWEB_PROJECTROOT="/srv/git" \
       WITH_OWN_SUBPROCESS_PY=YesPlease \
       DESTDIR=%{buildroot} \
       NO_CROSS_DIRECTORY_HARDLINKS=1 \
       NO_INSTALL_HARDLINKS=1 \
%if 0%{?suse_version} > 1320
       DC_SHA1_EXTERNAL=YesPlease \
%endif
%if %{with asciidoctor}
       USE_ASCIIDOCTOR=YesPlease \
%endif
       PYTHON_PATH=%{_bindir}/python3 \
       USE_LIBPCRE2=YesPlease \
       NO_PERL_CPAN_FALLBACKS=1 \
       V=1 \
       prefix=%{_prefix} mandir=%{_mandir} \
       gitexecdir=%{gitexecdir} \
       htmldir=%{_docdir}/git \
       perllibdir=%{perl_vendorlib} \
       "$@"
EOF
#
chmod 755 .make
./.make all %{?_smp_mflags}
%if %{with docs}
./.make doc %{?_smp_mflags}
%endif

%if %{with git_gnome_keyring}
./.make -C contrib/credential/gnome-keyring
%endif
%if %{with git_libsecret}
./.make -C contrib/credential/libsecret
%endif
./.make -C contrib/subtree/

%install
./.make install %{!?_without_docs: install-doc}
### git-web
cp gitweb/INSTALL INSTALL.gitweb
cp gitweb/README README.gitweb
install -d %{buildroot}%{_datadir}/git-web
install -d %{buildroot}%{_sysconfdir}/apache2/conf.d
install -m 644 %{SOURCE1} %{buildroot}%{_sysconfdir}/apache2/conf.d/gitweb.conf
### git-daemon
install -d -m 755 %{buildroot}%{_unitdir}
install -m 644 %{SOURCE3} %{buildroot}/%{_unitdir}/git-daemon.service
install -d -m 755 %{buildroot}%{_sbindir}
ln -s %{_sbindir}/service %{buildroot}%{_sbindir}/rcgit-daemon
install -d -m 755 %{buildroot}%{_fillupdir}
install -m 644 %{SOURCE2} %{buildroot}%{_fillupdir}/sysconfig.git-daemon
install -d -m 755 %{buildroot}/srv/git
%if 0%{?SuSEfirewall2}
mkdir -p %{buildroot}/%{_fwdefdir}
install -m 644 %{SOURCE6} %{buildroot}/%{_fwdefdir}/git-daemon
%endif
###
./.make -C contrib/subtree install
%{!?_without_docs: ./.make -C contrib/subtree install-doc}
(find %{buildroot}%{_bindir} -type f -o -type l | grep -vE "archimport|p4|svn|cvs|email|gitk|git-daemon|gui" | sed -e s@^%{buildroot}@@)                   > bin-man-doc-files
(find %{buildroot}%{gitexecdir} ! -type d | grep -vE "archimport|p4|svn|cvs|email|gitk|git-daemon|gui" | sed -e s@^%{buildroot}@@)               >> bin-man-doc-files
(find %{buildroot}%{_mandir} -type f | grep -vE "archimport|p4|svn|git-cvs|email|gitk|git-daemon|gui" | sed -e s@^%{buildroot}@@ -e 's/$/*/' ) >> bin-man-doc-files
%perl_process_packlist
%if %{with docs}
find %{buildroot}/%{_mandir} -type f -exec chmod 644 "{}" "+"
%endif
install -m 644 -D contrib/completion/git-completion.bash %{buildroot}%{_sysconfdir}/bash_completion.d/git.sh
install -m 644 -D contrib/completion/git-prompt.sh %{buildroot}%{_sysconfdir}/bash_completion.d/git-prompt.sh
# contrib/credential
%if %{with git_gnome_keyring}
install -m 755 -D contrib/credential/gnome-keyring/git-credential-gnome-keyring %{buildroot}/%{gitexecdir}/git-credential-gnome-keyring
%endif
%if %{with git_libsecret}
install -m 755 -D contrib/credential/libsecret/git-credential-libsecret %{buildroot}/%{gitexecdir}/git-credential-libsecret
%endif
# contrib/workdir
install -m 755 -D contrib/workdir/git-new-workdir %{buildroot}/%{_bindir}
# process tcsh completion
(cd contrib/completion
 mkdir -p %{buildroot}%{_datadir}/tcsh
 tcsh ./git-completion.tcsh
 install -m 644 -D git.csh %{buildroot}%{_sysconfdir}/profile.d/git.csh
)
# zsh completion
install -m 644 -D contrib/completion/git-completion.zsh %{buildroot}%{_sysconfdir}/zsh_completion.d/_git
#
# apparmor profile for git-web
#
install -d -m 755 %{buildroot}%{_sysconfdir}/apparmor.d
install -m 644 %{SOURCE5} %{buildroot}%{_sysconfdir}/apparmor.d
#
# create predictable symlinks to make apparmor profile work
for i in git git-upload-archive git-receive-pack; do
  rm %{buildroot}%{_bindir}/$i
  ln -s %{gitexecdir}/git %{buildroot}%{_bindir}/$i
done
if ! test -f %{buildroot}%{gitexecdir}/git-add; then
  echo "git-add is not a regular file, apparmor profile won't work!" >&2
  exit 1
fi

mkdir -p "%{buildroot}/%{_docdir}/git" "%{buildroot}/%{_docdir}/git/howto" "%{buildroot}/%{_docdir}/git/technical"
cp -a README.md Documentation/*.txt "%{buildroot}/%{_docdir}/git/"
cp -a Documentation/howto/*.txt "%{buildroot}/%{_docdir}/git/howto/"
cp -a Documentation/technical/*.txt "%{buildroot}/%{_docdir}/git/technical/"
%{!?_without_docs: cp -a Documentation/*.html "%{buildroot}/%{_docdir}/git/"}
%{!?_without_docs: cp -a Documentation/howto/*.html "%{buildroot}/%{_docdir}/git/howto/"}
%{!?_without_docs: cp -a Documentation/technical/*.html "%{buildroot}/%{_docdir}/git/technical/"}

install -d -m 755 %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE9} %{buildroot}%{_datadir}/applications
install -d -m 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 %{SOURCE10} %{buildroot}%{_datadir}/pixmaps
%suse_update_desktop_file %{buildroot}%{_datadir}/applications/%{name}-gui.desktop

%find_lang %{name}
cat %{name}.lang >>bin-man-doc-files
# use symlinks instead of hardlinks in sub-commands
%fdupes -s %{buildroot}

%check
./.make %{?_smp_mflags} test

%pre daemon
if ! %{_bindir}/getent passwd git-daemon >/dev/null; then
  %{_sbindir}/useradd -r -d %{_localstatedir}/lib/empty -s /bin/false -c "git daemon" -g nogroup git-daemon
fi
%service_add_pre git-daemon.service

%post daemon
%{fillup_only -n git-daemon}
%service_add_post git-daemon.service

%preun daemon
%service_del_preun git-daemon.service

%postun daemon
%service_del_postun git-daemon.service

%files
%dir %{_docdir}/%{name}
%{_docdir}/%{name}/README.md

%files doc
%{_docdir}/%{name}/
%exclude %{_docdir}/%{name}/README.md

%files svn
%{gitexecdir}/*svn*
%{!?_without_docs: %{_mandir}/man1/*svn*.1*}

%files cvs
%{_bindir}/git-cvs*
%{gitexecdir}/*cvs*
%{!?_without_docs: %{_mandir}/man1/*cvs*.1*}

%if %{with git_gnome_keyring}
%files credential-gnome-keyring
%{gitexecdir}/git-credential-gnome-keyring
%endif

%if %{with git_libsecret}
%files credential-libsecret
%{gitexecdir}/git-credential-libsecret
%endif

%files arch
%{gitexecdir}/git-archimport
%{!?_without_docs: %{_mandir}/man1/git-archimport.1*}

%files p4
%{gitexecdir}/git-p4
%{gitexecdir}/mergetools/p4merge
%{!?_without_docs: %{_mandir}/man1/git-p4.1*}

%files email
%{gitexecdir}/*email*
%{!?_without_docs: %{_mandir}/man1/*email*.1*}

%files daemon
%{gitexecdir}/git-daemon
%{_unitdir}/git-daemon.service
%{_sbindir}/rcgit-daemon
%dir /srv/git
%{_fillupdir}/sysconfig.git-daemon
%{!?_without_docs: %{_mandir}/man1/git-daemon.1*}
%if 0%{?SuSEfirewall2}
%config %{_fwdefdir}/*
%endif

%files -n gitk
%{_bindir}/gitk
%{_datadir}/gitk
%{!?_without_docs: %{_mandir}/man1/*gitk*.1*}

%files gui
%{gitexecdir}/git-gui*
%{_datadir}/git-gui
%{!?_without_docs: %{_mandir}/man1/*gui*.1*}
%{_datadir}/applications/%{name}-gui.desktop
%{_datadir}/pixmaps/%{name}-gui.png

%files web
%doc README.gitweb INSTALL.gitweb
%dir %{_sysconfdir}/apache2
%dir %{_sysconfdir}/apache2/conf.d/
%config(noreplace) %{_sysconfdir}/apache2/conf.d/gitweb.conf
%{_datadir}/gitweb
%{_sysconfdir}/apparmor.d

%files core -f bin-man-doc-files
%{_datadir}/git-core/
%dir %{gitexecdir}
%dir %{gitexecdir}/mergetools
%{gitexecdir}/mergetools/guiffy
%{_bindir}/git-new-workdir
%attr(-,root,root) %{perl_vendorlib}/*
%{_sysconfdir}/bash_completion.d/*.sh
%{_datadir}/tcsh
%{_sysconfdir}/profile.d/*.csh
%{_sysconfdir}/zsh_completion.d
%license COPYING

%changelog
