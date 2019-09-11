#
# spec file for package guilt
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


Url:            http://www.kernel.org/pub/linux/kernel/people/jsipek/guilt/

Name:           guilt
Version:        0.35
Release:        1
Summary:        quilt on top of git
License:        GPL-2.0
Group:          Productivity/Text/Utilities
Source0:        %{name}-%{version}.tar.gz
# PATCH-FIX-OPENSUSE drop-unneeded-git-version-check.patch bnc#810667 douglarek@outlook.com
Patch0:         drop-unneeded-git-version-check.patch
BuildRequires:  asciidoc
BuildRequires:  docbook_3
BuildRequires:  docbook_4
BuildRequires:  sgml-skel
BuildRequires:  xmlto
Requires:       git
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch

%description
Andrew Morton originally developed a set of scripts for maintaining
kernel patches outside of any SCM tool. Others extended these into a
suite called quilt. The basic idea behind quilt is to maintain patches
instead of maintaining source files. Patches can be added, removed or
reordered, and they can be refreshed as you fix bugs or update to a new
base revision. quilt is very powerful, but it is not integrated with
the underlying SCM tools. This makes it difficult to visualize your
changes.

Guilt allows one to use quilt functionality on top of a Git repository.
Changes are maintained as patches which are committed into Git.
Commits can be removed or reordered, and the underlying patch can be
refreshed based on changes made in the working directory. The patch
directory can also be placed under revision control, so you can have a
separate history of changes made to your patches.

%prep
%setup -q
%patch0 -p0

%build
make

%install
make PREFIX=%{_prefix} DESTDIR=%{buildroot} install
make PREFIX=%{_prefix} DESTDIR=%{buildroot} mandir=%{_mandir} install-doc

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Documentation/{Contributing,Features,HOWTO}
%{_bindir}/*
%{_prefix}/lib/*
%{_mandir}/man1/*
%{_mandir}/man7/*

%changelog
