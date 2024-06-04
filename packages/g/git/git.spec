#
# spec file for package git
#
# Copyright (c) 2024 SUSE LLC
# Copyright (c) 2024 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%define rb_build_ruby_abis     %{rb_default_ruby_abi}
%define rb_build_versions      %{rb_default_ruby}
%define gitexecdir %{_libexecdir}/git
%if 0%{?suse_version} < 1500
%define _fwdefdir %{_sysconfdir}/sysconfig/SuSEfirewall2.d/services
%define SuSEfirewall2 1
%endif
#Compat macro for new _fillupdir macro introduced in Nov 2017
%if ! %{defined _fillupdir}
  %define _fillupdir %{_localstatedir}/adm/fillup-templates
%endif
# Compat stub for python3_fix_shebang_path
%{?!python3_fix_shebang_path:%define python3_fix_shebang_path(+abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-=) \\\
    myargs="%{**}" \
    for f in ${myargs}; do \
        [ -f "$f" ] && sed -i -e "1s@#\\!.*python.*@#\\!$(realpath %__python3)@" $f \
    done
    }
%bcond_without git_libsecret
%bcond_without docs
%if 0%{?suse_version} >= 1500 && %{with docs}
%bcond_without asciidoctor
%else
%bcond_with    asciidoctor
%endif
Name:           git
Version:        2.45.2
Release:        0
Summary:        Fast, scalable, distributed revision control system
License:        GPL-2.0-only
Group:          Development/Tools/Version Control
URL:            https://git-scm.com/
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
Source11:       git-daemon.conf
Source12:       git-prompt
Patch3:         completion-wordbreaks.diff
# CVE-2011-2186, bnc#698456
Patch4:         git-prevent_xss-default.diff
# cook up tcsh completion to be installable (bnc#853183)
Patch6:         git-tcsh-completion-fixes.diff
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
BuildRequires:  pkgconfig
# for the %%python3_fix_shebang_path macro
BuildRequires:  python-rpm-macros
BuildRequires:  python3-base
BuildRequires:  systemd-rpm-macros
BuildRequires:  tcsh
BuildRequires:  update-desktop-files
BuildRequires:  xz
BuildRequires:  pkgconfig(zlib)
Requires:       git-core = %{version}
Requires:       perl-Git = %{version}
Recommends:     git-email
Suggests:       git-daemon
Suggests:       git-gui
Suggests:       git-web
Suggests:       gitk
%if 0%{?suse_version} >= 1500
BuildRequires:  openssh-clients
BuildRequires:  sysuser-tools
%endif
%if %{with docs}
BuildRequires:  sgml-skel
BuildRequires:  xmlto
%if %{with asciidoctor}
BuildRequires:  %{rubygem asciidoctor}
BuildRequires:  docbook5-xsl-stylesheets
%else
BuildRequires:  asciidoc
%endif
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
Obsoletes:      git-remote-helpers < %{version}
%if 0%{?suse_version} >= 1550 || 0%{?sle_version} >= 150300
Recommends:     openssh-clients
%else
Recommends:     openssh
%endif

%description core
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations and
full access to internals.

These are the core tools with minimal dependencies.

%package -n perl-Git
Summary:        perl Bindings for Git
Group:          Development/Libraries/Perl
Requires:       perl-Error
Provides:       git-core:%{perl_vendorlib}/Git
%{perl_requires}

%description -n perl-Git
Git is a fast, scalable, distributed revision control system with an
unusually rich command set that provides both high-level operations and
full access to internals.

This package provides the Perl interface to the Git version control system.

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
Requires:       perl-Git = %{version}
Requires:       perl-Term-ReadKey
Requires:       subversion
Requires:       subversion-perl
Supplements:    (%{name} and subversion)

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
Requires:       perl-Git = %{version}
Supplements:    (%{name} and cvs)

%description cvs
Tools for importing CVS repositories to the Git version control system.

%if %{with git_libsecret}
%package credential-libsecret
Summary:        Git credential backend using libsecret to access keyring
Group:          Development/Tools/Version Control
Requires:       git-core = %{version}
Obsoletes:      git-credential-gnome-keyring < %{version}

%description credential-libsecret
A Git credential backend which uses libsecret API to acces keyrings such as
kwallet or GNOME keyring.

%endif

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

%description p4
Tools for importing Perforce repositories to the GIT version control
system.

%package email
Summary:        Git tools for sending email
Group:          Development/Tools/Version Control
Requires:       git-core = %{version}
# For sending mails over secure SMTP:
Requires:       perl-Authen-SASL
Requires:       perl-Git = %{version}
Requires:       perl-MailTools
Requires:       perl-Net-SMTP-SSL

%description email
Email interface for the GIT version control system.

%package daemon
Summary:        Simple Server for Git Repositories
Group:          Development/Tools/Version Control
Requires:       bash
Requires:       git-core = %{version}
Requires(pre):  %fillup_prereq
%if 0%{?suse_version} >= 1500
%{?sysusers_requires}
%{?systemd_requires}
%else
Requires(pre):  %{_sbindir}/useradd
Requires(pre):  shadow
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
%if 0%{?suse_version} == 1315
Supplements:    (git-core and tk)
%else
Supplements:    (git-core and tk)
%endif

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
%if 0%{?suse_version} == 1315
Supplements:    (git-core and tk)
%else
Supplements:    (git-core and tk)
%endif

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
Requires:       perl-Git = %{version}
%if 0%{?suse_version} == 1315
Supplements:    (git-core and apache2)
%else
Supplements:    (git-core and apache2)
%endif

%description web
CGI script that allows browsing git repositories via web interface.

The apache2 configuration contained in this package installs a virtual
directory /git/ that calls the cgi script.

%prep
%autosetup -p1

%build
# update shebang to use python3
sed -e '1{s,.*,#!%{_bindir}/python3,}' git-p4.py
cat > .make <<'EOF'
#!/bin/bash
%make_build CFLAGS="%{optflags}" \
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

%if %{with git_libsecret}
./.make -C contrib/credential/libsecret
%endif
./.make -C contrib/subtree/

%if 0%{?suse_version} >= 1500
%sysusers_generate_pre %{SOURCE11} git-daemon git-daemon.conf
%endif

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
(find %{buildroot}%{_bindir} -type f -o -type l | grep -vE "archimport|p4|svn|cvs|email|gitk|git-daemon|gui|web" | sed -e s@^%{buildroot}@@)                   > bin-man-doc-files
(find %{buildroot}%{gitexecdir} ! -type d | grep -vE "archimport|p4|svn|cvs|email|gitk|git-daemon|gui|web" | sed -e s@^%{buildroot}@@)               >> bin-man-doc-files
(find %{buildroot}%{_mandir} -type f | grep -vE "archimport|p4|svn|git-cvs|email|gitk|git-daemon|gui|web" | sed -e s@^%{buildroot}@@ -e 's/$/*/' ) >> bin-man-doc-files
# Don't pick up dependencies from sample files
find %{buildroot}/%{_datadir}/git-core/templates -type f -name "*.sample" -exec chmod a-x "{}" "+"
%perl_process_packlist
%if %{with docs}
find %{buildroot}/%{_mandir} -type f -exec chmod 644 "{}" "+"
%endif
install -m 644 -D contrib/completion/git-completion.bash %{buildroot}%{_datadir}/bash-completion/completions/git
install -m 644 -D contrib/completion/git-prompt.sh %{buildroot}%{_datadir}/bash-completion/completions/git-prompt.sh
mkdir -p %{buildroot}/%{_sysconfdir}/bash_completion.d/
install -m 644 %{SOURCE12} %{buildroot}/%{_sysconfdir}/bash_completion.d/git-prompt
# contrib/credential
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
install -m 644 -D contrib/completion/git-completion.zsh %{buildroot}%{_datadir}/zsh/site-functions/_git
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

%if 0%{?suse_version} >= 1500
mkdir -p %{buildroot}%{_sysusersdir}
install -m 0644 %{SOURCE11} %{buildroot}%{_sysusersdir}/
%endif

%find_lang %{name}
cat %{name}.lang >>bin-man-doc-files

%if %{defined python3_fix_shebang_path}
# fix shebang for git-p4 (and possibly others)
%python3_fix_shebang_path %{buildroot}%{gitexecdir}/*
%endif

# use symlinks instead of hardlinks in sub-commands
%fdupes -s %{buildroot}

%check
# https://public-inbox.org/git/f1a5f758-d81f-5985-9b5d-2f0dbfaac071@opensuse.org/
%ifnarch s390x
./.make %{?_smp_mflags} test
%endif

%if 0%{?suse_version} >= 1500
%pre daemon -f git-daemon.pre
%else

%pre daemon
if ! %{_bindir}/getent passwd git-daemon >/dev/null; then
  %{_sbindir}/useradd -r -d %{_localstatedir}/lib/empty -s /bin/false -c "git daemon" -g nogroup git-daemon
fi
%endif
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
%if 0%{?suse_version} >= 1500
%{_sysusersdir}/git-daemon.conf
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
%dir %{_sysconfdir}/apparmor.d
%config(noreplace) %{_sysconfdir}/apparmor.d/usr.share.git-web.gitweb.cgi
%{gitexecdir}//git-instaweb
%{gitexecdir}//git-web--browse
%{_mandir}/man1/*web*1%{?ext_man}
%{_mandir}/man5/*web*5%{?ext_man}

%files core -f bin-man-doc-files
%license COPYING
%{_datadir}/git-core/
%dir %{gitexecdir}
%dir %{gitexecdir}/mergetools
%{gitexecdir}/mergetools/guiffy
%{_bindir}/git-new-workdir
%{_datadir}/bash-completion/completions/*
%{_sysconfdir}/bash_completion.d/git-prompt
%{_datadir}/tcsh
%{_datadir}/zsh/site-functions/_git
%{_sysconfdir}/profile.d/*.csh

%files -n perl-Git
%license COPYING
%attr(-,root,root) %{perl_vendorlib}/Git
%attr(-,root,root) %{perl_vendorlib}/Git.pm

%changelog
