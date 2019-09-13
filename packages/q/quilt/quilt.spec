#
# spec file for package quilt
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


Name:           quilt
Version:        0.66
Release:        0
Summary:        A Tool for Working with Many Patches
License:        GPL-2.0-or-later
Group:          Development/Tools/Version Control
BuildRequires:  diffstat
BuildRequires:  ed
BuildRequires:  emacs-nox
Requires:       coreutils
Requires:       diffstat
Requires:       diffutils
Requires:       file
Requires:       findutils
Requires:       gzip
Requires:       less
Requires:       mktemp
Requires:       patch
Requires:       perl
Url:            http://savannah.nongnu.org/projects/quilt
Source:         %{name}-%{version}.tar.bz2
Source1:        suse-start-quilt-mode.el
Patch1:         expand.diff
Patch2:         quilt-support-vimdiff.patch
Patch3:         test-faildiff-workaround-order-bug.patch
Patch4:         suse-workaround-pseudo-release.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
%if 0%{?suse_version}
Recommends:     procmail
Recommends:     bzip2
Recommends:     /usr/bin/rpmbuild
%endif
%if 0%{?suse_version} > 1120
Recommends:     xz
%endif

%description
Quilt allows you to easily manage large numbers of patches by keeping
track of the changes each patch makes. Patches can be applied,
un-applied, refreshed, and more.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
# --with-rpmbuild=/usr/lib/rpm/rpmb:
#
#   SUSE Autobuild uses a version of /usr/bin/rpmbuild that sources
#   /etc/profile to reset the PATH. We must not do that: the
#   inspect script needs to pass an additional path component to
#   rpmbuild for the tar and patch wrappers.
CFLAGS="%{optflags}" \
./configure --prefix=/usr \
    --mandir=%{_mandir} \
    --docdir=%{_docdir}/%{name}%{!?suse_version:-%{version}} \
    --sysconfdir=%{_sysconfdir} \
    --with-sendmail=/usr/sbin/sendmail \
    --with-diffstat=/usr/bin/diffstat \
    --with-patch-wrapper \
    --with-patch=/usr/bin/patch \
    --with-rpmbuild=/usr/lib/rpm/rpmb
make %{?_smp_mflags}
# Compile quilt.el for faster emacs startup (bnc#617673)
pushd lib
emacs -batch -q --no-site -f batch-byte-compile quilt.el
popd

%check
make check

%install
# /usr/share/quilt/compat/mta will be a stale symlink: we don't want to add
# sendmail to neededforbuild just because of this.
export NO_BRP_STALE_LINK_ERROR=yes
make install BUILD_ROOT=%{buildroot}
install -m 644 lib/quilt.elc \
	%{buildroot}%{_datadir}/emacs/site-lisp/
mv %{buildroot}%{_sysconfdir}/bash_completion.d/quilt{,.sh}
# We only needed the /usr/bin/patch compatibility symlink for the
# test suite.
[ %{buildroot}%{_datadir}/quilt/compat/patch -ef /usr/bin/patch ] \
    && rm -f %{buildroot}%{_datadir}/quilt/compat/patch
[ %{buildroot}%{_datadir}/quilt/compat/awk -ef /usr/bin/awk ] \
    && rm -f %{buildroot}%{_datadir}/quilt/compat/awk
%{find_lang} %{name}
# Make "vi" an alias for the edit command
ln -s edit %{buildroot}%{_datadir}/quilt/vi
# Autoload quilt-mode in the SuSE emacs package
install -m 644 %_sourcedir/suse-start-quilt-mode.el \
	%{buildroot}%{_datadir}/emacs/site-lisp/

%files -f %{name}.lang
%defattr(-, root, root)
%{_bindir}/guards
%{_bindir}/quilt
%{_datadir}/quilt/
%{_datadir}/emacs/
%config %{_sysconfdir}/quilt.quiltrc
%config %{_sysconfdir}/bash_completion.d/quilt.sh
%doc %{_mandir}/man1/guards.1.gz
%doc %{_mandir}/man1/quilt.1.gz
%doc doc/README
%doc doc/README.MAIL
%doc doc/quilt.pdf

%changelog
