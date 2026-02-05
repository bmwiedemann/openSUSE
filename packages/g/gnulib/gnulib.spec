#
# spec file for package gnulib
#
# Copyright (c) 2026 SUSE LLC and contributors
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


%global module1 git-merge-changelog

Name:           gnulib
Version:        git.20260114.2a288c048e
Release:        0
Summary:        GNU Portability Library
License:        GPL-2.0-or-later AND SUSE-Public-Domain AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            http://www.gnu.org/software/gnulib
Source:         %{name}-%{version}.tar.xz
Source1:        http://erislabs.net/gitweb/?p=gnulib.git;a=blob_plain;hb=HEAD;f=debian/manpages/check-module.1
Source2:        http://erislabs.net/gitweb/?p=gnulib.git;a=blob_plain;hb=HEAD;f=debian/manpages/gnulib-tool.1
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  bison
# For building Modules, all gnulib requires must be found, Modules BRs:
BuildRequires:  gettext-devel
BuildRequires:  gperf
BuildRequires:  help2man
BuildRequires:  java-devel
BuildRequires:  libacl-devel
BuildRequires:  libattr-devel
BuildRequires:  libtool
BuildRequires:  ncurses-devel
BuildRequires:  texinfo

%description
The GNU portability library is a macro system and C declarations and
definitions for commonly-used API elements and abstracted system behaviors.
It can be used to improve portability and other functionality in your programs.

%package devel
Summary:        Devel files of %{name}
License:        GPL-2.0-or-later AND SUSE-Public-Domain AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Group:          Development/Languages/C and C++
Requires:       bison
Requires:       coreutils
Requires:       diffutils
Requires:       gettext-devel
Requires:       gperf
Requires:       libtool
Requires:       make
Requires:       patch
Requires:       texinfo
Provides:       gnulib
BuildArch:      noarch
%define add_optflags(a:f:t:p:w:W:d:g:O:A:C:D:E:H:i:M:n:P:U:u:l:s:X:B:I:L:b:V:m:x:c:S:E:o:v:) \
%global optflags %{optflags} %{**}

%description devel
The GNU portability library is a macro system and C declarations and
definitions for commonly-used API elements and abstracted system behaviors.
It can be used to improve portability and other functionality in your programs.

This package contains devel files of %{name}.

%package docs
Summary:        Documentation for %{name} modules
License:        GFDL-1.3-only
Group:          Development/Languages/C and C++
Requires:       %{name}-devel = %{version}-%{release}
Requires(post): info
Requires(preun): info
BuildArch:      noarch

%description docs
The GNU portability library is a macro system and C declarations and
definitions for commonly-used API elements and abstracted system behaviors.
It can be used to improve portability and other functionality in your programs.

This package contains documentation for %{name}.

%prep
%setup -q -n gnulib-stable-202601
LC_ALL=C.UTF-8
LANG=C.UTF-8
export LC_ALL LANG
%add_optflags -D_DEFAULT_SOURCE

#modules not to be tested by direct import
toRemove="lib-symbol-visibility havelib .*-obsolete localcharset gettext-h gettext alloca-opt alloca "
toRemove="$(echo $toRemove | tr ' ' '|')"

list="$(./gnulib-tool --list | grep -vE "($toRemove)")"
unset toRemove

#is necessary to avoid some modules to test prep pass
./gnulib-tool --create-testdir --with-tests --with-obsolete --avoid=alloca --avoid=lib-symbol-visibility --dir=build-tests $list

rm lib/javaversion.class
# MODULE #1 - git-merge-changelog
./gnulib-tool --create-testdir --dir=build-git-merge-changelog git-merge-changelog

%build
LC_ALL=C.UTF-8
LANG=C.UTF-8
export LC_ALL LANG
# MODULE #1 - git-merge-changelog
pushd build-git-merge-changelog
%configure --prefix=%{_prefix}
make %{?_smp_mflags}
popd
#tests build
cp -p lib/timevar.def build-tests/gllib #Fix timevar.def not found
pushd build-tests
%configure --prefix=%{_prefix}
make %{?_smp_mflags}
popd
# Rebuild removed java class
javac -d lib -source 1.8 -target 1.8 lib/javaversion.java
# This part is done with the original path
make %{?_smp_mflags} MODULES.html
sed -i -r 's#HREF="(lib|m4|modules)#HREF="%{_datadir}/%{name}/\1#g' MODULES.html
sed -i "/^[ ]*gnulib_dir=/s#\`[^\`]*\`#%{_datadir}/%{name}#" gnulib-tool
# This part is done with the target path
make %{?_smp_mflags} info
make %{?_smp_mflags} html
# Removing unused files
rm -f */.cvsignore
rm -f */.gitignore
rm -f */.gitattributes
rm -f lib/.cppi-disable
rm -f lib/uniname/gen-uninames.lisp

%check
LC_ALL=C.UTF-8
LANG=C.UTF-8
export LC_ALL LANG
pushd build-tests
make %{?_smp_mflags} check
popd

%install
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/%{name}
mkdir -p %{buildroot}%{_datadir}/info
mkdir -p %{buildroot}%{_datadir}/%{name}/doc
mkdir -p %{buildroot}%{_docdir}/%{name}
mkdir -p %{buildroot}%{_mandir}/man1

cp -p check-module %{buildroot}%{_bindir}
cp -p gnulib-tool %{buildroot}%{_bindir}
cp -rp build-aux lib m4 modules config tests %{buildroot}%{_datadir}/%{name}/
# relocatable.texi is needed during compilation of PSPP. See rh#1474792 and
# https://src.fedoraproject.org/rpms/gnulib/c/cea2f6f12fe24479e282900341575352689d7cfe?branch=master
cp -p doc/relocatable.texi %{buildroot}%{_datadir}/%{name}/doc
# Needed for jitter
cp -p doc/{gendocs_template,gendocs_template_min,INSTALL} %{buildroot}%{_datadir}/%{name}/doc

cp -p doc/gnulib.info %{buildroot}%{_infodir}/
cp -p doc/gnulib.html MODULES.html NEWS COPYING ChangeLog users.txt doc/COPYING* %{buildroot}%{_docdir}/%{name}/
cp -p %{SOURCE1} %{SOURCE2} %{buildroot}%{_mandir}/man1

# Module installing
pushd build-git-merge-changelog
make DESTDIR=%{buildroot} install %{?_smp_mflags}
popd

%post docs
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun docs
if [ $1 = 0 ] ; then
  /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files docs
%defattr(-,root,root)
%{_infodir}/gnulib.info*
%{_docdir}/%{name}/gnulib.html
%{_docdir}/%{name}/MODULES.html
# license text is included directly in info and html files.

%files devel
%defattr(-,root,root)
%{_datadir}/%{name}/
%{_bindir}/gnulib-tool
%{_bindir}/check-module
%{_mandir}/*/check-module.*
%{_mandir}/*/gnulib-tool.*
%{_docdir}/%{name}/
%exclude %{_docdir}/%{name}/MODULES.html
%exclude %{_docdir}/%{name}/gnulib.html

%changelog
