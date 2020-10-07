#
# spec file for package gettext-csharp
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


Name:           gettext-csharp
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libcroco-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  mono-devel
BuildRequires:  perl-libintl-perl
BuildRequires:  tcl
Requires:       mono
URL:            http://www.gnu.org/software/gettext/
Version:        0.21
Release:        0
Summary:        Native Language Support (NLS) for C#
License:        LGPL-2.1-or-later
Group:          Development/Tools/Other
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source:         http://ftp.gnu.org/gnu/gettext/gettext-%{version}.tar.xz
Source1:        gettext-rpmlintrc
Source2:        suse-start-po-mode.el
Source3:        gettext-linkdupes.sh
Source4:        http://ftp.gnu.org/gnu/gettext/gettext-%{version}.tar.xz.sig
Source5:        %name.keyring
Patch:          gettext-0.12.1-sigfpe.patch
Patch2:         gettext-0.12.1-gettextize.patch
Patch4:         gettext-po-mode.diff
Patch5:         gettext-initialize_vars.patch

%if 0%{?fedora_version} || 0%{?centos_version} <= 600 || 0%{?scilin_version} <= 600 || 0%{?rhel_version} <= 600
%global debug_package %{nil}
%endif

%description
Mono with its 'resgen' program uses a design that Microsoft created and
that gives the power to the software vendor and not to the user: it
doesn't allow the end-user to create his own localisations for existing
programs. As documented in the gettext manual:

The advantages of the .dll' format over the .resources' format are:

1. 1. Freedom to localize: Users can add their own translations to an
   application after it has been built and distributed.  Whereas
   when the programmer uses a ResourceManager' constructor provided
   by the system, the set of .resources' files for an application
   must be specified when the application is built and cannot be
   extended afterwards.

2., 3., 4. ...

The included GNU.Gettext.dll gives the user this freedom back and the
also included msgfmt.net.exe and msgunfmt.net.exe handle PO files more
reliably than 'resgen'.


%prep
%setup -q -n gettext-%{version}
%patch
%patch2
%patch4
%patch5

%build
export CFLAGS="%{optflags} -pipe -W -Wall -Dgcc_is_lint -lm"
export CXXFLAGS="%{optflags} -pipe -W -Wall -Dgcc_is_lint"
# expect a couple "You should update your `aclocal.m4' by running aclocal."
#autoreconf -fiv
#sh autogen.sh
%configure --enable-shared --enable-csharp
make %{?_smp_mflags} GMSGFMT=../src/msgfmt V=1

%install
export LC_CTYPE=ISO-8859-15
%makeinstall
mkdir examples
mv %{buildroot}/%{_datadir}/doc/gettext/examples/*csharp* examples
mv %{buildroot}/%{_datadir}/doc/gettext/csharpdoc         csharpdoc
cd examples
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
rm -rf	     %{buildroot}/%{_datadir}/*
mkdir -p     %{buildroot}/%{_defaultdocdir}/%{name}
mv examples  %{buildroot}/%{_defaultdocdir}/%{name}
mv csharpdoc %{buildroot}/%{_defaultdocdir}/%{name}
# exclude files packaged via other spec files
rm -Rf %{buildroot}/%_bindir
rm -f %{buildroot}/%_libdir/lib*
rm -f %{buildroot}/%_libdir/gettext/hostname
rm -f %{buildroot}/%_libdir/gettext/project-id
rm -f %{buildroot}/%_libdir/gettext/urlget
rm -f %{buildroot}/%_libdir/gettext/user-email
rm -f %{buildroot}/%_libdir/gettext/cldr-plurals
rm -Rf %{buildroot}/%_includedir
rm -f %{buildroot}/%_libdir/preloadable_libintl.so

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{_defaultdocdir}/%{name}
%_libdir/GNU.Gettext.dll
%_libdir/gettext/msgfmt.net.exe
%_libdir/gettext/msgunfmt.net.exe

%changelog
