#
# spec file for package kernel-docs
#
# Copyright (c) 2025 SUSE LLC
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


%define srcversion 6.17
%define patchversion 6.17.0
%define git_commit 8490d9fb9ad8deab2079bb469502f71a97ffb5e6
%define variant %{nil}
%define build_html 1
%define build_pdf 0

%include %_sourcedir/kernel-spec-macros

%(chmod +x %_sourcedir/{guards,apply-patches,check-for-config-changes,group-source-files.pl,split-modules,modversions,kabi.pl,arch-symbols,check-module-license,splitflist,mergedep,moddep,modflist,kernel-subpackage-build})

Name:           kernel-docs
Version:        6.17.0
%if 0%{?is_kotd}
Release:        <RELEASE>.g8490d9f
%else
Release:        0
%endif
Summary:        Kernel Documentation
License:        GPL-2.0-only
Group:          Documentation/Man
URL:            https://www.kernel.org/
%if 0%{?suse_version} > 1500 || 0%{?sle_version} > 150300
BuildRequires:  bash-sh
%endif
# TW (4.13 or later) no longer needs xmlto
%if 0%{?sle_version}
BuildRequires:  xmlto
%endif
%if %build_pdf || %build_html
# ReST handling
BuildRequires:  ImageMagick
BuildRequires:  graphviz
BuildRequires:  graphviz-gd
BuildRequires:  graphviz-gnome
%if ! 0%{?suse_version} || 0%{?suse_version} > 1500
BuildRequires:  python3-base
BuildRequires:  python3-PyYAML
BuildRequires:  python3-Sphinx
BuildRequires:  texlive-amscls
%else
%if 0%{?suse_version} && 0%{?suse_version} < 1500
BuildRequires:  python-packaging
BuildRequires:  python-six
BuildRequires:  python-Sphinx
%else
BuildRequires:  python3-base
BuildRequires:  python3-Sphinx < 3
%endif
%endif
BuildRequires:  texlive-anyfontsize
%if %build_pdf
%if 0%{?suse_version} && 0%{?suse_version} < 1500
BuildRequires:  python-Sphinx-latex
%else
BuildRequires:  python3-base
BuildRequires:  python3-Sphinx-latex
%endif
BuildRequires:  texlive-adjustbox
BuildRequires:  texlive-dejavu
BuildRequires:  texlive-dejavu-fonts
BuildRequires:  texlive-glyphlist
BuildRequires:  texlive-makeindex
BuildRequires:  texlive-varwidth
BuildRequires:  texlive-xetex
BuildRequires:  texlive-zapfding
%endif
%endif
BuildArch:      noarch
Source0:        https://www.kernel.org/pub/linux/kernel/v6.x/linux-%srcversion.tar.xz
Source3:        kernel-source.rpmlintrc
Source14:       series.conf
Source16:       guards
Source17:       apply-patches
Source19:       kernel-binary-conflicts
Source20:       obsolete-kmps
Source21:       config.conf
Source23:       supported.conf
Source33:       check-for-config-changes
Source35:       group-source-files.pl
Source36:       README.PATCH-POLICY.SUSE
Source37:       README.SUSE
Source38:       README.KSYMS
Source40:       source-timestamp
Source46:       split-modules
Source47:       modversions
Source48:       macros.kernel-source
Source49:       kernel-module-subpackage
Source50:       kabi.pl
Source52:       kernel-source%variant.changes
Source57:       kernel-cert-subpackage
Source60:       config.sh
Source63:       arch-symbols
Source65:       kernel-spec-macros
Source75:       release-projects
Source76:       check-module-license
Source78:       modules.fips
Source79:       splitflist
Source80:       mergedep
Source81:       moddep
Source82:       modflist
Source83:       kernel-subpackage-build
Source84:       kernel-subpackage-spec
Source85:       kernel-default-base.spec.txt
Source86:       old_changelog.txt
Source100:      config.tar.bz2
Source101:      config.addon.tar.bz2
Source102:      patches.arch.tar.bz2
Source103:      patches.drivers.tar.bz2
Source104:      patches.fixes.tar.bz2
Source105:      patches.rpmify.tar.bz2
Source106:      patches.suse.tar.bz2
Source108:      patches.addon.tar.bz2
Source109:      patches.kernel.org.tar.bz2
Source110:      patches.apparmor.tar.bz2
Source111:      patches.rt.tar.bz2
Source113:      patches.kabi.tar.bz2
Source114:      patches.drm.tar.bz2
Source120:      kabi.tar.bz2
Source121:      sysctl.tar.bz2
# These files are found in the kernel-source package:
NoSource:       0
NoSource:       3
NoSource:       14
NoSource:       16
NoSource:       17
NoSource:       19
NoSource:       20
NoSource:       21
NoSource:       23
NoSource:       33
NoSource:       35
NoSource:       36
NoSource:       37
NoSource:       38
NoSource:       40
NoSource:       46
NoSource:       47
NoSource:       48
NoSource:       49
NoSource:       50
NoSource:       52
NoSource:       57
NoSource:       60
NoSource:       63
NoSource:       65
NoSource:       75
NoSource:       76
NoSource:       78
NoSource:       79
NoSource:       80
NoSource:       81
NoSource:       82
NoSource:       83
NoSource:       84
NoSource:       85
NoSource:       86
NoSource:       100
NoSource:       101
NoSource:       102
NoSource:       103
NoSource:       104
NoSource:       105
NoSource:       106
NoSource:       108
NoSource:       109
NoSource:       110
NoSource:       111
NoSource:       113
NoSource:       114
NoSource:       120
NoSource:       121
Provides:       %name = %version-%source_rel
Provides:       %name-srchash-%git_commit

%description
A few basic documents from the current kernel sources.

%source_timestamp

%files
%if 0%{?suse_version} && 0%{?suse_version} < 1500
%doc COPYING
%else
%license COPYING
%endif
%doc CREDITS MAINTAINERS README
%doc old_changelog.txt

%if %build_pdf
%package pdf
Summary:        Kernel Documentation (PDF)
Group:          Documentation/Other

%description pdf
These are PDF documents built from the current kernel sources.

%source_timestamp

%files pdf
%dir %{_datadir}/doc/kernel
%docdir %{_datadir}/doc/kernel/pdf
%{_datadir}/doc/kernel/pdf
%endif

%if %build_html
%package html
Summary:        Kernel Documentation (HTML)
Group:          Documentation/HTML

%description html
These are HTML documents built from the current kernel sources.

%source_timestamp

%files html
%dir %{_datadir}/doc/kernel
%docdir %{_datadir}/doc/kernel/html
%{_datadir}/doc/kernel/html
%endif

%prep
%setup -q -c -T -a 0 -a 100 -a 101 -a 102 -a 103 -a 104 -a 105 -a 106 -a 108 -a 109 -a 110 -a 111 -a 113 -a 114 -a 120 -a 121
cp -a linux-%srcversion/{COPYING,CREDITS,MAINTAINERS,README} .
cp %_sourcedir/old_changelog.txt .
cd linux-%srcversion
%_sourcedir/apply-patches %_sourcedir/series.conf %my_builddir %symbols

%build
# for reproducible builds (bsc#1238303)
export PARALLELISM=1
cd linux-%srcversion
export LANG=en_US.utf8
%if %build_html
mkdir -p html
make %{?make_arg} O=$PWD/html \
%if ! 0%{?suse_version} || 0%{?suse_version} >= 1500
	     PYTHON=python3 \
%endif
	     htmldocs
%endif
%if %build_pdf
mkdir -p pdf
make %{?make_arg} O=$PWD/pdf \
%if ! 0%{?suse_version} || 0%{?suse_version} >= 1500
	     PYTHON=python3 \
%endif
	     pdfdocs
%endif

%install
cd linux-%srcversion
%if %build_html
install -d %{buildroot}%{_datadir}/doc/kernel/html/rst
cp -a html/Documentation/output/* %{buildroot}%{_datadir}/doc/kernel/html/rst || true
%endif

%if %build_pdf
install -d %{buildroot}%{_datadir}/doc/kernel/pdf
for i in pdf/Documentation/output/latex/*.pdf; do
    cp -a $i %{buildroot}%{_datadir}/doc/kernel/pdf
done
%endif

%changelog
