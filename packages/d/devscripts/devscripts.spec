#
# spec file for package devscripts
#
# Copyright (c) 2024 SUSE LLC
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


%define flavor @BUILD_FLAVOR@%{nil}
%if "%{flavor}" == "checkbashisms"
  %define name_suffix -checkbashisms
%endif

%define _xsl_stylesheet %{_datadir}/xml/docbook/stylesheet/nwalsh/current/manpages/docbook.xsl
Name:           devscripts%{?name_suffix}
Version:        2.22.2
Release:        0
Summary:        Scripts to make the life of a Debian Package maintainer easier
License:        (Artistic-1.0 OR GPL-1.0-or-later) AND Artistic-2.0 AND GPL-2.0-only AND GPL-2.0-or-later AND GPL-3.0-or-later AND GPL-3.0-only AND SUSE-Public-Domain AND ISC
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
%if "%{flavor}" == ""
BuildRequires:  docbook-xsl-stylesheets
BuildRequires:  dpkg-devel >= 1.18.19
BuildRequires:  help2man
BuildRequires:  libxslt
%endif
BuildRequires:  perl
BuildRequires:  perl-macros
%if "%{flavor}" == ""
BuildRequires:  po4a
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  sgmltool
BuildRequires:  texlive-latex
BuildRequires:  zlib-devel
%endif
Requires:       checkbashisms >= %{version}
Requires:       dpkg
Requires:       html2text
Requires:       perl-File-HomeDir
Requires:       perl-IPC-Run
Requires:       perl-Moo
# provides same %_bindir/hardening-check binary
Conflicts:      hardening-check
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

%if "%{flavor}" == "checkbashisms"
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
bashisms are detected.*
%endif

%prep
%autosetup -p1 -n devscripts-v%{version}

%if "%{flavor}" == "foo"
echo %{version} > version
%endif

%build
%if "%{flavor}" == ""
make %{?_smp_mflags} V=1 \
  XSL_STYLESHEET="%{_xsl_stylesheet}"
%endif

%install
%if "%{flavor}" == ""
%make_install \
  XSL_STYLESHEET="%{_xsl_stylesheet}"
%python3_fix_shebang
%endif

%if "%{flavor}" == "checkbashisms"
mkdir -p %{buildroot}%{_bindir}
sed -e "s/###VERSION###/%{version}/" scripts/checkbashisms.pl > %{buildroot}%{_bindir}/checkbashisms
chmod a+x %{buildroot}%{_bindir}/checkbashisms
install -D -m755 scripts/checkbashisms.bash_completion %{buildroot}%{_datadir}/bash-completion/completions/checkbashisms
%endif

# remove completion that was provided in older bash completion
%if 0%{?suse_version} <= 1500
rm %{buildroot}%{_datadir}/bash-completion/completions/bts
%endif

mkdir -p %{buildroot}%{_mandir}/man1/
%if "%{flavor}" == ""
install -Dpm 0644 scripts/*.1 -t %{buildroot}%{_mandir}/man1/
%endif
%if "%{flavor}" == "checkbashisms"
install -Dpm 0644 scripts/checkbashisms.1 -t %{buildroot}%{_mandir}/man1/
%endif

%if "%{flavor}" == ""
while read target link; do
    if [ -d $(dirname "%{buildroot}$link") ]; then
        ln -sf "$target" "%{buildroot}$link"
    fi
done < debian/links
%endif

# Fix documentation.
%if "%{flavor}" == ""
mkdir -p %{buildroot}%{_docdir}/
if [ "%{_datadir}/doc" != "%{_docdir}" ]; then
    mv %{buildroot}%{_datadir}/doc/devscripts %{buildroot}%{_docdir}/
fi
install -Dpm 0644 debian/changelog %{buildroot}%{_docdir}/devscripts/changelog
%endif

%if "%{flavor}" == ""
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
%endif

%if "%{flavor}" == "checkbashisms"
%files -n checkbashisms
%license debian/copyright COPYING
%{_bindir}/checkbashisms
%{_datadir}/bash-completion/completions/checkbashisms
%{_mandir}/man1/checkbashisms.1%{?ext_man}
%endif

%changelog
