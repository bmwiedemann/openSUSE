#
# spec file for package hg-fast-export
#
# Copyright (c) 2015 SUSE LINUX GmbH, Nuernberg, Germany.
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


Name:           hg-fast-export
Version:        20140308
Release:        0
Summary:        Mercurial to git converter using git-fast-import
License:        GPL-2.0
Group:          Development/Tools/Version Control
Url:            http://repo.or.cz/w/fast-export.git
# git clone %{URL}
# VERSION=`git log -n 1 --pretty=%ci | cut -d ' ' -f 1 | tr -d '-'`
# tar -cjf fast-export-${VERSION}.tar.gz fast-export/
Source0:        http://ftp.de.debian.org/debian/pool/main/h/hg-fast-export/%{name}_%{version}.orig.tar.gz
Source1:        http://ftp.de.debian.org/debian/pool/main/h/hg-fast-export/%{name}_%{version}-1.debian.tar.xz
%if 0%{?suse_version} && 0%{?suse_version} <= 1110
%{!?python_sitelib: %global python_sitelib %(python -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}
%else
BuildArch:      noarch
%endif
BuildRequires:  python-devel
%if 0%{?suse_version} == 1110
BuildRequires:  xz
%endif
Requires:       git
Requires:       mercurial

%description
hg-fast-export tool allows incremental import of mercurial repositories to git
repositories.

It can automatically import a local hg repo into a local git repo using just
one command. Subsequent importing of new changesets is supported.

Included git-hg wrapper script can be used to transparently track Mercurial
repositories without a separate checkout. It also includes experimental support
for pushing back to Mercurial. 

%prep
%setup -q -a 1

sed --in-place 's@^ROOT=.*@ROOT="/usr/share/%{name}"@' hg-fast-export.sh hg-reset.sh
sed --in-place '/^#!\/usr\/bin\/env.*/d' *.py

%build
#nope

%install

# binaries
%{__install} -d -m 0755 %{buildroot}%{_bindir}
%{__install} -m 0755 debian/git-hg %{buildroot}%{_bindir}
%{__install} -m 0755 hg-fast-export.sh %{buildroot}/%{_bindir}/hg-fast-export
%{__install} -m 0755 hg-reset.sh %{buildroot}/%{_bindir}/hg-reset

# python lib
%{__install} -d -m 0755 %{buildroot}/%{python_sitelib}
%{__install} -m 0644 hg2git.py* %{buildroot}/%{python_sitelib}

# other stuff
%{__install} -d -m 0755 %{buildroot}/%{_datadir}/%{name}
%{__install} -m 0644 hg-fast-export.py hg-reset.py %{buildroot}/%{_datadir}/%{name}/

# compile python stuff
%py_compile    %{buildroot}/%{python_sitelib}
%py_compile -O %{buildroot}/%{python_sitelib}
%py_compile    %{buildroot}/%{_datadir}/%{name}
%py_compile -O %{buildroot}/%{_datadir}/%{name}

# manual pages
%{__install} -d -m 0755 %{buildroot}/%{_mandir}/man1
%{__install} -m 0644 debian/*.1 %{buildroot}/%{_mandir}/man1/

%files
%defattr(-,root,root)
%doc README
%doc debian/copyright debian/README.git-hg
%{_bindir}/git-hg
%{_bindir}/hg-fast-export
%{_bindir}/hg-reset
%{python_sitelib}/hg2git.py*
%{_datadir}/%{name}
%{_mandir}/man1/*.1*

%changelog
