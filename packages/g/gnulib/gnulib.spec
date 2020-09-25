#
# spec file for package gnulib
#
# Copyright (c) 2020 SUSE LLC
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
Version:        git.20200809.d6dabe8ee
Release:        0
Summary:        GNU Portability Library
License:        SUSE-Public-Domain AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.1-or-later AND LGPL-3.0-or-later
Group:          Development/Languages/C and C++
URL:            http://www.gnu.org/software/gnulib
Source:         %{name}-%{version}.tar.xz
Source1:        http://erislabs.net/gitweb/?p=gnulib.git;a=blob_plain;hb=HEAD;f=debian/manpages/check-module.1
Source2:        http://erislabs.net/gitweb/?p=gnulib.git;a=blob_plain;hb=HEAD;f=debian/manpages/gnulib-tool.1
BuildRequires:  bison
# For building Modules, all gnulib requires must be found, Modules BRs:
BuildRequires:  gettext-devel
BuildRequires:  gperf
BuildRequires:  help2man
BuildRequires:  java-devel
BuildRequires:  libtool
BuildRequires:  texinfo

%description
The GNU portability library is a macro system and C declarations and
definitions for commonly-used API elements and abstracted system behaviors.
It can be used to improve portability and other functionality in your programs.

%package devel
Summary:        Devel files of %{name}
License:        SUSE-Public-Domain AND GPL-2.0-or-later AND GPL-3.0-only AND GPL-3.0-or-later AND LGPL-2.0-only AND LGPL-2.1-or-later AND LGPL-3.0-or-later
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

%package -n git-merge-changelog
Summary:        Git merge driver for ChangeLog files
License:        GPL-2.0-or-later
Group:          Development/Languages/C and C++

%description -n git-merge-changelog
Git Merge Changelog is a git merge driver for changelogs that combines
parallel additions to the changelog without generating merge conflicts.
It can be enabled for specific files by setting appropriate git attributes.

%prep
%setup -q

#modules not to be tested by direct import
toRemove="lib-symbol-visibility havelib .*-obsolete localcharset gettext-h gettext alloca-opt alloca "

list="$(./gnulib-tool --list)"
for item in $toRemove
do
   list="$(echo $list| sed "s:\b$item\b::g")"
done
#is necessary to avoid some modules to test prep pass
./gnulib-tool --create-testdir --with-tests --with-obsolete --avoid=alloca --avoid=lib-symbol-visibility --avoid=havelib --dir=build-tests $list

rm lib/javaversion.class
# MODULE #1 - git-merge-changelog
./gnulib-tool --create-testdir --dir=build-git-merge-changelog git-merge-changelog

%build
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
javac -d lib -source 6 -target 1.6 lib/javaversion.java
# This part is done with the original path
make %{?_smp_mflags} MODULES.html
sed -i -r 's#HREF="(lib|m4|modules)#HREF="%{_datadir}/%{name}/\1#g' MODULES.html
sed -i "/^[ ]*gnulib_dir=/s#\`[^\`]*\`#%{_datadir}/%{name}#" gnulib-tool
# This part is done with the target path
make %{?_smp_mflags} info html
# Removing unused files
rm -f */.cvsignore
rm -f */.gitignore
rm -f */.gitattributes
rm -f lib/.cppi-disable
rm -f lib/uniname/gen-uninames.lisp

%check
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

cp -p doc/gnulib.info %{buildroot}%{_infodir}/
cp -p doc/gnulib.html MODULES.html NEWS COPYING ChangeLog users.txt doc/COPYING* %{buildroot}%{_docdir}/%{name}/
cp -p %{SOURCE1} %{SOURCE2} %{buildroot}%{_mandir}/man1

# Module installing
pushd build-git-merge-changelog
make DESTDIR=%{buildroot} install %{?_smp_mflags}
popd
help2man -N --no-discard-stderr %{buildroot}%{_bindir}/git-merge-changelog | gzip -9c > %{buildroot}%{_mandir}/man1/git-merge-changelog.1.gz

%post docs
/sbin/install-info %{_infodir}/%{name}.info %{_infodir}/dir || :

%preun docs
if [ $1 = 0 ] ; then
  /sbin/install-info --delete %{_infodir}/%{name}.info %{_infodir}/dir || :
fi

%files docs
%defattr(-,root,root)
%{_infodir}/gnulib.info.gz
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

%files -n git-merge-changelog
%defattr(-,root,root)
%{_bindir}/git-merge-changelog
%{_mandir}/*/git-merge-changelog.*
%doc doc/COPYINGv2

%changelog
