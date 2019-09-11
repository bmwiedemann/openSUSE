#
# spec file for package devscripts
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


%define _xsl_stylesheet %{_datadir}/xml/docbook/stylesheet/nwalsh/current/manpages/docbook.xsl
Name:           devscripts
Version:        2.18.10
Release:        0
Summary:        Scripts to make the life of a Debian Package maintainer easier
License:        GPL-2.0-or-later AND GPL-2.0-only AND GPL-3.0-or-later AND GPL-3.0-only AND Artistic-2.0 AND (GPL-1.0-or-later OR Artistic-1.0) AND SUSE-Public-Domain AND ISC
Group:          Development/Tools/Building
URL:            https://salsa.debian.org/debian/devscripts
Source:         https://salsa.debian.org/debian/devscripts/-/archive/v%{version}/devscripts-v%{version}.tar.bz2
# PATCH-FIX-OPENSUSE devscripts-fix-build.patch -- Fix docbook template directories path.
Patch0:         devscripts-fix-build.patch
# PATCH-FIX-OPENSUSE devscripts-fix-python-install-layout.patch -- Remove Debian's --install-layout=deb from setup.py.
Patch1:         devscripts-fix-python-install-layout.patch
# PATCH-FEATURE-OPENSUSE devscripts-debcommit-hg16.patch -- Mercurial cannot commit empty, fix it.
Patch2:         devscripts-debcommit-hg16.patch
BuildRequires:  bash-completion-devel
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  dpkg-devel >= 1.18.19
BuildRequires:  help2man
BuildRequires:  libxslt
BuildRequires:  perl
BuildRequires:  perl-macros
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  sgmltool
BuildRequires:  texlive-latex
BuildRequires:  zlib-devel
Requires:       checkbashisms >= %{version}
Requires:       dpkg
Requires:       html2text
Provides:       deb:%{_bindir}/debchange
%{?perl_requires}

%description
Collection of scripts for working on Debian packages.

Examples:
 - bts: A command-line tool for manipulating the Debian Bug
   Tracking System.
 - dcontrol: Remotely query package and source control files for
   all Debian distributions.
 - debchange/dch: Automagically add entries to debian/changelog
   files.
 - debsign, debrsign: Sign a .changes/.dsc pair without needing any
   of the rest of the package to be present; can sign the pair
   remotely or fetch the pair from a remote machine for signing.
 - diff2patches: Extract patches from a .diff.gz file placing them
    under debian/ or, if present, debian/patches.
 - licensecheck: Attempt to determine the license of source files.
 - uscan: Scan upstream sites for new releases of packages.

%package -n checkbashisms
Summary:        Tool for checking /bin/sh scripts for possible bashisms
License:        GPL-2.0-or-later
Group:          Development/Tools/Building
Provides:       deb:%{_bindir}/checkbashisms
Provides:       devscripts:%{_bindir}/checkbashisms
BuildArch:      noarch
%{?perl_requires}

%description -n checkbashisms
checkbashisms performs basic checks on /bin/sh shell scripts for
the possible presence of bashisms. It takes the names of the shell
scripts on the command line, and outputs warnings if possible
bashisms are detected.

%prep
%setup -q -n devscripts-v%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
make %{?_smp_mflags} V=1 \
  XSL_STYLESHEET="%{_xsl_stylesheet}"

%install
%make_install \
  XSL_STYLESHEET="%{_xsl_stylesheet}"

mkdir -p %{buildroot}%{_mandir}/man1/
install -Dpm 0644 scripts/*.1 -t %{buildroot}%{_mandir}/man1/

while read target link; do
    if [ -d $(dirname "%{buildroot}$link") ]; then
        ln -sf "$target" "%{buildroot}$link"
    fi
done < debian/links

# Fix documentation.
mkdir -p %{buildroot}%{_docdir}/
if [ "%{_datadir}/doc" != "%{_docdir}" ]; then
    mv %{buildroot}%{_datadir}/doc/devscripts %{buildroot}%{_docdir}/
fi
install -Dpm 0644 debian/changelog %{buildroot}%{_docdir}/devscripts/changelog

%files
%license debian/copyright COPYING
%doc %{_docdir}/devscripts/
%{_bindir}/*
%exclude %{_bindir}/checkbashisms
%{_datadir}/devscripts/
%{python3_sitelib}/devscripts/
%{python3_sitelib}/devscripts-*
%{perl_vendorlib}/Devscripts/
%{_datadir}/bash-completion/completions/*
%exclude %{_datadir}/bash-completion/completions/checkbashisms
%{_mandir}/man?/*.?%{?ext_man}
%exclude %{_mandir}/man1/checkbashisms.1%{?ext_man}

%files -n checkbashisms
%license debian/copyright COPYING
%{_bindir}/checkbashisms
%{_datadir}/bash-completion/completions/checkbashisms
%{_mandir}/man1/checkbashisms.1%{?ext_man}

%changelog
