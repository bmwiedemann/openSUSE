#
# spec file for package gettext-java
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


Name:           gettext-java
Version:        0.21
Release:        0
Summary:        Java Support for Native Language Support (NLS)
License:        LGPL-2.1-or-later
Group:          Development/Tools/Other
URL:            http://www.gnu.org/software/gettext/
Source0:        http://ftp.gnu.org/gnu/gettext/gettext-%{version}.tar.xz
Source1:        gettext-rpmlintrc
Source2:        suse-start-po-mode.el
Source3:        gettext-linkdupes.sh
Source4:        http://ftp.gnu.org/gnu/gettext/gettext-%{version}.tar.xz.sig
Source5:        %{name}.keyring
Patch0:         gettext-0.12.1-sigfpe.patch
Patch2:         gettext-0.12.1-gettextize.patch
Patch4:         gettext-po-mode.diff
Patch5:         gettext-initialize_vars.patch
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  java-devel
BuildRequires:  libcroco-devel
BuildRequires:  libtextstyle-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  perl-libintl-perl
BuildRequires:  tcl

%if 0%{?fedora_version} || 0%{?centos_version} <= 600 || 0%{?scilin_version} <= 600 || 0%{?rhel_version} <= 600
%global debug_package %{nil}
%endif

%description
This package includes the tools needed to support message catalogs in
Java applications. It also includes example code for java, java+awt and
java+swing.

%prep
%setup -q -n gettext-%{version}
%patch0
%patch2
%patch4
%patch5

%build
# expect a couple "You should update your `aclocal.m4' by running aclocal."
autoreconf -fiv
#sh autogen.sh
export CFLAGS="%{optflags} -pipe -W -Wall -Dgcc_is_lint -lm"
export CXXFLAGS="%{optflags} -pipe -W -Wall -Dgcc_is_lint"
%configure --enable-shared  --enable-java
make GMSGFMT=../src/msgfmt %{?_smp_mflags} V=1

%install
export LC_CTYPE=ISO-8859-15
make -C gettext-tools/gnulib-lib install DESTDIR=%{buildroot}
make -C gettext-tools/src         install DESTDIR=%{buildroot}
make -C gettext-runtime/intl-java install DESTDIR=$PWD docdir=/docs
make -C gettext-tools/examples    install DESTDIR=$PWD docdir=/allexamples
mkdir -p docs/examples
mv allexamples/examples/*java* docs/examples
cd docs/examples
fdupes -r *|while read dupe; do
	if [ -z "$dupe" ]; then
		startlink=
	elif [ -z "$startlink" ]; then
		startlink="$dupe"
	else
		ln -f "$startlink" "$dupe"
	fi
done
cd ..
find -type f -size 0 -delete
mkdir -p %{buildroot}%{_libdir}/gettext
mv %{buildroot}/%{_datadir}/gettext/gettext.jar %{buildroot}%{_libdir}/gettext/
# Create scripts that will launch the tools
for i in gnu.gettext.DumpResource gnu.gettext.GetURL; do
cat <<EOF > %{buildroot}%{_libdir}/gettext/$i
#!/bin/sh
exec java -cp %{_libdir}/gettext/gettext.jar $i \${1+\$@}
EOF
chmod +x %{buildroot}%{_libdir}/gettext/$i
done
rm -rf   %{buildroot}/%{_datadir}/*
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}
cp -av * %{buildroot}/%{_defaultdocdir}/%{name}
cd ../allexamples/examples
rm -rf *csharp*
fdupes -r * | while read dupe; do
	if [ -z "$dupe" ]; then
		startlink=
	elif [ -z "$startlink" ]; then
		startlink="$dupe"
	else
		echo "ln -f '$startlink' '$dupe'" >>../../gettext-linkdupes.sh
	fi
done
diff %{SOURCE3} . || {
	cat <<END
	######################################################
	######################################################
	## Updated gettext-linkdupes.sh in $PWD ##
	######################################################
	######################################################
END
}
ls -l %{buildroot}/%{_datadir}
# exclude files packaged via other spec files
rm -rf %{buildroot}/%{_bindir}
rm -f %{buildroot}/%{_libdir}/lib*
rm -f %{buildroot}/%{_libdir}/gettext/hostname
rm -f %{buildroot}/%{_libdir}/gettext/project-id
rm -f %{buildroot}/%{_libdir}/gettext/urlget
rm -f %{buildroot}/%{_libdir}/gettext/user-email
rm -f %{buildroot}/%{_libdir}/gettext/cldr-plurals

%files
%{_defaultdocdir}/%{name}
%{_libdir}/gettext/gettext.jar
%{_libdir}/gettext/gnu.gettext.DumpResource
%{_libdir}/gettext/gnu.gettext.GetURL

%changelog
