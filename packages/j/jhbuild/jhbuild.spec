#
# spec file for package jhbuild
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


%define moduleset latest
Name:           jhbuild
Version:        3.30.0~20190728
Release:        0
Summary:        Tool to build GNOME
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
URL:            https://wiki.gnome.org/Projects/Jhbuild
Source0:        %{name}-%{version}.tar.xz
Source1:        README.deps
Source2:        sample.jhbuildrc
Source99:       create-deps.sh
BuildRequires:  fdupes
BuildRequires:  gnome-common
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  python
BuildRequires:  translation-update-upstream
BuildRequires:  update-desktop-files
BuildRequires:  yelp-tools
# Packages required to pass `jhbuild sanitycheck`
Requires:       autoconf
Requires:       automake
Requires:       bison
Requires:       cvs
Requires:       docbook-xsl-stylesheets
Requires:       flex
Requires:       gettext-tools
Requires:       libtool
Requires:       python-gtk
Recommends:     %{name}-lang
Recommends:     git-core
Recommends:     patch
Recommends:     subversion
Suggests:       cvs

%description
Jhbuild is a tool used to build the whole GNOME desktop from the
git source, however, it can be used to build other projects
creating a moduleset for it.

%package recommended-deps
Summary:        Recommended dependencies to use jhbuild
Group:          Development/Tools/Building
Requires:       %{name} = %{version}
# Manual extracted deps from moduleset-3.16
Requires:       bison
Requires:       cmake
Requires:       cracklib-devel
Requires:       cups-devel
Requires:       db-devel
Requires:       doxygen
Requires:       flex
Requires:       font-util
Requires:       gettext-tools
Requires:       gperf
Requires:       intltool
Requires:       libacl-devel
Requires:       libcap-devel
Requires:       libiw-devel
Requires:       libtiff-devel
Requires:       libwebp-devel
Requires:       libyaml-devel
Requires:       makeinfo
Requires:       mpfr-devel
Requires:       pam-devel
Requires:       ppp-devel
Requires:       python-libxml2
Requires:       python-rdflib
Requires:       ragel
Requires:       raptor
Requires:       sqlite
Requires:       xmlto
Recommends:     autoconf
Recommends:     automake
# Note: the order is order in jhbuild moduleset files
## Compilers
Recommends:     gcc-c++
## From bootstrap:
Recommends:     gettext-tools
Recommends:     libtool
Recommends:     pkgconfig
Recommends:     python
## System Dependencies as defined by the moduleset configuration
# only pkg-config deps are auto extracted, as we do not have to
# worry about package names there
%(sh %{SOURCE99} %{SOURCE0} %{moduleset})

%description recommended-deps
Jhbuild is a tool used to build the whole GNOME desktop from the
git source, however, it can be used to build other projects
creating a moduleset for it.

This package will install the dependencies to build GNOME
with jhbuild, to make this tool easier to use on openSUSE

The list is extracted from the moduleset version %{moduleset}

%lang_package

%prep
%setup -q
translation-update-upstream
cp %{SOURCE1} .
cp %{SOURCE2} .

%build
NOCONFIGURE=1 gnome-autogen.sh
%configure \
	--disable-scrollkeeper \
    --enable-gui
make %{?_smp_mflags}

%install
%make_install
%suse_update_desktop_file jhbuild
%fdupes %{buildroot}%{python_sitelib}
%fdupes %{buildroot}%{_datadir}
%find_lang %{name} %{?no_lang_C}

%files
%license COPYING
%doc AUTHORS HACKING MAINTAINERS NEWS README sample.jhbuildrc
%{_bindir}/jhbuild
%{python_sitelib}/jhbuild/
%{_datadir}/applications/jhbuild.desktop
%{_datadir}/jhbuild/

%files recommended-deps
%doc README.deps

%files lang -f %{name}.lang

%changelog
