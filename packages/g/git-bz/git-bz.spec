#
# spec file for package git-bz
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


Name:           git-bz
Version:        0.0+git.20150908
Release:        0
Summary:        Command line integration of git with Bugzilla
License:        GPL-2.0+
Group:          Development/Tools/Version Control
Url:            http://blog.fishsoup.net/2008/11/16/git-bz-bugzilla-subcommand-for-git/
Source0:        %{name}-%{version}.tar.xz
BuildRequires:  asciidoc
BuildRequires:  xmlto
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build


%description
git-bz is a tool for integrating the Git command line with the
Bugzilla bug-tracking system. Operations such as attaching patches to
bugs, applying patches in bugs to your current tree, and closing bugs
once you've pushed the fixes publicly can be done completely from the
command line without having to go to your web browser.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
%make_install

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/git-bz
%{_mandir}/man1/git-bz.1%{ext_man}

%changelog
