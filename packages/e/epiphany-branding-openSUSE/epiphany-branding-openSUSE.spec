#
# spec file for package epiphany-branding-openSUSE
#
# Copyright (c) 2018 SUSE LINUX GmbH, Nuernberg, Germany.
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


%define epiphany_version %(rpm -q --qf '%%{version}' epiphany)
Name:           epiphany-branding-openSUSE
Version:        42.1
Release:        0
Summary:        GNOME Web Browser -- openSUSE default bookmarks and user agent string
License:        GPL-2.0-or-later
Group:          Productivity/Networking/Web/Browsers
URL:            http://www.gnome.org/projects/epiphany/
Source0:        COPYING
Source1:        branding.conf.in
# PATCH-FEATURE-OPENSUSE opensuse-bookmarks.patch vuntz@novell.com -- Add openSUSE bookmarks
Patch0:         opensuse-bookmarks.patch
BuildRequires:  epiphany >= 3.23.2
# To be in sync with upstream defaults, do branding as a patch for upstream file.
# WARNING: As this package conflicts with epiphany-branding-openSUSE, you cannot
#          reuse build root. You have to build in a clean build root every time!
BuildRequires:  epiphany-branding-upstream >= 3.11.2
Requires:       epiphany = %{epiphany_version}
Supplements:    packageand(epiphany:branding-openSUSE)
Conflicts:      epiphany-branding
Provides:       epiphany-branding = %{epiphany_version}
BuildArch:      noarch

%description
Epiphany is a Web Browser for the GNOME Desktop. Its principles are
simplicity and standards compliance.

This package provides the openSUSE default bookmarks and user
agent string.

%prep
cp -a %{_datadir}/epiphany/default-bookmarks.rdf .
%patch0
cp -a %{SOURCE0} .

%build
case "%{?suse_version}" in
  1330)
	DISTRO="Tumbleweed"
	;;
  1320)
	DISTRO="13.2"
	;;
  1315)
%if 0%{?is_opensuse}
	DISTRO="Leap 42.1"
%else
	DISTRO="SLE12"
%endif
	;;
  1310)
	DISTRO="13.1"
	;;
  *)
	DISTRO="undef"
	;;
esac
sed "s,@distroversion@,$DISTRO,g;s,@pkgversion@,%{epiphany_version},g" %{SOURCE1} > branding.conf

%install
# custom bookmarks
install -D -m0644 default-bookmarks.rdf %{buildroot}%{_datadir}/epiphany/default-bookmarks.rdf
# user agent
install -D -m0644 branding.conf %{buildroot}%{_datadir}/epiphany/branding.conf

%files
%license COPYING

%{_datadir}/epiphany/default-bookmarks.rdf
%{_datadir}/epiphany/branding.conf

%changelog
