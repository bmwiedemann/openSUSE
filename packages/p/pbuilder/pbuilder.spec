#
# spec file for package pbuilder
#
# Copyright (c) 2022 SUSE LLC
# Copyright (c) 2012 Frank Lichtenheld <frank@lichtenheld.de>
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


Name:           pbuilder
Version:        0.231
Release:        0
Summary:        Personal package builder for .deb packages
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://pbuilder-team.pages.debian.net/pbuilder
Source0:        http://deb.debian.org/debian/pool/main/p/pbuilder/pbuilder_%{version}.tar.xz
Patch0:         Makefile.patch
Patch1:         pdebuild-double-checkbuilddeps.patch
Patch2:         bash-completion-extglob.patch
Patch3:         pbuilder-ppc.patch
Requires:       debootstrap
Requires:       dpkg
Requires:       wget
%if 0%{?suse_version}
Recommends:     deb
Recommends:     fakeroot
Recommends:     sudo
%endif
BuildRequires:  dpkg
BuildRequires:  man
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
pbuilder constructs a chroot system, and builds a package inside the
chroot. It uses apt extensively, and a local mirror, or a fast
connection to a Debian/Ubuntu mirror is ideal, but not necessary.

"pbuilder create" uses debootstrap to create a chroot image.

"pbuilder update" updates the image to the current state of
testing/unstable/whatever

"pbuilder build" takes a *.dsc file and builds a binary in the chroot
image.

pdebuild is a wrapper for developers, to allow running pbuilder
just like "debuild", as a normal user.

Authors:
--------
    Junichi Uekawa

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%make_build

%install
%make_install

mkdir -p %{buildroot}/%{_defaultdocdir}
mv %{buildroot}/usr/share/doc/pbuilder %{buildroot}/%{_defaultdocdir}

for man in debuild-pbuilder.1 pbuilderrc.5 pbuilder.8 pdebuild.1; do
  category=${man: -1}
  install -D -m644 $man %{buildroot}%{_mandir}/man$category/$man
  gzip -9 %{buildroot}%{_mandir}/man$category/$man
done

for dir in build result aptcache ccache; do
  install -d %buildroot/var/cache/pbuilder/$dir
done

%check
%{__make} check

%files
%license COPYING AUTHORS
%doc ChangeLog README THANKS
%doc %{_defaultdocdir}/%{name}/examples
%dir    /etc/pbuilder
%config /etc/pbuilder/buildd-config.sh
%{_mandir}/man?/*
/usr/sbin/*
/usr/bin/*
/usr/lib/pbuilder
/usr/share/pbuilder
/var/cache/pbuilder
%{_datadir}/bash-completion/completions/%{name}

%changelog
