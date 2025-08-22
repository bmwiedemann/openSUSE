#
# spec file for package gettext-csharp
#
# Copyright (c) 2025 SUSE LLC and contributors
# Copyright (c) 2025 Andreas Stieger <Andreas.Stieger@gmx.de>
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


%if 0%{?fedora_version} || 0%{?centos_version} <= 600 || 0%{?scilin_version} <= 600 || 0%{?rhel_version} <= 600
%global debug_package %{nil}
%endif
Name:           gettext-csharp
Version:        0.26
Release:        0
Summary:        Native Language Support (NLS) for C#
License:        LGPL-2.1-or-later
Group:          Development/Tools/Other
URL:            https://www.gnu.org/software/gettext/
Source0:        https://ftp.gnu.org/gnu/gettext/gettext-%{version}.tar.xz
Source1:        https://ftp.gnu.org/gnu/gettext/gettext-%{version}.tar.xz.sig
Source2:        suse-start-po-mode.el
Source3:        gettext-linkdupes.sh
Source4:        gettext-rpmlintrc
# pub   ed25519 2025-01-28 [SC]
#       E0FF BD97 5397 F77A 32AB  76EC B630 1D9E 1BBE AC08
# uid   Bruno Haible (Free Software Development) <bruno@clisp.org>
# https://savannah.gnu.org/users/haible
Source5:        gettext-runtime.keyring
Patch1:         gettext-0.19.3-fix-bashisms.patch
Patch2:         gettext-0.12.1-gettextize.patch
Patch4:         gettext-po-mode.diff
Patch5:         gettext-initialize_vars.patch
# PATCH-FIX-OPENSUSE gettext-dont-test-gnulib.patch -- coolo@suse.de
Patch6:         gettext-dont-test-gnulib.patch
# PATCH-FIX-UPSTREAM boo#941629 -- pth@suse.com
Patch11:        boo941629-unnessary-rpath-on-standard-path.patch
# PATCH-FEATURE bsc#1165138
Patch14:        0001-msgcat-Add-feature-to-use-the-newest-po-file.patch
Patch15:        0002-msgcat-Merge-headers-when-use-first.patch
# PATCH-FEATURE-FIX-SUSE boo#1227316 -- sbrabec@suse.com
Patch16:        0003-Fix-malformed-header-processing.patch
BuildRequires:  automake >= 1.14
BuildRequires:  fdupes
BuildRequires:  gcc-c++
BuildRequires:  glib2-devel
BuildRequires:  libtool
BuildRequires:  libxml2-devel
BuildRequires:  mono-devel
BuildRequires:  perl-libintl-perl
BuildRequires:  tcl
BuildRequires:  pkgconfig(libacl)
BuildRequires:  pkgconfig(libattr)
Requires:       mono
ExcludeArch:    i586

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
%autosetup -p1 -n gettext-%{version}

%build
export CFLAGS="%{optflags} -pipe -W -Wall -Dgcc_is_lint -lm"
export CXXFLAGS="%{optflags} -pipe -W -Wall -Dgcc_is_lint"
# expect a couple "You should update your `aclocal.m4' by running aclocal."
autoreconf -fiv
%configure --enable-shared --enable-csharp
%make_build GMSGFMT=../src/msgfmt

%install
export LC_CTYPE=ISO-8859-15
%make_install
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
rm -Rf %{buildroot}/%{_bindir}
rm -f %{buildroot}/%{_libdir}/lib*
rm -rf %{buildroot}/%{_libexecdir}
rm -Rf %{buildroot}/%{_includedir}
rm -f %{buildroot}/%{_libdir}/preloadable_libintl.so

%files
%doc %{_defaultdocdir}/%{name}
%exclude %{_libdir}/gettext/GNU.Gettext.dll
%dir %{_libdir}/gettext
%{_libdir}/GNU.Gettext.dll
%{_libdir}/gettext/msgfmt.net.exe
%{_libdir}/gettext/msgunfmt.net.exe

%changelog
